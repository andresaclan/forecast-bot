from __future__ import print_function
from swagger_client.rest import ApiException
from pprint import pprint
import swagger_client
import os
from dotenv import load_dotenv

load_dotenv()
configuration = swagger_client.Configuration()
configuration.api_key['key'] = os.getenv('OPEN_WEATHER_KEY')

# create an instance of the API class
api_instance = swagger_client.APIsApi(swagger_client.ApiClient(configuration))

def fetch_weather(location): 
    try:
        # Realtime API
        api_response = api_instance.realtime_weather(location)
        temp_f = api_response.current.temp_f
        uv = api_response.current.uv
        pprint(temp_f)
        pprint(uv)
        return {
            "temp_f": temp_f,
            "uv_index": uv
        }
    except ApiException as e:
        print("Exception when calling APIsApi->realtime_weather: %s\n" % e)