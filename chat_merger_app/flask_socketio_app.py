import sys
from pathlib import Path

from flask import Flask
from flask_socketio import SocketIO, join_room, leave_room, emit

sys.path.append(str(Path(__file__).resolve().parents[1]))
from common.chat_merger_config import FLASK_SECRET_KEY

app = Flask(__name__)
app.config["SECRET_KEY"] = FLASK_SECRET_KEY
socketio = SocketIO(app)


@app.route("/")
def index():
    return "Hello world!"


@socketio.on("join_room")
def on_join(data):
    room = data["room"]
    join_room(room)
    emit("room_message", f"has joined the room.", room=room)


@socketio.on("leave_room")
def on_leave(data):
    room = data["room"]
    leave_room(room)
    emit("room_message", f"has left the room.", room=room)


@socketio.on("send_message")
def on_send_message(data):
    room = data["room"]
    message = data["message"]
    emit("room_message", message, room=room)


if __name__ == "__main__":
    socketio.run(app)  # TODO can this be used in production ?
