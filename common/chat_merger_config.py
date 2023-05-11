"""Configuration for ChatMerger project."""
import os

from dotenv import load_dotenv

load_dotenv()

FLASK_SECRET_KEY = os.environ["FLASK_SECRET_KEY"]
DJANGO_SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

DJANGO_DEBUG = (os.environ.get("DJANGO_DEBUG") or "false").lower() in ("true", "1", "yes", "y")
