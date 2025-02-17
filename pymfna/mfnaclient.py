from .mfna import MFNAConnect


class MFNAClient(MFNAConnect):
    def __init__(self, server, username, password, verbose=False):
        super(MFNAClient, self).__init__(server, username, password, verbose=verbose)

    def acquire_resource_id(self, name=None, poolid=None, id=None):
        """
        MFNA acquire_resource_id operation method

        :param name: name variable. Nullable: True
        :type name: str
        :param poolid: poolid variable. Nullable: True
        :type poolid: str
        :param id: id variable. Nullable: True
        :type id: str
        """
        out_args = {'name': name, 'poolid': poolid, 'id': id}
        return self.call("acquire_resource_id", **out_args)

    def activate_device(self, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA activate_device operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("activate_device", **out_args)

    def add_advanced_diagnostic(self, name, language, script, sitename=None, description=None, family=None, parameters=None):
        """
        MFNA add_advanced_diagnostic operation method

        :param name: name variable. Nullable: False
        :type name: str
        :param language: language variable. Nullable: False
        :type language: str
        :param script: script variable. Nullable: False
        :type script: str
        :param sitename: sitename variable. Nullable: True
        :type sitename: str
        :param description: description variable. Nullable: True
        :type description: str
        :param family: family variable. Nullable: True
        :type family: str
        :param parameters: parameters variable. Nullable: True
        :type parameters: str
        """
        out_args = {'name': name, 'language': language, 'script': script, 'sitename': sitename, 'description': description, 'family': family, 'parameters': parameters}
        return self.call("add_advanced_diagnostic", **out_args)

    def add_advanced_script(self, name, language, script, scripttype=None, sitename=None, description=None, family=None, parameters=None):
        """
        MFNA add_advanced_script operation method

        :param name: name variable. Nullable: False
        :type name: str
        :param language: language variable. Nullable: False
        :type language: str
        :param script: script variable. Nullable: False
        :type script: str
        :param scripttype: scripttype variable. Nullable: True
        :type scripttype: str
        :param sitename: sitename variable. Nullable: True
        :type sitename: str
        :param description: description variable. Nullable: True
        :type description: str
        :param family: family variable. Nullable: True
        :type family: str
        :param parameters: parameters variable. Nullable: True
        :type parameters: str
        """
        out_args = {'name': name, 'language': language, 'script': script, 'scripttype': scripttype, 'sitename': sitename, 'description': description, 'family': family, 'parameters': parameters}
        return self.call("add_advanced_script", **out_args)

    def add_authentication(self, loc, enablepasswd=None, snmpro=None, ruledevicegroup=None, snmpv3user=None, iprangeend=None, ip=None, start=None, rule=None, taskname=None, enableuser=None, accessvariables=None, snmpv3encryptpw=None, maxwaittime=None, rulehostname=None, site=None, appendsnmprw=None, passwd=None, snmpv3authpw=None, iprangestart=None, appendsnmpro=None, snmprw=None, user=None, connectionmethods=None, group=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA add_authentication operation method

        :param loc: loc variable. Nullable: False
        :type loc: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param ruledevicegroup: ruledevicegroup variable. Nullable: True
        :type ruledevicegroup: str
        :param snmpv3user: snmpv3user variable. Nullable: True
        :type snmpv3user: str
        :param iprangeend: iprangeend variable. Nullable: True
        :type iprangeend: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param start: start variable. Nullable: True
        :type start: str
        :param rule: rule variable. Nullable: True
        :type rule: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param enableuser: enableuser variable. Nullable: True
        :type enableuser: str
        :param accessvariables: accessvariables variable. Nullable: True
        :type accessvariables: str
        :param snmpv3encryptpw: snmpv3encryptpw variable. Nullable: True
        :type snmpv3encryptpw: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param rulehostname: rulehostname variable. Nullable: True
        :type rulehostname: str
        :param site: site variable. Nullable: True
        :type site: str
        :param appendsnmprw: appendsnmprw variable. Nullable: True
        :type appendsnmprw: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param snmpv3authpw: snmpv3authpw variable. Nullable: True
        :type snmpv3authpw: str
        :param iprangestart: iprangestart variable. Nullable: True
        :type iprangestart: str
        :param appendsnmpro: appendsnmpro variable. Nullable: True
        :type appendsnmpro: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        :param user: user variable. Nullable: True
        :type user: str
        :param connectionmethods: connectionmethods variable. Nullable: True
        :type connectionmethods: str
        :param group: group variable. Nullable: True
        :type group: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'loc': loc, 'enablepasswd': enablepasswd, 'snmpro': snmpro, 'ruledevicegroup': ruledevicegroup, 'snmpv3user': snmpv3user, 'iprangeend': iprangeend, 'ip': ip, 'start': start, 'rule': rule, 'taskname': taskname, 'enableuser': enableuser, 'accessvariables': accessvariables, 'snmpv3encryptpw': snmpv3encryptpw, 'maxwaittime': maxwaittime, 'rulehostname': rulehostname, 'site': site, 'appendsnmprw': appendsnmprw, 'passwd': passwd, 'snmpv3authpw': snmpv3authpw, 'iprangestart': iprangestart, 'appendsnmpro': appendsnmpro, 'snmprw': snmprw, 'user': user, 'connectionmethods': connectionmethods, 'group': group, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("add_authentication", **out_args)

    def add_change_plan(self, changescript, changetype, name, changename=None, driver=None, sitename=None, changedescription=None, language=None, changemode=None, tag=None, family=None, conditions=None, parameters=None, rollbackscript=None, desc=None):
        """
        MFNA add_change_plan operation method

        :param changescript: changescript variable. Nullable: False
        :type changescript: str
        :param changetype: changetype variable. Nullable: False
        :type changetype: str
        :param name: name variable. Nullable: False
        :type name: str
        :param changename: changename variable. Nullable: True
        :type changename: str
        :param driver: driver variable. Nullable: True
        :type driver: str
        :param sitename: sitename variable. Nullable: True
        :type sitename: str
        :param changedescription: changedescription variable. Nullable: True
        :type changedescription: str
        :param language: language variable. Nullable: True
        :type language: str
        :param changemode: changemode variable. Nullable: True
        :type changemode: str
        :param tag: tag variable. Nullable: True
        :type tag: str
        :param family: family variable. Nullable: True
        :type family: str
        :param conditions: conditions variable. Nullable: True
        :type conditions: str
        :param parameters: parameters variable. Nullable: True
        :type parameters: str
        :param rollbackscript: rollbackscript variable. Nullable: True
        :type rollbackscript: str
        :param desc: desc variable. Nullable: True
        :type desc: str
        """
        out_args = {'changescript': changescript, 'changetype': changetype, 'name': name, 'changename': changename, 'driver': driver, 'sitename': sitename, 'changedescription': changedescription, 'language': language, 'changemode': changemode, 'tag': tag, 'family': family, 'conditions': conditions, 'parameters': parameters, 'rollbackscript': rollbackscript, 'desc': desc}
        return self.call("add_change_plan", **out_args)

    def add_command_script(self, mode, name, script, scripttype=None, driver=None, sitename=None, description=None):
        """
        MFNA add_command_script operation method

        :param mode: mode variable. Nullable: False
        :type mode: str
        :param name: name variable. Nullable: False
        :type name: str
        :param script: script variable. Nullable: False
        :type script: str
        :param scripttype: scripttype variable. Nullable: True
        :type scripttype: str
        :param driver: driver variable. Nullable: True
        :type driver: str
        :param sitename: sitename variable. Nullable: True
        :type sitename: str
        :param description: description variable. Nullable: True
        :type description: str
        """
        out_args = {'mode': mode, 'name': name, 'script': script, 'scripttype': scripttype, 'driver': driver, 'sitename': sitename, 'description': description}
        return self.call("add_command_script", **out_args)

    def add_device(self, useconsoleserver=None, consoleport=None, nopoll=None, ip=None, origin=None, description=None, forcesave=None, consoleip=None, tftpserverip=None, hostname=None, accessmethods=None, natip=None, serial=None, hierarchylayer=None, vendor=None, domain=None, model=None, location=None, comment=None, asset=None, status=None):
        """
        MFNA add_device operation method

        :param useconsoleserver: useconsoleserver variable. Nullable: True
        :type useconsoleserver: str
        :param consoleport: consoleport variable. Nullable: True
        :type consoleport: str
        :param nopoll: nopoll variable. Nullable: True
        :type nopoll: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param origin: origin variable. Nullable: True
        :type origin: str
        :param description: description variable. Nullable: True
        :type description: str
        :param forcesave: forcesave variable. Nullable: True
        :type forcesave: str
        :param consoleip: consoleip variable. Nullable: True
        :type consoleip: str
        :param tftpserverip: tftpserverip variable. Nullable: True
        :type tftpserverip: str
        :param hostname: hostname variable. Nullable: True
        :type hostname: str
        :param accessmethods: accessmethods variable. Nullable: True
        :type accessmethods: str
        :param natip: natip variable. Nullable: True
        :type natip: str
        :param serial: serial variable. Nullable: True
        :type serial: str
        :param hierarchylayer: hierarchylayer variable. Nullable: True
        :type hierarchylayer: str
        :param vendor: vendor variable. Nullable: True
        :type vendor: str
        :param domain: domain variable. Nullable: True
        :type domain: str
        :param model: model variable. Nullable: True
        :type model: str
        :param location: location variable. Nullable: True
        :type location: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param asset: asset variable. Nullable: True
        :type asset: str
        :param status: status variable. Nullable: True
        :type status: str
        """
        out_args = {'useconsoleserver': useconsoleserver, 'consoleport': consoleport, 'nopoll': nopoll, 'ip': ip, 'origin': origin, 'description': description, 'forcesave': forcesave, 'consoleip': consoleip, 'tftpserverip': tftpserverip, 'hostname': hostname, 'accessmethods': accessmethods, 'natip': natip, 'serial': serial, 'hierarchylayer': hierarchylayer, 'vendor': vendor, 'domain': domain, 'model': model, 'location': location, 'comment': comment, 'asset': asset, 'status': status}
        return self.call("add_device", **out_args)

    def add_device_context(self, contextvariables, deviceid, useaaa=None, enablepasswd=None, snmpro=None, passwd=None, taskname=None, user=None, snmprw=None):
        """
        MFNA add_device_context operation method

        :param contextvariables: contextvariables variable. Nullable: False
        :type contextvariables: str
        :param deviceid: deviceid variable. Nullable: False
        :type deviceid: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        """
        out_args = {'contextvariables': contextvariables, 'deviceid': deviceid, 'useaaa': useaaa, 'enablepasswd': enablepasswd, 'snmpro': snmpro, 'passwd': passwd, 'taskname': taskname, 'user': user, 'snmprw': snmprw}
        return self.call("add_device_context", **out_args)

    def add_device_group(self, name, partitions=None, shared=None, searchgroups=None, criteria=None, limitsearchgroups=None, comment=None, type=None):
        """
        MFNA add_device_group operation method

        :param name: name variable. Nullable: False
        :type name: str
        :param partitions: partitions variable. Nullable: True
        :type partitions: str
        :param shared: shared variable. Nullable: True
        :type shared: str
        :param searchgroups: searchgroups variable. Nullable: True
        :type searchgroups: str
        :param criteria: criteria variable. Nullable: True
        :type criteria: str
        :param limitsearchgroups: limitsearchgroups variable. Nullable: True
        :type limitsearchgroups: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param type: type variable. Nullable: True
        :type type: str
        """
        out_args = {'name': name, 'partitions': partitions, 'shared': shared, 'searchgroups': searchgroups, 'criteria': criteria, 'limitsearchgroups': limitsearchgroups, 'comment': comment, 'type': type}
        return self.call("add_device_group", **out_args)

    def add_device_relationship(self, createdby, relationshiptypeid, origindeviceid, destdeviceid):
        """
        MFNA add_device_relationship operation method

        :param createdby: createdby variable. Nullable: False
        :type createdby: str
        :param relationshiptypeid: relationshiptypeid variable. Nullable: False
        :type relationshiptypeid: str
        :param origindeviceid: origindeviceid variable. Nullable: False
        :type origindeviceid: str
        :param destdeviceid: destdeviceid variable. Nullable: False
        :type destdeviceid: str
        """
        out_args = {'createdby': createdby, 'relationshiptypeid': relationshiptypeid, 'origindeviceid': origindeviceid, 'destdeviceid': destdeviceid}
        return self.call("add_device_relationship", **out_args)

    def add_device_template(self, hostname, customnames=None, customvalue=None, description=None, accessmethods=None, driver=None, hierarchylayer=None, vendor=None, customname=None, sitename=None, comment=None, model=None, location=None, customvalues=None):
        """
        MFNA add_device_template operation method

        :param hostname: hostname variable. Nullable: False
        :type hostname: str
        :param customnames: customnames variable. Nullable: True
        :type customnames: str
        :param customvalue: customvalue variable. Nullable: True
        :type customvalue: str
        :param description: description variable. Nullable: True
        :type description: str
        :param accessmethods: accessmethods variable. Nullable: True
        :type accessmethods: str
        :param driver: driver variable. Nullable: True
        :type driver: str
        :param hierarchylayer: hierarchylayer variable. Nullable: True
        :type hierarchylayer: str
        :param vendor: vendor variable. Nullable: True
        :type vendor: str
        :param customname: customname variable. Nullable: True
        :type customname: str
        :param sitename: sitename variable. Nullable: True
        :type sitename: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param model: model variable. Nullable: True
        :type model: str
        :param location: location variable. Nullable: True
        :type location: str
        :param customvalues: customvalues variable. Nullable: True
        :type customvalues: str
        """
        out_args = {'hostname': hostname, 'customnames': customnames, 'customvalue': customvalue, 'description': description, 'accessmethods': accessmethods, 'driver': driver, 'hierarchylayer': hierarchylayer, 'vendor': vendor, 'customname': customname, 'sitename': sitename, 'comment': comment, 'model': model, 'location': location, 'customvalues': customvalues}
        return self.call("add_device_template", **out_args)

    def add_device_to_group(self, group, deviceid=None, ip=None, host=None, fqdn=None):
        """
        MFNA add_device_to_group operation method

        :param group: group variable. Nullable: False
        :type group: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        """
        out_args = {'group': group, 'deviceid': deviceid, 'ip': ip, 'host': host, 'fqdn': fqdn}
        return self.call("add_device_to_group", **out_args)

    def add_diagnostic(self, mode, name, script, driver=None, sitename=None, description=None):
        """
        MFNA add_diagnostic operation method

        :param mode: mode variable. Nullable: False
        :type mode: str
        :param name: name variable. Nullable: False
        :type name: str
        :param script: script variable. Nullable: False
        :type script: str
        :param driver: driver variable. Nullable: True
        :type driver: str
        :param sitename: sitename variable. Nullable: True
        :type sitename: str
        :param description: description variable. Nullable: True
        :type description: str
        """
        out_args = {'mode': mode, 'name': name, 'script': script, 'driver': driver, 'sitename': sitename, 'description': description}
        return self.call("add_diagnostic", **out_args)

    def add_event(self, message, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA add_event operation method

        :param message: message variable. Nullable: False
        :type message: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'message': message, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("add_event", **out_args)

    def add_event_rule(self, name, action, site=None, eventtext=None, receiverport=None, community=None, events=None, eventtemplate=None, receiverhost=None):
        """
        MFNA add_event_rule operation method

        :param name: name variable. Nullable: False
        :type name: str
        :param action: action variable. Nullable: False
        :type action: str
        :param site: site variable. Nullable: True
        :type site: str
        :param eventtext: eventtext variable. Nullable: True
        :type eventtext: str
        :param receiverport: receiverport variable. Nullable: True
        :type receiverport: str
        :param community: community variable. Nullable: True
        :type community: str
        :param events: events variable. Nullable: True
        :type events: str
        :param eventtemplate: eventtemplate variable. Nullable: True
        :type eventtemplate: str
        :param receiverhost: receiverhost variable. Nullable: True
        :type receiverhost: str
        """
        out_args = {'name': name, 'action': action, 'site': site, 'eventtext': eventtext, 'receiverport': receiverport, 'community': community, 'events': events, 'eventtemplate': eventtemplate, 'receiverhost': receiverhost}
        return self.call("add_event_rule", **out_args)

    def add_group(self, name, type, shared=None, comment=None):
        """
        MFNA add_group operation method

        :param name: name variable. Nullable: False
        :type name: str
        :param type: type variable. Nullable: False
        :type type: str
        :param shared: shared variable. Nullable: True
        :type shared: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        """
        out_args = {'name': name, 'type': type, 'shared': shared, 'comment': comment}
        return self.call("add_group", **out_args)

    def add_group_to_parent_group(self, parent, child):
        """
        MFNA add_group_to_parent_group operation method

        :param parent: parent variable. Nullable: False
        :type parent: str
        :param child: child variable. Nullable: False
        :type child: str
        """
        out_args = {'parent': parent, 'child': child}
        return self.call("add_group_to_parent_group", **out_args)

    def add_image(self, images, imageset, bootrom=None, site=None, memory=None, driver=None, model=None, processor=None):
        """
        MFNA add_image operation method

        :param images: images variable. Nullable: False
        :type images: str
        :param imageset: imageset variable. Nullable: False
        :type imageset: str
        :param bootrom: bootrom variable. Nullable: True
        :type bootrom: str
        :param site: site variable. Nullable: True
        :type site: str
        :param memory: memory variable. Nullable: True
        :type memory: str
        :param driver: driver variable. Nullable: True
        :type driver: str
        :param model: model variable. Nullable: True
        :type model: str
        :param processor: processor variable. Nullable: True
        :type processor: str
        """
        out_args = {'images': images, 'imageset': imageset, 'bootrom': bootrom, 'site': site, 'memory': memory, 'driver': driver, 'model': model, 'processor': processor}
        return self.call("add_image", **out_args)

    def add_imageoption(self, imageprocessors=None, imagebootroms=None, imagemodels=None):
        """
        MFNA add_imageoption operation method

        :param imageprocessors: imageprocessors variable. Nullable: True
        :type imageprocessors: str
        :param imagebootroms: imagebootroms variable. Nullable: True
        :type imagebootroms: str
        :param imagemodels: imagemodels variable. Nullable: True
        :type imagemodels: str
        """
        out_args = {'imageprocessors': imageprocessors, 'imagebootroms': imagebootroms, 'imagemodels': imagemodels}
        return self.call("add_imageoption", **out_args)

    def add_ip(self, deviceip, ipvalue, usetoaccess=None, comment=None):
        """
        MFNA add_ip operation method

        :param deviceip: deviceip variable. Nullable: False
        :type deviceip: str
        :param ipvalue: ipvalue variable. Nullable: False
        :type ipvalue: str
        :param usetoaccess: usetoaccess variable. Nullable: True
        :type usetoaccess: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        """
        out_args = {'deviceip': deviceip, 'ipvalue': ipvalue, 'usetoaccess': usetoaccess, 'comment': comment}
        return self.call("add_ip", **out_args)

    def add_metadata(self, fieldid, associatedtableid, data=None):
        """
        MFNA add_metadata operation method

        :param fieldid: fieldid variable. Nullable: False
        :type fieldid: str
        :param associatedtableid: associatedtableid variable. Nullable: False
        :type associatedtableid: str
        :param data: data variable. Nullable: True
        :type data: str
        """
        out_args = {'fieldid': fieldid, 'associatedtableid': associatedtableid, 'data': data}
        return self.call("add_metadata", **out_args)

    def add_metadata_field(self, fieldname, associatedtable, flags=None, inuse=None, fieldvalues=None):
        """
        MFNA add_metadata_field operation method

        :param fieldname: fieldname variable. Nullable: False
        :type fieldname: str
        :param associatedtable: associatedtable variable. Nullable: False
        :type associatedtable: str
        :param flags: flags variable. Nullable: True
        :type flags: str
        :param inuse: inuse variable. Nullable: True
        :type inuse: str
        :param fieldvalues: fieldvalues variable. Nullable: True
        :type fieldvalues: str
        """
        out_args = {'fieldname': fieldname, 'associatedtable': associatedtable, 'flags': flags, 'inuse': inuse, 'fieldvalues': fieldvalues}
        return self.call("add_metadata_field", **out_args)

    def add_nnmi_integration(self, nnmiport, nnmiusername, nnmiusesssl, nnmipassword, nnmihostname, nnmisystemid, nausername, enabled=None):
        """
        MFNA add_nnmi_integration operation method

        :param nnmiport: nnmiport variable. Nullable: False
        :type nnmiport: str
        :param nnmiusername: nnmiusername variable. Nullable: False
        :type nnmiusername: str
        :param nnmiusesssl: nnmiusesssl variable. Nullable: False
        :type nnmiusesssl: str
        :param nnmipassword: nnmipassword variable. Nullable: False
        :type nnmipassword: str
        :param nnmihostname: nnmihostname variable. Nullable: False
        :type nnmihostname: str
        :param nnmisystemid: nnmisystemid variable. Nullable: False
        :type nnmisystemid: str
        :param nausername: nausername variable. Nullable: False
        :type nausername: str
        :param enabled: enabled variable. Nullable: True
        :type enabled: str
        """
        out_args = {'nnmiport': nnmiport, 'nnmiusername': nnmiusername, 'nnmiusesssl': nnmiusesssl, 'nnmipassword': nnmipassword, 'nnmihostname': nnmihostname, 'nnmisystemid': nnmisystemid, 'nausername': nausername, 'enabled': enabled}
        return self.call("add_nnmi_integration", **out_args)

    def add_nnmi_node_association(self, nnminodeuuid, deviceid, nnmisystemid):
        """
        MFNA add_nnmi_node_association operation method

        :param nnminodeuuid: nnminodeuuid variable. Nullable: False
        :type nnminodeuuid: str
        :param deviceid: deviceid variable. Nullable: False
        :type deviceid: str
        :param nnmisystemid: nnmisystemid variable. Nullable: False
        :type nnmisystemid: str
        """
        out_args = {'nnminodeuuid': nnminodeuuid, 'deviceid': deviceid, 'nnmisystemid': nnmisystemid}
        return self.call("add_nnmi_node_association", **out_args)

    def add_parent_group(self, name, type, comment=None):
        """
        MFNA add_parent_group operation method

        :param name: name variable. Nullable: False
        :type name: str
        :param type: type variable. Nullable: False
        :type type: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        """
        out_args = {'name': name, 'type': type, 'comment': comment}
        return self.call("add_parent_group", **out_args)

    def add_partition(self, viewname, name, comment=None):
        """
        MFNA add_partition operation method

        :param viewname: viewname variable. Nullable: False
        :type viewname: str
        :param name: name variable. Nullable: False
        :type name: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        """
        out_args = {'viewname': viewname, 'name': name, 'comment': comment}
        return self.call("add_partition", **out_args)

    def add_resource_id(self, name, poolid, description=None, status=None):
        """
        MFNA add_resource_id operation method

        :param name: name variable. Nullable: False
        :type name: str
        :param poolid: poolid variable. Nullable: False
        :type poolid: str
        :param description: description variable. Nullable: True
        :type description: str
        :param status: status variable. Nullable: True
        :type status: str
        """
        out_args = {'name': name, 'poolid': poolid, 'description': description, 'status': status}
        return self.call("add_resource_id", **out_args)

    def add_resource_id_pool(self, name, site=None, description=None):
        """
        MFNA add_resource_id_pool operation method

        :param name: name variable. Nullable: False
        :type name: str
        :param site: site variable. Nullable: True
        :type site: str
        :param description: description variable. Nullable: True
        :type description: str
        """
        out_args = {'name': name, 'site': site, 'description': description}
        return self.call("add_resource_id_pool", **out_args)

    def add_role(self, name, resources, type, viewname=None, desc=None):
        """
        MFNA add_role operation method

        :param name: name variable. Nullable: False
        :type name: str
        :param resources: resources variable. Nullable: False
        :type resources: str
        :param type: type variable. Nullable: False
        :type type: str
        :param viewname: viewname variable. Nullable: True
        :type viewname: str
        :param desc: desc variable. Nullable: True
        :type desc: str
        """
        out_args = {'name': name, 'resources': resources, 'type': type, 'viewname': viewname, 'desc': desc}
        return self.call("add_role", **out_args)

    def add_service_type(self, service, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA add_service_type operation method

        :param service: service variable. Nullable: False
        :type service: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'service': service, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("add_service_type", **out_args)

    def add_snmp_trap_config(self, value):
        """
        MFNA add_snmp_trap_config operation method

        :param value: value variable. Nullable: False
        :type value: str
        """
        out_args = {'value': value}
        return self.call("add_snmp_trap_config", **out_args)

    def add_system_message(self, message, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA add_system_message operation method

        :param message: message variable. Nullable: False
        :type message: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'message': message, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("add_system_message", **out_args)

    def add_user(self, p, u, ln=None, aaausername=None, fn=None, extauthfailover=None, useaaaloginforproxy=None, email=None, aaapassword=None):
        """
        MFNA add_user operation method

        :param p: p variable. Nullable: False
        :type p: str
        :param u: u variable. Nullable: False
        :type u: str
        :param ln: ln variable. Nullable: True
        :type ln: str
        :param aaausername: aaausername variable. Nullable: True
        :type aaausername: str
        :param fn: fn variable. Nullable: True
        :type fn: str
        :param extauthfailover: extauthfailover variable. Nullable: True
        :type extauthfailover: str
        :param useaaaloginforproxy: useaaaloginforproxy variable. Nullable: True
        :type useaaaloginforproxy: str
        :param email: email variable. Nullable: True
        :type email: str
        :param aaapassword: aaapassword variable. Nullable: True
        :type aaapassword: str
        """
        out_args = {'p': p, 'u': u, 'ln': ln, 'aaausername': aaausername, 'fn': fn, 'extauthfailover': extauthfailover, 'useaaaloginforproxy': useaaaloginforproxy, 'email': email, 'aaapassword': aaapassword}
        return self.call("add_user", **out_args)

    def add_user_to_group(self, u, g):
        """
        MFNA add_user_to_group operation method

        :param u: u variable. Nullable: False
        :type u: str
        :param g: g variable. Nullable: False
        :type g: str
        """
        out_args = {'u': u, 'g': g}
        return self.call("add_user_to_group", **out_args)

    def add_vlan(self, vlanid, vlanname, sessionlog=None, enablepasswd=None, retrycount=None, snmpro=None, start=None, taskname=None, priority=None, sync=None, maxwaittime=None, useaaa=None, retryinterval=None, addports=None, passwd=None, postsnapshot=None, comment=None, presnapshot=None, rep=None, user=None, snmprw=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA add_vlan operation method

        :param vlanid: vlanid variable. Nullable: False
        :type vlanid: str
        :param vlanname: vlanname variable. Nullable: False
        :type vlanname: str
        :param sessionlog: sessionlog variable. Nullable: True
        :type sessionlog: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param retrycount: retrycount variable. Nullable: True
        :type retrycount: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param start: start variable. Nullable: True
        :type start: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param sync: sync variable. Nullable: True
        :type sync: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param retryinterval: retryinterval variable. Nullable: True
        :type retryinterval: str
        :param addports: addports variable. Nullable: True
        :type addports: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param postsnapshot: postsnapshot variable. Nullable: True
        :type postsnapshot: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param presnapshot: presnapshot variable. Nullable: True
        :type presnapshot: str
        :param rep: rep variable. Nullable: True
        :type rep: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'vlanid': vlanid, 'vlanname': vlanname, 'sessionlog': sessionlog, 'enablepasswd': enablepasswd, 'retrycount': retrycount, 'snmpro': snmpro, 'start': start, 'taskname': taskname, 'priority': priority, 'sync': sync, 'maxwaittime': maxwaittime, 'useaaa': useaaa, 'retryinterval': retryinterval, 'addports': addports, 'passwd': passwd, 'postsnapshot': postsnapshot, 'comment': comment, 'presnapshot': presnapshot, 'rep': rep, 'user': user, 'snmprw': snmprw, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("add_vlan", **out_args)

    def add_vlan_trunk(self, portname, addvlanids, sessionlog=None, enablepasswd=None, retrycount=None, nativevlanid=None, snmpro=None, start=None, taskname=None, priority=None, sync=None, maxwaittime=None, useaaa=None, retryinterval=None, passwd=None, postsnapshot=None, comment=None, presnapshot=None, rep=None, user=None, snmprw=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA add_vlan_trunk operation method

        :param portname: portname variable. Nullable: False
        :type portname: str
        :param addvlanids: addvlanids variable. Nullable: False
        :type addvlanids: str
        :param sessionlog: sessionlog variable. Nullable: True
        :type sessionlog: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param retrycount: retrycount variable. Nullable: True
        :type retrycount: str
        :param nativevlanid: nativevlanid variable. Nullable: True
        :type nativevlanid: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param start: start variable. Nullable: True
        :type start: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param sync: sync variable. Nullable: True
        :type sync: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param retryinterval: retryinterval variable. Nullable: True
        :type retryinterval: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param postsnapshot: postsnapshot variable. Nullable: True
        :type postsnapshot: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param presnapshot: presnapshot variable. Nullable: True
        :type presnapshot: str
        :param rep: rep variable. Nullable: True
        :type rep: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'portname': portname, 'addvlanids': addvlanids, 'sessionlog': sessionlog, 'enablepasswd': enablepasswd, 'retrycount': retrycount, 'nativevlanid': nativevlanid, 'snmpro': snmpro, 'start': start, 'taskname': taskname, 'priority': priority, 'sync': sync, 'maxwaittime': maxwaittime, 'useaaa': useaaa, 'retryinterval': retryinterval, 'passwd': passwd, 'postsnapshot': postsnapshot, 'comment': comment, 'presnapshot': presnapshot, 'rep': rep, 'user': user, 'snmprw': snmprw, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("add_vlan_trunk", **out_args)

    def annotate_access(self, id, customnames=None, name=None, customname=None, customvalue=None, comment=None, customvalues=None):
        """
        MFNA annotate_access operation method

        :param id: id variable. Nullable: False
        :type id: str
        :param customnames: customnames variable. Nullable: True
        :type customnames: str
        :param name: name variable. Nullable: True
        :type name: str
        :param customname: customname variable. Nullable: True
        :type customname: str
        :param customvalue: customvalue variable. Nullable: True
        :type customvalue: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param customvalues: customvalues variable. Nullable: True
        :type customvalues: str
        """
        out_args = {'id': id, 'customnames': customnames, 'name': name, 'customname': customname, 'customvalue': customvalue, 'comment': comment, 'customvalues': customvalues}
        return self.call("annotate_access", **out_args)

    def annotate_config(self, comment, id):
        """
        MFNA annotate_config operation method

        :param comment: comment variable. Nullable: False
        :type comment: str
        :param id: id variable. Nullable: False
        :type id: str
        """
        out_args = {'comment': comment, 'id': id}
        return self.call("annotate_config", **out_args)

    def assign_auto_remediation_script(self, scriptid, ruleid):
        """
        MFNA assign_auto_remediation_script operation method

        :param scriptid: scriptid variable. Nullable: False
        :type scriptid: str
        :param ruleid: ruleid variable. Nullable: False
        :type ruleid: str
        """
        out_args = {'scriptid': scriptid, 'ruleid': ruleid}
        return self.call("assign_auto_remediation_script", **out_args)

    def assign_driver(self, ip=None, name=None, id=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA assign_driver operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param name: name variable. Nullable: True
        :type name: str
        :param id: id variable. Nullable: True
        :type id: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'name': name, 'id': id, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("assign_driver", **out_args)

    def check_policy_compliance(self, types, runmode=None, sessionlog=None, retrycount=None, stoponfailure=None, ip=None, start=None, taskname=None, priority=None, deviceid=None, sync=None, maxwaittime=None, retryinterval=None, comment=None, rep=None, group=None, host=None, fqdn=None):
        """
        MFNA check_policy_compliance operation method

        :param types: types variable. Nullable: False
        :type types: str
        :param runmode: runmode variable. Nullable: True
        :type runmode: str
        :param sessionlog: sessionlog variable. Nullable: True
        :type sessionlog: str
        :param retrycount: retrycount variable. Nullable: True
        :type retrycount: str
        :param stoponfailure: stoponfailure variable. Nullable: True
        :type stoponfailure: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param start: start variable. Nullable: True
        :type start: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        :param sync: sync variable. Nullable: True
        :type sync: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param retryinterval: retryinterval variable. Nullable: True
        :type retryinterval: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param rep: rep variable. Nullable: True
        :type rep: str
        :param group: group variable. Nullable: True
        :type group: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        """
        out_args = {'types': types, 'runmode': runmode, 'sessionlog': sessionlog, 'retrycount': retrycount, 'stoponfailure': stoponfailure, 'ip': ip, 'start': start, 'taskname': taskname, 'priority': priority, 'deviceid': deviceid, 'sync': sync, 'maxwaittime': maxwaittime, 'retryinterval': retryinterval, 'comment': comment, 'rep': rep, 'group': group, 'host': host, 'fqdn': fqdn}
        return self.call("check_policy_compliance", **out_args)

    def configure_syslog(self, runmode=None, enablepasswd=None, snmpro=None, stoponfailure=None, ip=None, start=None, taskname=None, priority=None, sync=None, maxwaittime=None, useaaa=None, passwd=None, usesyslogrelay=None, comment=None, rep=None, user=None, snmprw=None, group=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA configure_syslog operation method

        :param runmode: runmode variable. Nullable: True
        :type runmode: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param stoponfailure: stoponfailure variable. Nullable: True
        :type stoponfailure: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param start: start variable. Nullable: True
        :type start: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param sync: sync variable. Nullable: True
        :type sync: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param usesyslogrelay: usesyslogrelay variable. Nullable: True
        :type usesyslogrelay: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param rep: rep variable. Nullable: True
        :type rep: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        :param group: group variable. Nullable: True
        :type group: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'runmode': runmode, 'enablepasswd': enablepasswd, 'snmpro': snmpro, 'stoponfailure': stoponfailure, 'ip': ip, 'start': start, 'taskname': taskname, 'priority': priority, 'sync': sync, 'maxwaittime': maxwaittime, 'useaaa': useaaa, 'passwd': passwd, 'usesyslogrelay': usesyslogrelay, 'comment': comment, 'rep': rep, 'user': user, 'snmprw': snmprw, 'group': group, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("configure_syslog", **out_args)

    def create_policy(self, name, policydesc=None, ddate=None, site=None, dg=None, aurl=None, cve=None, solution=None, surl=None, tag=None, exceptions=None, desc=None, status=None):
        """
        MFNA create_policy operation method

        :param name: name variable. Nullable: False
        :type name: str
        :param policydesc: policydesc variable. Nullable: True
        :type policydesc: str
        :param ddate: ddate variable. Nullable: True
        :type ddate: str
        :param site: site variable. Nullable: True
        :type site: str
        :param dg: dg variable. Nullable: True
        :type dg: str
        :param aurl: aurl variable. Nullable: True
        :type aurl: str
        :param cve: cve variable. Nullable: True
        :type cve: str
        :param solution: solution variable. Nullable: True
        :type solution: str
        :param surl: surl variable. Nullable: True
        :type surl: str
        :param tag: tag variable. Nullable: True
        :type tag: str
        :param exceptions: exceptions variable. Nullable: True
        :type exceptions: str
        :param desc: desc variable. Nullable: True
        :type desc: str
        :param status: status variable. Nullable: True
        :type status: str
        """
        out_args = {'name': name, 'policydesc': policydesc, 'ddate': ddate, 'site': site, 'dg': dg, 'aurl': aurl, 'cve': cve, 'solution': solution, 'surl': surl, 'tag': tag, 'exceptions': exceptions, 'desc': desc, 'status': status}
        return self.call("create_policy", **out_args)

    def create_policy_rule(self, policyid, devicefamily, name, type, useblock=None, textblockendpattern=None, textblockstartpattern=None, importance=None, details=None, drivers=None, desc=None):
        """
        MFNA create_policy_rule operation method

        :param policyid: policyid variable. Nullable: False
        :type policyid: str
        :param devicefamily: devicefamily variable. Nullable: False
        :type devicefamily: str
        :param name: name variable. Nullable: False
        :type name: str
        :param type: type variable. Nullable: False
        :type type: str
        :param useblock: useblock variable. Nullable: True
        :type useblock: str
        :param textblockendpattern: textblockendpattern variable. Nullable: True
        :type textblockendpattern: str
        :param textblockstartpattern: textblockstartpattern variable. Nullable: True
        :type textblockstartpattern: str
        :param importance: importance variable. Nullable: True
        :type importance: str
        :param details: details variable. Nullable: True
        :type details: str
        :param drivers: drivers variable. Nullable: True
        :type drivers: str
        :param desc: desc variable. Nullable: True
        :type desc: str
        """
        out_args = {'policyid': policyid, 'devicefamily': devicefamily, 'name': name, 'type': type, 'useblock': useblock, 'textblockendpattern': textblockendpattern, 'textblockstartpattern': textblockstartpattern, 'importance': importance, 'details': details, 'drivers': drivers, 'desc': desc}
        return self.call("create_policy_rule", **out_args)

    def create_rule_condition(self, datamodel, label, ruleid, operator, operand, exceptoperand=None, regex=None, exactorder=None):
        """
        MFNA create_rule_condition operation method

        :param datamodel: datamodel variable. Nullable: False
        :type datamodel: str
        :param label: label variable. Nullable: False
        :type label: str
        :param ruleid: ruleid variable. Nullable: False
        :type ruleid: str
        :param operator: operator variable. Nullable: False
        :type operator: str
        :param operand: operand variable. Nullable: False
        :type operand: str
        :param exceptoperand: exceptoperand variable. Nullable: True
        :type exceptoperand: str
        :param regex: regex variable. Nullable: True
        :type regex: str
        :param exactorder: exactorder variable. Nullable: True
        :type exactorder: str
        """
        out_args = {'datamodel': datamodel, 'label': label, 'ruleid': ruleid, 'operator': operator, 'operand': operand, 'exceptoperand': exceptoperand, 'regex': regex, 'exactorder': exactorder}
        return self.call("create_rule_condition", **out_args)

    def create_rule_exception(self, ruleid, device, pattern=None, expirationdate=None):
        """
        MFNA create_rule_exception operation method

        :param ruleid: ruleid variable. Nullable: False
        :type ruleid: str
        :param device: device variable. Nullable: False
        :type device: str
        :param pattern: pattern variable. Nullable: True
        :type pattern: str
        :param expirationdate: expirationdate variable. Nullable: True
        :type expirationdate: str
        """
        out_args = {'ruleid': ruleid, 'device': device, 'pattern': pattern, 'expirationdate': expirationdate}
        return self.call("create_rule_exception", **out_args)

    def crypto(self, encrypt):
        """
        MFNA crypto operation method

        :param encrypt: encrypt variable. Nullable: False
        :type encrypt: str
        """
        out_args = {'encrypt': encrypt}
        return self.call("crypto", **out_args)

    def deactivate_device(self, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA deactivate_device operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("deactivate_device", **out_args)

    def del_access(self, id=None, cutoff=None):
        """
        MFNA del_access operation method

        :param id: id variable. Nullable: True
        :type id: str
        :param cutoff: cutoff variable. Nullable: True
        :type cutoff: str
        """
        out_args = {'id': id, 'cutoff': cutoff}
        return self.call("del_access", **out_args)

    def del_authentication(self, loc=None, site=None, ip=None, rulename=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA del_authentication operation method

        :param loc: loc variable. Nullable: True
        :type loc: str
        :param site: site variable. Nullable: True
        :type site: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param rulename: rulename variable. Nullable: True
        :type rulename: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'loc': loc, 'site': site, 'ip': ip, 'rulename': rulename, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("del_authentication", **out_args)

    def del_change_plan(self, name=None, id=None):
        """
        MFNA del_change_plan operation method

        :param name: name variable. Nullable: True
        :type name: str
        :param id: id variable. Nullable: True
        :type id: str
        """
        out_args = {'name': name, 'id': id}
        return self.call("del_change_plan", **out_args)

    def del_device(self, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA del_device operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("del_device", **out_args)

    def del_device_context(self, contextvariables, deviceid, useaaa=None, enablepasswd=None, snmpro=None, passwd=None, taskname=None, user=None, snmprw=None):
        """
        MFNA del_device_context operation method

        :param contextvariables: contextvariables variable. Nullable: False
        :type contextvariables: str
        :param deviceid: deviceid variable. Nullable: False
        :type deviceid: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        """
        out_args = {'contextvariables': contextvariables, 'deviceid': deviceid, 'useaaa': useaaa, 'enablepasswd': enablepasswd, 'snmpro': snmpro, 'passwd': passwd, 'taskname': taskname, 'user': user, 'snmprw': snmprw}
        return self.call("del_device_context", **out_args)

    def del_device_data(self, id=None, cutoff=None):
        """
        MFNA del_device_data operation method

        :param id: id variable. Nullable: True
        :type id: str
        :param cutoff: cutoff variable. Nullable: True
        :type cutoff: str
        """
        out_args = {'id': id, 'cutoff': cutoff}
        return self.call("del_device_data", **out_args)

    def del_device_from_group(self, group, deviceid=None, ip=None, host=None, fqdn=None):
        """
        MFNA del_device_from_group operation method

        :param group: group variable. Nullable: False
        :type group: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        """
        out_args = {'group': group, 'deviceid': deviceid, 'ip': ip, 'host': host, 'fqdn': fqdn}
        return self.call("del_device_from_group", **out_args)

    def del_device_relationship(self, relationshipid):
        """
        MFNA del_device_relationship operation method

        :param relationshipid: relationshipid variable. Nullable: False
        :type relationshipid: str
        """
        out_args = {'relationshipid': relationshipid}
        return self.call("del_device_relationship", **out_args)

    def del_device_template(self, templateid):
        """
        MFNA del_device_template operation method

        :param templateid: templateid variable. Nullable: False
        :type templateid: str
        """
        out_args = {'templateid': templateid}
        return self.call("del_device_template", **out_args)

    def del_drivers(self, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA del_drivers operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("del_drivers", **out_args)

    def del_event(self, id):
        """
        MFNA del_event operation method

        :param id: id variable. Nullable: False
        :type id: str
        """
        out_args = {'id': id}
        return self.call("del_event", **out_args)

    def del_group(self, type, name=None, force=None, id=None):
        """
        MFNA del_group operation method

        :param type: type variable. Nullable: False
        :type type: str
        :param name: name variable. Nullable: True
        :type name: str
        :param force: force variable. Nullable: True
        :type force: str
        :param id: id variable. Nullable: True
        :type id: str
        """
        out_args = {'type': type, 'name': name, 'force': force, 'id': id}
        return self.call("del_group", **out_args)

    def del_group_from_parent_group(self, parent, child):
        """
        MFNA del_group_from_parent_group operation method

        :param parent: parent variable. Nullable: False
        :type parent: str
        :param child: child variable. Nullable: False
        :type child: str
        """
        out_args = {'parent': parent, 'child': child}
        return self.call("del_group_from_parent_group", **out_args)

    def del_ip(self, deviceip, ipvalue):
        """
        MFNA del_ip operation method

        :param deviceip: deviceip variable. Nullable: False
        :type deviceip: str
        :param ipvalue: ipvalue variable. Nullable: False
        :type ipvalue: str
        """
        out_args = {'deviceip': deviceip, 'ipvalue': ipvalue}
        return self.call("del_ip", **out_args)

    def del_metadata(self, metadataid):
        """
        MFNA del_metadata operation method

        :param metadataid: metadataid variable. Nullable: False
        :type metadataid: str
        """
        out_args = {'metadataid': metadataid}
        return self.call("del_metadata", **out_args)

    def del_metadata_field(self, fieldid):
        """
        MFNA del_metadata_field operation method

        :param fieldid: fieldid variable. Nullable: False
        :type fieldid: str
        """
        out_args = {'fieldid': fieldid}
        return self.call("del_metadata_field", **out_args)

    def del_nnmi_integration(self, id=None, nnmisystemid=None):
        """
        MFNA del_nnmi_integration operation method

        :param id: id variable. Nullable: True
        :type id: str
        :param nnmisystemid: nnmisystemid variable. Nullable: True
        :type nnmisystemid: str
        """
        out_args = {'id': id, 'nnmisystemid': nnmisystemid}
        return self.call("del_nnmi_integration", **out_args)

    def del_nnmi_node_association(self, deviceid, nnmisystemid, nnminodeuuid=None):
        """
        MFNA del_nnmi_node_association operation method

        :param deviceid: deviceid variable. Nullable: False
        :type deviceid: str
        :param nnmisystemid: nnmisystemid variable. Nullable: False
        :type nnmisystemid: str
        :param nnminodeuuid: nnminodeuuid variable. Nullable: True
        :type nnminodeuuid: str
        """
        out_args = {'deviceid': deviceid, 'nnmisystemid': nnmisystemid, 'nnminodeuuid': nnminodeuuid}
        return self.call("del_nnmi_node_association", **out_args)

    def del_partition(self, name):
        """
        MFNA del_partition operation method

        :param name: name variable. Nullable: False
        :type name: str
        """
        out_args = {'name': name}
        return self.call("del_partition", **out_args)

    def del_resource_id(self, id):
        """
        MFNA del_resource_id operation method

        :param id: id variable. Nullable: False
        :type id: str
        """
        out_args = {'id': id}
        return self.call("del_resource_id", **out_args)

    def del_resource_id_pool(self, id):
        """
        MFNA del_resource_id_pool operation method

        :param id: id variable. Nullable: False
        :type id: str
        """
        out_args = {'id': id}
        return self.call("del_resource_id_pool", **out_args)

    def del_role(self, name):
        """
        MFNA del_role operation method

        :param name: name variable. Nullable: False
        :type name: str
        """
        out_args = {'name': name}
        return self.call("del_role", **out_args)

    def del_script(self, name=None, id=None, type=None):
        """
        MFNA del_script operation method

        :param name: name variable. Nullable: True
        :type name: str
        :param id: id variable. Nullable: True
        :type id: str
        :param type: type variable. Nullable: True
        :type type: str
        """
        out_args = {'name': name, 'id': id, 'type': type}
        return self.call("del_script", **out_args)

    def del_service_type(self, service=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA del_service_type operation method

        :param service: service variable. Nullable: True
        :type service: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'service': service, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("del_service_type", **out_args)

    def del_session(self, id):
        """
        MFNA del_session operation method

        :param id: id variable. Nullable: False
        :type id: str
        """
        out_args = {'id': id}
        return self.call("del_session", **out_args)

    def del_sshfingerprint(self, input=None, realmname=None, hostname=None, id=None, state=None, hostkeyalgorithm=None):
        """
        MFNA del_sshfingerprint operation method

        :param input: input variable. Nullable: True
        :type input: str
        :param realmname: realmname variable. Nullable: True
        :type realmname: str
        :param hostname: hostname variable. Nullable: True
        :type hostname: str
        :param id: id variable. Nullable: True
        :type id: str
        :param state: state variable. Nullable: True
        :type state: str
        :param hostkeyalgorithm: hostkeyalgorithm variable. Nullable: True
        :type hostkeyalgorithm: str
        """
        out_args = {'input': input, 'realmname': realmname, 'hostname': hostname, 'id': id, 'state': state, 'hostkeyalgorithm': hostkeyalgorithm}
        return self.call("del_sshfingerprint", **out_args)

    def del_system_message(self, id):
        """
        MFNA del_system_message operation method

        :param id: id variable. Nullable: False
        :type id: str
        """
        out_args = {'id': id}
        return self.call("del_system_message", **out_args)

    def del_task(self, id):
        """
        MFNA del_task operation method

        :param id: id variable. Nullable: False
        :type id: str
        """
        out_args = {'id': id}
        return self.call("del_task", **out_args)

    def del_user(self, u):
        """
        MFNA del_user operation method

        :param u: u variable. Nullable: False
        :type u: str
        """
        out_args = {'u': u}
        return self.call("del_user", **out_args)

    def del_user_from_group(self, u, g):
        """
        MFNA del_user_from_group operation method

        :param u: u variable. Nullable: False
        :type u: str
        :param g: g variable. Nullable: False
        :type g: str
        """
        out_args = {'u': u, 'g': g}
        return self.call("del_user_from_group", **out_args)

    def del_vlan(self, vlanid, sessionlog=None, enablepasswd=None, retrycount=None, snmpro=None, start=None, taskname=None, priority=None, sync=None, maxwaittime=None, useaaa=None, retryinterval=None, passwd=None, postsnapshot=None, comment=None, presnapshot=None, rep=None, user=None, snmprw=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA del_vlan operation method

        :param vlanid: vlanid variable. Nullable: False
        :type vlanid: str
        :param sessionlog: sessionlog variable. Nullable: True
        :type sessionlog: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param retrycount: retrycount variable. Nullable: True
        :type retrycount: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param start: start variable. Nullable: True
        :type start: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param sync: sync variable. Nullable: True
        :type sync: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param retryinterval: retryinterval variable. Nullable: True
        :type retryinterval: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param postsnapshot: postsnapshot variable. Nullable: True
        :type postsnapshot: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param presnapshot: presnapshot variable. Nullable: True
        :type presnapshot: str
        :param rep: rep variable. Nullable: True
        :type rep: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'vlanid': vlanid, 'sessionlog': sessionlog, 'enablepasswd': enablepasswd, 'retrycount': retrycount, 'snmpro': snmpro, 'start': start, 'taskname': taskname, 'priority': priority, 'sync': sync, 'maxwaittime': maxwaittime, 'useaaa': useaaa, 'retryinterval': retryinterval, 'passwd': passwd, 'postsnapshot': postsnapshot, 'comment': comment, 'presnapshot': presnapshot, 'rep': rep, 'user': user, 'snmprw': snmprw, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("del_vlan", **out_args)

    def del_vlan_trunk(self, nativevlanid, portname, sessionlog=None, enablepasswd=None, retrycount=None, snmpro=None, start=None, taskname=None, priority=None, sync=None, maxwaittime=None, useaaa=None, retryinterval=None, passwd=None, postsnapshot=None, comment=None, presnapshot=None, rep=None, user=None, snmprw=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA del_vlan_trunk operation method

        :param nativevlanid: nativevlanid variable. Nullable: False
        :type nativevlanid: str
        :param portname: portname variable. Nullable: False
        :type portname: str
        :param sessionlog: sessionlog variable. Nullable: True
        :type sessionlog: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param retrycount: retrycount variable. Nullable: True
        :type retrycount: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param start: start variable. Nullable: True
        :type start: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param sync: sync variable. Nullable: True
        :type sync: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param retryinterval: retryinterval variable. Nullable: True
        :type retryinterval: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param postsnapshot: postsnapshot variable. Nullable: True
        :type postsnapshot: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param presnapshot: presnapshot variable. Nullable: True
        :type presnapshot: str
        :param rep: rep variable. Nullable: True
        :type rep: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'nativevlanid': nativevlanid, 'portname': portname, 'sessionlog': sessionlog, 'enablepasswd': enablepasswd, 'retrycount': retrycount, 'snmpro': snmpro, 'start': start, 'taskname': taskname, 'priority': priority, 'sync': sync, 'maxwaittime': maxwaittime, 'useaaa': useaaa, 'retryinterval': retryinterval, 'passwd': passwd, 'postsnapshot': postsnapshot, 'comment': comment, 'presnapshot': presnapshot, 'rep': rep, 'user': user, 'snmprw': snmprw, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("del_vlan_trunk", **out_args)

    def delete_image(self, images, imageset, site=None):
        """
        MFNA delete_image operation method

        :param images: images variable. Nullable: False
        :type images: str
        :param imageset: imageset variable. Nullable: False
        :type imageset: str
        :param site: site variable. Nullable: True
        :type site: str
        """
        out_args = {'images': images, 'imageset': imageset, 'site': site}
        return self.call("delete_image", **out_args)

    def delete_policy(self, policyid):
        """
        MFNA delete_policy operation method

        :param policyid: policyid variable. Nullable: False
        :type policyid: str
        """
        out_args = {'policyid': policyid}
        return self.call("delete_policy", **out_args)

    def delete_policy_rule(self, ruleid):
        """
        MFNA delete_policy_rule operation method

        :param ruleid: ruleid variable. Nullable: False
        :type ruleid: str
        """
        out_args = {'ruleid': ruleid}
        return self.call("delete_policy_rule", **out_args)

    def delete_rule_condition(self, rcid):
        """
        MFNA delete_rule_condition operation method

        :param rcid: rcid variable. Nullable: False
        :type rcid: str
        """
        out_args = {'rcid': rcid}
        return self.call("delete_rule_condition", **out_args)

    def delete_rule_exception(self, exceptionid):
        """
        MFNA delete_rule_exception operation method

        :param exceptionid: exceptionid variable. Nullable: False
        :type exceptionid: str
        """
        out_args = {'exceptionid': exceptionid}
        return self.call("delete_rule_exception", **out_args)

    def deploy_change_plan(self, name, runmode=None, enablepasswd=None, snmpro=None, stoponfailure=None, taskname=None, maxwaittime=None, uselatest=None, presnapshot=None, rep=None, postchangesnapshot=None, group=None, sessionlog=None, variables=None, ip=None, start=None, priority=None, sync=None, useaaa=None, passwd=None, postsnapshot=None, comment=None, parameters=None, user=None, snmprw=None, nowait=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA deploy_change_plan operation method

        :param name: name variable. Nullable: False
        :type name: str
        :param runmode: runmode variable. Nullable: True
        :type runmode: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param stoponfailure: stoponfailure variable. Nullable: True
        :type stoponfailure: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param uselatest: uselatest variable. Nullable: True
        :type uselatest: str
        :param presnapshot: presnapshot variable. Nullable: True
        :type presnapshot: str
        :param rep: rep variable. Nullable: True
        :type rep: str
        :param postchangesnapshot: postchangesnapshot variable. Nullable: True
        :type postchangesnapshot: str
        :param group: group variable. Nullable: True
        :type group: str
        :param sessionlog: sessionlog variable. Nullable: True
        :type sessionlog: str
        :param variables: variables variable. Nullable: True
        :type variables: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param start: start variable. Nullable: True
        :type start: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param sync: sync variable. Nullable: True
        :type sync: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param postsnapshot: postsnapshot variable. Nullable: True
        :type postsnapshot: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param parameters: parameters variable. Nullable: True
        :type parameters: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        :param nowait: nowait variable. Nullable: True
        :type nowait: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'name': name, 'runmode': runmode, 'enablepasswd': enablepasswd, 'snmpro': snmpro, 'stoponfailure': stoponfailure, 'taskname': taskname, 'maxwaittime': maxwaittime, 'uselatest': uselatest, 'presnapshot': presnapshot, 'rep': rep, 'postchangesnapshot': postchangesnapshot, 'group': group, 'sessionlog': sessionlog, 'variables': variables, 'ip': ip, 'start': start, 'priority': priority, 'sync': sync, 'useaaa': useaaa, 'passwd': passwd, 'postsnapshot': postsnapshot, 'comment': comment, 'parameters': parameters, 'user': user, 'snmprw': snmprw, 'nowait': nowait, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("deploy_change_plan", **out_args)

    def deploy_config(self, option, enablepasswd=None, snmpro=None, start=None, taskname=None, priority=None, sync=None, maxwaittime=None, useaaa=None, configtext=None, passwd=None, id=None, user=None, snmprw=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA deploy_config operation method

        :param option: option variable. Nullable: False
        :type option: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param start: start variable. Nullable: True
        :type start: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param sync: sync variable. Nullable: True
        :type sync: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param configtext: configtext variable. Nullable: True
        :type configtext: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param id: id variable. Nullable: True
        :type id: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'option': option, 'enablepasswd': enablepasswd, 'snmpro': snmpro, 'start': start, 'taskname': taskname, 'priority': priority, 'sync': sync, 'maxwaittime': maxwaittime, 'useaaa': useaaa, 'configtext': configtext, 'passwd': passwd, 'id': id, 'user': user, 'snmprw': snmprw, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("deploy_config", **out_args)

    def deploy_image(self, images, imageset, enablepasswd=None, retrycount=None, snmpro=None, posttask=None, taskname=None, duration=None, maxwaittime=None, osslot=None, verify=None, customvalues=None, customnames=None, reboot=None, sessionlog=None, rebootwait=None, customvalue=None, start=None, priority=None, filesystem=None, pretask=None, useaaa=None, retryinterval=None, site=None, passwd=None, customname=None, bootslot=None, comment=None, bootimage=None, osimage=None, user=None, snmprw=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA deploy_image operation method

        :param images: images variable. Nullable: False
        :type images: str
        :param imageset: imageset variable. Nullable: False
        :type imageset: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param retrycount: retrycount variable. Nullable: True
        :type retrycount: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param posttask: posttask variable. Nullable: True
        :type posttask: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param duration: duration variable. Nullable: True
        :type duration: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param osslot: osslot variable. Nullable: True
        :type osslot: str
        :param verify: verify variable. Nullable: True
        :type verify: str
        :param customvalues: customvalues variable. Nullable: True
        :type customvalues: str
        :param customnames: customnames variable. Nullable: True
        :type customnames: str
        :param reboot: reboot variable. Nullable: True
        :type reboot: str
        :param sessionlog: sessionlog variable. Nullable: True
        :type sessionlog: str
        :param rebootwait: rebootwait variable. Nullable: True
        :type rebootwait: str
        :param customvalue: customvalue variable. Nullable: True
        :type customvalue: str
        :param start: start variable. Nullable: True
        :type start: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param filesystem: filesystem variable. Nullable: True
        :type filesystem: str
        :param pretask: pretask variable. Nullable: True
        :type pretask: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param retryinterval: retryinterval variable. Nullable: True
        :type retryinterval: str
        :param site: site variable. Nullable: True
        :type site: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param customname: customname variable. Nullable: True
        :type customname: str
        :param bootslot: bootslot variable. Nullable: True
        :type bootslot: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param bootimage: bootimage variable. Nullable: True
        :type bootimage: str
        :param osimage: osimage variable. Nullable: True
        :type osimage: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'images': images, 'imageset': imageset, 'enablepasswd': enablepasswd, 'retrycount': retrycount, 'snmpro': snmpro, 'posttask': posttask, 'taskname': taskname, 'duration': duration, 'maxwaittime': maxwaittime, 'osslot': osslot, 'verify': verify, 'customvalues': customvalues, 'customnames': customnames, 'reboot': reboot, 'sessionlog': sessionlog, 'rebootwait': rebootwait, 'customvalue': customvalue, 'start': start, 'priority': priority, 'filesystem': filesystem, 'pretask': pretask, 'useaaa': useaaa, 'retryinterval': retryinterval, 'site': site, 'passwd': passwd, 'customname': customname, 'bootslot': bootslot, 'comment': comment, 'bootimage': bootimage, 'osimage': osimage, 'user': user, 'snmprw': snmprw, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("deploy_image", **out_args)

    def diff_config(self, id2, id1):
        """
        MFNA diff_config operation method

        :param id2: id2 variable. Nullable: False
        :type id2: str
        :param id1: id1 variable. Nullable: False
        :type id1: str
        """
        out_args = {'id2': id2, 'id1': id1}
        return self.call("diff_config", **out_args)

    def disable_device(self, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA disable_device operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("disable_device", **out_args)

    def discover_driver(self, runmode=None, maxwaittime=None, useaaa=None, enablepasswd=None, snmpro=None, passwd=None, replace=None, taskname=None, nosync=None, priority=None, user=None, snmprw=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA discover_driver operation method

        :param runmode: runmode variable. Nullable: True
        :type runmode: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param replace: replace variable. Nullable: True
        :type replace: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param nosync: nosync variable. Nullable: True
        :type nosync: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'runmode': runmode, 'maxwaittime': maxwaittime, 'useaaa': useaaa, 'enablepasswd': enablepasswd, 'snmpro': snmpro, 'passwd': passwd, 'replace': replace, 'taskname': taskname, 'nosync': nosync, 'priority': priority, 'user': user, 'snmprw': snmprw, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("discover_driver", **out_args)

    def discover_drivers(self, runmode=None, enablepasswd=None, snmpro=None, stoponfailure=None, noskip=None, replace=None, taskname=None, priority=None, maxwaittime=None, useaaa=None, passwd=None, user=None, snmprw=None, group=None):
        """
        MFNA discover_drivers operation method

        :param runmode: runmode variable. Nullable: True
        :type runmode: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param stoponfailure: stoponfailure variable. Nullable: True
        :type stoponfailure: str
        :param noskip: noskip variable. Nullable: True
        :type noskip: str
        :param replace: replace variable. Nullable: True
        :type replace: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        :param group: group variable. Nullable: True
        :type group: str
        """
        out_args = {'runmode': runmode, 'enablepasswd': enablepasswd, 'snmpro': snmpro, 'stoponfailure': stoponfailure, 'noskip': noskip, 'replace': replace, 'taskname': taskname, 'priority': priority, 'maxwaittime': maxwaittime, 'useaaa': useaaa, 'passwd': passwd, 'user': user, 'snmprw': snmprw, 'group': group}
        return self.call("discover_drivers", **out_args)

    def download_binaryconfig(self, outputfilepath, ip=None, deviceid=None, host=None, fqdn=None):
        """
        MFNA download_binaryconfig operation method

        :param outputfilepath: outputfilepath variable. Nullable: False
        :type outputfilepath: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        """
        out_args = {'outputfilepath': outputfilepath, 'ip': ip, 'deviceid': deviceid, 'host': host, 'fqdn': fqdn}
        return self.call("download_binaryconfig", **out_args)

    def enable_device(self, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA enable_device operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("enable_device", **out_args)

    def export_policy(self, filename, policies):
        """
        MFNA export_policy operation method

        :param filename: filename variable. Nullable: False
        :type filename: str
        :param policies: policies variable. Nullable: False
        :type policies: str
        """
        out_args = {'filename': filename, 'policies': policies}
        return self.call("export_policy", **out_args)

    def export_sshfingerprint(self, filename, all=None, realmname=None, hostname=None, id=None, state=None, hostkeyalgorithm=None):
        """
        MFNA export_sshfingerprint operation method

        :param filename: filename variable. Nullable: False
        :type filename: str
        :param all: all variable. Nullable: True
        :type all: str
        :param realmname: realmname variable. Nullable: True
        :type realmname: str
        :param hostname: hostname variable. Nullable: True
        :type hostname: str
        :param id: id variable. Nullable: True
        :type id: str
        :param state: state variable. Nullable: True
        :type state: str
        :param hostkeyalgorithm: hostkeyalgorithm variable. Nullable: True
        :type hostkeyalgorithm: str
        """
        out_args = {'filename': filename, 'all': all, 'realmname': realmname, 'hostname': hostname, 'id': id, 'state': state, 'hostkeyalgorithm': hostkeyalgorithm}
        return self.call("export_sshfingerprint", **out_args)

    def fulltextsearch(self, numthreads=None, option=None):
        """
        MFNA fulltextsearch operation method

        :param numthreads: numthreads variable. Nullable: True
        :type numthreads: str
        :param option: option variable. Nullable: True
        :type option: str
        """
        out_args = {'numthreads': numthreads, 'option': option}
        return self.call("fulltextsearch", **out_args)

    def get_snapshot(self, runmode=None, checkpoint=None, enablepasswd=None, retrycount=None, snmpro=None, stoponfailure=None, taskname=None, duration=None, maxwaittime=None, customvalues=None, rep=None, group=None, customnames=None, sessionlog=None, ip=None, customvalue=None, start=None, priority=None, sync=None, useaaa=None, retryinterval=None, passwd=None, customname=None, comment=None, user=None, snmprw=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA get_snapshot operation method

        :param runmode: runmode variable. Nullable: True
        :type runmode: str
        :param checkpoint: checkpoint variable. Nullable: True
        :type checkpoint: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param retrycount: retrycount variable. Nullable: True
        :type retrycount: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param stoponfailure: stoponfailure variable. Nullable: True
        :type stoponfailure: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param duration: duration variable. Nullable: True
        :type duration: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param customvalues: customvalues variable. Nullable: True
        :type customvalues: str
        :param rep: rep variable. Nullable: True
        :type rep: str
        :param group: group variable. Nullable: True
        :type group: str
        :param customnames: customnames variable. Nullable: True
        :type customnames: str
        :param sessionlog: sessionlog variable. Nullable: True
        :type sessionlog: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param customvalue: customvalue variable. Nullable: True
        :type customvalue: str
        :param start: start variable. Nullable: True
        :type start: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param sync: sync variable. Nullable: True
        :type sync: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param retryinterval: retryinterval variable. Nullable: True
        :type retryinterval: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param customname: customname variable. Nullable: True
        :type customname: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'runmode': runmode, 'checkpoint': checkpoint, 'enablepasswd': enablepasswd, 'retrycount': retrycount, 'snmpro': snmpro, 'stoponfailure': stoponfailure, 'taskname': taskname, 'duration': duration, 'maxwaittime': maxwaittime, 'customvalues': customvalues, 'rep': rep, 'group': group, 'customnames': customnames, 'sessionlog': sessionlog, 'ip': ip, 'customvalue': customvalue, 'start': start, 'priority': priority, 'sync': sync, 'useaaa': useaaa, 'retryinterval': retryinterval, 'passwd': passwd, 'customname': customname, 'comment': comment, 'user': user, 'snmprw': snmprw, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("get_snapshot", **out_args)

    def _import(self, debug=None, data=None, auth=None, log=None, cleanafter=None, deviceorigin=None, configuresyslog=None, filter=None, input=None, usesyslogrelay=None, discoverafter=None, device=None, append=None):
        """
        MFNA import operation method

        :param debug: debug variable. Nullable: True
        :type debug: str
        :param data: data variable. Nullable: True
        :type data: str
        :param auth: auth variable. Nullable: True
        :type auth: str
        :param log: log variable. Nullable: True
        :type log: str
        :param cleanafter: cleanafter variable. Nullable: True
        :type cleanafter: str
        :param deviceorigin: deviceorigin variable. Nullable: True
        :type deviceorigin: str
        :param configuresyslog: configuresyslog variable. Nullable: True
        :type configuresyslog: str
        :param filter: filter variable. Nullable: True
        :type filter: str
        :param input: input variable. Nullable: True
        :type input: str
        :param usesyslogrelay: usesyslogrelay variable. Nullable: True
        :type usesyslogrelay: str
        :param discoverafter: discoverafter variable. Nullable: True
        :type discoverafter: str
        :param device: device variable. Nullable: True
        :type device: str
        :param append: append variable. Nullable: True
        :type append: str
        """
        out_args = {'debug': debug, 'data': data, 'auth': auth, 'log': log, 'cleanafter': cleanafter, 'deviceorigin': deviceorigin, 'configuresyslog': configuresyslog, 'filter': filter, 'input': input, 'usesyslogrelay': usesyslogrelay, 'discoverafter': discoverafter, 'device': device, 'append': append}
        return self.call("import", **out_args)

    def import_policy(self, filename):
        """
        MFNA import_policy operation method

        :param filename: filename variable. Nullable: False
        :type filename: str
        """
        out_args = {'filename': filename}
        return self.call("import_policy", **out_args)

    def import_sshfingerprint(self, input):
        """
        MFNA import_sshfingerprint operation method

        :param input: input variable. Nullable: False
        :type input: str
        """
        out_args = {'input': input}
        return self.call("import_sshfingerprint", **out_args)

    def list_access(self, start=None, end=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_access operation method

        :param start: start variable. Nullable: True
        :type start: str
        :param end: end variable. Nullable: True
        :type end: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'start': start, 'end': end, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_access", **out_args)

    def list_access_all(self):
        return self.call("list_access_all")

    def list_acl(self, aclid=None, includescript=None, fqdn=None, ip=None, host=None, handle=None, includeapplication=None, deviceid=None, recent=None):
        """
        MFNA list_acl operation method

        :param aclid: aclid variable. Nullable: True
        :type aclid: str
        :param includescript: includescript variable. Nullable: True
        :type includescript: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param handle: handle variable. Nullable: True
        :type handle: str
        :param includeapplication: includeapplication variable. Nullable: True
        :type includeapplication: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        :param recent: recent variable. Nullable: True
        :type recent: str
        """
        out_args = {'aclid': aclid, 'includescript': includescript, 'fqdn': fqdn, 'ip': ip, 'host': host, 'handle': handle, 'includeapplication': includeapplication, 'deviceid': deviceid, 'recent': recent}
        return self.call("list_acl", **out_args)

    def list_all_drivers(self):
        return self.call("list_all_drivers")

    def list_authentication(self, rulename=None):
        """
        MFNA list_authentication operation method

        :param rulename: rulename variable. Nullable: True
        :type rulename: str
        """
        out_args = {'rulename': rulename}
        return self.call("list_authentication", **out_args)

    def list_basicip(self, start=None, end=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_basicip operation method

        :param start: start variable. Nullable: True
        :type start: str
        :param end: end variable. Nullable: True
        :type end: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'start': start, 'end': end, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_basicip", **out_args)

    def list_change_plan(self, name=None, sitename=None, tag=None, family=None):
        """
        MFNA list_change_plan operation method

        :param name: name variable. Nullable: True
        :type name: str
        :param sitename: sitename variable. Nullable: True
        :type sitename: str
        :param tag: tag variable. Nullable: True
        :type tag: str
        :param family: family variable. Nullable: True
        :type family: str
        """
        out_args = {'name': name, 'sitename': sitename, 'tag': tag, 'family': family}
        return self.call("list_change_plan", **out_args)

    def list_config(self, size=None, ip=None, start=None, ids=None, end=None, mask=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_config operation method

        :param size: size variable. Nullable: True
        :type size: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param start: start variable. Nullable: True
        :type start: str
        :param ids: ids variable. Nullable: True
        :type ids: str
        :param end: end variable. Nullable: True
        :type end: str
        :param mask: mask variable. Nullable: True
        :type mask: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'size': size, 'ip': ip, 'start': start, 'ids': ids, 'end': end, 'mask': mask, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_config", **out_args)

    def list_config_all(self):
        return self.call("list_config_all")

    def list_config_id(self, ip=None, start=None, end=None, id=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_config_id operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param start: start variable. Nullable: True
        :type start: str
        :param end: end variable. Nullable: True
        :type end: str
        :param id: id variable. Nullable: True
        :type id: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'start': start, 'end': end, 'id': id, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_config_id", **out_args)

    def list_core(self):
        return self.call("list_core")

    def list_custom_data_definition(self, tablename):
        """
        MFNA list_custom_data_definition operation method

        :param tablename: tablename variable. Nullable: False
        :type tablename: str
        """
        out_args = {'tablename': tablename}
        return self.call("list_custom_data_definition", **out_args)

    def list_device(self, limitcount=None, software=None, ip=None, hierarchy=None, type=None, partition=None, vendor=None, startid=None, vtpdomain=None, host=None, ids=None, model=None, disabled=None, realm=None, family=None, pollexcluded=None, group=None, fqdn=None):
        """
        MFNA list_device operation method

        :param limitcount: limitcount variable. Nullable: True
        :type limitcount: str
        :param software: software variable. Nullable: True
        :type software: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param hierarchy: hierarchy variable. Nullable: True
        :type hierarchy: str
        :param type: type variable. Nullable: True
        :type type: str
        :param partition: partition variable. Nullable: True
        :type partition: str
        :param vendor: vendor variable. Nullable: True
        :type vendor: str
        :param startid: startid variable. Nullable: True
        :type startid: str
        :param vtpdomain: vtpdomain variable. Nullable: True
        :type vtpdomain: str
        :param host: host variable. Nullable: True
        :type host: str
        :param ids: ids variable. Nullable: True
        :type ids: str
        :param model: model variable. Nullable: True
        :type model: str
        :param disabled: disabled variable. Nullable: True
        :type disabled: str
        :param realm: realm variable. Nullable: True
        :type realm: str
        :param family: family variable. Nullable: True
        :type family: str
        :param pollexcluded: pollexcluded variable. Nullable: True
        :type pollexcluded: str
        :param group: group variable. Nullable: True
        :type group: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        """
        out_args = {'limitcount': limitcount, 'software': software, 'ip': ip, 'hierarchy': hierarchy, 'type': type, 'partition': partition, 'vendor': vendor, 'startid': startid, 'vtpdomain': vtpdomain, 'host': host, 'ids': ids, 'model': model, 'disabled': disabled, 'realm': realm, 'family': family, 'pollexcluded': pollexcluded, 'group': group, 'fqdn': fqdn}
        return self.call("list_device", **out_args)

    def list_device_context_variables(self, action, deviceid):
        """
        MFNA list_device_context_variables operation method

        :param action: action variable. Nullable: False
        :type action: str
        :param deviceid: deviceid variable. Nullable: False
        :type deviceid: str
        """
        out_args = {'action': action, 'deviceid': deviceid}
        return self.call("list_device_context_variables", **out_args)

    def list_device_data(self, datatype=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_device_data operation method

        :param datatype: datatype variable. Nullable: True
        :type datatype: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'datatype': datatype, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_device_data", **out_args)

    def list_device_family(self, software=None, vendor=None, model=None, type=None, group=None):
        """
        MFNA list_device_family operation method

        :param software: software variable. Nullable: True
        :type software: str
        :param vendor: vendor variable. Nullable: True
        :type vendor: str
        :param model: model variable. Nullable: True
        :type model: str
        :param type: type variable. Nullable: True
        :type type: str
        :param group: group variable. Nullable: True
        :type group: str
        """
        out_args = {'software': software, 'vendor': vendor, 'model': model, 'type': type, 'group': group}
        return self.call("list_device_family", **out_args)

    def list_device_group(self, parent=None, software=None, vendor=None, model=None, type=None, family=None):
        """
        MFNA list_device_group operation method

        :param parent: parent variable. Nullable: True
        :type parent: str
        :param software: software variable. Nullable: True
        :type software: str
        :param vendor: vendor variable. Nullable: True
        :type vendor: str
        :param model: model variable. Nullable: True
        :type model: str
        :param type: type variable. Nullable: True
        :type type: str
        :param family: family variable. Nullable: True
        :type family: str
        """
        out_args = {'parent': parent, 'software': software, 'vendor': vendor, 'model': model, 'type': type, 'family': family}
        return self.call("list_device_group", **out_args)

    def list_device_id(self, software=None, ip=None, hierarchy=None, type=None, vendor=None, host=None, viewable_by=None, model=None, disabled=None, realm=None, id=None, family=None, pollexcluded=None, group=None, fqdn=None):
        """
        MFNA list_device_id operation method

        :param software: software variable. Nullable: True
        :type software: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param hierarchy: hierarchy variable. Nullable: True
        :type hierarchy: str
        :param type: type variable. Nullable: True
        :type type: str
        :param vendor: vendor variable. Nullable: True
        :type vendor: str
        :param host: host variable. Nullable: True
        :type host: str
        :param viewable_by: viewable_by variable. Nullable: True
        :type viewable_by: str
        :param model: model variable. Nullable: True
        :type model: str
        :param disabled: disabled variable. Nullable: True
        :type disabled: str
        :param realm: realm variable. Nullable: True
        :type realm: str
        :param id: id variable. Nullable: True
        :type id: str
        :param family: family variable. Nullable: True
        :type family: str
        :param pollexcluded: pollexcluded variable. Nullable: True
        :type pollexcluded: str
        :param group: group variable. Nullable: True
        :type group: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        """
        out_args = {'software': software, 'ip': ip, 'hierarchy': hierarchy, 'type': type, 'vendor': vendor, 'host': host, 'viewable_by': viewable_by, 'model': model, 'disabled': disabled, 'realm': realm, 'id': id, 'family': family, 'pollexcluded': pollexcluded, 'group': group, 'fqdn': fqdn}
        return self.call("list_device_id", **out_args)

    def list_device_model(self, software=None, vendor=None, type=None, family=None, group=None):
        """
        MFNA list_device_model operation method

        :param software: software variable. Nullable: True
        :type software: str
        :param vendor: vendor variable. Nullable: True
        :type vendor: str
        :param type: type variable. Nullable: True
        :type type: str
        :param family: family variable. Nullable: True
        :type family: str
        :param group: group variable. Nullable: True
        :type group: str
        """
        out_args = {'software': software, 'vendor': vendor, 'type': type, 'family': family, 'group': group}
        return self.call("list_device_model", **out_args)

    def list_device_nnm(self):
        return self.call("list_device_nnm")

    def list_device_relationships(self, createdby=None, relationshipid=None, relationshiptypeid=None, origindeviceid=None, destdeviceid=None):
        """
        MFNA list_device_relationships operation method

        :param createdby: createdby variable. Nullable: True
        :type createdby: str
        :param relationshipid: relationshipid variable. Nullable: True
        :type relationshipid: str
        :param relationshiptypeid: relationshiptypeid variable. Nullable: True
        :type relationshiptypeid: str
        :param origindeviceid: origindeviceid variable. Nullable: True
        :type origindeviceid: str
        :param destdeviceid: destdeviceid variable. Nullable: True
        :type destdeviceid: str
        """
        out_args = {'createdby': createdby, 'relationshipid': relationshipid, 'relationshiptypeid': relationshiptypeid, 'origindeviceid': origindeviceid, 'destdeviceid': destdeviceid}
        return self.call("list_device_relationships", **out_args)

    def list_device_software(self, vendor=None, model=None, type=None, family=None, group=None):
        """
        MFNA list_device_software operation method

        :param vendor: vendor variable. Nullable: True
        :type vendor: str
        :param model: model variable. Nullable: True
        :type model: str
        :param type: type variable. Nullable: True
        :type type: str
        :param family: family variable. Nullable: True
        :type family: str
        :param group: group variable. Nullable: True
        :type group: str
        """
        out_args = {'vendor': vendor, 'model': model, 'type': type, 'family': family, 'group': group}
        return self.call("list_device_software", **out_args)

    def list_device_template(self, deviceip=None, vendor=None, host=None, model=None, type=None, deviceid=None):
        """
        MFNA list_device_template operation method

        :param deviceip: deviceip variable. Nullable: True
        :type deviceip: str
        :param vendor: vendor variable. Nullable: True
        :type vendor: str
        :param host: host variable. Nullable: True
        :type host: str
        :param model: model variable. Nullable: True
        :type model: str
        :param type: type variable. Nullable: True
        :type type: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'deviceip': deviceip, 'vendor': vendor, 'host': host, 'model': model, 'type': type, 'deviceid': deviceid}
        return self.call("list_device_template", **out_args)

    def list_device_type(self, software=None, vendor=None, model=None, family=None, group=None):
        """
        MFNA list_device_type operation method

        :param software: software variable. Nullable: True
        :type software: str
        :param vendor: vendor variable. Nullable: True
        :type vendor: str
        :param model: model variable. Nullable: True
        :type model: str
        :param family: family variable. Nullable: True
        :type family: str
        :param group: group variable. Nullable: True
        :type group: str
        """
        out_args = {'software': software, 'vendor': vendor, 'model': model, 'family': family, 'group': group}
        return self.call("list_device_type", **out_args)

    def list_device_vendor(self, software=None, model=None, type=None, family=None, group=None):
        """
        MFNA list_device_vendor operation method

        :param software: software variable. Nullable: True
        :type software: str
        :param model: model variable. Nullable: True
        :type model: str
        :param type: type variable. Nullable: True
        :type type: str
        :param family: family variable. Nullable: True
        :type family: str
        :param group: group variable. Nullable: True
        :type group: str
        """
        out_args = {'software': software, 'model': model, 'type': type, 'family': family, 'group': group}
        return self.call("list_device_vendor", **out_args)

    def list_device_vtp(self, domain):
        """
        MFNA list_device_vtp operation method

        :param domain: domain variable. Nullable: False
        :type domain: str
        """
        out_args = {'domain': domain}
        return self.call("list_device_vtp", **out_args)

    def list_deviceinfo(self, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_deviceinfo operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_deviceinfo", **out_args)

    def list_diagnostic(self, diagnostic, start=None, end=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_diagnostic operation method

        :param diagnostic: diagnostic variable. Nullable: False
        :type diagnostic: str
        :param start: start variable. Nullable: True
        :type start: str
        :param end: end variable. Nullable: True
        :type end: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'diagnostic': diagnostic, 'start': start, 'end': end, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_diagnostic", **out_args)

    def list_diagnostic_all(self):
        return self.call("list_diagnostic_all")

    def list_event(self, ip=None, start=None, end=None, type=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_event operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param start: start variable. Nullable: True
        :type start: str
        :param end: end variable. Nullable: True
        :type end: str
        :param type: type variable. Nullable: True
        :type type: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'start': start, 'end': end, 'type': type, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_event", **out_args)

    def list_group_id(self, type, viewable_by=None):
        """
        MFNA list_group_id operation method

        :param type: type variable. Nullable: False
        :type type: str
        :param viewable_by: viewable_by variable. Nullable: True
        :type viewable_by: str
        """
        out_args = {'type': type, 'viewable_by': viewable_by}
        return self.call("list_group_id", **out_args)

    def list_groups(self, type, parent=None, grouptype=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_groups operation method

        :param type: type variable. Nullable: False
        :type type: str
        :param parent: parent variable. Nullable: True
        :type parent: str
        :param grouptype: grouptype variable. Nullable: True
        :type grouptype: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'type': type, 'parent': parent, 'grouptype': grouptype, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_groups", **out_args)

    def list_icmp(self, start=None, end=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_icmp operation method

        :param start: start variable. Nullable: True
        :type start: str
        :param end: end variable. Nullable: True
        :type end: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'start': start, 'end': end, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_icmp", **out_args)

    def list_image(self, site=None, imageset=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_image operation method

        :param site: site variable. Nullable: True
        :type site: str
        :param imageset: imageset variable. Nullable: True
        :type imageset: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'site': site, 'imageset': imageset, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_image", **out_args)

    def list_imageoption(self, name):
        """
        MFNA list_imageoption operation method

        :param name: name variable. Nullable: False
        :type name: str
        """
        out_args = {'name': name}
        return self.call("list_imageoption", **out_args)

    def list_imageset(self, site=None):
        """
        MFNA list_imageset operation method

        :param site: site variable. Nullable: True
        :type site: str
        """
        out_args = {'site': site}
        return self.call("list_imageset", **out_args)

    def list_int(self, start=None, end=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_int operation method

        :param start: start variable. Nullable: True
        :type start: str
        :param end: end variable. Nullable: True
        :type end: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'start': start, 'end': end, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_int", **out_args)

    def list_ip(self, deviceip):
        """
        MFNA list_ip operation method

        :param deviceip: deviceip variable. Nullable: False
        :type deviceip: str
        """
        out_args = {'deviceip': deviceip}
        return self.call("list_ip", **out_args)

    def list_ip_all(self):
        return self.call("list_ip_all")

    def list_metadata(self, table, associatedtableid):
        """
        MFNA list_metadata operation method

        :param table: table variable. Nullable: False
        :type table: str
        :param associatedtableid: associatedtableid variable. Nullable: False
        :type associatedtableid: str
        """
        out_args = {'table': table, 'associatedtableid': associatedtableid}
        return self.call("list_metadata", **out_args)

    def list_metadata_field(self, table):
        """
        MFNA list_metadata_field operation method

        :param table: table variable. Nullable: False
        :type table: str
        """
        out_args = {'table': table}
        return self.call("list_metadata_field", **out_args)

    def list_module(self, memory=None, ip=None, model=None, comment=None, type=None, firmware=None, hardware=None, group=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_module operation method

        :param memory: memory variable. Nullable: True
        :type memory: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param model: model variable. Nullable: True
        :type model: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param type: type variable. Nullable: True
        :type type: str
        :param firmware: firmware variable. Nullable: True
        :type firmware: str
        :param hardware: hardware variable. Nullable: True
        :type hardware: str
        :param group: group variable. Nullable: True
        :type group: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'memory': memory, 'ip': ip, 'model': model, 'comment': comment, 'type': type, 'firmware': firmware, 'hardware': hardware, 'group': group, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_module", **out_args)

    def list_nnmi_integration(self):
        return self.call("list_nnmi_integration")

    def list_nnmi_node_associations(self, deviceid):
        """
        MFNA list_nnmi_node_associations operation method

        :param deviceid: deviceid variable. Nullable: False
        :type deviceid: str
        """
        out_args = {'deviceid': deviceid}
        return self.call("list_nnmi_node_associations", **out_args)

    def list_nnmi_node_associations_all(self):
        return self.call("list_nnmi_node_associations_all")

    def list_ospfneighbor(self, start=None, end=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_ospfneighbor operation method

        :param start: start variable. Nullable: True
        :type start: str
        :param end: end variable. Nullable: True
        :type end: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'start': start, 'end': end, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_ospfneighbor", **out_args)

    def list_partition(self, viewname):
        """
        MFNA list_partition operation method

        :param viewname: viewname variable. Nullable: False
        :type viewname: str
        """
        out_args = {'viewname': viewname}
        return self.call("list_partition", **out_args)

    def list_policies(self):
        return self.call("list_policies")

    def list_policy_id(self, deviceid):
        """
        MFNA list_policy_id operation method

        :param deviceid: deviceid variable. Nullable: False
        :type deviceid: str
        """
        out_args = {'deviceid': deviceid}
        return self.call("list_policy_id", **out_args)

    def list_policy_rule(self, policyid):
        """
        MFNA list_policy_rule operation method

        :param policyid: policyid variable. Nullable: False
        :type policyid: str
        """
        out_args = {'policyid': policyid}
        return self.call("list_policy_rule", **out_args)

    def list_port(self, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_port operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_port", **out_args)

    def list_port_channels(self, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_port_channels operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_port_channels", **out_args)

    def list_refreshtoken(self, token=None):
        """
        MFNA list_refreshtoken operation method

        :param token: token variable. Nullable: True
        :type token: str
        """
        out_args = {'token': token}
        return self.call("list_refreshtoken", **out_args)

    def list_relationship_type(self, id=None, modifiable=None):
        """
        MFNA list_relationship_type operation method

        :param id: id variable. Nullable: True
        :type id: str
        :param modifiable: modifiable variable. Nullable: True
        :type modifiable: str
        """
        out_args = {'id': id, 'modifiable': modifiable}
        return self.call("list_relationship_type", **out_args)

    def list_relationships_for_device(self, filterdestination=None, hostname=None, relationshiptypeids=None, createdby=None, domain=None, filteroriginating=None, deviceid=None, ip=None, host=None, fqdn=None):
        """
        MFNA list_relationships_for_device operation method

        :param filterdestination: filterdestination variable. Nullable: True
        :type filterdestination: str
        :param hostname: hostname variable. Nullable: True
        :type hostname: str
        :param relationshiptypeids: relationshiptypeids variable. Nullable: True
        :type relationshiptypeids: str
        :param createdby: createdby variable. Nullable: True
        :type createdby: str
        :param domain: domain variable. Nullable: True
        :type domain: str
        :param filteroriginating: filteroriginating variable. Nullable: True
        :type filteroriginating: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        """
        out_args = {'filterdestination': filterdestination, 'hostname': hostname, 'relationshiptypeids': relationshiptypeids, 'createdby': createdby, 'domain': domain, 'filteroriginating': filteroriginating, 'deviceid': deviceid, 'ip': ip, 'host': host, 'fqdn': fqdn}
        return self.call("list_relationships_for_device", **out_args)

    def list_resource_id(self, poolid):
        """
        MFNA list_resource_id operation method

        :param poolid: poolid variable. Nullable: False
        :type poolid: str
        """
        out_args = {'poolid': poolid}
        return self.call("list_resource_id", **out_args)

    def list_resource_id_custom_field_data(self, resourceidentityid):
        """
        MFNA list_resource_id_custom_field_data operation method

        :param resourceidentityid: resourceidentityid variable. Nullable: False
        :type resourceidentityid: str
        """
        out_args = {'resourceidentityid': resourceidentityid}
        return self.call("list_resource_id_custom_field_data", **out_args)

    def list_resource_id_pool(self, site=None):
        """
        MFNA list_resource_id_pool operation method

        :param site: site variable. Nullable: True
        :type site: str
        """
        out_args = {'site': site}
        return self.call("list_resource_id_pool", **out_args)

    def list_resource_id_pool_all(self):
        return self.call("list_resource_id_pool_all")

    def list_role(self, type=None):
        """
        MFNA list_role operation method

        :param type: type variable. Nullable: True
        :type type: str
        """
        out_args = {'type': type}
        return self.call("list_role", **out_args)

    def list_routing(self, start=None, end=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_routing operation method

        :param start: start variable. Nullable: True
        :type start: str
        :param end: end variable. Nullable: True
        :type end: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'start': start, 'end': end, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_routing", **out_args)

    def list_rule_condition(self, ruleid):
        """
        MFNA list_rule_condition operation method

        :param ruleid: ruleid variable. Nullable: False
        :type ruleid: str
        """
        out_args = {'ruleid': ruleid}
        return self.call("list_rule_condition", **out_args)

    def list_script(self, mode=None, name=None, sitename=None, ids=None, type=None):
        """
        MFNA list_script operation method

        :param mode: mode variable. Nullable: True
        :type mode: str
        :param name: name variable. Nullable: True
        :type name: str
        :param sitename: sitename variable. Nullable: True
        :type sitename: str
        :param ids: ids variable. Nullable: True
        :type ids: str
        :param type: type variable. Nullable: True
        :type type: str
        """
        out_args = {'mode': mode, 'name': name, 'sitename': sitename, 'ids': ids, 'type': type}
        return self.call("list_script", **out_args)

    def list_script_id(self, mode=None, name=None, id=None, type=None):
        """
        MFNA list_script_id operation method

        :param mode: mode variable. Nullable: True
        :type mode: str
        :param name: name variable. Nullable: True
        :type name: str
        :param id: id variable. Nullable: True
        :type id: str
        :param type: type variable. Nullable: True
        :type type: str
        """
        out_args = {'mode': mode, 'name': name, 'id': id, 'type': type}
        return self.call("list_script_id", **out_args)

    def list_script_mode(self, ip=None, id=None, type=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_script_mode operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param id: id variable. Nullable: True
        :type id: str
        :param type: type variable. Nullable: True
        :type type: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'id': id, 'type': type, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_script_mode", **out_args)

    def list_session(self, start=None, end=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_session operation method

        :param start: start variable. Nullable: True
        :type start: str
        :param end: end variable. Nullable: True
        :type end: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'start': start, 'end': end, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_session", **out_args)

    def list_site(self, name=None, id=None, coreid=None):
        """
        MFNA list_site operation method

        :param name: name variable. Nullable: True
        :type name: str
        :param id: id variable. Nullable: True
        :type id: str
        :param coreid: coreid variable. Nullable: True
        :type coreid: str
        """
        out_args = {'name': name, 'id': id, 'coreid': coreid}
        return self.call("list_site", **out_args)

    def list_sys_oids_all(self):
        return self.call("list_sys_oids_all")

    def list_system_message(self, ip=None, start=None, end=None, type=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_system_message operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param start: start variable. Nullable: True
        :type start: str
        :param end: end variable. Nullable: True
        :type end: str
        :param type: type variable. Nullable: True
        :type type: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'start': start, 'end': end, 'type': type, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_system_message", **out_args)

    def list_task(self, priorities=None, ip=None, start=None, name=None, end=None, id=None, coreid=None, type=None, parentid=None, status=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_task operation method

        :param priorities: priorities variable. Nullable: True
        :type priorities: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param start: start variable. Nullable: True
        :type start: str
        :param name: name variable. Nullable: True
        :type name: str
        :param end: end variable. Nullable: True
        :type end: str
        :param id: id variable. Nullable: True
        :type id: str
        :param coreid: coreid variable. Nullable: True
        :type coreid: str
        :param type: type variable. Nullable: True
        :type type: str
        :param parentid: parentid variable. Nullable: True
        :type parentid: str
        :param status: status variable. Nullable: True
        :type status: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'priorities': priorities, 'ip': ip, 'start': start, 'name': name, 'end': end, 'id': id, 'coreid': coreid, 'type': type, 'parentid': parentid, 'status': status, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_task", **out_args)

    def list_task_all(self):
        return self.call("list_task_all")

    def list_template_devices(self, id):
        """
        MFNA list_template_devices operation method

        :param id: id variable. Nullable: False
        :type id: str
        """
        out_args = {'id': id}
        return self.call("list_template_devices", **out_args)

    def list_topology(self, ip=None, mac=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_topology operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param mac: mac variable. Nullable: True
        :type mac: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'mac': mac, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_topology", **out_args)

    def list_topology_graph(self, endip=None, startip=None, deviceids=None, hideunconnected=None, type=None, deviceid=None, hideinactive=None, serverids=None, layer=None, hopcount=None, hideunmanaged=None, hierarchylayer=None, deviceportids=None, serverportids=None):
        """
        MFNA list_topology_graph operation method

        :param endip: endip variable. Nullable: True
        :type endip: str
        :param startip: startip variable. Nullable: True
        :type startip: str
        :param deviceids: deviceids variable. Nullable: True
        :type deviceids: str
        :param hideunconnected: hideunconnected variable. Nullable: True
        :type hideunconnected: str
        :param type: type variable. Nullable: True
        :type type: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        :param hideinactive: hideinactive variable. Nullable: True
        :type hideinactive: str
        :param serverids: serverids variable. Nullable: True
        :type serverids: str
        :param layer: layer variable. Nullable: True
        :type layer: str
        :param hopcount: hopcount variable. Nullable: True
        :type hopcount: str
        :param hideunmanaged: hideunmanaged variable. Nullable: True
        :type hideunmanaged: str
        :param hierarchylayer: hierarchylayer variable. Nullable: True
        :type hierarchylayer: str
        :param deviceportids: deviceportids variable. Nullable: True
        :type deviceportids: str
        :param serverportids: serverportids variable. Nullable: True
        :type serverportids: str
        """
        out_args = {'endip': endip, 'startip': startip, 'deviceids': deviceids, 'hideunconnected': hideunconnected, 'type': type, 'deviceid': deviceid, 'hideinactive': hideinactive, 'serverids': serverids, 'layer': layer, 'hopcount': hopcount, 'hideunmanaged': hideunmanaged, 'hierarchylayer': hierarchylayer, 'deviceportids': deviceportids, 'serverportids': serverportids}
        return self.call("list_topology_graph", **out_args)

    def list_topology_ip(self, deviceip=None, address=None, notcurrent=None, serverportid=None, portid=None, type=None, deviceid=None, serverid=None):
        """
        MFNA list_topology_ip operation method

        :param deviceip: deviceip variable. Nullable: True
        :type deviceip: str
        :param address: address variable. Nullable: True
        :type address: str
        :param notcurrent: notcurrent variable. Nullable: True
        :type notcurrent: str
        :param serverportid: serverportid variable. Nullable: True
        :type serverportid: str
        :param portid: portid variable. Nullable: True
        :type portid: str
        :param type: type variable. Nullable: True
        :type type: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        :param serverid: serverid variable. Nullable: True
        :type serverid: str
        """
        out_args = {'deviceip': deviceip, 'address': address, 'notcurrent': notcurrent, 'serverportid': serverportid, 'portid': portid, 'type': type, 'deviceid': deviceid, 'serverid': serverid}
        return self.call("list_topology_ip", **out_args)

    def list_topology_mac(self, deviceip=None, address=None, notcurrent=None, serverportid=None, portid=None, type=None, deviceid=None, serverid=None):
        """
        MFNA list_topology_mac operation method

        :param deviceip: deviceip variable. Nullable: True
        :type deviceip: str
        :param address: address variable. Nullable: True
        :type address: str
        :param notcurrent: notcurrent variable. Nullable: True
        :type notcurrent: str
        :param serverportid: serverportid variable. Nullable: True
        :type serverportid: str
        :param portid: portid variable. Nullable: True
        :type portid: str
        :param type: type variable. Nullable: True
        :type type: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        :param serverid: serverid variable. Nullable: True
        :type serverid: str
        """
        out_args = {'deviceip': deviceip, 'address': address, 'notcurrent': notcurrent, 'serverportid': serverportid, 'portid': portid, 'type': type, 'deviceid': deviceid, 'serverid': serverid}
        return self.call("list_topology_mac", **out_args)

    def list_trunk_port(self, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_trunk_port operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_trunk_port", **out_args)

    def list_user(self, archive=None, group=None):
        """
        MFNA list_user operation method

        :param archive: archive variable. Nullable: True
        :type archive: str
        :param group: group variable. Nullable: True
        :type group: str
        """
        out_args = {'archive': archive, 'group': group}
        return self.call("list_user", **out_args)

    def list_user_id(self, viewable_by=None):
        """
        MFNA list_user_id operation method

        :param viewable_by: viewable_by variable. Nullable: True
        :type viewable_by: str
        """
        out_args = {'viewable_by': viewable_by}
        return self.call("list_user_id", **out_args)

    def list_user_site(self, u=None, id=None):
        """
        MFNA list_user_site operation method

        :param u: u variable. Nullable: True
        :type u: str
        :param id: id variable. Nullable: True
        :type id: str
        """
        out_args = {'u': u, 'id': id}
        return self.call("list_user_site", **out_args)

    def list_view(self):
        return self.call("list_view")

    def list_vlan(self, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_vlan operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_vlan", **out_args)

    def list_vlan_on_port(self, portid):
        """
        MFNA list_vlan_on_port operation method

        :param portid: portid variable. Nullable: False
        :type portid: str
        """
        out_args = {'portid': portid}
        return self.call("list_vlan_on_port", **out_args)

    def list_vlan_ports(self, vlanid, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA list_vlan_ports operation method

        :param vlanid: vlanid variable. Nullable: False
        :type vlanid: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'vlanid': vlanid, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("list_vlan_ports", **out_args)

    def list_vtp_domain(self):
        return self.call("list_vtp_domain")

    def mod_advanced_diagnostic(self, name=None, sitename=None, description=None, language=None, id=None, newname=None, family=None, parameters=None, script=None):
        """
        MFNA mod_advanced_diagnostic operation method

        :param name: name variable. Nullable: True
        :type name: str
        :param sitename: sitename variable. Nullable: True
        :type sitename: str
        :param description: description variable. Nullable: True
        :type description: str
        :param language: language variable. Nullable: True
        :type language: str
        :param id: id variable. Nullable: True
        :type id: str
        :param newname: newname variable. Nullable: True
        :type newname: str
        :param family: family variable. Nullable: True
        :type family: str
        :param parameters: parameters variable. Nullable: True
        :type parameters: str
        :param script: script variable. Nullable: True
        :type script: str
        """
        out_args = {'name': name, 'sitename': sitename, 'description': description, 'language': language, 'id': id, 'newname': newname, 'family': family, 'parameters': parameters, 'script': script}
        return self.call("mod_advanced_diagnostic", **out_args)

    def mod_advanced_script(self, scripttype=None, name=None, sitename=None, description=None, language=None, id=None, newname=None, family=None, parameters=None, script=None):
        """
        MFNA mod_advanced_script operation method

        :param scripttype: scripttype variable. Nullable: True
        :type scripttype: str
        :param name: name variable. Nullable: True
        :type name: str
        :param sitename: sitename variable. Nullable: True
        :type sitename: str
        :param description: description variable. Nullable: True
        :type description: str
        :param language: language variable. Nullable: True
        :type language: str
        :param id: id variable. Nullable: True
        :type id: str
        :param newname: newname variable. Nullable: True
        :type newname: str
        :param family: family variable. Nullable: True
        :type family: str
        :param parameters: parameters variable. Nullable: True
        :type parameters: str
        :param script: script variable. Nullable: True
        :type script: str
        """
        out_args = {'scripttype': scripttype, 'name': name, 'sitename': sitename, 'description': description, 'language': language, 'id': id, 'newname': newname, 'family': family, 'parameters': parameters, 'script': script}
        return self.call("mod_advanced_script", **out_args)

    def mod_authentication(self, loc, enablepasswd=None, snmpro=None, ruledevicegroup=None, iprangeend=None, taskname=None, rulename=None, snmpv3encryptpw=None, maxwaittime=None, rulehostname=None, connectionmethods=None, group=None, snmpv3user=None, ip=None, start=None, enableuser=None, accessvariables=None, sync=None, site=None, appendsnmprw=None, passwd=None, snmpv3authpw=None, iprangestart=None, appendsnmpro=None, snmprw=None, user=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA mod_authentication operation method

        :param loc: loc variable. Nullable: False
        :type loc: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param ruledevicegroup: ruledevicegroup variable. Nullable: True
        :type ruledevicegroup: str
        :param iprangeend: iprangeend variable. Nullable: True
        :type iprangeend: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param rulename: rulename variable. Nullable: True
        :type rulename: str
        :param snmpv3encryptpw: snmpv3encryptpw variable. Nullable: True
        :type snmpv3encryptpw: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param rulehostname: rulehostname variable. Nullable: True
        :type rulehostname: str
        :param connectionmethods: connectionmethods variable. Nullable: True
        :type connectionmethods: str
        :param group: group variable. Nullable: True
        :type group: str
        :param snmpv3user: snmpv3user variable. Nullable: True
        :type snmpv3user: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param start: start variable. Nullable: True
        :type start: str
        :param enableuser: enableuser variable. Nullable: True
        :type enableuser: str
        :param accessvariables: accessvariables variable. Nullable: True
        :type accessvariables: str
        :param sync: sync variable. Nullable: True
        :type sync: str
        :param site: site variable. Nullable: True
        :type site: str
        :param appendsnmprw: appendsnmprw variable. Nullable: True
        :type appendsnmprw: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param snmpv3authpw: snmpv3authpw variable. Nullable: True
        :type snmpv3authpw: str
        :param iprangestart: iprangestart variable. Nullable: True
        :type iprangestart: str
        :param appendsnmpro: appendsnmpro variable. Nullable: True
        :type appendsnmpro: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        :param user: user variable. Nullable: True
        :type user: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'loc': loc, 'enablepasswd': enablepasswd, 'snmpro': snmpro, 'ruledevicegroup': ruledevicegroup, 'iprangeend': iprangeend, 'taskname': taskname, 'rulename': rulename, 'snmpv3encryptpw': snmpv3encryptpw, 'maxwaittime': maxwaittime, 'rulehostname': rulehostname, 'connectionmethods': connectionmethods, 'group': group, 'snmpv3user': snmpv3user, 'ip': ip, 'start': start, 'enableuser': enableuser, 'accessvariables': accessvariables, 'sync': sync, 'site': site, 'appendsnmprw': appendsnmprw, 'passwd': passwd, 'snmpv3authpw': snmpv3authpw, 'iprangestart': iprangestart, 'appendsnmpro': appendsnmpro, 'snmprw': snmprw, 'user': user, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("mod_authentication", **out_args)

    def mod_caseinsensitive(self, option=None):
        """
        MFNA mod_caseinsensitive operation method

        :param option: option variable. Nullable: True
        :type option: str
        """
        out_args = {'option': option}
        return self.call("mod_caseinsensitive", **out_args)

    def mod_change_plan(self, changename=None, changedescription=None, language=None, changemode=None, newname=None, rollbackscript=None, changescript=None, driver=None, updatetasks=None, changetype=None, name=None, id=None, tag=None, conditions=None, parameters=None, desc=None):
        """
        MFNA mod_change_plan operation method

        :param changename: changename variable. Nullable: True
        :type changename: str
        :param changedescription: changedescription variable. Nullable: True
        :type changedescription: str
        :param language: language variable. Nullable: True
        :type language: str
        :param changemode: changemode variable. Nullable: True
        :type changemode: str
        :param newname: newname variable. Nullable: True
        :type newname: str
        :param rollbackscript: rollbackscript variable. Nullable: True
        :type rollbackscript: str
        :param changescript: changescript variable. Nullable: True
        :type changescript: str
        :param driver: driver variable. Nullable: True
        :type driver: str
        :param updatetasks: updatetasks variable. Nullable: True
        :type updatetasks: str
        :param changetype: changetype variable. Nullable: True
        :type changetype: str
        :param name: name variable. Nullable: True
        :type name: str
        :param id: id variable. Nullable: True
        :type id: str
        :param tag: tag variable. Nullable: True
        :type tag: str
        :param conditions: conditions variable. Nullable: True
        :type conditions: str
        :param parameters: parameters variable. Nullable: True
        :type parameters: str
        :param desc: desc variable. Nullable: True
        :type desc: str
        """
        out_args = {'changename': changename, 'changedescription': changedescription, 'language': language, 'changemode': changemode, 'newname': newname, 'rollbackscript': rollbackscript, 'changescript': changescript, 'driver': driver, 'updatetasks': updatetasks, 'changetype': changetype, 'name': name, 'id': id, 'tag': tag, 'conditions': conditions, 'parameters': parameters, 'desc': desc}
        return self.call("mod_change_plan", **out_args)

    def mod_command_script(self, mode=None, scripttype=None, driver=None, name=None, sitename=None, description=None, id=None, newname=None, script=None):
        """
        MFNA mod_command_script operation method

        :param mode: mode variable. Nullable: True
        :type mode: str
        :param scripttype: scripttype variable. Nullable: True
        :type scripttype: str
        :param driver: driver variable. Nullable: True
        :type driver: str
        :param name: name variable. Nullable: True
        :type name: str
        :param sitename: sitename variable. Nullable: True
        :type sitename: str
        :param description: description variable. Nullable: True
        :type description: str
        :param id: id variable. Nullable: True
        :type id: str
        :param newname: newname variable. Nullable: True
        :type newname: str
        :param script: script variable. Nullable: True
        :type script: str
        """
        out_args = {'mode': mode, 'scripttype': scripttype, 'driver': driver, 'name': name, 'sitename': sitename, 'description': description, 'id': id, 'newname': newname, 'script': script}
        return self.call("mod_command_script", **out_args)

    def mod_custom_data(self, tablename, columnname, fieldname=None, flags=None, inuse=None, fieldlabel=None, fieldvalues=None):
        """
        MFNA mod_custom_data operation method

        :param tablename: tablename variable. Nullable: False
        :type tablename: str
        :param columnname: columnname variable. Nullable: False
        :type columnname: str
        :param fieldname: fieldname variable. Nullable: True
        :type fieldname: str
        :param flags: flags variable. Nullable: True
        :type flags: str
        :param inuse: inuse variable. Nullable: True
        :type inuse: str
        :param fieldlabel: fieldlabel variable. Nullable: True
        :type fieldlabel: str
        :param fieldvalues: fieldvalues variable. Nullable: True
        :type fieldvalues: str
        """
        out_args = {'tablename': tablename, 'columnname': columnname, 'fieldname': fieldname, 'flags': flags, 'inuse': inuse, 'fieldlabel': fieldlabel, 'fieldvalues': fieldvalues}
        return self.call("mod_custom_data", **out_args)

    def mod_device(self, customnames=None, useconsoleserver=None, consoleport=None, nopoll=None, customvalue=None, description=None, consoleip=None, tftpserverip=None, hostname=None, accessmethods=None, natip=None, serial=None, hierarchylayer=None, vendor=None, domain=None, customname=None, model=None, location=None, comment=None, newip=None, customvalues=None, asset=None, status=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA mod_device operation method

        :param customnames: customnames variable. Nullable: True
        :type customnames: str
        :param useconsoleserver: useconsoleserver variable. Nullable: True
        :type useconsoleserver: str
        :param consoleport: consoleport variable. Nullable: True
        :type consoleport: str
        :param nopoll: nopoll variable. Nullable: True
        :type nopoll: str
        :param customvalue: customvalue variable. Nullable: True
        :type customvalue: str
        :param description: description variable. Nullable: True
        :type description: str
        :param consoleip: consoleip variable. Nullable: True
        :type consoleip: str
        :param tftpserverip: tftpserverip variable. Nullable: True
        :type tftpserverip: str
        :param hostname: hostname variable. Nullable: True
        :type hostname: str
        :param accessmethods: accessmethods variable. Nullable: True
        :type accessmethods: str
        :param natip: natip variable. Nullable: True
        :type natip: str
        :param serial: serial variable. Nullable: True
        :type serial: str
        :param hierarchylayer: hierarchylayer variable. Nullable: True
        :type hierarchylayer: str
        :param vendor: vendor variable. Nullable: True
        :type vendor: str
        :param domain: domain variable. Nullable: True
        :type domain: str
        :param customname: customname variable. Nullable: True
        :type customname: str
        :param model: model variable. Nullable: True
        :type model: str
        :param location: location variable. Nullable: True
        :type location: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param newip: newip variable. Nullable: True
        :type newip: str
        :param customvalues: customvalues variable. Nullable: True
        :type customvalues: str
        :param asset: asset variable. Nullable: True
        :type asset: str
        :param status: status variable. Nullable: True
        :type status: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'customnames': customnames, 'useconsoleserver': useconsoleserver, 'consoleport': consoleport, 'nopoll': nopoll, 'customvalue': customvalue, 'description': description, 'consoleip': consoleip, 'tftpserverip': tftpserverip, 'hostname': hostname, 'accessmethods': accessmethods, 'natip': natip, 'serial': serial, 'hierarchylayer': hierarchylayer, 'vendor': vendor, 'domain': domain, 'customname': customname, 'model': model, 'location': location, 'comment': comment, 'newip': newip, 'customvalues': customvalues, 'asset': asset, 'status': status, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("mod_device", **out_args)

    def mod_device_group(self, name, customnames=None, partitions=None, newtype=None, shared=None, searchgroups=None, criteria=None, customvalue=None, customname=None, limitsearchgroups=None, comment=None, customvalues=None, newname=None):
        """
        MFNA mod_device_group operation method

        :param name: name variable. Nullable: False
        :type name: str
        :param customnames: customnames variable. Nullable: True
        :type customnames: str
        :param partitions: partitions variable. Nullable: True
        :type partitions: str
        :param newtype: newtype variable. Nullable: True
        :type newtype: str
        :param shared: shared variable. Nullable: True
        :type shared: str
        :param searchgroups: searchgroups variable. Nullable: True
        :type searchgroups: str
        :param criteria: criteria variable. Nullable: True
        :type criteria: str
        :param customvalue: customvalue variable. Nullable: True
        :type customvalue: str
        :param customname: customname variable. Nullable: True
        :type customname: str
        :param limitsearchgroups: limitsearchgroups variable. Nullable: True
        :type limitsearchgroups: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param customvalues: customvalues variable. Nullable: True
        :type customvalues: str
        :param newname: newname variable. Nullable: True
        :type newname: str
        """
        out_args = {'name': name, 'customnames': customnames, 'partitions': partitions, 'newtype': newtype, 'shared': shared, 'searchgroups': searchgroups, 'criteria': criteria, 'customvalue': customvalue, 'customname': customname, 'limitsearchgroups': limitsearchgroups, 'comment': comment, 'customvalues': customvalues, 'newname': newname}
        return self.call("mod_device_group", **out_args)

    def mod_device_relationship(self, newrelationshiptypeid, relationshipid):
        """
        MFNA mod_device_relationship operation method

        :param newrelationshiptypeid: newrelationshiptypeid variable. Nullable: False
        :type newrelationshiptypeid: str
        :param relationshipid: relationshipid variable. Nullable: False
        :type relationshipid: str
        """
        out_args = {'newrelationshiptypeid': newrelationshiptypeid, 'relationshipid': relationshipid}
        return self.call("mod_device_relationship", **out_args)

    def mod_device_template(self, templateid, customnames=None, newdriver=None, customvalue=None, description=None, hostname=None, accessmethods=None, hierarchylayer=None, vendor=None, customname=None, sitename=None, comment=None, model=None, location=None, customvalues=None):
        """
        MFNA mod_device_template operation method

        :param templateid: templateid variable. Nullable: False
        :type templateid: str
        :param customnames: customnames variable. Nullable: True
        :type customnames: str
        :param newdriver: newdriver variable. Nullable: True
        :type newdriver: str
        :param customvalue: customvalue variable. Nullable: True
        :type customvalue: str
        :param description: description variable. Nullable: True
        :type description: str
        :param hostname: hostname variable. Nullable: True
        :type hostname: str
        :param accessmethods: accessmethods variable. Nullable: True
        :type accessmethods: str
        :param hierarchylayer: hierarchylayer variable. Nullable: True
        :type hierarchylayer: str
        :param vendor: vendor variable. Nullable: True
        :type vendor: str
        :param customname: customname variable. Nullable: True
        :type customname: str
        :param sitename: sitename variable. Nullable: True
        :type sitename: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param model: model variable. Nullable: True
        :type model: str
        :param location: location variable. Nullable: True
        :type location: str
        :param customvalues: customvalues variable. Nullable: True
        :type customvalues: str
        """
        out_args = {'templateid': templateid, 'customnames': customnames, 'newdriver': newdriver, 'customvalue': customvalue, 'description': description, 'hostname': hostname, 'accessmethods': accessmethods, 'hierarchylayer': hierarchylayer, 'vendor': vendor, 'customname': customname, 'sitename': sitename, 'comment': comment, 'model': model, 'location': location, 'customvalues': customvalues}
        return self.call("mod_device_template", **out_args)

    def mod_device_template_config(self, templateid, configtext=None, configfile=None):
        """
        MFNA mod_device_template_config operation method

        :param templateid: templateid variable. Nullable: False
        :type templateid: str
        :param configtext: configtext variable. Nullable: True
        :type configtext: str
        :param configfile: configfile variable. Nullable: True
        :type configfile: str
        """
        out_args = {'templateid': templateid, 'configtext': configtext, 'configfile': configfile}
        return self.call("mod_device_template_config", **out_args)

    def mod_diagnostic(self, mode=None, driver=None, name=None, sitename=None, description=None, id=None, newname=None, script=None):
        """
        MFNA mod_diagnostic operation method

        :param mode: mode variable. Nullable: True
        :type mode: str
        :param driver: driver variable. Nullable: True
        :type driver: str
        :param name: name variable. Nullable: True
        :type name: str
        :param sitename: sitename variable. Nullable: True
        :type sitename: str
        :param description: description variable. Nullable: True
        :type description: str
        :param id: id variable. Nullable: True
        :type id: str
        :param newname: newname variable. Nullable: True
        :type newname: str
        :param script: script variable. Nullable: True
        :type script: str
        """
        out_args = {'mode': mode, 'driver': driver, 'name': name, 'sitename': sitename, 'description': description, 'id': id, 'newname': newname, 'script': script}
        return self.call("mod_diagnostic", **out_args)

    def mod_group(self, name, type, customnames=None, shared=None, customname=None, customvalue=None, comment=None, customvalues=None, newname=None):
        """
        MFNA mod_group operation method

        :param name: name variable. Nullable: False
        :type name: str
        :param type: type variable. Nullable: False
        :type type: str
        :param customnames: customnames variable. Nullable: True
        :type customnames: str
        :param shared: shared variable. Nullable: True
        :type shared: str
        :param customname: customname variable. Nullable: True
        :type customname: str
        :param customvalue: customvalue variable. Nullable: True
        :type customvalue: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param customvalues: customvalues variable. Nullable: True
        :type customvalues: str
        :param newname: newname variable. Nullable: True
        :type newname: str
        """
        out_args = {'name': name, 'type': type, 'customnames': customnames, 'shared': shared, 'customname': customname, 'customvalue': customvalue, 'comment': comment, 'customvalues': customvalues, 'newname': newname}
        return self.call("mod_group", **out_args)

    def mod_ip(self, deviceip, ipvalue, usetoaccess=None, comment=None):
        """
        MFNA mod_ip operation method

        :param deviceip: deviceip variable. Nullable: False
        :type deviceip: str
        :param ipvalue: ipvalue variable. Nullable: False
        :type ipvalue: str
        :param usetoaccess: usetoaccess variable. Nullable: True
        :type usetoaccess: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        """
        out_args = {'deviceip': deviceip, 'ipvalue': ipvalue, 'usetoaccess': usetoaccess, 'comment': comment}
        return self.call("mod_ip", **out_args)

    def mod_metadata(self, metadataid, data=None, fieldid=None, associatedtableid=None):
        """
        MFNA mod_metadata operation method

        :param metadataid: metadataid variable. Nullable: False
        :type metadataid: str
        :param data: data variable. Nullable: True
        :type data: str
        :param fieldid: fieldid variable. Nullable: True
        :type fieldid: str
        :param associatedtableid: associatedtableid variable. Nullable: True
        :type associatedtableid: str
        """
        out_args = {'metadataid': metadataid, 'data': data, 'fieldid': fieldid, 'associatedtableid': associatedtableid}
        return self.call("mod_metadata", **out_args)

    def mod_metadata_field(self, fieldid, fieldname=None, associatedtable=None, flags=None, inuse=None, fieldvalues=None):
        """
        MFNA mod_metadata_field operation method

        :param fieldid: fieldid variable. Nullable: False
        :type fieldid: str
        :param fieldname: fieldname variable. Nullable: True
        :type fieldname: str
        :param associatedtable: associatedtable variable. Nullable: True
        :type associatedtable: str
        :param flags: flags variable. Nullable: True
        :type flags: str
        :param inuse: inuse variable. Nullable: True
        :type inuse: str
        :param fieldvalues: fieldvalues variable. Nullable: True
        :type fieldvalues: str
        """
        out_args = {'fieldid': fieldid, 'fieldname': fieldname, 'associatedtable': associatedtable, 'flags': flags, 'inuse': inuse, 'fieldvalues': fieldvalues}
        return self.call("mod_metadata_field", **out_args)

    def mod_module(self, id, customnames=None, customname=None, customvalue=None, comment=None, customvalues=None):
        """
        MFNA mod_module operation method

        :param id: id variable. Nullable: False
        :type id: str
        :param customnames: customnames variable. Nullable: True
        :type customnames: str
        :param customname: customname variable. Nullable: True
        :type customname: str
        :param customvalue: customvalue variable. Nullable: True
        :type customvalue: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param customvalues: customvalues variable. Nullable: True
        :type customvalues: str
        """
        out_args = {'id': id, 'customnames': customnames, 'customname': customname, 'customvalue': customvalue, 'comment': comment, 'customvalues': customvalues}
        return self.call("mod_module", **out_args)

    def mod_nnmi_integration(self, nnmiport=None, nnmiusername=None, nnmiusesssl=None, id=None, nnmipassword=None, nnmihostname=None, enabled=None, nnmisystemid=None, nausername=None):
        """
        MFNA mod_nnmi_integration operation method

        :param nnmiport: nnmiport variable. Nullable: True
        :type nnmiport: str
        :param nnmiusername: nnmiusername variable. Nullable: True
        :type nnmiusername: str
        :param nnmiusesssl: nnmiusesssl variable. Nullable: True
        :type nnmiusesssl: str
        :param id: id variable. Nullable: True
        :type id: str
        :param nnmipassword: nnmipassword variable. Nullable: True
        :type nnmipassword: str
        :param nnmihostname: nnmihostname variable. Nullable: True
        :type nnmihostname: str
        :param enabled: enabled variable. Nullable: True
        :type enabled: str
        :param nnmisystemid: nnmisystemid variable. Nullable: True
        :type nnmisystemid: str
        :param nausername: nausername variable. Nullable: True
        :type nausername: str
        """
        out_args = {'nnmiport': nnmiport, 'nnmiusername': nnmiusername, 'nnmiusesssl': nnmiusesssl, 'id': id, 'nnmipassword': nnmipassword, 'nnmihostname': nnmihostname, 'enabled': enabled, 'nnmisystemid': nnmisystemid, 'nausername': nausername}
        return self.call("mod_nnmi_integration", **out_args)

    def mod_nnmi_node_association(self, deviceid, nnmisystemid, nnminodeuuid=None):
        """
        MFNA mod_nnmi_node_association operation method

        :param deviceid: deviceid variable. Nullable: False
        :type deviceid: str
        :param nnmisystemid: nnmisystemid variable. Nullable: False
        :type nnmisystemid: str
        :param nnminodeuuid: nnminodeuuid variable. Nullable: True
        :type nnminodeuuid: str
        """
        out_args = {'deviceid': deviceid, 'nnmisystemid': nnmisystemid, 'nnminodeuuid': nnminodeuuid}
        return self.call("mod_nnmi_node_association", **out_args)

    def mod_opticdlreporting(self, option):
        """
        MFNA mod_opticdlreporting operation method

        :param option: option variable. Nullable: False
        :type option: str
        """
        out_args = {'option': option}
        return self.call("mod_opticdlreporting", **out_args)

    def mod_oraclecaseinsensitive(self, option=None):
        """
        MFNA mod_oraclecaseinsensitive operation method

        :param option: option variable. Nullable: True
        :type option: str
        """
        out_args = {'option': option}
        return self.call("mod_oraclecaseinsensitive", **out_args)

    def mod_partition(self, name, comment=None, realm=None, newname=None, managingcoreid=None):
        """
        MFNA mod_partition operation method

        :param name: name variable. Nullable: False
        :type name: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param realm: realm variable. Nullable: True
        :type realm: str
        :param newname: newname variable. Nullable: True
        :type newname: str
        :param managingcoreid: managingcoreid variable. Nullable: True
        :type managingcoreid: str
        """
        out_args = {'name': name, 'comment': comment, 'realm': realm, 'newname': newname, 'managingcoreid': managingcoreid}
        return self.call("mod_partition", **out_args)

    def mod_policy(self, policydesc=None, ddate=None, dg=None, aurl=None, surl=None, newname=None, exceptions=None, site=None, cve=None, policyid=None, solution=None, name=None, tag=None, desc=None, status=None):
        """
        MFNA mod_policy operation method

        :param policydesc: policydesc variable. Nullable: True
        :type policydesc: str
        :param ddate: ddate variable. Nullable: True
        :type ddate: str
        :param dg: dg variable. Nullable: True
        :type dg: str
        :param aurl: aurl variable. Nullable: True
        :type aurl: str
        :param surl: surl variable. Nullable: True
        :type surl: str
        :param newname: newname variable. Nullable: True
        :type newname: str
        :param exceptions: exceptions variable. Nullable: True
        :type exceptions: str
        :param site: site variable. Nullable: True
        :type site: str
        :param cve: cve variable. Nullable: True
        :type cve: str
        :param policyid: policyid variable. Nullable: True
        :type policyid: str
        :param solution: solution variable. Nullable: True
        :type solution: str
        :param name: name variable. Nullable: True
        :type name: str
        :param tag: tag variable. Nullable: True
        :type tag: str
        :param desc: desc variable. Nullable: True
        :type desc: str
        :param status: status variable. Nullable: True
        :type status: str
        """
        out_args = {'policydesc': policydesc, 'ddate': ddate, 'dg': dg, 'aurl': aurl, 'surl': surl, 'newname': newname, 'exceptions': exceptions, 'site': site, 'cve': cve, 'policyid': policyid, 'solution': solution, 'name': name, 'tag': tag, 'desc': desc, 'status': status}
        return self.call("mod_policy", **out_args)

    def mod_policy_rule(self, ruleid, useblock=None, textblockendpattern=None, textblockstartpattern=None, devicefamily=None, importance=None, details=None, newname=None, drivers=None, desc=None):
        """
        MFNA mod_policy_rule operation method

        :param ruleid: ruleid variable. Nullable: False
        :type ruleid: str
        :param useblock: useblock variable. Nullable: True
        :type useblock: str
        :param textblockendpattern: textblockendpattern variable. Nullable: True
        :type textblockendpattern: str
        :param textblockstartpattern: textblockstartpattern variable. Nullable: True
        :type textblockstartpattern: str
        :param devicefamily: devicefamily variable. Nullable: True
        :type devicefamily: str
        :param importance: importance variable. Nullable: True
        :type importance: str
        :param details: details variable. Nullable: True
        :type details: str
        :param newname: newname variable. Nullable: True
        :type newname: str
        :param drivers: drivers variable. Nullable: True
        :type drivers: str
        :param desc: desc variable. Nullable: True
        :type desc: str
        """
        out_args = {'ruleid': ruleid, 'useblock': useblock, 'textblockendpattern': textblockendpattern, 'textblockstartpattern': textblockstartpattern, 'devicefamily': devicefamily, 'importance': importance, 'details': details, 'newname': newname, 'drivers': drivers, 'desc': desc}
        return self.call("mod_policy_rule", **out_args)

    def mod_port(self, id, customnames=None, customname=None, customvalue=None, comment=None, customvalues=None):
        """
        MFNA mod_port operation method

        :param id: id variable. Nullable: False
        :type id: str
        :param customnames: customnames variable. Nullable: True
        :type customnames: str
        :param customname: customname variable. Nullable: True
        :type customname: str
        :param customvalue: customvalue variable. Nullable: True
        :type customvalue: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param customvalues: customvalues variable. Nullable: True
        :type customvalues: str
        """
        out_args = {'id': id, 'customnames': customnames, 'customname': customname, 'customvalue': customvalue, 'comment': comment, 'customvalues': customvalues}
        return self.call("mod_port", **out_args)

    def mod_resource_id_custom_field_data(self, resourceidentityid=None, fieldname=None, fielddataid=None, data=None):
        """
        MFNA mod_resource_id_custom_field_data operation method

        :param resourceidentityid: resourceidentityid variable. Nullable: True
        :type resourceidentityid: str
        :param fieldname: fieldname variable. Nullable: True
        :type fieldname: str
        :param fielddataid: fielddataid variable. Nullable: True
        :type fielddataid: str
        :param data: data variable. Nullable: True
        :type data: str
        """
        out_args = {'resourceidentityid': resourceidentityid, 'fieldname': fieldname, 'fielddataid': fielddataid, 'data': data}
        return self.call("mod_resource_id_custom_field_data", **out_args)

    def mod_resource_id_pool(self, id, addcustomfieldid=None, site=None, name=None, description=None, removecustomfieldid=None):
        """
        MFNA mod_resource_id_pool operation method

        :param id: id variable. Nullable: False
        :type id: str
        :param addcustomfieldid: addcustomfieldid variable. Nullable: True
        :type addcustomfieldid: str
        :param site: site variable. Nullable: True
        :type site: str
        :param name: name variable. Nullable: True
        :type name: str
        :param description: description variable. Nullable: True
        :type description: str
        :param removecustomfieldid: removecustomfieldid variable. Nullable: True
        :type removecustomfieldid: str
        """
        out_args = {'id': id, 'addcustomfieldid': addcustomfieldid, 'site': site, 'name': name, 'description': description, 'removecustomfieldid': removecustomfieldid}
        return self.call("mod_resource_id_pool", **out_args)

    def mod_role(self, name, resources, viewname=None, desc=None):
        """
        MFNA mod_role operation method

        :param name: name variable. Nullable: False
        :type name: str
        :param resources: resources variable. Nullable: False
        :type resources: str
        :param viewname: viewname variable. Nullable: True
        :type viewname: str
        :param desc: desc variable. Nullable: True
        :type desc: str
        """
        out_args = {'name': name, 'resources': resources, 'viewname': viewname, 'desc': desc}
        return self.call("mod_role", **out_args)

    def mod_rule_condition(self, rcid, exceptoperand=None, regex=None, exactorder=None, operator=None, operand=None):
        """
        MFNA mod_rule_condition operation method

        :param rcid: rcid variable. Nullable: False
        :type rcid: str
        :param exceptoperand: exceptoperand variable. Nullable: True
        :type exceptoperand: str
        :param regex: regex variable. Nullable: True
        :type regex: str
        :param exactorder: exactorder variable. Nullable: True
        :type exactorder: str
        :param operator: operator variable. Nullable: True
        :type operator: str
        :param operand: operand variable. Nullable: True
        :type operand: str
        """
        out_args = {'rcid': rcid, 'exceptoperand': exceptoperand, 'regex': regex, 'exactorder': exactorder, 'operator': operator, 'operand': operand}
        return self.call("mod_rule_condition", **out_args)

    def mod_server_option(self, name, persistent, value):
        """
        MFNA mod_server_option operation method

        :param name: name variable. Nullable: False
        :type name: str
        :param persistent: persistent variable. Nullable: False
        :type persistent: str
        :param value: value variable. Nullable: False
        :type value: str
        """
        out_args = {'name': name, 'persistent': persistent, 'value': value}
        return self.call("mod_server_option", **out_args)

    def mod_site(self, name, managingcoreid):
        """
        MFNA mod_site operation method

        :param name: name variable. Nullable: False
        :type name: str
        :param managingcoreid: managingcoreid variable. Nullable: False
        :type managingcoreid: str
        """
        out_args = {'name': name, 'managingcoreid': managingcoreid}
        return self.call("mod_site", **out_args)

    def mod_task(self, id, runmode=None, enablepasswd=None, retrycount=None, snmpro=None, stoponfailure=None, taskname=None, duration=None, maxwaittime=None, reject=None, override=None, customvalues=None, repeatinterval=None, customnames=None, sessionlog=None, customvalue=None, start=None, priority=None, expensive=None, useaaa=None, retryinterval=None, notexpensive=None, passwd=None, approve=None, customname=None, days=None, repeattype=None, comment=None, coreid=None, user=None, snmprw=None):
        """
        MFNA mod_task operation method

        :param id: id variable. Nullable: False
        :type id: str
        :param runmode: runmode variable. Nullable: True
        :type runmode: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param retrycount: retrycount variable. Nullable: True
        :type retrycount: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param stoponfailure: stoponfailure variable. Nullable: True
        :type stoponfailure: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param duration: duration variable. Nullable: True
        :type duration: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param reject: reject variable. Nullable: True
        :type reject: str
        :param override: override variable. Nullable: True
        :type override: str
        :param customvalues: customvalues variable. Nullable: True
        :type customvalues: str
        :param repeatinterval: repeatinterval variable. Nullable: True
        :type repeatinterval: str
        :param customnames: customnames variable. Nullable: True
        :type customnames: str
        :param sessionlog: sessionlog variable. Nullable: True
        :type sessionlog: str
        :param customvalue: customvalue variable. Nullable: True
        :type customvalue: str
        :param start: start variable. Nullable: True
        :type start: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param expensive: expensive variable. Nullable: True
        :type expensive: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param retryinterval: retryinterval variable. Nullable: True
        :type retryinterval: str
        :param notexpensive: notexpensive variable. Nullable: True
        :type notexpensive: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param approve: approve variable. Nullable: True
        :type approve: str
        :param customname: customname variable. Nullable: True
        :type customname: str
        :param days: days variable. Nullable: True
        :type days: str
        :param repeattype: repeattype variable. Nullable: True
        :type repeattype: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param coreid: coreid variable. Nullable: True
        :type coreid: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        """
        out_args = {'id': id, 'runmode': runmode, 'enablepasswd': enablepasswd, 'retrycount': retrycount, 'snmpro': snmpro, 'stoponfailure': stoponfailure, 'taskname': taskname, 'duration': duration, 'maxwaittime': maxwaittime, 'reject': reject, 'override': override, 'customvalues': customvalues, 'repeatinterval': repeatinterval, 'customnames': customnames, 'sessionlog': sessionlog, 'customvalue': customvalue, 'start': start, 'priority': priority, 'expensive': expensive, 'useaaa': useaaa, 'retryinterval': retryinterval, 'notexpensive': notexpensive, 'passwd': passwd, 'approve': approve, 'customname': customname, 'days': days, 'repeattype': repeattype, 'comment': comment, 'coreid': coreid, 'user': user, 'snmprw': snmprw}
        return self.call("mod_task", **out_args)

    def mod_topology_graph(self, data, type, deviceid, remotedeviceid=None, deviceportid=None, remotedeviceportid=None, serverportid=None, serverid=None):
        """
        MFNA mod_topology_graph operation method

        :param data: data variable. Nullable: False
        :type data: str
        :param type: type variable. Nullable: False
        :type type: str
        :param deviceid: deviceid variable. Nullable: False
        :type deviceid: str
        :param remotedeviceid: remotedeviceid variable. Nullable: True
        :type remotedeviceid: str
        :param deviceportid: deviceportid variable. Nullable: True
        :type deviceportid: str
        :param remotedeviceportid: remotedeviceportid variable. Nullable: True
        :type remotedeviceportid: str
        :param serverportid: serverportid variable. Nullable: True
        :type serverportid: str
        :param serverid: serverid variable. Nullable: True
        :type serverid: str
        """
        out_args = {'data': data, 'type': type, 'deviceid': deviceid, 'remotedeviceid': remotedeviceid, 'deviceportid': deviceportid, 'remotedeviceportid': remotedeviceportid, 'serverportid': serverportid, 'serverid': serverid}
        return self.call("mod_topology_graph", **out_args)

    def mod_unmanaged_device(self, comment=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA mod_unmanaged_device operation method

        :param comment: comment variable. Nullable: True
        :type comment: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'comment': comment, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("mod_unmanaged_device", **out_args)

    def mod_user(self, u, customnames=None, newusername=None, ln=None, aaausername=None, view3partition=None, fn=None, customvalue=None, extauthfailover=None, aaapassword=None, p=None, view2partition=None, customname=None, priv=None, customvalues=None, view1partition=None, useaaaloginforproxy=None, email=None, status=None):
        """
        MFNA mod_user operation method

        :param u: u variable. Nullable: False
        :type u: str
        :param customnames: customnames variable. Nullable: True
        :type customnames: str
        :param newusername: newusername variable. Nullable: True
        :type newusername: str
        :param ln: ln variable. Nullable: True
        :type ln: str
        :param aaausername: aaausername variable. Nullable: True
        :type aaausername: str
        :param view3partition: view3partition variable. Nullable: True
        :type view3partition: str
        :param fn: fn variable. Nullable: True
        :type fn: str
        :param customvalue: customvalue variable. Nullable: True
        :type customvalue: str
        :param extauthfailover: extauthfailover variable. Nullable: True
        :type extauthfailover: str
        :param aaapassword: aaapassword variable. Nullable: True
        :type aaapassword: str
        :param p: p variable. Nullable: True
        :type p: str
        :param view2partition: view2partition variable. Nullable: True
        :type view2partition: str
        :param customname: customname variable. Nullable: True
        :type customname: str
        :param priv: priv variable. Nullable: True
        :type priv: str
        :param customvalues: customvalues variable. Nullable: True
        :type customvalues: str
        :param view1partition: view1partition variable. Nullable: True
        :type view1partition: str
        :param useaaaloginforproxy: useaaaloginforproxy variable. Nullable: True
        :type useaaaloginforproxy: str
        :param email: email variable. Nullable: True
        :type email: str
        :param status: status variable. Nullable: True
        :type status: str
        """
        out_args = {'u': u, 'customnames': customnames, 'newusername': newusername, 'ln': ln, 'aaausername': aaausername, 'view3partition': view3partition, 'fn': fn, 'customvalue': customvalue, 'extauthfailover': extauthfailover, 'aaapassword': aaapassword, 'p': p, 'view2partition': view2partition, 'customname': customname, 'priv': priv, 'customvalues': customvalues, 'view1partition': view1partition, 'useaaaloginforproxy': useaaaloginforproxy, 'email': email, 'status': status}
        return self.call("mod_user", **out_args)

    def mod_user_group(self, name, view2partition=None, cmdperms=None, view3partition=None, scriptperms=None, viewperms=None, description=None, view1partition=None, newname=None, deviceperms=None):
        """
        MFNA mod_user_group operation method

        :param name: name variable. Nullable: False
        :type name: str
        :param view2partition: view2partition variable. Nullable: True
        :type view2partition: str
        :param cmdperms: cmdperms variable. Nullable: True
        :type cmdperms: str
        :param view3partition: view3partition variable. Nullable: True
        :type view3partition: str
        :param scriptperms: scriptperms variable. Nullable: True
        :type scriptperms: str
        :param viewperms: viewperms variable. Nullable: True
        :type viewperms: str
        :param description: description variable. Nullable: True
        :type description: str
        :param view1partition: view1partition variable. Nullable: True
        :type view1partition: str
        :param newname: newname variable. Nullable: True
        :type newname: str
        :param deviceperms: deviceperms variable. Nullable: True
        :type deviceperms: str
        """
        out_args = {'name': name, 'view2partition': view2partition, 'cmdperms': cmdperms, 'view3partition': view3partition, 'scriptperms': scriptperms, 'viewperms': viewperms, 'description': description, 'view1partition': view1partition, 'newname': newname, 'deviceperms': deviceperms}
        return self.call("mod_user_group", **out_args)

    def mod_version(self, add=None, remove=None):
        """
        MFNA mod_version operation method

        :param add: add variable. Nullable: True
        :type add: str
        :param remove: remove variable. Nullable: True
        :type remove: str
        """
        out_args = {'add': add, 'remove': remove}
        return self.call("mod_version", **out_args)

    def mod_vlan(self, vlanid, removeports=None, sessionlog=None, enablepasswd=None, renameto=None, retrycount=None, snmpro=None, start=None, taskname=None, priority=None, sync=None, maxwaittime=None, useaaa=None, retryinterval=None, addports=None, passwd=None, postsnapshot=None, comment=None, presnapshot=None, rep=None, user=None, snmprw=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA mod_vlan operation method

        :param vlanid: vlanid variable. Nullable: False
        :type vlanid: str
        :param removeports: removeports variable. Nullable: True
        :type removeports: str
        :param sessionlog: sessionlog variable. Nullable: True
        :type sessionlog: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param renameto: renameto variable. Nullable: True
        :type renameto: str
        :param retrycount: retrycount variable. Nullable: True
        :type retrycount: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param start: start variable. Nullable: True
        :type start: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param sync: sync variable. Nullable: True
        :type sync: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param retryinterval: retryinterval variable. Nullable: True
        :type retryinterval: str
        :param addports: addports variable. Nullable: True
        :type addports: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param postsnapshot: postsnapshot variable. Nullable: True
        :type postsnapshot: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param presnapshot: presnapshot variable. Nullable: True
        :type presnapshot: str
        :param rep: rep variable. Nullable: True
        :type rep: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'vlanid': vlanid, 'removeports': removeports, 'sessionlog': sessionlog, 'enablepasswd': enablepasswd, 'renameto': renameto, 'retrycount': retrycount, 'snmpro': snmpro, 'start': start, 'taskname': taskname, 'priority': priority, 'sync': sync, 'maxwaittime': maxwaittime, 'useaaa': useaaa, 'retryinterval': retryinterval, 'addports': addports, 'passwd': passwd, 'postsnapshot': postsnapshot, 'comment': comment, 'presnapshot': presnapshot, 'rep': rep, 'user': user, 'snmprw': snmprw, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("mod_vlan", **out_args)

    def mod_vlan_trunk(self, nativevlanid, portname, sessionlog=None, enablepasswd=None, retrycount=None, snmpro=None, start=None, taskname=None, priority=None, addvlanids=None, sync=None, removevlanids=None, maxwaittime=None, useaaa=None, retryinterval=None, passwd=None, postsnapshot=None, comment=None, presnapshot=None, rep=None, user=None, snmprw=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA mod_vlan_trunk operation method

        :param nativevlanid: nativevlanid variable. Nullable: False
        :type nativevlanid: str
        :param portname: portname variable. Nullable: False
        :type portname: str
        :param sessionlog: sessionlog variable. Nullable: True
        :type sessionlog: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param retrycount: retrycount variable. Nullable: True
        :type retrycount: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param start: start variable. Nullable: True
        :type start: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param addvlanids: addvlanids variable. Nullable: True
        :type addvlanids: str
        :param sync: sync variable. Nullable: True
        :type sync: str
        :param removevlanids: removevlanids variable. Nullable: True
        :type removevlanids: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param retryinterval: retryinterval variable. Nullable: True
        :type retryinterval: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param postsnapshot: postsnapshot variable. Nullable: True
        :type postsnapshot: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param presnapshot: presnapshot variable. Nullable: True
        :type presnapshot: str
        :param rep: rep variable. Nullable: True
        :type rep: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'nativevlanid': nativevlanid, 'portname': portname, 'sessionlog': sessionlog, 'enablepasswd': enablepasswd, 'retrycount': retrycount, 'snmpro': snmpro, 'start': start, 'taskname': taskname, 'priority': priority, 'addvlanids': addvlanids, 'sync': sync, 'removevlanids': removevlanids, 'maxwaittime': maxwaittime, 'useaaa': useaaa, 'retryinterval': retryinterval, 'passwd': passwd, 'postsnapshot': postsnapshot, 'comment': comment, 'presnapshot': presnapshot, 'rep': rep, 'user': user, 'snmprw': snmprw, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("mod_vlan_trunk", **out_args)

    def passwd(self, oldpwd, newpwd):
        """
        MFNA passwd operation method

        :param oldpwd: oldpwd variable. Nullable: False
        :type oldpwd: str
        :param newpwd: newpwd variable. Nullable: False
        :type newpwd: str
        """
        out_args = {'oldpwd': oldpwd, 'newpwd': newpwd}
        return self.call("passwd", **out_args)

    def pause_polling(self):
        return self.call("pause_polling")

    def ping(self, dest, sourcegroup=None, enablepasswd=None, snmpro=None, start=None, source=None, priority=None, maxwaittime=None, useaaa=None, async_=None, passwd=None, rep=None, user=None, snmprw=None):
        """
        MFNA ping operation method

        :param dest: dest variable. Nullable: False
        :type dest: str
        :param sourcegroup: sourcegroup variable. Nullable: True
        :type sourcegroup: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param start: start variable. Nullable: True
        :type start: str
        :param source: source variable. Nullable: True
        :type source: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param async_: async variable. Nullable: True
        :type async_: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param rep: rep variable. Nullable: True
        :type rep: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        """
        out_args = {'dest': dest, 'sourcegroup': sourcegroup, 'enablepasswd': enablepasswd, 'snmpro': snmpro, 'start': start, 'source': source, 'priority': priority, 'maxwaittime': maxwaittime, 'useaaa': useaaa, 'async': async_, 'passwd': passwd, 'rep': rep, 'user': user, 'snmprw': snmprw}
        return self.call("ping", **out_args)

    def port_scan(self, maxwaittime=None, async_=None, ip=None, start=None, taskname=None, id=None, rep=None, priority=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA port_scan operation method

        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param async_: async variable. Nullable: True
        :type async_: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param start: start variable. Nullable: True
        :type start: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param id: id variable. Nullable: True
        :type id: str
        :param rep: rep variable. Nullable: True
        :type rep: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'maxwaittime': maxwaittime, 'async': async_, 'ip': ip, 'start': start, 'taskname': taskname, 'id': id, 'rep': rep, 'priority': priority, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("port_scan", **out_args)

    def provision_device(self, templateid, sessionlog=None, copydata=None, variables=None, retrycount=None, start=None, taskname=None, priority=None, maxwaittime=None, duration=None, nocompliance=None, ignorevariables=None, retryinterval=None, name=None, postsnapshot=None, comment=None, presnapshot=None, rep=None, setactive=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA provision_device operation method

        :param templateid: templateid variable. Nullable: False
        :type templateid: str
        :param sessionlog: sessionlog variable. Nullable: True
        :type sessionlog: str
        :param copydata: copydata variable. Nullable: True
        :type copydata: str
        :param variables: variables variable. Nullable: True
        :type variables: str
        :param retrycount: retrycount variable. Nullable: True
        :type retrycount: str
        :param start: start variable. Nullable: True
        :type start: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param duration: duration variable. Nullable: True
        :type duration: str
        :param nocompliance: nocompliance variable. Nullable: True
        :type nocompliance: str
        :param ignorevariables: ignorevariables variable. Nullable: True
        :type ignorevariables: str
        :param retryinterval: retryinterval variable. Nullable: True
        :type retryinterval: str
        :param name: name variable. Nullable: True
        :type name: str
        :param postsnapshot: postsnapshot variable. Nullable: True
        :type postsnapshot: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param presnapshot: presnapshot variable. Nullable: True
        :type presnapshot: str
        :param rep: rep variable. Nullable: True
        :type rep: str
        :param setactive: setactive variable. Nullable: True
        :type setactive: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'templateid': templateid, 'sessionlog': sessionlog, 'copydata': copydata, 'variables': variables, 'retrycount': retrycount, 'start': start, 'taskname': taskname, 'priority': priority, 'maxwaittime': maxwaittime, 'duration': duration, 'nocompliance': nocompliance, 'ignorevariables': ignorevariables, 'retryinterval': retryinterval, 'name': name, 'postsnapshot': postsnapshot, 'comment': comment, 'presnapshot': presnapshot, 'rep': rep, 'setactive': setactive, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("provision_device", **out_args)

    def reboot_device(self, runmode=None, sessionlog=None, enablepasswd=None, estimatedreboottime=None, retrycount=None, snmpro=None, stoponfailure=None, ip=None, start=None, taskname=None, forcesave=None, priority=None, verifyreboot=None, maxwaittime=None, useaaa=None, retryinterval=None, passwd=None, comment=None, rep=None, user=None, snmprw=None, group=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA reboot_device operation method

        :param runmode: runmode variable. Nullable: True
        :type runmode: str
        :param sessionlog: sessionlog variable. Nullable: True
        :type sessionlog: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param estimatedreboottime: estimatedreboottime variable. Nullable: True
        :type estimatedreboottime: str
        :param retrycount: retrycount variable. Nullable: True
        :type retrycount: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param stoponfailure: stoponfailure variable. Nullable: True
        :type stoponfailure: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param start: start variable. Nullable: True
        :type start: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param forcesave: forcesave variable. Nullable: True
        :type forcesave: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param verifyreboot: verifyreboot variable. Nullable: True
        :type verifyreboot: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param retryinterval: retryinterval variable. Nullable: True
        :type retryinterval: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param rep: rep variable. Nullable: True
        :type rep: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        :param group: group variable. Nullable: True
        :type group: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'runmode': runmode, 'sessionlog': sessionlog, 'enablepasswd': enablepasswd, 'estimatedreboottime': estimatedreboottime, 'retrycount': retrycount, 'snmpro': snmpro, 'stoponfailure': stoponfailure, 'ip': ip, 'start': start, 'taskname': taskname, 'forcesave': forcesave, 'priority': priority, 'verifyreboot': verifyreboot, 'maxwaittime': maxwaittime, 'useaaa': useaaa, 'retryinterval': retryinterval, 'passwd': passwd, 'comment': comment, 'rep': rep, 'user': user, 'snmprw': snmprw, 'group': group, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("reboot_device", **out_args)

    def release_resource_id(self, id):
        """
        MFNA release_resource_id operation method

        :param id: id variable. Nullable: False
        :type id: str
        """
        out_args = {'id': id}
        return self.call("release_resource_id", **out_args)

    def reload_content(self):
        return self.call("reload_content")

    def reload_drivers(self, force=None):
        """
        MFNA reload_drivers operation method

        :param force: force variable. Nullable: True
        :type force: str
        """
        out_args = {'force': force}
        return self.call("reload_drivers", **out_args)

    def reload_plugins(self):
        return self.call("reload_plugins")

    def reload_server_options(self):
        return self.call("reload_server_options")

    def remove_auto_remediation_script(self, scriptid, ruleid):
        """
        MFNA remove_auto_remediation_script operation method

        :param scriptid: scriptid variable. Nullable: False
        :type scriptid: str
        :param ruleid: ruleid variable. Nullable: False
        :type ruleid: str
        """
        out_args = {'scriptid': scriptid, 'ruleid': ruleid}
        return self.call("remove_auto_remediation_script", **out_args)

    def replication_start(self):
        return self.call("replication_start")

    def replication_status(self):
        return self.call("replication_status")

    def replication_stop(self):
        return self.call("replication_stop")

    def replication_sync(self):
        return self.call("replication_sync")

    def resume_polling(self):
        return self.call("resume_polling")

    def run_advanced_script(self, name, runmode=None, sessionlog=None, enablepasswd=None, variables=None, snmpro=None, stoponfailure=None, ip=None, start=None, taskname=None, priority=None, sync=None, maxwaittime=None, useaaa=None, passwd=None, postsnapshot=None, presnapshot=None, comment=None, rep=None, parameters=None, user=None, snmprw=None, nowait=None, group=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA run_advanced_script operation method

        :param name: name variable. Nullable: False
        :type name: str
        :param runmode: runmode variable. Nullable: True
        :type runmode: str
        :param sessionlog: sessionlog variable. Nullable: True
        :type sessionlog: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param variables: variables variable. Nullable: True
        :type variables: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param stoponfailure: stoponfailure variable. Nullable: True
        :type stoponfailure: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param start: start variable. Nullable: True
        :type start: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param sync: sync variable. Nullable: True
        :type sync: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param postsnapshot: postsnapshot variable. Nullable: True
        :type postsnapshot: str
        :param presnapshot: presnapshot variable. Nullable: True
        :type presnapshot: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param rep: rep variable. Nullable: True
        :type rep: str
        :param parameters: parameters variable. Nullable: True
        :type parameters: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        :param nowait: nowait variable. Nullable: True
        :type nowait: str
        :param group: group variable. Nullable: True
        :type group: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'name': name, 'runmode': runmode, 'sessionlog': sessionlog, 'enablepasswd': enablepasswd, 'variables': variables, 'snmpro': snmpro, 'stoponfailure': stoponfailure, 'ip': ip, 'start': start, 'taskname': taskname, 'priority': priority, 'sync': sync, 'maxwaittime': maxwaittime, 'useaaa': useaaa, 'passwd': passwd, 'postsnapshot': postsnapshot, 'presnapshot': presnapshot, 'comment': comment, 'rep': rep, 'parameters': parameters, 'user': user, 'snmprw': snmprw, 'nowait': nowait, 'group': group, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("run_advanced_script", **out_args)

    def run_command_script(self, name, runmode=None, sessionlog=None, enablepasswd=None, variables=None, linebyline=None, snmpro=None, stoponfailure=None, ip=None, start=None, taskname=None, priority=None, sync=None, maxwaittime=None, useaaa=None, passwd=None, postsnapshot=None, presnapshot=None, comment=None, rep=None, user=None, snmprw=None, nowait=None, group=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA run_command_script operation method

        :param name: name variable. Nullable: False
        :type name: str
        :param runmode: runmode variable. Nullable: True
        :type runmode: str
        :param sessionlog: sessionlog variable. Nullable: True
        :type sessionlog: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param variables: variables variable. Nullable: True
        :type variables: str
        :param linebyline: linebyline variable. Nullable: True
        :type linebyline: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param stoponfailure: stoponfailure variable. Nullable: True
        :type stoponfailure: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param start: start variable. Nullable: True
        :type start: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param sync: sync variable. Nullable: True
        :type sync: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param postsnapshot: postsnapshot variable. Nullable: True
        :type postsnapshot: str
        :param presnapshot: presnapshot variable. Nullable: True
        :type presnapshot: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param rep: rep variable. Nullable: True
        :type rep: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        :param nowait: nowait variable. Nullable: True
        :type nowait: str
        :param group: group variable. Nullable: True
        :type group: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'name': name, 'runmode': runmode, 'sessionlog': sessionlog, 'enablepasswd': enablepasswd, 'variables': variables, 'linebyline': linebyline, 'snmpro': snmpro, 'stoponfailure': stoponfailure, 'ip': ip, 'start': start, 'taskname': taskname, 'priority': priority, 'sync': sync, 'maxwaittime': maxwaittime, 'useaaa': useaaa, 'passwd': passwd, 'postsnapshot': postsnapshot, 'presnapshot': presnapshot, 'comment': comment, 'rep': rep, 'user': user, 'snmprw': snmprw, 'nowait': nowait, 'group': group, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("run_command_script", **out_args)

    def run_diagnostic(self, diagnostic, runmode=None, enablepasswd=None, retrycount=None, snmpro=None, stoponfailure=None, taskname=None, duration=None, maxwaittime=None, customvalues=None, rep=None, group=None, customnames=None, sessionlog=None, ip=None, customvalue=None, start=None, priority=None, sync=None, useaaa=None, retryinterval=None, passwd=None, customname=None, comment=None, user=None, snmprw=None, nowait=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA run_diagnostic operation method

        :param diagnostic: diagnostic variable. Nullable: False
        :type diagnostic: str
        :param runmode: runmode variable. Nullable: True
        :type runmode: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param retrycount: retrycount variable. Nullable: True
        :type retrycount: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param stoponfailure: stoponfailure variable. Nullable: True
        :type stoponfailure: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param duration: duration variable. Nullable: True
        :type duration: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param customvalues: customvalues variable. Nullable: True
        :type customvalues: str
        :param rep: rep variable. Nullable: True
        :type rep: str
        :param group: group variable. Nullable: True
        :type group: str
        :param customnames: customnames variable. Nullable: True
        :type customnames: str
        :param sessionlog: sessionlog variable. Nullable: True
        :type sessionlog: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param customvalue: customvalue variable. Nullable: True
        :type customvalue: str
        :param start: start variable. Nullable: True
        :type start: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param sync: sync variable. Nullable: True
        :type sync: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param retryinterval: retryinterval variable. Nullable: True
        :type retryinterval: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param customname: customname variable. Nullable: True
        :type customname: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        :param nowait: nowait variable. Nullable: True
        :type nowait: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'diagnostic': diagnostic, 'runmode': runmode, 'enablepasswd': enablepasswd, 'retrycount': retrycount, 'snmpro': snmpro, 'stoponfailure': stoponfailure, 'taskname': taskname, 'duration': duration, 'maxwaittime': maxwaittime, 'customvalues': customvalues, 'rep': rep, 'group': group, 'customnames': customnames, 'sessionlog': sessionlog, 'ip': ip, 'customvalue': customvalue, 'start': start, 'priority': priority, 'sync': sync, 'useaaa': useaaa, 'retryinterval': retryinterval, 'passwd': passwd, 'customname': customname, 'comment': comment, 'user': user, 'snmprw': snmprw, 'nowait': nowait, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("run_diagnostic", **out_args)

    def run_external_application(self, app, maxwaittime=None, startdir=None, start=None, taskname=None, comment=None, errorifnonzero=None, resultfile=None, rep=None, priority=None, sync=None):
        """
        MFNA run_external_application operation method

        :param app: app variable. Nullable: False
        :type app: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param startdir: startdir variable. Nullable: True
        :type startdir: str
        :param start: start variable. Nullable: True
        :type start: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param errorifnonzero: errorifnonzero variable. Nullable: True
        :type errorifnonzero: str
        :param resultfile: resultfile variable. Nullable: True
        :type resultfile: str
        :param rep: rep variable. Nullable: True
        :type rep: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param sync: sync variable. Nullable: True
        :type sync: str
        """
        out_args = {'app': app, 'maxwaittime': maxwaittime, 'startdir': startdir, 'start': start, 'taskname': taskname, 'comment': comment, 'errorifnonzero': errorifnonzero, 'resultfile': resultfile, 'rep': rep, 'priority': priority, 'sync': sync}
        return self.call("run_external_application", **out_args)

    def run_gc(self):
        return self.call("run_gc")

    def run_script(self, runmode=None, enablepasswd=None, snmpro=None, linebyline=None, stoponfailure=None, ip=None, start=None, taskname=None, priority=None, sync=None, script=None, mode=None, maxwaittime=None, useaaa=None, disablesessionlogging=None, passwd=None, postsnapshot=None, comment=None, presnapshot=None, rep=None, user=None, snmprw=None, nowait=None, group=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA run_script operation method

        :param runmode: runmode variable. Nullable: True
        :type runmode: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param linebyline: linebyline variable. Nullable: True
        :type linebyline: str
        :param stoponfailure: stoponfailure variable. Nullable: True
        :type stoponfailure: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param start: start variable. Nullable: True
        :type start: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param sync: sync variable. Nullable: True
        :type sync: str
        :param script: script variable. Nullable: True
        :type script: str
        :param mode: mode variable. Nullable: True
        :type mode: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param disablesessionlogging: disablesessionlogging variable. Nullable: True
        :type disablesessionlogging: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param postsnapshot: postsnapshot variable. Nullable: True
        :type postsnapshot: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param presnapshot: presnapshot variable. Nullable: True
        :type presnapshot: str
        :param rep: rep variable. Nullable: True
        :type rep: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        :param nowait: nowait variable. Nullable: True
        :type nowait: str
        :param group: group variable. Nullable: True
        :type group: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'runmode': runmode, 'enablepasswd': enablepasswd, 'snmpro': snmpro, 'linebyline': linebyline, 'stoponfailure': stoponfailure, 'ip': ip, 'start': start, 'taskname': taskname, 'priority': priority, 'sync': sync, 'script': script, 'mode': mode, 'maxwaittime': maxwaittime, 'useaaa': useaaa, 'disablesessionlogging': disablesessionlogging, 'passwd': passwd, 'postsnapshot': postsnapshot, 'comment': comment, 'presnapshot': presnapshot, 'rep': rep, 'user': user, 'snmprw': snmprw, 'nowait': nowait, 'group': group, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("run_script", **out_args)

    def search_reports(self, expression, queryname, type):
        """
        MFNA search_reports operation method

        :param expression: expression variable. Nullable: False
        :type expression: str
        :param queryname: queryname variable. Nullable: False
        :type queryname: str
        :param type: type variable. Nullable: False
        :type type: str
        """
        out_args = {'expression': expression, 'queryname': queryname, 'type': type}
        return self.call("search_reports", **out_args)

    def set_core_status(self, coreid, status):
        """
        MFNA set_core_status operation method

        :param coreid: coreid variable. Nullable: False
        :type coreid: str
        :param status: status variable. Nullable: False
        :type status: str
        """
        out_args = {'coreid': coreid, 'status': status}
        return self.call("set_core_status", **out_args)

    def set_policy_rule_logic(self, ruleid, boolexpr):
        """
        MFNA set_policy_rule_logic operation method

        :param ruleid: ruleid variable. Nullable: False
        :type ruleid: str
        :param boolexpr: boolexpr variable. Nullable: False
        :type boolexpr: str
        """
        out_args = {'ruleid': ruleid, 'boolexpr': boolexpr}
        return self.call("set_policy_rule_logic", **out_args)

    def show_access(self, id):
        """
        MFNA show_access operation method

        :param id: id variable. Nullable: False
        :type id: str
        """
        out_args = {'id': id}
        return self.call("show_access", **out_args)

    def show_acl(self, id):
        """
        MFNA show_acl operation method

        :param id: id variable. Nullable: False
        :type id: str
        """
        out_args = {'id': id}
        return self.call("show_acl", **out_args)

    def show_basicip(self, ip=None, id=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA show_basicip operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param id: id variable. Nullable: True
        :type id: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'id': id, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("show_basicip", **out_args)

    def show_caseinsensitive(self):
        return self.call("show_caseinsensitive")

    def show_change_plan(self, name=None, id=None):
        """
        MFNA show_change_plan operation method

        :param name: name variable. Nullable: True
        :type name: str
        :param id: id variable. Nullable: True
        :type id: str
        """
        out_args = {'name': name, 'id': id}
        return self.call("show_change_plan", **out_args)

    def show_config(self, id, mask=None):
        """
        MFNA show_config operation method

        :param id: id variable. Nullable: False
        :type id: str
        :param mask: mask variable. Nullable: True
        :type mask: str
        """
        out_args = {'id': id, 'mask': mask}
        return self.call("show_config", **out_args)

    def show_configlet(self, start=None, end=None, type=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA show_configlet operation method

        :param start: start variable. Nullable: True
        :type start: str
        :param end: end variable. Nullable: True
        :type end: str
        :param type: type variable. Nullable: True
        :type type: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'start': start, 'end': end, 'type': type, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("show_configlet", **out_args)

    def show_device(self, nodeuuid=None, ip=None, id=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA show_device operation method

        :param nodeuuid: nodeuuid variable. Nullable: True
        :type nodeuuid: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param id: id variable. Nullable: True
        :type id: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'nodeuuid': nodeuuid, 'ip': ip, 'id': id, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("show_device", **out_args)

    def show_device_config(self, ip=None, id=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA show_device_config operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param id: id variable. Nullable: True
        :type id: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'id': id, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("show_device_config", **out_args)

    def show_device_credentials(self, protocol=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA show_device_credentials operation method

        :param protocol: protocol variable. Nullable: True
        :type protocol: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'protocol': protocol, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("show_device_credentials", **out_args)

    def show_device_family(self, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA show_device_family operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("show_device_family", **out_args)

    def show_device_latest_diff(self, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA show_device_latest_diff operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("show_device_latest_diff", **out_args)

    def show_device_template(self, templateid):
        """
        MFNA show_device_template operation method

        :param templateid: templateid variable. Nullable: False
        :type templateid: str
        """
        out_args = {'templateid': templateid}
        return self.call("show_device_template", **out_args)

    def show_device_template_config(self, templateid):
        """
        MFNA show_device_template_config operation method

        :param templateid: templateid variable. Nullable: False
        :type templateid: str
        """
        out_args = {'templateid': templateid}
        return self.call("show_device_template_config", **out_args)

    def show_device_template_config_variables(self, templateid):
        """
        MFNA show_device_template_config_variables operation method

        :param templateid: templateid variable. Nullable: False
        :type templateid: str
        """
        out_args = {'templateid': templateid}
        return self.call("show_device_template_config_variables", **out_args)

    def show_deviceinfo(self, ip=None, id=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA show_deviceinfo operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param id: id variable. Nullable: True
        :type id: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'id': id, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("show_deviceinfo", **out_args)

    def show_diagnostic(self, id):
        """
        MFNA show_diagnostic operation method

        :param id: id variable. Nullable: False
        :type id: str
        """
        out_args = {'id': id}
        return self.call("show_diagnostic", **out_args)

    def show_driver(self, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA show_driver operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("show_driver", **out_args)

    def show_event(self, id):
        """
        MFNA show_event operation method

        :param id: id variable. Nullable: False
        :type id: str
        """
        out_args = {'id': id}
        return self.call("show_event", **out_args)

    def show_group(self, name=None, id=None):
        """
        MFNA show_group operation method

        :param name: name variable. Nullable: True
        :type name: str
        :param id: id variable. Nullable: True
        :type id: str
        """
        out_args = {'name': name, 'id': id}
        return self.call("show_group", **out_args)

    def show_icmp(self, ip=None, id=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA show_icmp operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param id: id variable. Nullable: True
        :type id: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'id': id, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("show_icmp", **out_args)

    def show_int(self, ip=None, id=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA show_int operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param id: id variable. Nullable: True
        :type id: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'id': id, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("show_int", **out_args)

    def show_ip(self, deviceip, ipvalue):
        """
        MFNA show_ip operation method

        :param deviceip: deviceip variable. Nullable: False
        :type deviceip: str
        :param ipvalue: ipvalue variable. Nullable: False
        :type ipvalue: str
        """
        out_args = {'deviceip': deviceip, 'ipvalue': ipvalue}
        return self.call("show_ip", **out_args)

    def show_latest_access(self, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA show_latest_access operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("show_latest_access", **out_args)

    def show_memory(self):
        return self.call("show_memory")

    def show_metadata(self, metadataid):
        """
        MFNA show_metadata operation method

        :param metadataid: metadataid variable. Nullable: False
        :type metadataid: str
        """
        out_args = {'metadataid': metadataid}
        return self.call("show_metadata", **out_args)

    def show_metadata_field(self, fieldid):
        """
        MFNA show_metadata_field operation method

        :param fieldid: fieldid variable. Nullable: False
        :type fieldid: str
        """
        out_args = {'fieldid': fieldid}
        return self.call("show_metadata_field", **out_args)

    def show_module(self, id):
        """
        MFNA show_module operation method

        :param id: id variable. Nullable: False
        :type id: str
        """
        out_args = {'id': id}
        return self.call("show_module", **out_args)

    def show_nnmi_integration(self, id=None, nnmisystemid=None):
        """
        MFNA show_nnmi_integration operation method

        :param id: id variable. Nullable: True
        :type id: str
        :param nnmisystemid: nnmisystemid variable. Nullable: True
        :type nnmisystemid: str
        """
        out_args = {'id': id, 'nnmisystemid': nnmisystemid}
        return self.call("show_nnmi_integration", **out_args)

    def show_nnmi_node_association(self, deviceid, nnmisystemid):
        """
        MFNA show_nnmi_node_association operation method

        :param deviceid: deviceid variable. Nullable: False
        :type deviceid: str
        :param nnmisystemid: nnmisystemid variable. Nullable: False
        :type nnmisystemid: str
        """
        out_args = {'deviceid': deviceid, 'nnmisystemid': nnmisystemid}
        return self.call("show_nnmi_node_association", **out_args)

    def show_oraclecaseinsensitive(self):
        return self.call("show_oraclecaseinsensitive")

    def show_ospfneighbor(self, ip=None, id=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA show_ospfneighbor operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param id: id variable. Nullable: True
        :type id: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'id': id, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("show_ospfneighbor", **out_args)

    def show_permission(self, resource, u=None, id=None):
        """
        MFNA show_permission operation method

        :param resource: resource variable. Nullable: False
        :type resource: str
        :param u: u variable. Nullable: True
        :type u: str
        :param id: id variable. Nullable: True
        :type id: str
        """
        out_args = {'resource': resource, 'u': u, 'id': id}
        return self.call("show_permission", **out_args)

    def show_policy(self, id):
        """
        MFNA show_policy operation method

        :param id: id variable. Nullable: False
        :type id: str
        """
        out_args = {'id': id}
        return self.call("show_policy", **out_args)

    def show_policy_compliance(self, policyid=None, compliance=None, deviceid=None):
        """
        MFNA show_policy_compliance operation method

        :param policyid: policyid variable. Nullable: True
        :type policyid: str
        :param compliance: compliance variable. Nullable: True
        :type compliance: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'policyid': policyid, 'compliance': compliance, 'deviceid': deviceid}
        return self.call("show_policy_compliance", **out_args)

    def show_policy_rule(self, id):
        """
        MFNA show_policy_rule operation method

        :param id: id variable. Nullable: False
        :type id: str
        """
        out_args = {'id': id}
        return self.call("show_policy_rule", **out_args)

    def show_polling_status(self):
        return self.call("show_polling_status")

    def show_port(self, id):
        """
        MFNA show_port operation method

        :param id: id variable. Nullable: False
        :type id: str
        """
        out_args = {'id': id}
        return self.call("show_port", **out_args)

    def show_resource_id(self, name=None, poolid=None, id=None):
        """
        MFNA show_resource_id operation method

        :param name: name variable. Nullable: True
        :type name: str
        :param poolid: poolid variable. Nullable: True
        :type poolid: str
        :param id: id variable. Nullable: True
        :type id: str
        """
        out_args = {'name': name, 'poolid': poolid, 'id': id}
        return self.call("show_resource_id", **out_args)

    def show_resource_id_custom_field_data(self, fielddataid):
        """
        MFNA show_resource_id_custom_field_data operation method

        :param fielddataid: fielddataid variable. Nullable: False
        :type fielddataid: str
        """
        out_args = {'fielddataid': fielddataid}
        return self.call("show_resource_id_custom_field_data", **out_args)

    def show_resource_id_pool(self, site=None, name=None, id=None):
        """
        MFNA show_resource_id_pool operation method

        :param site: site variable. Nullable: True
        :type site: str
        :param name: name variable. Nullable: True
        :type name: str
        :param id: id variable. Nullable: True
        :type id: str
        """
        out_args = {'site': site, 'name': name, 'id': id}
        return self.call("show_resource_id_pool", **out_args)

    def show_role(self, name=None, id=None):
        """
        MFNA show_role operation method

        :param name: name variable. Nullable: True
        :type name: str
        :param id: id variable. Nullable: True
        :type id: str
        """
        out_args = {'name': name, 'id': id}
        return self.call("show_role", **out_args)

    def show_routing(self, ip=None, id=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA show_routing operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param id: id variable. Nullable: True
        :type id: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'id': id, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("show_routing", **out_args)

    def show_rule_compliance(self, policyid=None, compliance=None, ruleid=None, deviceid=None):
        """
        MFNA show_rule_compliance operation method

        :param policyid: policyid variable. Nullable: True
        :type policyid: str
        :param compliance: compliance variable. Nullable: True
        :type compliance: str
        :param ruleid: ruleid variable. Nullable: True
        :type ruleid: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'policyid': policyid, 'compliance': compliance, 'ruleid': ruleid, 'deviceid': deviceid}
        return self.call("show_rule_compliance", **out_args)

    def show_rule_condition(self, id):
        """
        MFNA show_rule_condition operation method

        :param id: id variable. Nullable: False
        :type id: str
        """
        out_args = {'id': id}
        return self.call("show_rule_condition", **out_args)

    def show_script(self, name=None, id=None, type=None):
        """
        MFNA show_script operation method

        :param name: name variable. Nullable: True
        :type name: str
        :param id: id variable. Nullable: True
        :type id: str
        :param type: type variable. Nullable: True
        :type type: str
        """
        out_args = {'name': name, 'id': id, 'type': type}
        return self.call("show_script", **out_args)

    def show_server_option(self, name, default=None):
        """
        MFNA show_server_option operation method

        :param name: name variable. Nullable: False
        :type name: str
        :param default: default variable. Nullable: True
        :type default: str
        """
        out_args = {'name': name, 'default': default}
        return self.call("show_server_option", **out_args)

    def show_service_type(self, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA show_service_type operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("show_service_type", **out_args)

    def show_session(self, id):
        """
        MFNA show_session operation method

        :param id: id variable. Nullable: False
        :type id: str
        """
        out_args = {'id': id}
        return self.call("show_session", **out_args)

    def show_session_commands(self, id):
        """
        MFNA show_session_commands operation method

        :param id: id variable. Nullable: False
        :type id: str
        """
        out_args = {'id': id}
        return self.call("show_session_commands", **out_args)

    def show_snapshot(self, ip=None, id=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA show_snapshot operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param id: id variable. Nullable: True
        :type id: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'id': id, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("show_snapshot", **out_args)

    def show_system_message(self, id):
        """
        MFNA show_system_message operation method

        :param id: id variable. Nullable: False
        :type id: str
        """
        out_args = {'id': id}
        return self.call("show_system_message", **out_args)

    def show_task(self, id):
        """
        MFNA show_task operation method

        :param id: id variable. Nullable: False
        :type id: str
        """
        out_args = {'id': id}
        return self.call("show_task", **out_args)

    def show_topology(self, id):
        """
        MFNA show_topology operation method

        :param id: id variable. Nullable: False
        :type id: str
        """
        out_args = {'id': id}
        return self.call("show_topology", **out_args)

    def show_user(self, u=None, id=None):
        """
        MFNA show_user operation method

        :param u: u variable. Nullable: True
        :type u: str
        :param id: id variable. Nullable: True
        :type id: str
        """
        out_args = {'u': u, 'id': id}
        return self.call("show_user", **out_args)

    def show_user_group(self, name=None, id=None):
        """
        MFNA show_user_group operation method

        :param name: name variable. Nullable: True
        :type name: str
        :param id: id variable. Nullable: True
        :type id: str
        """
        out_args = {'name': name, 'id': id}
        return self.call("show_user_group", **out_args)

    def show_version(self):
        return self.call("show_version")

    def show_vlan(self, vlanid, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA show_vlan operation method

        :param vlanid: vlanid variable. Nullable: False
        :type vlanid: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'vlanid': vlanid, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("show_vlan", **out_args)

    def show_vtp(self, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA show_vtp operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("show_vtp", **out_args)

    def snmp_get(self, oid, deviceid, readwrite=None, type=None, timeout=None):
        """
        MFNA snmp_get operation method

        :param oid: oid variable. Nullable: False
        :type oid: str
        :param deviceid: deviceid variable. Nullable: False
        :type deviceid: str
        :param readwrite: readwrite variable. Nullable: True
        :type readwrite: str
        :param type: type variable. Nullable: True
        :type type: str
        :param timeout: timeout variable. Nullable: True
        :type timeout: str
        """
        out_args = {'oid': oid, 'deviceid': deviceid, 'readwrite': readwrite, 'type': type, 'timeout': timeout}
        return self.call("snmp_get", **out_args)

    def snmp_set(self, oid, deviceid, value, readwrite=None, type=None, timeout=None):
        """
        MFNA snmp_set operation method

        :param oid: oid variable. Nullable: False
        :type oid: str
        :param deviceid: deviceid variable. Nullable: False
        :type deviceid: str
        :param value: value variable. Nullable: False
        :type value: str
        :param readwrite: readwrite variable. Nullable: True
        :type readwrite: str
        :param type: type variable. Nullable: True
        :type type: str
        :param timeout: timeout variable. Nullable: True
        :type timeout: str
        """
        out_args = {'oid': oid, 'deviceid': deviceid, 'value': value, 'readwrite': readwrite, 'type': type, 'timeout': timeout}
        return self.call("snmp_set", **out_args)

    def stop_task(self, id):
        """
        MFNA stop_task operation method

        :param id: id variable. Nullable: False
        :type id: str
        """
        out_args = {'id': id}
        return self.call("stop_task", **out_args)

    def stop_task_all(self):
        return self.call("stop_task_all")

    def synchronize(self, runmode=None, enablepasswd=None, skipinsync=None, snmpro=None, stoponfailure=None, ip=None, start=None, taskname=None, priority=None, sync=None, maxwaittime=None, useaaa=None, passwd=None, comment=None, rep=None, user=None, snmprw=None, group=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA synchronize operation method

        :param runmode: runmode variable. Nullable: True
        :type runmode: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param skipinsync: skipinsync variable. Nullable: True
        :type skipinsync: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param stoponfailure: stoponfailure variable. Nullable: True
        :type stoponfailure: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param start: start variable. Nullable: True
        :type start: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param sync: sync variable. Nullable: True
        :type sync: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param rep: rep variable. Nullable: True
        :type rep: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        :param group: group variable. Nullable: True
        :type group: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'runmode': runmode, 'enablepasswd': enablepasswd, 'skipinsync': skipinsync, 'snmpro': snmpro, 'stoponfailure': stoponfailure, 'ip': ip, 'start': start, 'taskname': taskname, 'priority': priority, 'sync': sync, 'maxwaittime': maxwaittime, 'useaaa': useaaa, 'passwd': passwd, 'comment': comment, 'rep': rep, 'user': user, 'snmprw': snmprw, 'group': group, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("synchronize", **out_args)

    def synchronize_nnmi_node(self, nnminodehostname, nnminodeipaddress, nnminodeuuid, deviceid, nnmisystemid, partitionid=None):
        """
        MFNA synchronize_nnmi_node operation method

        :param nnminodehostname: nnminodehostname variable. Nullable: False
        :type nnminodehostname: str
        :param nnminodeipaddress: nnminodeipaddress variable. Nullable: False
        :type nnminodeipaddress: str
        :param nnminodeuuid: nnminodeuuid variable. Nullable: False
        :type nnminodeuuid: str
        :param deviceid: deviceid variable. Nullable: False
        :type deviceid: str
        :param nnmisystemid: nnmisystemid variable. Nullable: False
        :type nnmisystemid: str
        :param partitionid: partitionid variable. Nullable: True
        :type partitionid: str
        """
        out_args = {'nnminodehostname': nnminodehostname, 'nnminodeipaddress': nnminodeipaddress, 'nnminodeuuid': nnminodeuuid, 'deviceid': deviceid, 'nnmisystemid': nnmisystemid, 'partitionid': partitionid}
        return self.call("synchronize_nnmi_node", **out_args)

    def test_config(self, script, site=None, family=None, device=None, policy=None, group=None):
        """
        MFNA test_config operation method

        :param script: script variable. Nullable: False
        :type script: str
        :param site: site variable. Nullable: True
        :type site: str
        :param family: family variable. Nullable: True
        :type family: str
        :param device: device variable. Nullable: True
        :type device: str
        :param policy: policy variable. Nullable: True
        :type policy: str
        :param group: group variable. Nullable: True
        :type group: str
        """
        out_args = {'script': script, 'site': site, 'family': family, 'device': device, 'policy': policy, 'group': group}
        return self.call("test_config", **out_args)

    def test_software(self, ip=None, group=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA test_software operation method

        :param ip: ip variable. Nullable: True
        :type ip: str
        :param group: group variable. Nullable: True
        :type group: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'ip': ip, 'group': group, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("test_software", **out_args)

    def traceroute(self, dest, sourcegroup=None, enablepasswd=None, snmpro=None, start=None, source=None, priority=None, maxwaittime=None, useaaa=None, async_=None, passwd=None, rep=None, user=None, snmprw=None):
        """
        MFNA traceroute operation method

        :param dest: dest variable. Nullable: False
        :type dest: str
        :param sourcegroup: sourcegroup variable. Nullable: True
        :type sourcegroup: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param start: start variable. Nullable: True
        :type start: str
        :param source: source variable. Nullable: True
        :type source: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param async_: async variable. Nullable: True
        :type async_: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param rep: rep variable. Nullable: True
        :type rep: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        """
        out_args = {'dest': dest, 'sourcegroup': sourcegroup, 'enablepasswd': enablepasswd, 'snmpro': snmpro, 'start': start, 'source': source, 'priority': priority, 'maxwaittime': maxwaittime, 'useaaa': useaaa, 'async': async_, 'passwd': passwd, 'rep': rep, 'user': user, 'snmprw': snmprw}
        return self.call("traceroute", **out_args)

    def undeploy_image(self, images, customnames=None, reboot=None, sessionlog=None, enablepasswd=None, retrycount=None, snmpro=None, rebootwait=None, posttask=None, customvalue=None, start=None, taskname=None, priority=None, filesystem=None, pretask=None, duration=None, maxwaittime=None, useaaa=None, retryinterval=None, passwd=None, customname=None, comment=None, customvalues=None, user=None, snmprw=None, ip=None, host=None, fqdn=None, deviceid=None):
        """
        MFNA undeploy_image operation method

        :param images: images variable. Nullable: False
        :type images: str
        :param customnames: customnames variable. Nullable: True
        :type customnames: str
        :param reboot: reboot variable. Nullable: True
        :type reboot: str
        :param sessionlog: sessionlog variable. Nullable: True
        :type sessionlog: str
        :param enablepasswd: enablepasswd variable. Nullable: True
        :type enablepasswd: str
        :param retrycount: retrycount variable. Nullable: True
        :type retrycount: str
        :param snmpro: snmpro variable. Nullable: True
        :type snmpro: str
        :param rebootwait: rebootwait variable. Nullable: True
        :type rebootwait: str
        :param posttask: posttask variable. Nullable: True
        :type posttask: str
        :param customvalue: customvalue variable. Nullable: True
        :type customvalue: str
        :param start: start variable. Nullable: True
        :type start: str
        :param taskname: taskname variable. Nullable: True
        :type taskname: str
        :param priority: priority variable. Nullable: True
        :type priority: str
        :param filesystem: filesystem variable. Nullable: True
        :type filesystem: str
        :param pretask: pretask variable. Nullable: True
        :type pretask: str
        :param duration: duration variable. Nullable: True
        :type duration: str
        :param maxwaittime: maxwaittime variable. Nullable: True
        :type maxwaittime: str
        :param useaaa: useaaa variable. Nullable: True
        :type useaaa: str
        :param retryinterval: retryinterval variable. Nullable: True
        :type retryinterval: str
        :param passwd: passwd variable. Nullable: True
        :type passwd: str
        :param customname: customname variable. Nullable: True
        :type customname: str
        :param comment: comment variable. Nullable: True
        :type comment: str
        :param customvalues: customvalues variable. Nullable: True
        :type customvalues: str
        :param user: user variable. Nullable: True
        :type user: str
        :param snmprw: snmprw variable. Nullable: True
        :type snmprw: str
        :param ip: ip variable. Nullable: True
        :type ip: str
        :param host: host variable. Nullable: True
        :type host: str
        :param fqdn: fqdn variable. Nullable: True
        :type fqdn: str
        :param deviceid: deviceid variable. Nullable: True
        :type deviceid: str
        """
        out_args = {'images': images, 'customnames': customnames, 'reboot': reboot, 'sessionlog': sessionlog, 'enablepasswd': enablepasswd, 'retrycount': retrycount, 'snmpro': snmpro, 'rebootwait': rebootwait, 'posttask': posttask, 'customvalue': customvalue, 'start': start, 'taskname': taskname, 'priority': priority, 'filesystem': filesystem, 'pretask': pretask, 'duration': duration, 'maxwaittime': maxwaittime, 'useaaa': useaaa, 'retryinterval': retryinterval, 'passwd': passwd, 'customname': customname, 'comment': comment, 'customvalues': customvalues, 'user': user, 'snmprw': snmprw, 'ip': ip, 'host': host, 'fqdn': fqdn, 'deviceid': deviceid}
        return self.call("undeploy_image", **out_args)

    def update_dynamic_group(self, name):
        """
        MFNA update_dynamic_group operation method

        :param name: name variable. Nullable: False
        :type name: str
        """
        out_args = {'name': name}
        return self.call("update_dynamic_group", **out_args)

    def _login(self, username, password):
        """
        MFNA login operation method

        :param username: username variable. Nullable: False
        :type username: str
        :param password: password variable. Nullable: False
        :type password: str
        """
        out_args = {'username': username, 'password': password}
        return self.call("login", **out_args)

    def signin(self, username, password):
        """
        MFNA signin operation method

        :param username: username variable. Nullable: False
        :type username: str
        :param password: password variable. Nullable: False
        :type password: str
        """
        out_args = {'username': username, 'password': password}
        return self.call("signin", **out_args)

    def _logout(self):
        return self.call("logout")

