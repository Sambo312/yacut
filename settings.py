import os


MAX_URL_LENGTH = 256
MAX_SHORT_URL_LENGTH = 16
MAX_RANDOM_URL_LENGTH = 6
VALID_SYMBOLS = r'^[a-zA-Z0-9]+$'


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'xxx')
