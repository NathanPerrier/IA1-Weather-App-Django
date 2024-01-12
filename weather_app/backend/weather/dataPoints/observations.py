from ..__init__ import *

class RetrieveObservations():
    def __init__(self, request):
        self.request = request
        self.model = observations.Observations(self.request.location())
        
    def get_observations(self):
        return self.request.api('observations')
        
    def get_predicted_air_temperature(self):
        return self.model.air_temperature()
    
    def get_predicted_rainfall(self):
        return self.model.rainfall()