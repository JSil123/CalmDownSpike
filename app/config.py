import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost/calmdownspike')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'INFO')

    # Input validation constraints
    DEVICE_NAME_MAX_LENGTH = 50
    USERNAME_MAX_LENGTH = 30
    PASSWORD_MIN_LENGTH = 8

config = Config()