# Assumes default wiring scheme
#
# https://raspberrytips.nl/lichtsensor-aansluiten-raspberry-pi/
# https://pinout.xyz/
# https://sourceforge.net/p/raspberry-gpio-python/wiki/
#
# Sensor      RasPi Pin   RasPi function
# GND         20           GND
# VCC         17           3.3v
# SIGNAL D0   19           GPIO 10

import RPi.GPIO as GPIO
import time
import sys
import getopt

import file_loader
from player import Mediaplayer

# Set the folder which contains the media
read_folder = "./input/"
media_player = Mediaplayer()

# Set the connected pin function
PIN = 10
BTN_NEXT_PIN = 16
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

# set up button listener
GPIO.setup(BTN_NEXT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

if DEBUG:
    print(GPIO.RPI_INFO)


def play_start():
    print("Starting playback")
    file_to_play = file_loader.random_file(read_folder)
    print("Loaded: " + file_to_play)
    media_player.player_load(file_to_play, 1)
    media_player.player_start()
    IS_PLAYING = True

def play_stop():
    print("Stopping playback")
    media_player.player_stop()
    IS_PLAYING = False

def pushButton():
    if GPIO.input(BTN_NEXT_PIN) == False:
        print("Shutting down now")
        call("sudo nohup shutdown -h now", shell=True)
    return

def waitForLight():
    print("Waiting for light to hit the sensor")
    while True:

	pushButton()

        if GPIO.input(PIN) == False:
            print("Light input detected")
            play_start()
            waitForDarkness()
            return
        time.sleep(1)


def waitForDarkness():
    print("Waiting for low light threshold")
    while True:

	pushButton()

        if GPIO.input(PIN):
            print("Darkness")
            play_stop()
            waitForLight()
            return
        time.sleep(1)

waitForLight()
