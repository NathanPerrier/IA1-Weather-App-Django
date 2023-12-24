from decouple import config
import openai
from openai import OpenAI

client = OpenAI(api_key=config("OPENAI_API_KEY"))

#client.api_key = config("OPENAI_API_KEY")

GPT_MODEL = "gpt-3.5-turbo-1106"

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather of a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city or town e.g. New York",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["metric", "imperial"],
                        "description": "The temperature unit to use. Infer this from the users location.",
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
                        "description": "The city or town e.g. New York",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["metric", "imperial"],
                        "description": "The temperature unit to use. Infer this from the users location.",
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
                        "description": "The city or town e.g. New York",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["metric", "imperial"],
                        "description": "The temperature unit to use. Infer this from the users location.",
                    },
                },
                "required": []
            },
        }
    },
]