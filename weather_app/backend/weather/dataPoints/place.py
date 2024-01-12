from ..__init__ import *

class RetrievePlace():
    def __init__(self, request):
        self.request = request
        self.model = place.Place(self.request.location()[0]['state'], self.request.location()[0]['name'])
        
    def get_forecast(self):
        return self.model.forecast()
    
    def get_air_temperature(self):
        return self.model.air_temperature()
    
    # Location info
    
    def get_place(self):
        return self.request.location()
    
    def get_place_state(self):
        return self.request.location()[0]['state']
    
    def get_place_name(self):
        return self.request.location()[0]['name']
    
    def get_place_country(self):
        return self.get_timezone.split('/')[0]
    
    def get_place_timezone(self):
        return self.request.location()[0]['timezone']

    