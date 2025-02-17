Quick Start Guide
=================

This package makes connections to MFNA appliances for provisioning and obtaining data.

Installing directly using pip::

    pip3 install pymnfa


All MFNA API calls can be regenerated on demand from an initial WSDL file as show below.
This will generate a full client class. This class can then be installed and used in the following way.
Note that an example WSDL file has been included, however this should be replaced by the WSDL file supplied by your MFNA
appliance.

Class Generation Example::

    git clone https://github.com/andy-shady-org/pymfna.git
    cd pymfna/pymfna
    python mfna.py -v -o mfnaclient.py ../wsdl/api.wsdl.soappy
    cd ..
    python setup.py install

In the above step, the class MFNAClient was created within the 'mfnaclient.py' file as specified by the '-o' flag for output.
The class, after the package containing the new class file has been installed, can be easily imported and used.

Simple Usage Example::

    from pymfna import MFNAClient
    mfna = MFNAClient('<MFNA Host>', '<username>', '<password>')
    mfna.login()
    result = mfna.list_device(host='<your host in MFNA>')
