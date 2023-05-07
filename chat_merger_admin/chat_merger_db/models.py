"""Models of chat_merger_db."""
from django.db import models

from chat_merger_utils import generate_secret


class Bot(models.Model):
    """A bot that can talk to a user as well as to other bots."""

    class Meta:
        """Meta information about the model."""

        verbose_name = "🤖 Bot"
        verbose_name_plural = "🤖 Bots"

    # TODO use uuid instead of sequential id ?
    name = models.CharField(max_length=255, db_index=True)
    api_token = models.CharField(max_length=255, unique=True, default=generate_secret)

    # TODO add created and edited timestamps

    def __str__(self):
        return f"{self.name} 🤖"
