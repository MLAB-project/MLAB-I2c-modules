[![Build Status](https://travis-ci.org/MLAB-project/pymlab.svg?branch=master)](https://travis-ci.org/MLAB-project/pymlab)

Python MLAB control modules
================

I2C bus, SPI, RS232, Ethernet and USB modules binding. The code purpose is easy control as many digital electronic MLAB modules as possible. Initial development of this library was focused on I2C devices but it is suitable for use with another interfaces for now.

Installation
------------

### Dependencies
    $ sudo apt-get install git python3-setuptools python3-smbus python3-six python3-pip python3-numpy python3-hidapi python3-smbus2

Dependencies are also available on pip (useful on systems without native packages)
    $ sudo python3 -m pip install smbus2

The latest version of pymlab library use true I²C transfers instead of SMBus transfers. It is needed by some sensors. Namely by SHT31, SHT25 etc.  Therefore an updated version of i2c-tools and python-smbus module is needed for correct working of pymlab library and some examples.
The latest version of python-smbus could be installed from [this fork of i2c-tools](https://github.com/MLAB-project/i2c-tools).

### Install in to Ubuntu venv system

Create venv by `python3 -m ven .venv` then activate it using `source .venv/bin/activate` in the python enviroment you can install the pymlab library: 

    $ git clone https://github.com/MLAB-project/pymlab
    $ cd pymlab/
    $ pip install -e .

#### HIDAPI interface for the USBI2C01A  MLAB module (Optional support)

Required if you want to use the [USBI2C01A](http://wiki.mlab.cz/doku.php?id=en:usbi2c) module to communicate with SMBus/I2C devices via USB HID layer. Very useful in Windows environment where standard hardware interfaces are not accessible directly.

    $ sudo apt-get install libudev-dev libusb-1.0-0-dev libhidapi-dev python3-setuptools python3-smbus cython

Usage
-----

For use of this python library the bus topology (e.g. I²C) and connected devices must be defined. The system is not plug-and-play. Definition is described by the Config object defined at the beginning of the following script. Additional documentation is available at [MLAB Wiki](http://wiki.mlab.cz/doku.php?id=en:pymlab).

### Example

```python3
from pymlab import config

cfg = config.Config(
    i2c = {
        "port": port,
    },

    bus = [
        {
            "type": "i2chub",
            "address": 0x72,

            "children": [
                {"name": "altimet", "type": "altimet01" , "channel": 7, },   
            ],
        },
    ],
)
cfg.initialize()
gauge = cfg.get_device("altimet")
time.sleep(0.5)

gauge.route()
(t1, p1) = gauge.get_tp()

```

Some more examples of usage are in 'examples' directory in that repository. If you have some compatible device and interface on your computer you can run an example directly.
