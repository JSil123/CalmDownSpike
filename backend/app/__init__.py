from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Load the configuration
    app.config.from_object('app.config.Config')

    # Ensure instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)

    with app.app_context():
        from .routes import main as main_blueprint
        app.register_blueprint(main_blueprint)
        db.create_all()

    return app