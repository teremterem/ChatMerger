"""Utility functions for ChatMerger."""
import random
import string


def generate_secret(length: int = 63) -> str:
    """Generate a random string of the given length."""
    return "".join([random.choice(string.ascii_letters + string.digits) for _ in range(length)])
