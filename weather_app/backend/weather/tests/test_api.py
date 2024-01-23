import os, sys
from django.test import TestCase

sys.path.append(os.path.abspath('.'))

import pytest

from ..weatherAU import api

class TestAPI(TestCase):
    def setUp(self):
        self.w1 = api.WeatherApi(search='parkville+vic')
        self.w1a = api.WeatherApi(search='some+unknown+place')

    def test_api(self):
        assert api.WeatherApi() is not None
        
    def test_search_single(self):
        assert self.w1.geohash == 'r1r143n'[:6]

    def test_search_repr(self):
        assert "WeatherApi(geohash='r1r143', search='Parkville VIC', debug=0)" in repr(self.w1)

    def test_search_location(self):
        location = self.w1.location()

        assert location['name']     == 'Parkville'
        assert location['state']    == 'VIC'
        assert location['timezone'] == 'Australia/Melbourne'



    def test_observations(self):
        observations = self.w1.observations()

        assert float(observations['temp']) > -50

    def test_forecast_rain(self):
        forecast_rain = self.w1.forecast_rain()

        assert 'amount' in forecast_rain
        assert 'chance' in forecast_rain

    def test_forecasts_daily(self):
        fd = self.w1.forecasts_daily()

        assert len(fd) >= 7
        assert 'temp_min' in fd[0]
        assert 'temp_max' in fd[0]
        assert 'short_text' in fd[0]


    def test_forecasts_hourly(self):
        f1 = self.w1.forecasts_hourly()

        assert len(f1) >= 72
        assert 'time' in f1[0]
        assert 'temp' in f1[0]
        assert 'icon_descriptor' in f1[0]


    def test_search_single_unknown(self):
        assert self.w1a.geohash is None

    def test_search_repr_unknown(self):
        assert "WeatherApi(geohash=None, search='', debug=0)" in repr(self.w1a)

    def test_search_location_unknown(self):
        assert self.w1a.location() is None

    def test_observations_unknown():
        assert self.w1a.observations() is None

    def test_forecast_rain_unknown():
        assert self.w1a.forecast_rain() is None

    def test_forecasts_daily_unknown():
        assert self.w1a.forecasts_daily() is None

    def test_forecasts_hourly_unknown():
        assert self.w1a.forecasts_hourly() is None


    w2 = api.WeatherApi() 

    def test_search_multiple():
        assert len(w2.search('vic')) > 10

    def test_search_invalid():
        assert w2.search('zzz') == []

    def test_search_invalid():
        assert len(w2.acknowedgment) > 0


    w3 = api.WeatherApi(search='')

    def test_search_nothing1():
        assert w3.geohash is None


    w4 = api.WeatherApi(search='endeavour-hills+vic')

    def test_search_single_endeavour_hills():
        assert w4.geohash == None


    w5 = api.WeatherApi(search='endeavour+hills+vic')

    def test_search_single_endeavour_hills():
        assert w5.geohash == 'r1prcrs'[:6]

    def test_search_repr_endeavour_hills():
        # repr returns the six character geohash
        assert "WeatherApi(geohash='r1prcr', search='Endeavour Hills VIC', debug=0)" in repr(w5)

    def test_search_location_endeavour_hills():
        location = w5.location()

        assert location['name']     == 'Endeavour Hills'
        assert location['state']    == 'VIC'
        assert location['timezone'] == 'Australia/Melbourne'


