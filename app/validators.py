import re
from config import config

def validate_username(username):
    if len(username) > config.USERNAME_MAX_LENGTH:
        raise ValueError("Username exceeds maximum length")

def validate_password(password):
    if len(password) < config.PASSWORD_MIN_LENGTH:
        raise ValueError("Password is too short")

def validate_device_name(name):
    if len(name) > config.DEVICE_NAME_MAX_LENGTH:
        raise ValueError("Device name exceeds maximum length")
