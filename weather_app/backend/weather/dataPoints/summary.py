from ..__init__ import *

class RetrieveSummary():
    def __init__(self, request):
        self.request = request
        self.model = summary.Summary(self.request.location(), debug=0)
        
    def get_summary(self):
        return self.model.summary()
        
    def get_summary_text(self):
        result = ''

        for item in self.get_summary().values():
            result += f"{item.label:20s}{item.value}{item.unit}\n"
            
        return result