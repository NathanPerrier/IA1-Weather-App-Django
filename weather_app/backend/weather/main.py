from .__init__ import *

from .dataPoints.__init__ import *

class RetrieveWeather():
    def __init__(self, zipCode):
        self.zip = zipCode

        self.request = api.WeatherApi(q=(f'{self.zip}'), debug=0)
        
        self.location = self.request.location()

        print('location:', self.location)
        
    class Forecast(RetrieveForecast):
        ''' usage: RetrieveWeather('brisbane', 'qld').Forecast.get_daily() '''
        def __init__(self, request):
            super().__init__(request)

        def get_rain(self):  #?  self or super()?
            return super().get_rain_data_fields()  

        def get_daily(self): #, days=7, type=''
            return super().get_daily_data_fields()  

        def get_hourly(self):
            return super().get_hourly_data_fields()
        
    class UvData(RetrieveUvIndex):
        ''' usage: RetrieveWeather('brisbane', 'qld').UvIndex.get_uv_descriptions() '''
        def __init__(self, request):
            super().__init__(request)

        # def get_uv_descriptions(self):
        #     return super().get_uv_descriptions()

        def get_uv_message(self):
            return super().get_uv_message()
        
    class Warnings(RetrieveWarnings):
        ''' usage: RetrieveWeather('brisbane', 'qld').Warnings.get_warnings() '''
        def __init__(self, request):
            super().__init__(request)
            
        def get_warnings(self):
            return super().get_warnings()

        def get_title(self):
            return super().get_warning_title()
        
        def get_warning_description(self):
            return super().get_warning_description()
        
        def get_warning_id(self):
            return super().get_warning_id()
    
    class Summary(RetrieveSummary):
        ''' usage: RetrieveWeather('brisbane', 'qld').Summary.get_summary() '''
        def __init__(self, request):
            super().__init__(request)

        def get_summary(self):
            return super().get_summary()
        
        def get_summary_text(self):
            return super().get_summary_text()
        
    class Observations(RetrieveObservations):
        ''' usage: RetrieveWeather('brisbane', 'qld').Observations.get_observations() '''
        def __init__(self, request):
            super().__init__(request)
            
        def get_observations(self):
            return super().get_observations()

        def get_predicted_air_temperature(self):
            return super().get_predicted_air_temperature()
        
        def get_predicted_rainfall(self):
            return super().get_predicted_rainfall()
        
    class Place(RetrievePlace):
        def __init__(self, request):
            super().__init__(request)
            
        def get_forecast(self):
            return super().get_forecast()
        
        def get_aire_temperature(self):
            return super().get_air_temperature()
            
        def get_place(self):
            return super().get_place()
    
        def get_place_state(self):
            return super().get_place_state()
        
        def get_place_name(self):
            return super().get_place_name()
        
        def get_place_country(self):
            return super().get_place_country()
        
        def get_place_timezone(self):
            return super().get_place_timezone()
        
    