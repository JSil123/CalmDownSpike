import pytest
from app import create_app, db
from models import User

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()

    # Configure the app for testing
    flask_app.config['TESTING'] = True
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    # Create a test client
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            db.create_all()
            yield testing_client
            db.session.remove()
            db.drop_all()

@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table(s)
    db.create_all()

    # Insert user data
    user1 = User(username='inituser', email='init@example.com', password_hash='testpassword')
    db.session.add(user1)

    # Commit the changes for the users
    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()
