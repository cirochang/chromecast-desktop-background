# Chromecast Desktop Background

Auto change background of desktop to images from chromecast. Works on Ubuntu 16.04

## How to run
Install dependencies from PyVirtualDisplay
```
sudo apt-get install xvfb
```

[OPTIONAL] Install and create a virtualenv and activate it.
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

Install the libs
```
python setup.py install
```

Run
```
python main.py
```
