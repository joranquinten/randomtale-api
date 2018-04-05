# Assumes default wiring scheme
#
# https://raspberrytips.nl/lichtsensor-aansluiten-raspberry-pi/
# https://pinout.xyz/
# https://sourceforge.net/p/raspberry-gpio-python/wiki/
#
# Sensor      RasPi Pin   RasPi function
# GND         6           GND
# VCC         1           3.3v
# SIGNAL D0   7           GPIO 4

import RPi.GPIO as GPIO
import time

# Set the connected pin function
PIN = 4
DEBUG = False

GPIO.setmode(GPIO.BCM)   # Set up to use GPIO numbering
GPIO.setup(PIN, GPIO.IN) # We are reading INput, not OUTput

if DEBUG:
  print(GPIO.RPI_INFO)

while True:
  if GPIO.input(PIN):
    print("Sensitivity threshold met")

  time.sleep(1)