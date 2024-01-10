from django.db import models

class LocationImagesModel(models.Model):
    country = models.CharField(max_length=200, black=False)
    city = models.TextField(black=False)
    zip = models.TextField(blank=False)
    lat = models.FloatField()
    lon = models.FloatField()
    image_url = models.TextField(black=False)
    is_safe = models.BooleanField(default=False)
    