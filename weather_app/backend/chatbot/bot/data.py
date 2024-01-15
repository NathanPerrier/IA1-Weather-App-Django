import requests
from requests import get
from decouple import config
from django.db import models
from django.core.cache import cache
import json

from ...location.main import GetLocation

class BotData(models.Model):
    def __init__(self):
        self.ip_address = None
            
        self.route = None
        self.routeStart = None
        self.routeEnd = None
        self.routeMode = None
        
    def get_city_from_ip(self, ip_address=None):
        return GetLocation().get_location().city
        # print(cache.get('latitude'), cache.get('longitude'))
        # if cache.get('latitude') is not None and cache.get('longitude') is not None:
        #     try:
        #         url = f'http://api.openweathermap.org/geo/1.0/reverse?lat={cache.get("longitude")}&lon={cache.get("latitude")}&limit=1&appid={config("OPENWEATHERMAP_API_KEY")}'
        #         data = requests.get(url).json()
        #         return data[0]['name']
        #     except Exception as e:
        #         print('Error:', e)
        #         pass       
        # return GetLocation().get_location()['city']

    def get_current_weather(self, fields, location=None, unit="metric", timesteps='current'): #="temperature,humidity,weatherCode"
        try:
            print('current')
            print(list(fields.keys()))
            location = self.get_city_from_ip() if location is None else location
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
            print('location:', location, '\nresponse:', response.text)
            return response.text

        except Exception as e:
            print('error:', e)
            return str(('error occured:', e))
    

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
            return self.format_response_forecast(json.loads(response.text), location, unit)

        except Exception as e:
            print('error:', e)
            return str(('error occured:', e))
        
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
            return str(('error occured:', e))
        
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
            return str(('error occured:', e))
    
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