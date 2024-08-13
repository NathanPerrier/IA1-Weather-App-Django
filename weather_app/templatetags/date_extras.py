from django import template
from datetime import timedelta
import datetime
import pytz
from weather_app.backend.location.main import GetLocation

register = template.Library()

@register.filter
def add_days(date, days):
    return date + timedelta(days=days)

@register.filter
def add_day(date):
    created = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
    # Add 2 days
    created_date = created + timedelta(days=1)
    
    return created_date