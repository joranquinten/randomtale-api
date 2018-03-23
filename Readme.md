# RandomTale API Server & Webclient

This builds a Flask API to play a random media file in a designated folder and can be controlled via a webclient. This is designed to run on a Raspberry Pi with audio support, but can be run on any device with Python 2.7.

* Make sure you have Python 2.7 installed (not tested on Python 3.
* The webclient is vanilla JS and should work in any major recent browser. (An internet connection is required for styling purposes)

## Getting Started

* Clone the repo to your local machine
* Install the dependencies for the Python scripts
* Make sure there's an /input/ folder with \*.mp3s on the root level
  * The script just tries to play a random file from the folder, so only place media files over here!

```
pip install -r requirements.txt
```

Then run the script:

```
python flask-simply.py
```

The application starts in debug mode. You should be able to open the webclient on the localhost address with the predefined port number: http://127.0.0.1:5000. The webclient offers controls to play random files from the input folder.

_Bear in mind that I've *disabled* the shutdown command on the repo!_

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
