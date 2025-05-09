from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve
import os

app = Flask(__name__)


@app.route("/")

@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/weather')


def get_weather():
    city = request.args.get('city')

    #Check for empty strings or string with only spaces
    if not bool(city.strip()):
        city = "Kansas City"
    weather_data = get_current_weather(city)
    #City is not found 
    if not weather_data['cod'] == 200:
        return  render_template('city_not_found.html', title="City not found", city=city)

    #Pasar de grados Fahrenheit a Celsius
    # weather_data["main"]["temp"] = (weather_data["main"]["temp"] - 32) * 5/9

    if weather_data:
        return render_template('weather.html',title=weather_data['name'], 
                               status=weather_data["weather"][0]["description"].capitalize(), 
                               temp=f"{(weather_data['main']['temp'] - 32) * 5/9:.1f}°C", 
                               feels_like=f"{(weather_data['main']['feels_like'] - 32) * 5/9:.1f}°C",

                            )

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
  