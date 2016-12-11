from flask import Blueprint, request, jsonify
from flask import current_app as ca
from models import Event, db
import logging
import ast

views_bp = Blueprint("views_bp", __name__)

@views_bp.route("/receive", methods=["POST"])
def receive():
    resp = {}
    resp["speech"] = "This is a test"
    resp["displayText"] = "This is a text test"
    resp["data"] = {"content":"test"}
    resp["contextOut"] = [{"parameters":{"arrival_time":"2 minutes"}}]
    resp["source"] = "Straight from the mouths of babes"
    event = Event(str(resp))
    db.session.add(event)
    db.session.commit()
    ca.logger.info("Saved event")    
    return jsonify(**resp)

@views_bp.route("/get_last_response", methods=["GET"])
def get_last_response():
    return jsonify(**ast.literal_eval(db.session.query(Event).order_by(Event.id.desc()).first().response))
    
@views_bp.route("/", methods=["GET"])
def default():
    return "Default return"
