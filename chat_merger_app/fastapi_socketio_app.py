"""FastAPI + Socket.IO app for ChatMerger."""
# pylint: disable=import-error
import asyncio

import socketio
from fastapi import FastAPI, Header, HTTPException, status

from chat_merger_app.pydantic_models import BotUpdate, StatusResponse, StatusResponseOK
from common.chat_merger_config import FASTAPI_SECRET_KEY

sio = socketio.AsyncServer(
    # TODO client_manager=socketio.AsyncRedisManager(),
    async_mode="asgi",
    transports=["websocket"],
)
fapi = FastAPI(secret_key=FASTAPI_SECRET_KEY)
app = socketio.ASGIApp(sio, other_asgi_app=fapi)


@fapi.post("/bot_update")
async def bot_update(update: BotUpdate, x_chat_merger_bot_token: str = Header(None)) -> StatusResponse:
    """Receive bot updates from the bot and emit them to the clients."""
    if not x_chat_merger_bot_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="X-Chat-Merger-Bot-Token header is missing."
        )
    # TODO elif wrong token, then raise http 403 forbidden

    asyncio.create_task(sio.emit("bot_update", update.dict(), room=x_chat_merger_bot_token))
    return StatusResponseOK()


@sio.event
async def connect(sid: str, env) -> bool:
    """Called when a client connects to the server."""
    bot_token = env.get("HTTP_X_CHAT_MERGER_BOT_TOKEN")  # TODO put this in a constant
    if not bot_token:
        return False  # TODO raise exception instead ?
    sio.enter_room(sid, bot_token)
    return True


# @sio.event
# async def disconnect(sid: str) -> None:
#     # TODO sio.leave_room(sid, room) ?
#     pass


@fapi.get("/")
async def index():
    """A health check endpoint."""
    return "Hello world!"
