from decouple import config
import openai
from openai import OpenAI

client = OpenAI(api_key=config("OPENAI_API_KEY"))

#client.api_key = config("OPENAI_API_KEY")

GPT_MODEL = "gpt-3.5-turbo-1106"

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather of a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city or town e.g. New York. return city/town name only",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["metric", "imperial"],
                        "description": "The temperature unit to use. Defualt is metric. Infer this from the users location. only return either imperial or metric",
                    },
                    'fields': {
                        'type': 'string',
                        #properties: {  
                        #   'temperature': {'type': 'string', 'description': 'The temperature in Celcius or Fahrenheit'},
                        #   'humidity': {'type': 'string', 'description': 'The humidity in %'},
                        #   etc.
                        'enum': ['temperature', 'humidity', 'cloudCover', 'dewPoint', 'epaHealthConcern', 'epaIndex', 'epaPrimaryPollutant', 'fireIdex', 'hailBinary', 'humidity', 'iceAccumilation', 'moonPhase', 'pollutantCO', 'pollutantNO2', 'pollutantO3', 'pollutantSO2', 'precipitationIntensity', 'precipitationProbability', 'precipitationType', 'snowAccumulation', 'temperature', 'temperatureApparent', 'visibility', 'waveSignificantHeight', 'windDirection', 'windGust', 'windSpeed', 'weatherCode', 'weatherCodeFullDay'],
                        'description': 'The weather data fields that you will recieve. Default: temperature, humidity, weatherCodeFullDay, precipitationIntensity, precipitationProbability, precipitationType, snowAccumulation, temperatureApparent (feels like), windSpeed. optional parameters are cloudCover (%), dewPoint (Celcius:Fahrenheit), epaHealthConcern (0 (good)-5 (hazardous)), epaIndex (0 (good)-5 (hazardous)), epaPrimaryPollutant (PM2.5 (0), PM10 (1), O3 (2), NO2 (3), CO (4), SO2 (5)), fireIdex (FWI), hailBinary (Binary Prediction), humidity (%), iceAccumilation (mm:in), moonPhase (0 (new), 1 (waxing cresent), 2 (first quarter), 3 (waxing gibbous), 4 (full), 5 (waning gibbous), 6 (third quarter), 7 (waning cresent)), pollutantCO (ppb), pollutantNO2 (ppb), pollutantO3 (ppb), pollutantSO2 (ppb), precipitationIntensity (mm/hr:in/hr), precipitationProbability (%), precipitationType (0 (none), 1 (rain), 2 (snow), 3 (freezing rain), 4 (ice pellets)), snowAccumulation (mm:in), temperature (Celcius:Fahrenheit), temperatureApparent (Celcius:Fahrenheit), visibility (km:mi), waveSignificantHeight (m:ft), windDirection (degrees), windGust (m/s:mph), windSpeed (m/s:mph), weatherCode (0 (Unknown), 1000 (clear, Sunny), 1100 (Mostly Clear), 1101 (Partly Cloudy), 1102 (Mostly Cloudy), 2000 (Fog), 2100 (Light Fog), 4000 (Drizzle), 4001 (Rain), 4200 (Light Rain), 4201 (Heavy Rain), 5000 (Snow), 5001 (Flurries), 5100 (Light Snow), 5101 (Heavy Snow), 6000 (Freezing Drizzle), 6001 (Freezing Rain), 6200 (Light Freezing Rain), 6201 (Heavy Freezing Rain), 7000 (Ice Pellets), 7101 (Heavy Ice Pellets), 7102 (Light Ice Pellets), 8000 (Thunderstorm), 8001 (Heavy Thunderstorm), 8002 (Light Thunderstorm), 9000 (Lightning), 9001 (Heavy Lightning), 9002 (Light Lightning Rain), 9003 (Heavy Lightning Rain), 9999 (Unknown Precipitation)), weatherCodeFullDay (0 (Unknown), 1000 (clear, Sunny), 1100 (Mostly Clear), 1101 (Partly Cloudy), 1102 (Mostly Cloudy), 2000 (Fog), 2100 (Light Fog), 4000 (Drizzle), 4001 (Rain), 4200 (Light Rain), 4201 (Heavy Rain), 5000 (Snow), 5001 (Flurries), 5100 (Light Snow), 5101 (Heavy Snow), 6000 (Freezing Drizzle), 6001 (Freezing Rain), 6200 (Light Freezing Rain), 6201 (Heavy Freezing Rain), 7000 (Ice Pellets), 7101 (Heavy Ice Pellets), 7102 (Light Ice Pellets), 8000 (Thunderstorm), 8001 (Heavy Thunderstorm), 8002 (Light Thunderstorm), 9000 (Lightning), 9001 (Heavy Lightning), 9002 (Light Lightning Rain), 9003 (Heavy Lightning Rain), 9999 (Unknown Precipitation)). add feilds from optional data when you see fit'
                    },
                },
                "required": [],
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_daily_weather_forecast",
            "description": "Get the dialy weather forecast of a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city or town e.g. New York. return city/town name only",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["metric", "imperial"],
                        "description": "The temperature unit to use. Defualt is metric. Infer this from the users location. only return either imperial or metric",
                    },
                    'fields': {
                        'type': 'string',
                        'enum': ['temperature', 'humidity', 'cloudCover', 'dewPoint', 'epaHealthConcern', 'epaIndex', 'epaPrimaryPollutant', 'fireIdex', 'hailBinary', 'humidity', 'iceAccumilation', 'moonPhase', 'pollutantCO', 'pollutantNO2', 'pollutantO3', 'pollutantSO2', 'precipitationIntensity', 'precipitationProbability', 'precipitationType', 'snowAccumulation', 'temperature', 'temperatureApparent', 'visibility', 'waveSignificantHeight', 'windDirection', 'windGust', 'windSpeed', 'weatherCode', 'weatherCodeFullDay'],
                        'description': 'The weather data fields that you will recieve. Default: temperature, humidity, weatherCodeFullDay, precipitationIntensity, precipitationProbability, precipitationType, snowAccumulation, temperatureApparent (feels like), windSpeed. optional parameters are cloudCover (%), dewPoint (Celcius:Fahrenheit), epaHealthConcern (0 (good)-5 (hazardous)), epaIndex (0 (good)-5 (hazardous)), epaPrimaryPollutant (PM2.5 (0), PM10 (1), O3 (2), NO2 (3), CO (4), SO2 (5)), fireIdex (FWI), hailBinary (Binary Prediction), humidity (%), iceAccumilation (mm:in), moonPhase (0 (new), 1 (waxing cresent), 2 (first quarter), 3 (waxing gibbous), 4 (full), 5 (waning gibbous), 6 (third quarter), 7 (waning cresent)), pollutantCO (ppb), pollutantNO2 (ppb), pollutantO3 (ppb), pollutantSO2 (ppb), precipitationIntensity (mm/hr:in/hr), precipitationProbability (%), precipitationType (0 (none), 1 (rain), 2 (snow), 3 (freezing rain), 4 (ice pellets)), snowAccumulation (mm:in), temperature (Celcius:Fahrenheit), temperatureApparent (Celcius:Fahrenheit), visibility (km:mi), waveSignificantHeight (m:ft), windDirection (degrees), windGust (m/s:mph), windSpeed (m/s:mph), weatherCode (0 (Unknown), 1000 (clear, Sunny), 1100 (Mostly Clear), 1101 (Partly Cloudy), 1102 (Mostly Cloudy), 2000 (Fog), 2100 (Light Fog), 4000 (Drizzle), 4001 (Rain), 4200 (Light Rain), 4201 (Heavy Rain), 5000 (Snow), 5001 (Flurries), 5100 (Light Snow), 5101 (Heavy Snow), 6000 (Freezing Drizzle), 6001 (Freezing Rain), 6200 (Light Freezing Rain), 6201 (Heavy Freezing Rain), 7000 (Ice Pellets), 7101 (Heavy Ice Pellets), 7102 (Light Ice Pellets), 8000 (Thunderstorm), 8001 (Heavy Thunderstorm), 8002 (Light Thunderstorm), 9000 (Lightning), 9001 (Heavy Lightning), 9002 (Light Lightning Rain), 9003 (Heavy Lightning Rain), 9999 (Unknown Precipitation)), weatherCodeFullDay (0 (Unknown), 1000 (clear, Sunny), 1100 (Mostly Clear), 1101 (Partly Cloudy), 1102 (Mostly Cloudy), 2000 (Fog), 2100 (Light Fog), 4000 (Drizzle), 4001 (Rain), 4200 (Light Rain), 4201 (Heavy Rain), 5000 (Snow), 5001 (Flurries), 5100 (Light Snow), 5101 (Heavy Snow), 6000 (Freezing Drizzle), 6001 (Freezing Rain), 6200 (Light Freezing Rain), 6201 (Heavy Freezing Rain), 7000 (Ice Pellets), 7101 (Heavy Ice Pellets), 7102 (Light Ice Pellets), 8000 (Thunderstorm), 8001 (Heavy Thunderstorm), 8002 (Light Thunderstorm), 9000 (Lightning), 9001 (Heavy Lightning), 9002 (Light Lightning Rain), 9003 (Heavy Lightning Rain), 9999 (Unknown Precipitation)). add feilds from optional data when you see fit'
                    },
                },
                "required": []
            },
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_hourly_weather_forecast",
            "description": "Get the hourly weather forecast for the current day of a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city or town e.g. New York. return city/town name only",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["metric", "imperial"],
                        "description": "The temperature unit to use. Defualt is metric. Infer this from the users location. only return either imperial or metric",
                    },
                    'fields': {
                        'type': 'string',
                        'enum': ['temperature', 'humidity', 'cloudCover', 'dewPoint', 'epaHealthConcern', 'epaIndex', 'epaPrimaryPollutant', 'fireIdex', 'hailBinary', 'humidity', 'iceAccumilation', 'moonPhase', 'pollutantCO', 'pollutantNO2', 'pollutantO3', 'pollutantSO2', 'precipitationIntensity', 'precipitationProbability', 'precipitationType', 'snowAccumulation', 'temperature', 'temperatureApparent', 'visibility', 'waveSignificantHeight', 'windDirection', 'windGust', 'windSpeed', 'weatherCode', 'weatherCodeFullDay'],
                        'description': 'The weather data fields that you will recieve. Default: temperature, humidity, weatherCodeFullDay, precipitationIntensity, precipitationProbability, precipitationType, snowAccumulation, temperatureApparent (feels like), windSpeed. optional parameters are cloudCover (%), dewPoint (Celcius:Fahrenheit), epaHealthConcern (0 (good)-5 (hazardous)), epaIndex (0 (good)-5 (hazardous)), epaPrimaryPollutant (PM2.5 (0), PM10 (1), O3 (2), NO2 (3), CO (4), SO2 (5)), fireIdex (FWI), hailBinary (Binary Prediction), humidity (%), iceAccumilation (mm:in), moonPhase (0 (new), 1 (waxing cresent), 2 (first quarter), 3 (waxing gibbous), 4 (full), 5 (waning gibbous), 6 (third quarter), 7 (waning cresent)), pollutantCO (ppb), pollutantNO2 (ppb), pollutantO3 (ppb), pollutantSO2 (ppb), precipitationIntensity (mm/hr:in/hr), precipitationProbability (%), precipitationType (0 (none), 1 (rain), 2 (snow), 3 (freezing rain), 4 (ice pellets)), snowAccumulation (mm:in), temperature (Celcius:Fahrenheit), temperatureApparent (Celcius:Fahrenheit), visibility (km:mi), waveSignificantHeight (m:ft), windDirection (degrees), windGust (m/s:mph), windSpeed (m/s:mph), weatherCode (0 (Unknown), 1000 (clear, Sunny), 1100 (Mostly Clear), 1101 (Partly Cloudy), 1102 (Mostly Cloudy), 2000 (Fog), 2100 (Light Fog), 4000 (Drizzle), 4001 (Rain), 4200 (Light Rain), 4201 (Heavy Rain), 5000 (Snow), 5001 (Flurries), 5100 (Light Snow), 5101 (Heavy Snow), 6000 (Freezing Drizzle), 6001 (Freezing Rain), 6200 (Light Freezing Rain), 6201 (Heavy Freezing Rain), 7000 (Ice Pellets), 7101 (Heavy Ice Pellets), 7102 (Light Ice Pellets), 8000 (Thunderstorm), 8001 (Heavy Thunderstorm), 8002 (Light Thunderstorm), 9000 (Lightning), 9001 (Heavy Lightning), 9002 (Light Lightning Rain), 9003 (Heavy Lightning Rain), 9999 (Unknown Precipitation)), weatherCodeFullDay (0 (Unknown), 1000 (clear, Sunny), 1100 (Mostly Clear), 1101 (Partly Cloudy), 1102 (Mostly Cloudy), 2000 (Fog), 2100 (Light Fog), 4000 (Drizzle), 4001 (Rain), 4200 (Light Rain), 4201 (Heavy Rain), 5000 (Snow), 5001 (Flurries), 5100 (Light Snow), 5101 (Heavy Snow), 6000 (Freezing Drizzle), 6001 (Freezing Rain), 6200 (Light Freezing Rain), 6201 (Heavy Freezing Rain), 7000 (Ice Pellets), 7101 (Heavy Ice Pellets), 7102 (Light Ice Pellets), 8000 (Thunderstorm), 8001 (Heavy Thunderstorm), 8002 (Light Thunderstorm), 9000 (Lightning), 9001 (Heavy Lightning), 9002 (Light Lightning Rain), 9003 (Heavy Lightning Rain), 9999 (Unknown Precipitation)). add feilds from optional data when you see fit'
                    },
                },
                "required": []
            },
        }
    },
]