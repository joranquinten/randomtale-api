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
import sys
import getopt

# Set the connected pin function
PIN = 4
DEBUG = False

# Read command line args
myopts, args = getopt.getopt(sys.argv[1:], "p:d:")
for option, arg in myopts:
    if option == '-p':
        PIN = arg
        print("GPIO Pin set to " + PIN)
    elif option == '-d':
        DEBUG = arg
        print("Debugging mode on")
    else:
        print("Usage: %s -p gpiopinnumber -d debugmode" % sys.argv[0])

GPIO.setmode(GPIO.BCM)   # Set up to use GPIO numbering
GPIO.setup(PIN, GPIO.IN)  # We are reading INput, not OUTput


if DEBUG:
    print(GPIO.RPI_INFO)


def waitForLight():
    while True:
        if GPIO.input(PIN) == False:
            print("Light input detected")
            waitForDarkness()
            return
        time.sleep(1)


def waitForDarkness():
    while True:
        if GPIO.input(PIN):
            print("Darkness")
            waitForLight()
            return
        time.sleep(1)


waitForLight()
