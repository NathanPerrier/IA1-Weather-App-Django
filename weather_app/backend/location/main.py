import requests
from requests import get
from decouple import config
from django.core.cache import cache
from requests.exceptions import ReadTimeout
import json

class GetLocation:
    def __init__(self):
        pass

    def get_location(self):
        ip_address = self.get_ip_address()
        print('ip address:', ip_address)
        try:
            location_info = get(f'http://ip-api.com/json/{str(ip_address)}', timeout=5).json()
            return location_info
        except ReadTimeout:
            return None
        
    def get_ip_address(self):
        try:
            return get('https://api.ipify.org?format=json', timeout=5).json()['ip']
        except ReadTimeout:
            return None