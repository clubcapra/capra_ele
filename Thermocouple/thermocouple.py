#This script read the temperature from the max31855
#
#The SPI0 pin are:
#CS0: p9_p17
#MISO: P9_21
#MOSI: P9_18
#SCLK: P9_22
#
#The SPI1 pin are:
#CS0: P9_28
#CS1: P9_42
#MISO: P9_29
#MOSI: P9_30
#SCLK: P9_31

from bbio import *
from bbio.libraries.MAX31855 import MAX31855
SPI1.open()

cs_pin = 0

thermocouple = MAX31855(SPI1, cs_pin)


#There is nothing to do here
def setup():

    pass


def loop():
    temp = thermocouple.readTempC()

    if(temp == None):

        if thermocouple.error == thermocouple.OPEN_CIRCUIT:
            print "Thermocouple not connected"

        if thermocouple.error == thermocouple.SHORT_TO_GND:
            print "Thermocouple shorted to gnd"

        if thermocouple.error == thermocouple.SHORT_TO_VCC:
            print "Thermocouple shorted to vcc"

    else:
        print "Temp: {:0.2f} C".format(temp)
    delay(1000)

run(setup, loop)
