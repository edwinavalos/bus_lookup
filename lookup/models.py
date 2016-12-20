from sqlalchemy import create_engine, Column, Integer, DateTime, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .extensions import db
from whoosh.analysis import SimpleAnalyzer
import flask_whooshalchemy
import datetime

class Event(db.Model):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime(timezone=False))
    response = Column(String)
    
    def __init__(self, response=None):
        self.date = datetime.datetime.utcnow()
        self.response = response

class BusStop(db.Model):
    __tablename__ = "bus_stop"
    __searchable__ = ["stop_name"]
    __analyzer__ = SimpleAnalyzer()

    id = Column(Integer, primary_key=True)
    stop_id = Column(Integer)
    stop_name = Column(String)
    stop_desc = Column(String)
    stop_url = Column(String)
    
    def __init__(self, stop_id, stop_name, stop_desc, stop_url):
        self.stop_id = stop_id
        self.stop_name = stop_name
        self.stop_desc = stop_desc
        self.stop_url = stop_url

def create_all(app=None):
    db.create_all(app=app)
