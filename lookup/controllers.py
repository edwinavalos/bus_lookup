from flask import current_app as ca
from lxml import html
import requests, logging

def get_next(request_json):
    direction = request_json["result"]["parameters"]["direction"]
    bus_number = request_json["result"]["parameters"]["bus_number"]
    page = requests.get("https://www.metrotransit.org/NexTripBadge.aspx?stopnumber=1890")
    tree = html.fromstring(page.content)
    due_time = tree.xpath('//*[@id="NexTripControl1_NexTripResults1_departures"]/div[1]/span[3]/text()')
    if "Due" in due_time:
        due_time = now
    else:
        due_time = due_time[0].replace("Min","minutes")
    return bus_number, direction, due_time
    
