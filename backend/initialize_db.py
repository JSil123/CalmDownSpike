# C:\CalmDownSpike\backend\initialize_db.py
from backend import app, db

with app.app_context():
    db.create_all()
    print("Database tables created")