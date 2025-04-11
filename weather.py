from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="Kansas City"):
    request_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv('API_KEY')}&units=imperial"

    weather_data = requests.get(request_url).json()
    return weather_data



if __name__ == "__main__":
    city = input("Enter the name of the city: ")
    
    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)
    # print(weather_data["main"]["temp"])
    # print(weather_data["weather"][0]["description"])
    # print(weather_data["main"]["humidity"])
    # print(weather_data["wind"]["speed"])