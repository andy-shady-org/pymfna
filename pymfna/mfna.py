#!/usr/bin/env python
"""
:Author: Andy Wilson
:Email:  andy@shady.org

:Package: pymfna
:Description: MFNAConnect Python Module
:Function: To provide a connector and facilitate basic actions for a MFNA servers

| This module is used to connect to an MFNA server or appliance.
| This module contains a single class which is used as a parent class of the MFNAClient class.
| This class should not be called directly.

The module also contains code for generating the MFNAClient class from a given WSDL file.

.. highlight:: python
.. code-block:: python

    python mfna.py -v -o newmfnaclient.py my-wsdl-file.wsdl
    ...

The new HMFNA client python file should contain all the processed calls within the WSDL file, presented as methods
within a usable class.
"""

from __future__ import print_function
import httpx
import logging
import keyword
from lxml import etree
from lxml.etree import Element
from lxml.builder import ElementMaker
import xmltodict


class MyMFNAError(Exception):
    pass


class MyMFNASoapError(MyMFNAError):
    pass


class MFNAConnect(object):
    """
    Abstraction class that simplifies and unifies all access to MFNA objects and information.
    """

    def __init__(self, server, username, password, ssl_verify=False, headers=None, verbose=False):
        """

        This class is the MFNAClient Connector. All requests to MFNA are sent via this class.

        Constructor builds up session object for use with MFNA Appliance.

        Authentication is based on supplied user credentials.

        This class requires 3 basic required parameters and 3 optional parameters

        :param server: Server IP Address'
        :type server: str
        :param username: Username required to perform any desired actions
        :type username: str
        :param password: Password associated with username
        :type password: str
        :param ssl_verify: Check SSL certificates on the remote server (set to True, default is False)
        :type ssl_verify: bool
        :param headers: HTTP Headers
        :type headers: dict
        :param verbose: A debugging flag (set to 1 or 2), default covers basic warnings
        :type verbose: int
        """
        super(MFNAConnect, self).__init__()
        self._server = server
        self._username = username
        self._password = password
        self._ssl_verify = ssl_verify
        self._session_id = None
        self._headers = {"Content-type": "application/xml"}
        self.verbose = verbose
        self._setup_logging()
        if isinstance(headers, dict) and headers:
            self._headers.update(headers)
        self._session = httpx.Client(verify=self._ssl_verify)
        self._url = f'https://{server}/soap'
        self._last_xml = None
        self.status_code = None

    def _setup_logging(self):
        """
        Setup initial logging

        :return:
        """
        if self.verbose:
            if self.verbose == 1:
                formatter = "%(asctime)s (%(levelname)s) %(message)s"
                logging.basicConfig(level=logging.INFO, format=formatter, datefmt="%H:%M:%S")
                logging.getLogger('ubshpnaclient').setLevel(logging.INFO)
            elif self.verbose > 1:
                formatter = "%(asctime)s %(levelname)s %(funcName)s():%(lineno)d %(message)s"
                logging.basicConfig(level=logging.DEBUG, format=formatter, datefmt="%H:%M:%S")
                logging.getLogger('ubshpnaclient').setLevel(logging.DEBUG)
        else:
            formatter = "(%(levelname)s) %(message)s"
            logging.basicConfig(level=logging.WARNING, format=formatter, datefmt="%H:%M:%S")
            logging.getLogger('ubshpnaclient').setLevel(logging.WARNING)

        self.logger = logging.getLogger('ubshpnaclient')

    def _request(self, operation, timeout=60, extra_headers=None, method='post', **kwargs):
        """
        Make basic request without checking for authentication.

        :param method: Request method - get, post, delete (default: post)
        :type method: str
        :param operation: MFNA operation (e.g. login, logout, list_device, etc.)
        :type operation: str
        :param timeout: Request timeout in seconds or fractions of second (default: 10 seconds)
        :type timeout: int or float
        :param extra_headers: Extra headers to send with the request
        :type extra_headers: dict or None
        :param files: Files reference for file upload
        :type: dict or None
        :param should_auth: Should basic authentication be used for requests (default: True)
        :type should_auth: bool
        :return: JSON data returned by the call
        :rtype: dict or list or None
        """
        self.logger.info('KWARGS: %s', kwargs)
        self._last_xml = None
        if method.lower() not in ['get', 'post', 'put', 'delete', 'options']:
            raise MyMFNAError('Invalid method {0}'.format(method))
        headers = {}
        if isinstance(self._headers, dict) and self._headers:
            headers.update(self._headers)
        if isinstance(extra_headers, dict) and extra_headers:
            headers.update(extra_headers)
        out_xml = self._build_request(operation, **kwargs)
        self.logger.debug('Sending XML: %s', out_xml)
        try:
            result = self._session.request(method, self._url, headers=headers, data=out_xml, timeout=httpx.Timeout(3.05, connect=timeout))
            self.logger.debug('Status code: %d', result.status_code)
        except Exception as exp:
            self.logger.exception(exp)
            raise
        try:
            self.logger.debug('Received document body: %s', str(result.text.encode('utf-8')))
            h_parser = etree.XMLParser(ns_clean=True, recover=True, encoding='utf-8')
            in_xml = etree.fromstring(result.content, parser=h_parser)
            self._last_xml = in_xml
            self.logger.debug('Received XML:\n%s', etree.tostring(in_xml))
            self.logger.debug('Content type: %s', str(result.headers))
        except Exception as exp:
            self.logger.exception(exp)
            self.logger.warning('Request did not return XML data: %s', str(exp))
            self.logger.debug('Response body: ' + str(result.text.encode('utf-8')))
            return None, result.headers, result.status_code
        return self._parse_response(operation, in_xml), result.headers, result.status_code

    def login(self):
        """
        Method that performs login operation

        """
        if self._session_id is not None:
            raise MyMFNAError('Already logged in. Logout first!')
        try:
            in_dict, in_header, in_status = self._request('login', username=self._username, password=self._password)
            if 'nas:Result' in in_dict and 'nas:Status' in in_dict['nas:Result'] and in_dict['nas:Result']['nas:Status'].startswith('200 '):
                return True
        except MyMFNAError as exp:
            if 'unable to login' not in str(exp).lower():
                raise

        return False

    def logout(self):
        """
        Method that performs logout operation

        """
        if self._session_id is None:
            raise MyMFNAError('Not logged in.')
        in_dict, in_header, in_status = self._request('logout')
        if 'nas:Result' in in_dict and 'nas:Status' in in_dict['nas:Result'] and in_dict['nas:Result']['nas:Status'].startswith('200 '):
            return True
        return False

    def call(self, op, **kwargs):
        """
        Method that performs actual call operation

        """
        in_dict, in_header, in_status = self._request(op, **kwargs)
        return in_dict

    def __getattr__(self, item):
        that = self
        op_name = item

        def missing_func(*args, **kwargs):
            self.logger.debug('Missing func call args: %s kwargs: %s', str(args), str(kwargs))
            in_dict, in_header, in_status = self._request(op_name, **kwargs)
            return in_dict

        return missing_func

    def _build_request(self, operation, **kwargs):
        soap_env_url = 'http://schemas.xmlsoap.org/soap/envelope/'
        hpna_url = 'http://opsware.com/nas/922'

        out_args = dict(**kwargs)
        if operation != 'login' and 'sessionid' not in out_args:
            out_args['sessionid'] = self._session_id

        soap = ElementMaker(namespace=soap_env_url, nsmap={'soap-env': soap_env_url})
        env = soap('Envelope')
        body = soap('Body')
        hpna_op = ElementMaker(namespace=hpna_url, nsmap={'ns0': hpna_url})
        hpna_operation = hpna_op(operation)

        # soap = ElementMaker('Envelope', namespace=soap_env_url, nsmap={'soap-env': soap_env_url})
        # body = ElementMaker('Body', namespace=soap_env_url, nsmap={'soap-env': soap_env_url})

        body.append(hpna_operation)
        hpna_parameters = Element('parameters')
        for kw in out_args:
            if out_args[kw]:
                item = hpna_op(kw, str(out_args[kw]) if out_args[kw] is not None else '')
                hpna_parameters.append(item)
        hpna_operation.append(hpna_parameters)
        body.append(hpna_operation)
        env.append(body)
        xml_declaration = '<?xml version="1.0" encoding="utf-8"?>\n'
        return xml_declaration + etree.tostring(env, encoding='utf-8', xml_declaration=False, pretty_print=False).decode('utf-8')

    def _parse_response(self, operation, in_xml):
        ns_list = dict(in_xml.nsmap, **{'nas': 'http://opsware.com/nas/922'})
        fault_msg = in_xml.find('.//nas:Fault', namespaces=ns_list)
        if fault_msg is not None:
            fault_string = fault_msg.find('.//faultstring', namespaces=ns_list)
            if fault_string is not None:
                fault_string = fault_string.text
            fault_msg = fault_msg.find('.//nas:message', namespaces=ns_list)
            if fault_msg is not None:
                fault_msg = fault_msg.text
            raise MyMFNASoapError(fault_string if not fault_msg else fault_msg)
        else:
            login_error = in_xml.find('.//nas:error/./nas:message', namespaces=ns_list)
            if login_error is not None:
                raise MyMFNASoapError(login_error.text)
        response_str = 'nas:' + operation + 'Response'
        self.logger.debug('Response key: %s', response_str)
        response = in_xml.find('.//' + response_str, namespaces=ns_list)
        if response is None:
            raise MyMFNAError('Failed to locate operation response in the returned XML')
        self.logger.debug('Reponse value: %s', etree.tostring(response))
        result = response.find('.//nas:Result', namespaces=ns_list)
        if result is None:
            raise MyMFNAError('Failed to locate result within the operation response message')
        status = result.find('.//nas:Status', namespaces=ns_list)
        if status is None:
            raise MyMFNAError('Failed to locate SOAP operation status value')
        status_text = status.text
        try:
            self.status_code = int(status_text.split(' ')[0])
            self.logger.debug('STATUS: %s', self.status_code)
            if (self.status_code < 200 or self.status_code > 299) and self.status_code != 501:
                raise MyMFNASoapError('Unexpected SOAP status value: {0}'.format(status_text))
        except (ValueError, TypeError):
            raise MyMFNAError('Failed to retrieve SOAP status value from string: {0}'.format(str(status_text)))
        self.logger.debug('Result value: %s', etree.tostring(result))
        if operation == 'login':
            session_text = result.find('.//nas:Text', namespaces=ns_list)
            self.logger.debug('Session Test: %s', session_text)
            if session_text is None:
                raise MyMFNAError('Failed to locate session id after login operation in SOAP response')
            self._session_id = session_text.text
        elif operation == 'logout':
            self._session_id = None
        else:
            text_result = result.find('.//nas:Text', namespaces=ns_list)
            if text_result is not None:
                return text_result.text
            else:
                rows = result.findall('.//nas:Row', namespaces=ns_list)
                if rows is not None:
                    out_result = list()
                    for row in rows:
                        self.logger.debug('Processing row: %s', etree.tostring(row))
                        items = list(row)
                        out_row = dict()
                        for item in items:
                            self.logger.debug('Processing record: %s', etree.tostring(item))
                            out_row[item.tag if '}' not in item.tag else item.tag.split('}')[1]] = item.text
                        out_result.append(out_row)
                    if len(out_result) == 0:
                        return []
                    elif len(out_result) == 1:
                        return out_result[0]
                    return out_result
        response_dict = xmltodict.parse(etree.tostring(result), encoding='utf-8')
        return response_dict


