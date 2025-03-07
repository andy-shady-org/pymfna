PyMFNA
======

|docs|

PyMFNA is a Python client wrapper for connecting to and performing actions against MFNA appliances.

Install
-------

Python3 Install from pip3::
```bash
pip3 install pymnfa
```

Or you can run build this locally::

```bash
git clone https://github.com/andy-shady-org/pymfna.git
cd pymnfa
pip install .
```

How to Use
----------

###### Example Usage

This package makes connections to MFNA appliances for provisioning and obtaining data. 
All MFNA API calls can be regenerated on demand from an initial WSDL file as show below.
This will generate a full client class. This class can then be installed and used in the following way.
Note that an example WSDL file has been included, however this should be replaced by the WSDL file supplied by your MFNA 
appliance.

```bash
git clone https://github.com/andy-shady-org/pymfna.git
cd pymnfa/pymnfa
python mnfa.py -v -o mnfaclient.py ../wsdl/api.wsdl.soappy
cd ..
pip install .
```

In the above step, the class MFNAClient was created within the 'mnfaclient.py' file as specified by the '-o' flag for output.
The class, after the package containing the new class file has been installed, can be easily imported and used.

```python
from pymfna import MFNAClient

mfna = MFNAClient('<MFNA Host>', '<username>', '<password>')
mfna.login()
result = mfna.list_device(host='<your host in MFNA>')            
```


Building Sphinx Documentation
-----------------------------
Sphinx can be used to generate technical documentation for this project.


How to build Sphinx documentation::

```bash
git clone https://github.com/andy-shady-org/pymfna.git
pip install sphinx_rtd_theme
cd pymnfa/docs
make html
```

Documentation will be built into the docs/build/html folder


.. |docs| image:: https://readthedocs.org/projects/pymfna/badge/?version=latest
    :alt: Documentation Status
    :scale: 100%
    :target: https://readthedocs.org/projects/pymfna/badge/?version=latest