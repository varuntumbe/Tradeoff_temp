from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# app instance
app = Flask(__name__)
app.config.from_object(Config)

# database instance
db = SQLAlchemy(app)

# migration instance
migrate = Migrate(app=app, db=db)

# importing all the py modules
from app import routes, models
