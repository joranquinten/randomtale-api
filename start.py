import RPi.GPIO as GPIO
import time
import subprocess

import file_loader
from player import Mediaplayer

# Set the folder which contains the media
read_folder = "./input/"
media_player = Mediaplayer()

# Set the connected pin function
PIN = 10
BTN_OFF_PIN = 16

# Set up to use GPIO numbering
GPIO.setmode(GPIO.BCM)

# set up sensor listener
# We are reading INput, not OUTput
GPIO.setup(PIN, GPIO.IN)

# set up button listener
GPIO.setup(BTN_OFF_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def play_start():
    print("Starting playback")
    file_to_play = file_loader.random_file(read_folder)
    print("Loaded: " + file_to_play)
    media_player.player_load(file_to_play, 1)
    media_player.player_start()


def play_stop():
    print("Stopping playback")
    media_player.player_stop()


def pushButton():
    if not GPIO.input(BTN_OFF_PIN):
        print("Shutting down now")
        subprocess.call(['shutdown', '-h', 'now'], shell=False)
    return


def waitForLight():
    print("Waiting for light to hit the sensor")
    while True:

        pushButton()

        if not GPIO.input(PIN):
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


def bootup():
    file_to_play = "fx/chime.mp3"
    media_player.player_load(file_to_play, 0.5)
    media_player.player_start()
    time.sleep(4)  # Wait for the sound to finish playing
    waitForLight()
    return


bootup()
