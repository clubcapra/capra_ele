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
  
