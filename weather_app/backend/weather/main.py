from .__init__ import *

from .dataPoints.__init__ import *

class RetrieveWeather():
    def __init__(self, city, state):
        self.city = city
        self.state = state

        self.request = api.WeatherApi(search=(f'{city}+{state}'), debug=0)
        
        self.location = self.request.location()
        
        
    class Forecast(RetrieveForecast):
        ''' usage: RetrieveWeather('brisbane', 'qld').Forecast.get_daily() '''
        def __init__(self, request):
            super().__init__(request)

        def get_current(self):
            return self.get_current_data_fields()  #  forcast_rain??

        def get_daily(self): #, days=7, type=''
            return self.get_daily_data_fields()  #? get_daily

        def get_hourly(self):
            return self.get_hourly_data_fields()
        
    class UvIndex(RetrieveUvIndex):
        ''' usage: RetrieveWeather('brisbane', 'qld').UvIndex.get_uv_descriptions() '''
        def __init__(self, request):
            super().__init__(request)

        def get_uv_descriptions(self):
            return self.get_uv_descriptions()

        def get_uv_message(self):
            return self.get_uv_message()