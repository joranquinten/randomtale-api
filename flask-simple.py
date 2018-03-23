import json
# import call
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, join_room, emit

import file_loader
from player import Mediaplayer

read_folder = "./input/"

# initialize Flask
app = Flask(__name__)
socketio = SocketIO(app)

media_player = Mediaplayer()

@app.route('/')
def index():
    """Serve the index HTML"""
    return render_template('index.html')


@socketio.on('controls')
def on_controls(data):
    """Instance of controls"""
    print("Controls received:" + data)

    if data == "start":
        emit("notify", "Starting playback")
        print("Starting playback")
        file_to_play = file_loader.random_file(read_folder)
        emit("notify", "Loaded: " + file_to_play)
        media_player.player_load(file_to_play, 0.7)
        media_player.player_start()
        emit_player_status(media_player.status())

    if data == "stop":
        emit("notify", "Stopping playback")
        print("Stopping playback")
        media_player.player_stop()
        emit_player_status(media_player.status())

    if data == "pause":
        emit("notify", "Toggling pause")
        print("Toggling pause")
        media_player.player_pause()
        emit_player_status(media_player.status())

    if data == "shutdown":
        print("sudo halt")
        # call("sudo halt", shell=True)

def emit_player_status(status):

    status_json = json.dumps({
        "player": {
            "is_paused": status.player_is_paused,
            "is_started": status.player_is_started,
            "is_stopped": status.player_is_stopped
            },
        "file_loaded": status.file_loaded
        })

    emit("status", status_json)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
