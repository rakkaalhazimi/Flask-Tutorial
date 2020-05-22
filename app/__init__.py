from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models # circular import

# Initial flow : app = Flask(__name__)
#               from app import routes

# FLASK_APP = yourfilename
# type in cmd: flask run

# Add extentions flow : var = Extention(app)
# Flask database flow : db init => db migrate => db upgrade/downgrade