# -- for testing only
# from lxml import etree
# xml = etree.fromstring(open('hpna/api.wsdl.gsoap-original').read().encode("utf-8"))

class MFNAVariable(object):
    def __init__(self, name, **kwargs):
        super(MFNAVariable, self).__init__()
        self.name = name
        self.__dict__.update(**{x: kwargs[x] for x in kwargs if x != 'types'})
        if 'type' in self.__dict__:
            if self.__dict__['type'].startswith('xsd:'):
                t_val = self.__dict__['type'][4:]
                if t_val == 'string':
                    self.__dict__['type'] = str
                elif t_val == 'int' or t_val == 'long':
                    self.__dict__['type'] = int
                else:
                    self.__dict__['type'] = t_val
            elif self.__dict__['type'].startswith('nas:'):
                type_val = self.__dict__['type'][4:]
                if type_val in kwargs.get('types', {}):
                    self.__dict__['type'] = kwargs.get('types', {})[type_val]
        if 'nillable' in self.__dict__ and self.__dict__['nillable'] in ['true', 'false']:
            self.__dict__['nillable'] = True if self.__dict__['nillable'] == 'true' else False
        if 'maxOccurs' in self.__dict__ and self.__dict__['maxOccurs'] == 'unbounded':
            self.__dict__['maxOccurs'] = -1

    def __repr__(self):
        return 'MFNAVariable({0})'.format(','.join(['{0}={1}'.format(x, self.__dict__[x]) for x in self.__dict__ if x[0] != '_']))

    def get_arguments(self):
        args = list()
        if 'type' in self.__dict__ and isinstance(self.__dict__['type'], MFNAVariable):
            args.extend(self.__dict__['type'].get_arguments())
        else:
            args.append(self.name)
        return args

    def __contains__(self, item):
        if item in self.__dict__:
            return True
        return False

    def __getitem__(self, item):
        if item in self.__dict__:
            return self.__dict__[item]
        raise KeyError('Not found')


