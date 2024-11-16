from pymlab import config
import time
import sys
import math
import datetime
import os

#### Script Arguments ###############################################

if len(sys.argv) not in (2, 3):
    sys.stderr.write("Invalid number of arguments.\n")
    sys.stderr.write("Usage: %s #I2CPORT [Config number] \n" % (sys.argv[0]))
    sys.exit(1)

port = eval(sys.argv[1])

cfg_number = 0

cfglist=[
    config.Config(
        i2c = {
            #"port": port,
            "device": "hid",
            #"serial": "00A59713"
        },
        bus = [
            {
                "name":        "sdp",
                "type":        "SDP3x",
            },
        ],
    ),
]

try:
    cfg = cfglist[cfg_number]
except IndexError:
    sys.stdout.write("Invalid configuration number.\n")
    sys.exit(1)

sdp3x_sensor = cfg.get_device("sdp")
sdp3x_sensor.initialize()

while True:

    try:
        dp, temp = sdp3x_sensor.readData()
        print(temp, dp)
        time.sleep(0.2)

    # except KeyboardInterrupt:
    #     pass

    except IOError:
        pass
