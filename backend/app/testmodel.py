from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

# Create an engine and a session
engine = create_engine('postgresql+psycopg2://username:password@localhost/calmdownspike')
Session = sessionmaker(bind=engine)
session = Session()