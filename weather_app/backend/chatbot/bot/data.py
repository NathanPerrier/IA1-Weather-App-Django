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
        print('ip address!:', ip_address)
        try:
            print('ip address:', ip_address)
            location_info = get(f'http://ip-api.com/json/{str(ip_address)}').json()
            print('location info:', location_info)
            return location_info['city']
        except Exception as e:
            ip_address = get('https://api.ipify.org?format=json').json()['ip']
            print('ip addressss:', ip_address)
            location_info = get(f'http://ip-api.com/json/{str(ip_address)}').json()
            print('location info:', location_info)
            return location_info['city']

    def get_current_weather(self, location=None, unit="metric", fields="temperature,humidity,weatherCode"):
        try:
            print('fields: \n', fields)
            location = self.get_city_from_ip() if location is None else location
            url = f'https://api.tomorrow.io/v4/weather/realtime?location={location}&fields={fields}&units={unit}&apikey={config("TOMORROWIO_API_KEY")}'
            headers = {"accept": "application/json"}
            response = requests.get(url, headers=headers)
            print(response.text)
            print(json.loads(response.text))
            return response.text
        except Exception as e:
            print('error:', e)
            return json.loads(e)
    

    def get_daily_weather_forecast(self, location=None, unit="metric", fields="temperature,humidity,weatherCode"):
        try:
            print('fields: \n', fields)
            location = self.get_city_from_ip() if location is None else location
            print('location:', location)
            url = f'https://api.tomorrow.io/v4/timelines?location={location}&fields={fields}&timesteps=1d&units={unit}&apikey={config("TOMORROWIO_API_KEY")}'
            headers = {"accept": "application/json"}
            response = requests.get(url, headers=headers)
            print('response (daily):', response.text)
            if 'code' in json.loads(response.text):
                return json.loads(str(response.text['message']))
            return self.format_response_forecast(json.loads(response.text), location, unit)
        except Exception as e:
            print('error:', e)
            return json.loads(str(e))
        
    def get_hourly_weather_forecast(self, location=None, unit="metric", fields="temperature,humidity,weatherCode"):
        try:
            print('fields: \n', fields)
            location = self.get_city_from_ip() if location is None else location
            url = f'https://api.tomorrow.io/v4/timelines?location={location}&fields={fields}&timesteps=1h&units={unit}&apikey={config("TOMORROWIO_API_KEY")}'
            headers = {"accept": "application/json"}
            response = requests.get(url, headers=headers)
            print('response (hourly):', response.text)
            print(response.text)
            return self.format_response_forecast(json.loads(response.text), location, unit)
        except Exception as e:
            print('error:', e)
            return json.loads(e)
    
    def format_response_forecast(self, json_data, location, unit):
        tool_results = [
            {
                "name": "your_function_name",
                "results": [
                    {
                        "location": location,  # Replace with the actual location
                        "unit": unit,  # Replace with the desired unit
                        "fields": list(json_data["data"]["timelines"][0]["intervals"][0]["values"].keys()),
                        "data": [
                            {
                                "timestamp": interval["startTime"],
                                **interval["values"],
                            }
                            for interval in json_data["data"]["timelines"][0]["intervals"]
                        ],
                    }
                ],
            }
        ]
        formatted_data = {"tool_results": tool_results}
        json_response = json.dumps(formatted_data, indent=2)
        print(json_response)
        return json_response