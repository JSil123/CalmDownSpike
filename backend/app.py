from flask import Flask, send_from_directory
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask app
app = Flask(__name__)

# Set up the SQLAlchemy database instance (adjust your database URI accordingly)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
db = SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Your routes and logic
@app.route('/backend/static/js/scripts.js')
def serve_js():
    return send_from_directory(app.static_folder, 'js/scripts.js')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
