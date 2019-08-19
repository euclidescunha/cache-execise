from flask import render_template, request
from src.main.core.last_recent_used_redis import set_localization, get_localization

from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import logging

logger = logging.getLogger(__name__)

"""Initializing geocoder"""
geocoder = Nominatim(user_agent="my-application")


def healthcheck():
    return "OK"


def index():
    last_recent_used = []

    if request.method == 'POST':
        address = geocoder.geocode(request.form['address'])
        set_localization(request.form['user'],
                         address.latitude,
                         address.longitude)

        last_recent_used = get_localization(2)

    if request.method == 'GET':
        last_recent_used = get_localization(1)

    return render_template('index.html', last_recent_used=last_recent_used)


def get_closest_location():
    closest = None

    if request.method == 'POST':
        localizations = get_localization()
        if len(localizations) > 0:
            address = geocoder.geocode(request.form['address'])
            coordenade = (address.latitude, address.longitude)

            for local in localizations:
                distance = geodesic(coordenade, (local["latitude"], local["longitude"]))
                if closest is None:
                    closest = local, distance
                elif distance < closest[1]:
                    closest = local, distance

    return render_template('closest.html', closest=closest)

