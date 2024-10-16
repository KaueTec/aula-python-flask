from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from app import routes

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(routes.bp)
    return app