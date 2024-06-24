from sqlalchemy import Column, Integer, String, ForeignKey
from . import Base

class Device(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    status = Column(String, nullable=False)
