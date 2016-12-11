from flask import current_app as ca
from lxml import html
import requests, logging

def get_next(request_json):
    page = requests.get("https://www.metrotransit.org/NexTripBadge.aspx?stopnumber=1890")
    tree = html.fromstring(page.content)
    next_due = tree.xpath('//*[@id="NexTripControl1_NexTripResults1_departures"]/div[1]/span[3]/text()')
    return next_due
    
