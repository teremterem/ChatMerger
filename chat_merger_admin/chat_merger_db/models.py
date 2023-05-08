"""Models of chat_merger_db."""
from django.db import models

from chat_merger_utils import generate_secret  # pylint: disable=import-error


class Bot(models.Model):
    """A bot that can talk to a user as well as to other bots."""

    class Meta:
        """Meta information about the model."""

        verbose_name = "🤖 Bot"
        verbose_name_plural = "🤖 Bots"

    api_token = models.CharField(max_length=255, unique=True, default=generate_secret)
    name = models.TextField()
    custom_data = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} 🤖"


# class Human(models.Model):
#     class Meta:
#         verbose_name = "👶 Human"
#         verbose_name_plural = "👶 Humans"
#
#     user_uuid = models.UUIDField(unique=True, default=uuid4)
#     name = models.TextField()
#     custom_data = models.JSONField(blank=True, null=True)
#
#     def __str__(self):
#         return f"{self.name} 👶"
#
#
# class Channel(models.Model):
#     class Meta:
#         verbose_name = "📡 Channel"
#         verbose_name_plural = "📡 Channels"
#
#         unique_together = ("channel_type", "channel_specific_id")
#
#     channel_type = models.CharField(max_length=255, unique=True)
#     channel_specific_id = models.CharField(max_length=255, unique=True)
#     recipient_bot = models.ForeignKey(Bot, blank=True, null=True, on_delete=models.CASCADE)
#     recipient_human = models.ForeignKey(Human, blank=True, null=True, on_delete=models.CASCADE)
#     custom_data = models.JSONField(blank=True, null=True)
#
#
# class Conversation(models.Model):
#     pass
#
#
# class Message(models.Model):
#     pass
#
#
# class MessageVersion(models.Model):
#     pass
