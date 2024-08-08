from backend import app, db
from backend.models import User

with app.app_context():
    db.create_all()