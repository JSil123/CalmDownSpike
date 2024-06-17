from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(30), nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

class Device(Base):
    __tablename__ = 'devices'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    name = Column(String(50), nullable=False)
    type = Column(String, nullable=False)
    status = Column(String, nullable=False)

class Settings(Base):
    __tablename__ = 'settings'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.id'), nullable=False)
    device_id = Column(UUID(as_uuid=True), ForeignKey('devices.id'), nullable=False)
    sound = Column(Boolean, default=False)
    temperature = Column(Integer, nullable=False)
    light = Column(Boolean, default=False)
    vibration = Column(Boolean, default=False)

class Log(Base):
    __tablename__ = 'logs'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    device_id = Column(UUID(as_uuid=True), ForeignKey('devices.id'), nullable=False)
    event = Column(String, nullable=False)
    timestamp = Column(String, nullable=False)
