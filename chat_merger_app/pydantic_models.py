"""Pydantic models for the ChatMerger app."""
# pylint: disable=no-name-in-module
from pydantic import BaseModel


class StatusResponse(BaseModel):
    """Base class for status responses."""

    status: str


class StatusResponseOK(StatusResponse):
    """Status response for successful requests."""

    status = "ok"


class BotUpdate(BaseModel):
    """Model for bot updates."""

    message: str
