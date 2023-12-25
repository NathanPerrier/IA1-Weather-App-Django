import json
from tenacity import retry, wait_random_exponential, stop_after_attempt
import requests

from .__init__ import *
from .data import BotData

@retry(wait=wait_random_exponential(multiplier=1, max=60), stop=stop_after_attempt(3))
def chat_completion_request(messages, tools=None):
    
    response = client.chat.completions.create(
        model=GPT_MODEL,
        messages=messages,
        tools=TOOLS,
        tool_choice="auto",  # auto is default, but we'll be explicit
    )
    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls
    
    # Step 2: check if the model wanted to call a function
    if tool_calls:
        
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "get_current_weather": BotData().get_current_weather,
            "get_daily_weather_forecast": BotData().get_daily_weather_forecast,
            "get_hourly_weather_forecast": BotData().get_hourly_weather_forecast,
        }  
        
        messages.append(response_message)  # extend conversation with assistant's reply
        
        # Step 4: send the info for each function call and function response to the model
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(
                location=function_args.get("location"),
                unit=function_args.get("unit"),
            )
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )  # extend conversation with function response
        second_response = client.chat.completions.create(
            model=GPT_MODEL,
            messages=messages,
        )  # get a new response from the model where it can see the function response
        return second_response.choices[0].message.content
    else:
        return response_message.content
