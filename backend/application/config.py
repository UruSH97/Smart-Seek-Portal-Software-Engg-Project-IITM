import os
import secrets
from flask_security import current_user

basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    DEBUG = False
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = False
    WTF_CSRF_ENABLED = False
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authentication-Token'
    CELERY_BROKER_URL = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/2"
    CELERY_TIMEZONE = "Asia/Kolkata"
    REDIS_URL = "redis://localhost:6379"
    BROKER_CONNECTION_RETRY_ON_STARTUP = True
    GMAIL_CREDS_FILE = '/GamilApi/appdev2-391904-167712a96be2.json'
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_HOST = "localhost"
    CACHE_REDIS_PORT = 6379



class LocalDevelopmentConfig(Config):
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_HOST = "localhost"
    CACHE_REDIS_PORT = 6379
    SQLITE_DB_DIR = os.path.join(basedir, "../db_directory")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + \
        os.path.join(SQLITE_DB_DIR, "testdb.sqlite3")
    SQLALCHEMY_POOL_SIZE = 40
    DEBUG = True
    # os.getenv("SECRET_KEY", '_5#y2L"F4Q8z\n\xec]/') # should be strong, unique, difficult, random key
    SECRET_KEY = secrets.token_urlsafe()
    # str(secrets.SystemRandom().getrandbits(128)) should be strong, unique, difficult, random key
    SECURITY_PASSWORD_SALT = os.getenv(
        "SECURITY_PASSWORD_SALT", 'super girl from china')
    SECURITY_TRACKABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_UNAUTHORIZED_VIEW = None
    SECURITY_POST_REGISTER_VIEW = '/redirecting'
    BROKER_CONNECTION_RETRY_ON_STARTUP = True
    # SECURITY_REGISTER_URL='/register'
    SECURITY_POST_LOGIN_VIEW = '/redirecting'
    SECURITY_POST_LOGOUT_VIEW = '/'
    # SECURITY_USERNAME_ENABLE=True
    # SECURITY_USERNAME_REQUIRED=True
    SECURITY_CHANGEABLE = True
    # SECURITY_RECOVERABLE=True
    SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False
    CELERY_BROKER_URL = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/2"
    CELERY_TIMEZONE = "Asia/Kolkata"
    REDIS_URL = "redis://localhost:6379"
    GMAIL_CREDS_FILE = 'GamilApi/appdev2-391904-167712a96be2.json'


class TestingConfig(Config):
    # for testing we don't want actual database, we want in-memory database.
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_HOST = "localhost"
    CACHE_REDIS_PORT = 6379
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_POOL_SIZE = 40
    TESTING = True
    DEBUG = True
    # os.getenv("SECRET_KEY", '_5#y2L"F4Q8z\n\xec]/') # should be strong, unique, difficult, random key
    SECRET_KEY = secrets.token_urlsafe()
    # str(secrets.SystemRandom().getrandbits(128)) should be strong, unique, difficult, random key
    SECURITY_PASSWORD_SALT = os.getenv(
        "SECURITY_PASSWORD_SALT", 'super girl from china')
    SECURITY_TRACKABLE = True
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_UNAUTHORIZED_VIEW = None
    SECURITY_POST_REGISTER_VIEW = '/redirecting'
    BROKER_CONNECTION_RETRY_ON_STARTUP = True
    # SECURITY_REGISTER_URL='/register'
    SECURITY_POST_LOGIN_VIEW = '/redirecting'
    SECURITY_POST_LOGOUT_VIEW = '/'
    # SECURITY_USERNAME_ENABLE=True
    # SECURITY_USERNAME_REQUIRED=True
    SECURITY_CHANGEABLE = True
    # SECURITY_RECOVERABLE=True
    SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False
    CELERY_BROKER_URL = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/2"
    CELERY_TIMEZONE = "Asia/Kolkata"
    REDIS_URL = "redis://localhost:6379"
    GMAIL_CREDS_FILE = 'GamilApi/appdev2-391904-167712a96be2.json'


class StageConfig(Config):
    CACHE_TYPE = "RedisCache"
    CACHE_REDIS_HOST = "localhost"
    CACHE_REDIS_PORT = 6379
    SQLITE_DB_DIR = os.path.join(basedir, "../db_directory")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + \
        os.path.join(SQLITE_DB_DIR, "testdb.sqlite3")
    SQLALCHEMY_POOL_SIZE = 40
    DEBUG = True
    # os.getenv("SECRET_KEY", '_5#y2L"F4Q8z\n\xec]/') # should be strong, unique, difficult, random key
    SECRET_KEY = secrets.token_urlsafe()
    # str(secrets.SystemRandom().getrandbits(128)) should be strong, unique, difficult, random key
    SECURITY_PASSWORD_SALT = os.getenv(
        "SECURITY_PASSWORD_SALT", 'super girl from china')
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    SECURITY_UNAUTHORIZED_VIEW = None
    SECURITY_POST_REGISTER_VIEW = '/redirecting'
    BROKER_CONNECTION_RETRY_ON_STARTUP = True
    # SECURITY_REGISTER_URL='/register'
    SECURITY_POST_LOGIN_VIEW = '/redirecting'
    SECURITY_POST_LOGOUT_VIEW = '/'
    # SECURITY_USERNAME_ENABLE=True
    # SECURITY_RECOVERABLE=False
    # SECURITY_USERNAME_REQUIRED=True
    SECURITY_CHANGEABLE = True
    SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False
    CELERY_BROKER_URL = "redis://localhost:6379/1"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/2"
    REDIS_URL = "redis://localhost:6379"
    CELERY_TIMEZONE = "Asia/Kolkata"
    GMAIL_CREDS_FILE = 'GamilApi/appdev2-391904-167712a96be2.json'
# One can also define class for production config
