from datetime import date, timedelta

import requests
from flask import Blueprint, render_template, request

bp = Blueprint("default", __name__)

WEATHER_KEY = "012f0069daf77316eb66470ef741449b"

@bp.route("/")
def index():
    mock_data = {}
    for item in range(5):
        event_date = date.today() + timedelta(days=item)
        date_str = event_date.strftime("%d %B")
        mock_data[date_str] = []
        for _ in range(3):
            event = requests.get("https://www.boredapi.com/api/activity/")
            mock_data[date_str].append(event.json().get("activity"))
    return render_template("main.html", data=mock_data)


# https://openweathermap.org/

@bp.route("/weather")
def weather():
    value = request.args.get('q')
    weather = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={value}&appid={WEATHER_KEY}&units=metric"
    )
    data = weather.json()
    temperature = int(data['main']['temp'])
    return render_template("weather.html", data=data, temperature=temperature)