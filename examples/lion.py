#!/usr/bin/python

# Python example of use pymlab with LIONCELL01 MLAB module

import time
import sys
from pymlab import config

while True:
    #### Sensor Configuration ###########################################
    cfg = config.Config(
        i2c = {
            "port": 0, # I2C bus number
        },

	    bus = [
		    {
                "type": "i2chub",
                "address": 0x73,
                
                "children": [
                    {"name": "guage", "type": "lioncell", "channel": 7, },
                ],
		    },
	    ],
    )


    cfg.initialize()
    guage = cfg.get_device("guage")

    flash = guage.ReadFlashBlock(64, 0)
    print " ".join([hex(i) for i in flash])

    print hex(guage.PackConfiguration())

    #guage.WriteFlashByte(64, 0, 0, 0x9)    # External Voltage Measurement
    #guage.WriteFlashByte(64, 0, 7, 0x2)    # Two Cells
    #guage.WriteFlashByte(64, 0, 4, 0x74)    # 8 LED (1+7), Shift Register
    #guage.WriteFlashByte(104, 0, 14, 0x28)   # Voltage Measurement Range 10240 mV
    #guage.WriteFlashByte(104, 0, 15, 0x00)   # 

    flash = guage.ReadFlashBlock(64, 0)
    print " ".join([hex(i) for i in flash])

    try:
        while True:
            # Battery status readout
            print "Temp =", guage.getTemp(), "degC, RemainCapacity =", guage.getRemainingCapacity(), "mAh, cap =", guage.FullChargeCapacity(), "mAh, U =", guage.Voltage(), "mV, I =", guage.AverageCurrent(), "mA, charge =", guage.StateOfCharge(), "%"
            time.sleep(3)


    except IOError:
        err = err + 1
        print "IOError"
        continue

    except KeyboardInterrupt:
    	sys.exit(0)
