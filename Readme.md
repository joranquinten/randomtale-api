# RandomTale Light Sensitive Playback

This repo is designed to run on a Raspberry Pi with audio playback (used with pimoronis Speaker pHAT) and a light~~saber~~sensor wired up on top of the shield (see schematics).

Tried and tested with (not included in this repo):
* [Raspberry Pi zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/)
* [Pimoroni Speaker pHAT](https://shop.pimoroni.com/products/speaker-phat) (_Assumes you installed the shield and the provided libraries._)
* Lightsensitive sensor
* Bunch of mp3's in the /input/ folder

## Wiring schema

The script assumes the schema as shown below. For identifying pins on the Raspberry Pi, take a look at [pinout.xyz](https://pinout.xyz). This config doesn't interfere with the pins reserved for the speaker shield.

| Sensor    	| RaspPi Pin 	| RaspPi function 	|
|-----------	|------------	|-----------------	|
| GND       	| 20         	| GND             	|
| VCC       	| 17         	| 3.3v            	|
| SIGNAL D0 	| 19         	| GPIO 10         	|

## Getting Started

* Clone the repo to your pi
* Install the dependencies for the Python scripts
* Make sure there's an /input/ folder with \*.mp3s on the root level
  * The script just tries to play a random file from the folder, so only place media files over here!

```
pip install -r requirements.txt
```

Then run the script:

```
python start.py
```

Want it to start up the script _automagically_? Take a look at [these instructions](http://www.instructables.com/id/Raspberry-Pi-Launch-Python-script-on-startup/) 


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
