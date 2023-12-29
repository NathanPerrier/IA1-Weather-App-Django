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

    def get_current_weather(self, fields, location=None, unit="metric", timesteps='current'): #="temperature,humidity,weatherCode"
        try:
            print('current')
            print(list(fields.keys()))
            location = self.get_city_from_ip() if location is None else location
            print('location:', location)
            if 'sunsetTime' or 'sunriseTime' in fields:
                timesteps='1d'
            url = f'https://api.tomorrow.io/v4/timelines?apikey={config("TOMORROWIO_API_KEY")}'
            headers = {
                'Accept-Encoding': 'gzip',
                'accept': 'application/json',
                'content-type': 'application/json',
            }
            data = {
                "location": location,
                "fields": list(fields.keys()),
                "units": unit,
                "timesteps": [
                    timesteps
                ],
                "timezone": 'auto'
            }

            response = requests.post(url, headers=headers, data=json.dumps(data))
            print('response:', response.text)
            return response.text

        except Exception as e:
            print('error:', e)
            return json.loads(e)
    

    def get_daily_weather_forecast(self, fields, location=None, unit="metric"):
        try:
            print('daily')
            print(list(fields.keys()))
            location = self.get_city_from_ip() if location is None else location
            print('location:', location)
            url = f'https://api.tomorrow.io/v4/timelines?apikey={config("TOMORROWIO_API_KEY")}'
            headers = {
                'Accept-Encoding': 'gzip',
                'accept': 'application/json',
                'content-type': 'application/json',
            }
            data = {
                "location": location,
                "fields": list(fields.keys()),
                "units": unit,
                "timesteps": [
                    "1d"
                ],
                "timezone": "auto"
            }

            response = requests.post(url, headers=headers, data=json.dumps(data))
            print('response (json):', json.loads(response.text))
            return self.format_response_forecast(json.loads(response.text), location, unit)

        except Exception as e:
            print('error:', e)
            return str('error occured:', e)
        
    def get_hourly_weather_forecast(self, fields, location=None, unit="metric"):
        try:
            print(list(fields.keys()))
            url = f'https://api.tomorrow.io/v4/timelines?apikey={config("TOMORROWIO_API_KEY")}'
            headers = {
                'Accept-Encoding': 'gzip',
                'accept': 'application/json',
                'content-type': 'application/json',
            }
            data = {
                "location": location,
                "fields": list(fields.keys()),
                "units": unit,
                "timesteps": [
                    "1h"
                ],
                "timezone": "auto"
            }

            response = requests.post(url, headers=headers, data=json.dumps(data))
            print('response (json):', json.loads(response.text))
            return self.format_response_forecast(json.loads(response.text), location, unit)

        except Exception as e:
            print('error:', e)
            return e
        
    def get_recent_weather_history(self, location=None, unit="metric", timestep='1d'):
        try:
            print('location:', location)
            location = self.get_city_from_ip() if location is None else location
            print('location:', location)
            print('time step:', timestep)
            url = f'https://api.tomorrow.io/v4/weather/history/recent?location={location}&timesteps={timestep}&units={unit}&apikey={config("TOMORROWIO_API_KEY")}'
            headers = {"accept": "application/json"}
            response = requests.get(url, headers=headers)
            print('response (dhistorical):', response.text)
            if 'code' in json.loads(response.text):
                return json.loads(str(response.text['message']))
            return self.format_response_historical(json.loads(response.text), location, unit, timestep)
        except Exception as e:
            print('error:', e)
            return json.loads(e)
    
    def format_response_forecast(self, json_data, location, unit):
        tool_results = [
            {
                "name": "weather_data",
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
    
    def format_response_historical(self, json_data, location, unit, timestep):
        intervals = 'daily' if timestep == '1d' else 'hourly'
        tool_results = [
            {
                "name": "weather_data",
                "results": [
                    {
                        "location": location,  # Replace with the actual location
                        "unit": unit,  # Replace with the desired unit
                        "fields": list(json_data["timelines"][intervals][0]["values"].keys()),
                        "data": [
                            {
                                "timestamp": interval["time"],
                                **interval["values"],
                            }
                            for interval in json_data["timelines"][intervals]
                        ],
                    }
                ],
            }
        ]
        formatted_data = {"tool_results": tool_results}
        json_response = json.dumps(formatted_data, indent=2)
        print(json_response)
        return json_response