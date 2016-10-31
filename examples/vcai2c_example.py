#!/usr/bin/python

import time
import datetime
import sys
from pymlab import config

#### Script Arguments ###############################################

if len(sys.argv) != 3:
    sys.stderr.write("Invalid number of arguments.\n")
    sys.stderr.write("Usage: %s PORT_ADDRESS LOG_FILE.csv\n" % (sys.argv[0], ))
    sys.exit(1)

port    = eval(sys.argv[1])
log_file    = sys.argv[2]

#### Sensor Configuration ###########################################

cfg = config.Config(
    i2c = {
            "port": port,
    },
    bus = [
        {
            "name":          "current_sensor",
            "type":        "vcai2c01",
        },
    ],
)
cfg.initialize()

print "Current loop sensor example \r\n"
print "Time, channel #1,  channel #2,  channel #3 ,  channel #4   \r\n"
sensor = cfg.get_device("current_sensor")
time.sleep(0.5)

#### Data Logging ###################################################

try:        
    with open(log_file, "a") as f:
        while True:

            sensor.setADC(channel = 1, gain = 2);
            time.sleep(0.5)
            channel1 = sensor.readADC();

            sensor.setADC(channel = 2, gain = 2);
            time.sleep(0.5)
            channel2 = sensor.readADC();

            sensor.setADC(channel = 3, gain = 2);
            time.sleep(0.5)
            channel3 = sensor.readADC();

            sensor.setADC(channel = 4, gain = 2);
            time.sleep(0.5)
            channel4 = sensor.readADC();

            sys.stdout.write("%s \t %d \t %d \t %d \t %d \n" % (datetime.datetime.now().isoformat(), channel1, channel2, channel3, channel4))

            f.write("%d\t%d\t%d\t%d\t%d\n" % (time.time(), channel1, channel2, channel3, channel4))
            f.flush()

            sys.stdout.flush()

except KeyboardInterrupt:
    f.close()
    sys.exit(0)


