from .__init__ import *

from .dataPoints.__init__ import *

class RetrieveWeather():
    def __init__(self, city, state):
        self.city = city
        self.state = state

        self.request = api.WeatherApi(search=(f'{city}+{state}'), debug=0)
        
        self.location = self.request.location()
        
        
    class Forecast(RetrieveForecast):
        def __init__(self, request):
            super().__init__(request)

        def get_current(self):
            return self.request.current

        def get_daily(self): #, days=7, type=''
            return self.get_daily_data_fields()  #/ get_daily

        def get_hourly(self):
            return self.request.hourly
        
    # usage: RetrieveWeather('brisbane', 'qld').Forecast.get_daily()