
#Software portion of weather

import requests
import os
from dotenv import load_dotenv
import json
load_dotenv()

def getdata(city="Austin"):
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=imperial"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

