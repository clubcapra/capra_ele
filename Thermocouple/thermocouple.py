from bbio import *
from bbio.libraries.MAX31855 import MAX31855

SPI1.open()


cs_pin = 0


thermocouple = MAX31855(SPI1, cs_pin)

def setup():

  pass

def loop():
  
