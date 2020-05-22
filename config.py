import os
base_dir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess" # get value from environ or use fallback value
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or\
        "sqlite:///" + os.path.join(base_dir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Signal app whenever the database is about to change


# Config flow: var = os.environ(key) or fallback value