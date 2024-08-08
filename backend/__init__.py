from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .models import db  # Import db inside the function
    db.init_app(app)

    from .routes import auth_bp  # Import the blueprint inside the function
    app.register_blueprint(auth_bp)

    return app