import requests
from requests import get
from decouple import config
from django.db import models
from django.core.cache import cache
import requests
import urllib.request, json
import json
from ...weather.main import RetrieveWeather
import pygeohash_fast as pgh 
from geopy.geocoders import Nominatim
from geopy.point import Point


from ..models import Route

from ...location.main import GetLocation
from .get_zip import PostcodeDatabase

class BotData(models.Model):
    def __init__(self):
        self.ip_address = None
            
        self.route = None
        self.routeStart = None
        self.routeEnd = None
        self.routeMode = None
        
    def get_city_from_ip(self, ip_address=None):
        return GetLocation().get_location().city
        
    def does_route_exist(self):
        ip = GetLocation().get_ip_address()
        if Route.objects.filter(ip=Route.hash_ip(ip)).exists():
            route = Route.objects.filter(ip=Route.hash_ip(ip)).last()
            self.route = route.route
            self.routeStart = route.start
            self.routeEnd = route.end
            self.routeMode = route.mode
            return True
        return False
    
    def get_route(self):
        print(self.routeStart, self.routeEnd, self.routeMode)
        url = f'https://api.mapbox.com/directions/v5/mapbox/{ self.routeMode }/{ str(self.routeStart[0]) }%2C{ str(self.routeStart[1]) }%3B{ str(self.routeEnd[0]) }%2C{ str(self.routeEnd[1]) }?alternatives=false&geometries=geojson&language=en&overview=simplified&steps=false&notifications=none&access_token={config("MAPBOX_ACCESS_TOKEN")}'
        print(url)
        with urllib.request.urlopen(url) as url:
            data = json.load(url)
        print(data)
        return list(data['routes'][0]['geometry']['coordinates'])
    
    def get_weather_on_route(self, startLocation=None, endLocation=None, mode='driving', startTime='now', timezones='auto', unit='metric'):
        if startLocation is None:
            startLocation = (lambda location: [location.lat, location.lon])(GetLocation().get_location())
        if not self.does_route_exist():
            self.routeStart = startLocation
            self.routeEnd = endLocation
            self.routeMode = mode
            self.route = self.get_route()[0]
            
        coord_list = []
        
        for coordinate in self.route.strip('[]],').split('],'):
            coordinates = coordinate.strip(' [')
            coord_list.append(list(coordinates.split(', ')))
            
        print('coord_list:', coord_list)
        
        for coordinates in coord_list: #! issue
            print('geohash ', PostcodeDatabase(coordinates[1], coordinates[0]).get_postcode()) # i think issue is with this line +- <--
            model = RetrieveWeather(PostcodeDatabase(coordinates[1], coordinates[0]).get_postcode())
            print(model.request)
            print(model.request.location())
            print(model.Warnings(model.request).get_warnings())
        
        
    
    def lat_lon_to_geohash(self, coordinates): #limit reaches too quickly
        print('latitude:', coordinates[0], 'coordinates[1]:', coordinates[1])
        try:
            return pgh.encode(float(coordinates[0]), float(coordinates[1]), len=8)
        except Exception as e:
            print('error:', e)
            response = requests.get(f"https://us1.locationiq.com/v1/reverse?key={config('LOCATIONIQ_API_KEY')}&lat={coordinates[1]}&lon={coordinates[0]}&format=json&statecode=1&accept-language=en")
            data = response.json() #['geohash']
            print('data:', data)
            try:
                return data['address']['postcode']
            except:
                return data['address']['city_district'] if 'city_district' in data['address'] else data['address']['city'] if 'city' in data['address'] else None

    def lat_lon_to_postcode(self, coordinates):
        print('latitude:', coordinates[0], 'longitude:', coordinates[1])
        try:
            geolocator = Nominatim(user_agent="geoapiExercises")
            location = geolocator.reverse(Point(float(coordinates[1]), float(coordinates[0])), exactly_one=True)
            return location.raw['address']['postcode']
        except Exception as e:
            print('error:', e)
            return None

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