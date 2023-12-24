import requests
from requests import get
from decouple import config

from ...views import get_user_ip

def get_city_from_ip():
    ip = get_user_ip()
    location_info = requests.get(f'http://ip-api.com/json/{ip}').json()
    return location_info['city']

def get_current_weather(location=get_city_from_ip(), unit="metric"):
    url = f'https://api.tomorrow.io/v4/weather/realtime?location={location}&units={unit}&apikey={config("TOMORROW_API_KEY")}'
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)

    print(response.text)
    return response.text

def get_daily_weather_forecast(location=get_city_from_ip(), unit="metric"):
    url = f'https://api.tomorrow.io/v4/timelines?location={location}&timesteps=1d&units={unit}&apikey={config("TOMORROW_API_KEY")}'
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    return response.text
    
def get_hourly_weather_forecast(location=get_city_from_ip(), unit="metric"):
    url = f'https://api.tomorrow.io/v4/timelines?location={location}&timesteps=1h&units={unit}&apikey={config("TOMORROW_API_KEY")}'
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)

    print(response.text)
    return response.text