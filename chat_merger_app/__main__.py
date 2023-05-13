"""Main module for running the FastAPI app."""
# pylint: disable=wrong-import-position,import-error
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from chat_merger_app.fastapi_socketio_app import app

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
