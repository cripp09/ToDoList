from os import environ

DB_USER = environ.get("DB_USER", "user")
DB_PASSWORD = environ.get("DB_PASS", "password")
DB_HOST = environ.get("DB_HOST", "localhost")
DB_NAME = environ.get("DB_NAME", "todolist")
DB_PORT = environ.get("DB_PORT", "port")
SECRET_AUTH = environ.get("SECRET_AUTH")