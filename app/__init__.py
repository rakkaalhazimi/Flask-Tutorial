from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = "login" # The name of the view to redirect to when the user needs to log in.

from app import routes, models # circular import

# Initial flow : app = Flask(__name__)
#               from app import routes

# FLASK_APP = yourfilename
# type in cmd: flask run

# Add extentions flow : var = Extention(app)
# Flask database flow : db init => db migrate => db upgrade/downgrade
