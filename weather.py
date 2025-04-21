import requests
from dotenv import load_dotenv
import os
from pprint import pprint


load_dotenv()

def get_weather_data():
   print("Fetching weather data...")

   city= input("\n  Enter the city name:")
               
               
   request_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial"

   weather_data = requests.get(request_url).json()

#   pprint(weather_data)
   print(f"\nWeather data for {weather_data["name"]}:")
   print(f"Temperature: {weather_data["main"]["temp"]}°F") 
   print(f"Humidity: {weather_data["main"]["humidity"]}%") 
   print(f"Weather: {weather_data["weather"][0]["description"]}")
   print(f"Wind Speed: {weather_data["wind"]["speed"]} mph")
   
if __name__ == "__main__":
    get_weather_data()  


   