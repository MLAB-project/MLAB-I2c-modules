#!/usr/bin/python

# Python library for SHT3101A MLAB module with SHT31 Temperature and relative humidity sensor.

#uncomment for debbug purposes
#import logging
#logging.basicConfig(level=logging.DEBUG)

import time
import datetime
import sys
from pymlab import config

#### Script Arguments ###############################################

if len(sys.argv) not in (2, 3):
    sys.stderr.write("Invalid number of arguments.\n")
    sys.stderr.write("Usage: %s PORT ADDRESS\n" % (sys.argv[0], ))
    sys.exit(1)

port    = eval(sys.argv[1])

if len(sys.argv) == 3:
    address = eval(sys.argv[2])
else:
    address = 0x45

#### Sensor Configuration ###########################################

''''
cfg = config.Config(
    i2c = {
        "port": port,
    },

	bus = [
		{
            "type": "i2chub",
            "address": 0x72,

            "children": [
                {"name": "sht", "type": "sht31", "channel": 1, }
            ],
		},
	],
)

'''
cfg = config.Config(
    i2c = {
        "port": port,
#        "device": 'hid',
    },
    bus = [
        {
            "name":          "sht",
            "type":        "sht31",
            "address":        address,
        },
    ],
)


cfg.initialize()

print ("SHT31 sensor readout example \r\n")
sensor = cfg.get_device("sht")

sensor.reset()
time.sleep(0.1)

#### Data Logging ###################################################

try:
    while True:
        temperature, humidity = sensor.get_TempHum()
        sys.stdout.write("Sensor status: %s, Temperature: %0.2f, Humidity: %0.2f\r\n" % (sensor.get_status(), temperature, humidity))
        sys.stdout.flush()
        time.sleep(1)
except KeyboardInterrupt:
    sys.exit(0)
