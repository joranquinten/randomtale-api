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
LIGHT_PIN = 10
BTN_NEXT_PIN = 21
DEBUG = False

# Read command line args
myopts, args = getopt.getopt(sys.argv[1:], "p:d:")
for option, arg in myopts:
    if option == '-p':
        LIGHT_PIN = arg
        print("GPIO Pin set to " + LIGHT_PIN)
    elif option == '-d':
        DEBUG = arg
        print("Debugging mode on")
    else:
        print("Usage: %s -p gpiopinnumber -d debugmode" % sys.argv[0])

GPIO.setmode(GPIO.BCM)   # Set up to use GPIO numbering
GPIO.setup(LIGHT_PIN, GPIO.IN)  # We are reading INput, not OUTput

GPIO.setup(BTN_NEXT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP))  # set up button listener

if DEBUG:
    print(GPIO.RPI_INFO)


def play_start():
    print("Starting playback")
    file_to_play=file_loader.random_file(read_folder)
    print("Loaded: " + file_to_play)
    media_player.player_load(file_to_play, 0.5)
    media_player.player_start()


def play_stop():
    print("Stopping playback")
    media_player.player_stop()


while True:
    if GPIO.input(LIGHT_PIN) == False:
        print("Light input detected")
        play_start()

    if GPIO.input(LIGHT_PIN):
        print("Darkness")
        play_stop()

    if GPIO.input(BTN_NEXT_PIN):
        print("Skip")
        play_start()

    time.sleep(1)