class MFNAMessage(object):
    def __init__(self, name, **kwargs):
        super(MFNAMessage, self).__init__()
        self.name = name
        self.__dict__.update(**kwargs)

    def add(self, name, value):
        self.__dict__[name] = value

    def get_arguments(self):
        if 'parameters' in self.__dict__ and self.__dict__['parameters'] is not None:
            return self.__dict__['parameters'].get_arguments()
        return []

    def __repr__(self):
        return 'MFNAMessage({0})'.format(','.join(['{0}={1}'.format(x, self.__dict__[x]) for x in self.__dict__ if x[0] != '_']))


class MFNAType(object):
    def __init__(self, name):
        super(MFNAType, self).__init__()
        self.name = name
        self.vars = list()  # list[MFNAVariable]

    def add(self, v):
        self.vars.append(v)

    def keys(self):
        return [v.name for v in self.vars]

    def get_arguments(self):
        args = list()
        for v in self.vars:
            args.extend(v.get_arguments())
        return args

    def __contains__(self, item):
        for v in self.vars:
            if v.name == item:
                return True
        return False

    def __iter__(self):
        return self.vars.__iter__()

    def __getitem__(self, item):
        for v in self.vars:
            if v.name == item:
                return v
        raise KeyError('Item not found')

    def __repr__(self):
        return 'MFNAType({0}, {1})'.format(self.name, ','.join([repr(v) for v in self.vars]))


