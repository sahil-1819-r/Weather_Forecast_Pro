import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY= os.getenv("WEATHER_API_KEY")

def get_weather(city):
   
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
   
    response= requests.get(url)
   
    data= response.json()
    
    if "error" in data:
      return None
    
    weather = {
           "temperature": data["current"]["temp_c"],
           "country": data["location"]["country"],
           "humidity": data["current"]["humidity"],
           "wind_kph": data["current"]["wind_kph"],
           "condition": data["current"]["condition"]["text"],
           "icon": data["current"]["condition"]["icon"]
    }
    return weather
    
def get_weather_by_coordinates(latitude,longitude):
     
     url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={latitude},{longitude}"
     response= requests.get(url)
     data= response.json()
    
     if "error" in data:
          return None
     
     weather = {
           "temperature": data["current"]["temp_c"],
           "country": data["location"]["country"],
           "humidity": data["current"]["humidity"],
           "wind_kph": data["current"]["wind_kph"],
           "condition": data["current"]["condition"]["text"],
           "icon": data["current"]["condition"]["icon"]
    }
     return weather