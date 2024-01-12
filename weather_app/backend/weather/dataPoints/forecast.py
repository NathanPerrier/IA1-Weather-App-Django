from ..__init__ import *

class RetrieveForecast():
    def __init__(self, request):
        self.request = request
        print('request11:', self.request)
        
    def get_current_data_fields(self):
        return self.request.forcast_rain() #? rain??  is there a current one?

    def get_daily_data_fields(self):
        return [field for field in self.request.forcast_daily()]

    def get_hourly_data_fields(self):
        return self.request.forecasts_hourly()