class MFNAOperation(object):
    def __init__(self, name, input=None, output=None, fault=None):
        super(MFNAOperation, self).__init__()
        self.name = name
        self.input = input  # type: MFNAType
        self.output = output  # type: MFNAType
        self.fault = fault  # type: MFNAType

    def get_arguments(self):
        if self.input:
            return self.input.get_arguments()
        return []

    def __repr__(self):
        return 'MFNAOperation({0}, input={1}, output={2}, fault={3})'.format(self.name, repr(self.input), repr(self.output), repr(self.fault))


def parse_wsdl(parsed_xml):
    wsdl_types = parsed_xml.find('.//wsdl:types', namespaces=parsed_xml.nsmap)
    types = dict()
    for c_type in wsdl_types.findall('.//xsd:complexType', namespaces=parsed_xml.nsmap):
        out_name = c_type.attrib['name']
        out_type = MFNAType(out_name)
        types[out_name] = out_type
        seq = c_type.find('.//xsd:sequence', namespaces=parsed_xml.nsmap)
        for el in seq.findall('.//xsd:element', namespaces=parsed_xml.nsmap):
            name = el.attrib['name']
            out_t = MFNAVariable(name, types=types, **{x:el.attrib[x] for x in el.attrib if x != 'name'})
            out_type.add(out_t)
        logging.debug('Type {0} values {1}'.format(out_name, str(types[out_name])))
    messages = dict()
    for msg_ in parsed_xml.findall('.//wsdl:message', namespaces=parsed_xml.nsmap):
        out_parts = dict()
        out_name = msg_.attrib['name']
        msg = MFNAMessage(out_name)
        messages[out_name] = msg
        for el in msg_.findall('.//wsdl:part', namespaces=parsed_xml.nsmap):
            name = el.attrib['name']
            in_type = el.attrib['type'] if 'type' in el.attrib else el.attrib['element']
            if in_type.startswith('nas:'):
                in_type = in_type[4:]
            if in_type and in_type in types:
                msg.add(name, types[in_type])
            else:
                msg.add(name, in_type)

        logging.debug('Type {0} values {1}'.format(out_name, str(messages[out_name])))

    operations = dict()
    portType = parsed_xml.find('.//wsdl:portType', namespaces=parsed_xml.nsmap)
    if 'name' in portType.attrib and portType.attrib['name'] == 'NetworkManagementApi':
        for x in portType.findall('.//wsdl:operation', namespaces=parsed_xml.nsmap):
            op_name = x.attrib['name']
            in_input = x.find('.//wsdl:input', namespaces=parsed_xml.nsmap)
            if in_input is not None:
                in_val_name = in_input.attrib['message'] if 'message' in in_input.attrib else ''
                if in_val_name.startswith('nas:') and in_val_name[4:] in messages:
                    logging.info('Found data type: %s', in_val_name[4:])
                    out_input = messages[in_val_name[4:]]
                else:
                    logging.info('in> Data type %s not found in messages: %s', in_val_name[4:], etree.tostring(in_input))
                    out_input = None
            else:
                logging.info('Failed to locate input message entry')
                out_input = None
            output = x.find('.//wsdl:output', namespaces=parsed_xml.nsmap)
            if output is not None:
                out_val_name = output.attrib['message'] if 'message' in output.attrib else ''
                if out_val_name.startswith('nas:') and out_val_name[4:] in messages:
                    logging.info('Found data type: %s', out_val_name[4:])
                    out_output = messages[out_val_name[4:]]
                else:
                    logging.info('out> Data type %s not found in messages: %s', out_val_name[4:], etree.tostring(output))
                    out_output = None
            else:
                logging.info('Failed to locate output message entry')
                out_output = None
            fault = x.find('.//wsdl:fault', namespaces=parsed_xml.nsmap)
            if fault is not None:
                fault_val_name = fault.attrib['message'] if 'message' in fault.attrib else ''
                if fault_val_name.startswith('nas:') and fault_val_name[4:] in messages:
                    logging.info('Found data type: %s', fault_val_name[4:])
                    out_fault = messages[fault_val_name[4:]]
                else:
                    logging.info('fault> Data type %s not found in messages: %s', fault_val_name[4:], etree.tostring(fault))
                    out_fault = None
            else:
                logging.info('Failed to locate fault message entry')
                out_fault = None
            operations[op_name] = MFNAOperation(op_name, out_input, out_output, out_fault)
    else:
        logging.error('Did not find portType wrapper in XML data')

    return types, messages, operations


