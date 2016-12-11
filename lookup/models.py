from sqlalchemy import create_engine, Column, Integer, DateTime, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .extensions import db
import datetime

class Event(db.Model):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime(timezone=False))
    response = Column(String)
    
    def __init__(self, response=None):
        self.date = datetime.datetime.now()
        self.response = response

def create_all(app=None):
    db.create_all(app=app)
