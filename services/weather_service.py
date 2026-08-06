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
           "city": data["location"]["name"],

           "condition": data["current"]["condition"]["text"],
           "icon": data["current"]["condition"]["icon"],

           "humidity": data["current"]["humidity"],
           "wind_kph": data["current"]["wind_kph"],

          "feels_like": data["current"]["feelslike_c"],
          "pressure": data["current"]["pressure_mb"],
          "visibility": data["current"]["vis_km"],
          "uv": data["current"]["uv"],

          "local_time": data["location"]["localtime"]
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
           "city": data["location"]["name"],
           "region": data["location"]["region"],
           "country": data["location"]["country"],
           

           "condition": data["current"]["condition"]["text"],
           "icon": data["current"]["condition"]["icon"],

           "humidity": data["current"]["humidity"],
           "wind_kph": data["current"]["wind_kph"],

          "feels_like": data["current"]["feelslike_c"],
          "pressure": data["current"]["pressure_mb"],
          "visibility": data["current"]["vis_km"],
          "uv": data["current"]["uv"],

          "local_time": data["location"]["localtime"]
    }
     return weather 

def get_forecast(city):
     
     url= url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=3"
     response= requests.get(url)
     data= response.json()
     
     if "error" in data:
          return None
     
     forecast= []
     
     for day in data["forecast"]["forecastday"]:
          forecast.append({
               "date": day["date"],
               
               "max_temp": day["day"]["maxtemp_c"],
               "min_temp": day["day"]["mintemp_c"],
               
               "condition": day["day"]["condition"]["text"],
               "icon": day["day"]["condition"]["icon"]
          })
     return forecast

def get_major_cities_weather():

    cities = [
        "New Delhi",
        "Mumbai",
        "Bengaluru",
        "Chennai",
        "Hyderabad",
        "Kolkata",
        "Pune",
        "Ahmedabad"
    ]

    cities_weather = []

    for city in cities:

        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

        response = requests.get(url)

        data = response.json()

        cities_weather.append({

            "city": city,

            "temperature": data["current"]["temp_c"],

            "condition": data["current"]["condition"]["text"],

            "icon": data["current"]["condition"]["icon"]

        })

    return cities_weather