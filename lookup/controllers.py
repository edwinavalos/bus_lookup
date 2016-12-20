from .models import db, BusStop
from lxml import html
import requests, logging

def get_next(request_json):
    direction = request_json["result"]["parameters"]["direction"]
    bus_number = request_json["result"]["parameters"]["bus_number"]
    page = requests.get("https://www.metrotransit.org/NexTripBadge.aspx?stopnumber=1890")
    tree = html.fromstring(page.content)
    due_time = tree.xpath('//*[@id="NexTripControl1_NexTripResults1_departures"]/div[1]/span[3]/text()')
    if "Due" in due_time:
        due_time = "now"
    elif "Min" in due_time:
        due_time = "in " + due_time[0].replace("Min","minutes")
    else:
        due_time = "at " + due_time[0]
    return bus_number, direction, due_time

def download_stops(app):
    from urllib.request import urlretrieve
    urlretrieve(app.config["STOPS_URL"], app.config["STOPS_FILE_LOCATION"])

def unzip_stops(app):
    import zipfile
    with zipfile.ZipFile(app.config["STOPS_FILE_LOCATION"], "r") as zip_ref:
        zip_ref.extractall("/tmp")
    return True

def create_stops(app):
    with app.app_context():
        download_stops(app)
        unzip_stops(app)
        with open(app.config['STOPS_FINAL_LOCATION'], 'r') as f:
            stops = f.read().splitlines()[1:]
            for stop in stops:
                s = stop.split(",")
                db.session.add(BusStop(stop_id=int(s[0]), stop_name=s[2], stop_desc=s[3], stop_url=s[7]))
                db.session.commit()
    return True
