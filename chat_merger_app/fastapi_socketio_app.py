import sys
from pathlib import Path

import socketio
from fastapi import FastAPI

sys.path.append(str(Path(__file__).resolve().parents[1]))
from common.chat_merger_config import FASTAPI_SECRET_KEY

sio = socketio.AsyncServer(
    # client_manager=socketio.AsyncManager(),  # TODO replace with AsyncRedisManager ?
    async_mode="asgi",
    transports=["websocket"],
)
fapi = FastAPI(secret_key=FASTAPI_SECRET_KEY)
app = socketio.ASGIApp(sio, other_asgi_app=fapi)


# @fapi.get("/")
# async def index():
#     return "Hello world!"


@sio.on("join_room")
async def on_join(sid, data):
    room = data["room"]
    sio.enter_room(sid, room)  # TODO this doesn't seem to support async, is it a problem ?
    await sio.emit("room_message", f"has joined the room.", room=room)


@sio.on("leave_room")
async def on_leave(sid, data):
    room = data["room"]
    sio.leave_room(sid, room)  # TODO this doesn't seem to support async, is it a problem ?
    await sio.emit("room_message", f"has left the room.", room=room)


@sio.on("send_message")
async def on_send_message(sid, data):
    room = data["room"]
    message = data["message"]
    await sio.emit("room_message", message, room=room)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
