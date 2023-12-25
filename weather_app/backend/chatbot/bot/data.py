import requests
from requests import get
from decouple import config
from django.db import models
from ipware import get_client_ip
from django.core.cache import cache
import json
class BotData(models.Model):
    def __init__(self):
        self.ip_address = None
             
    def get_user_ip(self, request):
        self.ip_address = get_client_ip(request)[0]
        cache.set('ip_address', self.ip_address)
        print(self.ip_address)
        
    def get_city_from_ip(self, ip_address=None):
        ip_address = self.ip_address if self.ip_address is not None else cache.get('ip_address')
        print('ip address:', ip_address)
        if ip_address is None:
            try:
                print('ip address:', ip_address)
                location_info = get(f'http://ip-api.com/json/{str(ip_address)}').json()
                print('location info:', location_info)
                return location_info['city']
            except Exception as e:
                print(e)
                return 'brisbane' #! fix
        else:
            ip_address = get(f'https://api.ipify.org/')
            print('ip address:', ip_address)

    # def get_current_weather(self, location=None, unit="metric"):
    #     location = self.get_city_from_ip() if location is None else location
    #     url = f'https://api.tomorrow.io/v4/weather/realtime?location={location}&units={unit}&apikey={config("TOMORROWIO_API_KEY")}'
    #     headers = {"accept": "application/json"}
    #     response = requests.get(url, headers=headers)
    #     print('response:', response)
    #     print(response.text)
    #     return response.text
    
    def get_current_weather(self, location, unit="imperial"):
        """Get the current weather in a given location"""
        if "tokyo" in location.lower():
            return json.dumps({"location": "Tokyo", "temperature": "10", "unit": unit})
        elif "san francisco" in location.lower():
            return json.dumps({"location": "San Francisco", "temperature": "72", "unit": unit})
        elif "paris" in location.lower():
            return json.dumps({"location": "Paris", "temperature": "22", "unit": unit})
        else:
            return json.dumps({"location": location, "temperature": "unknown"})


    def get_daily_weather_forecast(self, location=None, unit="metric"):
        location = self.get_city_from_ip() if location is None else location
        print('location:', location)
        url = f'https://api.tomorrow.io/v4/timelines?location={location}&timesteps=1d&units={unit}&apikey={config("TOMORROWIO_API_KEY")}'
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        print('response:', response.text)
        return response.text
        
    def get_hourly_weather_forecast(self, location=None, unit="metric"):
        location = self.get_city_from_ip() if location is None else location
        url = f'https://api.tomorrow.io/v4/timelines?location={location}&timesteps=1h&units={unit}&apikey={config("TOMORROWIO_API_KEY")}'
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)
        print('response:', response)
        print(response.text)
        return response.text