from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, emit

import file_loader
import player

read_folder = "./input/"

# initialize Flask
app = Flask(__name__)
socketio = SocketIO(app)


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
        player.player_load(file_to_play, 0.7)
        player.player_start()

    if data == "stop":
        emit("notify", "Stopping playback")
        print("Stopping playback")
        player.player_stop()


if __name__ == '__main__':
    socketio.run(app, debug=True)
