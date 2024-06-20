import logging
from logging.handlers import RotatingFileHandler
from sqlalchemy.exc import SQLAlchemyError
from database import engine, Base, get_db
from models import User, Device, Settings, Log
from validators import validate_username, validate_password, validate_device_name
from config import config

# Set up logging
logging.basicConfig(level=config.LOGGING_LEVEL)
handler = RotatingFileHandler('logs/app.log', maxBytes=2000, backupCount=10)
logger = logging.getLogger(__name__)
logger.addHandler(handler)

def create_user(db, username, email, password):
    try:
        validate_username(username)
        validate_password(password)
        new_user = User(username=username, email=email, password=password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        logger.info(f"User created: {username}")
    except (ValueError, SQLAlchemyError) as e:
        db.rollback()
        logger.error(f"Error creating user: {e}")
        raise

def create_device(db, user_id, name, type, status):
    try:
        validate_device_name(name)
        new_device = Device(user_id=user_id, name=name, type=type, status=status)
        db.add(new_device)
        db.commit()
        db.refresh(new_device)
        logger.info(f"Device created: {name}")
    except (ValueError, SQLAlchemyError) as e:
        db.rollback()
        logger.error(f"Error creating device: {e}")
        raise

def log_event(db, device_id, event):
    try:
        new_log = Log(device_id=device_id, event=event, timestamp='now')
        db.add(new_log)
        db.commit()
        db.refresh(new_log)
        logger.info(f"Event logged for device {device_id}: {event}")
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Error logging event: {e}")
        raise

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

    db = next(get_db())
    try:
        username = input("Enter username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")

        create_user(db, username, email, password)
        user = db.query(User).filter_by(username=username).first()

        if user:
            device_name = input("Enter device name: ")
            device_type = input("Enter device type: ")
            device_status = input("Enter device status: ")

            create_device(db, user.id, device_name, device_type, device_status)
            logger.info(f"Device '{device_name}' created successfully.")
        else:
            logger.error(f"User '{username}' not found after creation.")

    except Exception as e:
        logger.exception("An error occurred while setting up the user and device.")

    finally:
        db.close()