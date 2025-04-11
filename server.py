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
    weather_data = get_current_weather(city)
    if weather_data:
        return render_template('weather.html',title=weather_data['name'], 
                               status=weather_data["weather"][0]["description"].capitalize(), 
                               temp=f"{weather_data["main"]["temp"]:.1f}°C", 
                               feels_like=f"{weather_data["main"]["feels_like"]:.1f}°C",
                            )
    else:
        return "City not found", 404
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)