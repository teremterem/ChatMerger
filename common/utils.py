"""Utility functions for ChatMerger."""
import secrets


def generate_secret(length: int = 63) -> str:
    """Generate a random string of the given length."""
    return secrets.token_urlsafe(length)