def generate_util_class(types, messages, operations):
    out_str = 'from .' + os.path.splitext(os.path.basename(__file__))[0] + ' import MFNAConnect\n'
    out_str += '\n\n'
    out_str += 'class MFNAClient(MFNAConnect):\n'
    out_str += '    def __init__(self, server, username, password, verbose=False):\n'
    out_str += '        super(MFNAClient, self).__init__(server, username, password, verbose=verbose)\n\n'
    for op_key in operations:
        op = operations[op_key]
        out_op = op.name if op.name not in ['login', 'logout'] and op.name not in keyword.kwlist else ('_' + op.name)
        out_str += '    def ' + out_op + '(self'
        if op.input is not None:
            params = [x for x in op.input.parameters.get_arguments() if x != 'sessionid' and not isinstance(op.input.parameters[x].type, MFNAVariable)]
            out_p = list()
            for p in params:
                p_name = str(p) if str(p) not in keyword.kwlist else (str(p) + '_')
                if 'nillable' in op.input.parameters[p] and op.input.parameters[p].nillable is True:
                    out_p.append(p_name + '=None')
                else:
                    out_p.append(p_name)
            if params and len(params) > 0:
                out_str += ', ' + ', '.join(out_p)
            out_str += '):\n'
            if params and len(params) > 0:
                out_str += '        """\n'
                out_str += '        MFNA ' + op.name + ' operation method\n\n'
                for p in params:
                    p_name = str(p) if str(p) not in keyword.kwlist else (str(p) + '_')
                    out_str += '        :param ' + p_name + ': ' + str(p) + ' variable. Nullable: ' + (str(op.input.parameters[p].nillable if 'nillable' in op.input.parameters[p] else 'False')) + '\n'
                    if op.input.parameters[p].type in [str, int]:
                        out_str += '        :type ' + p_name + ': '
                        if op.input.parameters[p].type == 'int':
                            out_str += 'int\n'
                        else:
                            out_str += 'str\n'
                out_str += '        """\n'
                out_str += '        out_args = {' + ', '.join([('\'' + str(p) + '\': '+(str(p) if str(p) not in keyword.kwlist else (str(p) + '_'))) for p in params]) + '}\n'
                # out_str += '        return self.call("' + op.name + '", ' + ', '.join([(str(p)+'='+(str(p) if str(p) not in keyword.kwlist else (str(p) + '_'))) for p in params]) + ')\n'
                out_str += '        return self.call("' + op.name + '", **out_args)\n'
            else:
                out_str += '        return self.call("' + op.name + '")\n'
        else:
            out_str += '):\n'
            out_str += '        return self.call("' + op.name + '")\n'
        out_str += '\n'
    return out_str


if __name__ == '__main__':
    import os
    import argparse

    parser = argparse.ArgumentParser(description='Convert MFNA WSDL file into a wrapper class')
    parser.add_argument('-v', '--verbose', action='count', default=0, help='Set verbosity (0=warning, 1=info, 2=debug)')
    parser.add_argument('-o', '--outfile', help='Output file name')
    parser.add_argument('wsdl', help='WSDL file to parse')

    args = parser.parse_args()

    xml = etree.fromstring(open(args.wsdl).read().encode('utf-8'))
    if args.verbose == 0:
        logging.basicConfig(level=logging.WARNING)
    elif args.verbose == 1:
        logging.basicConfig(level=logging.INFO)
    elif args.verbose > 1:
        logging.basicConfig(level=logging.DEBUG)

    xml = etree.fromstring(open(args.wsdl).read().encode("utf-8"))
    res = generate_util_class(*parse_wsdl(xml))
    if args.outfile:
        with open(args.outfile, 'w') as outf:
            outf.write(res)
    else:
        print(res)
