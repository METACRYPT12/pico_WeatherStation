from machine import Pin, reset
from time import sleep, ticks_ms, ticks_diff
import wlan
import secrets
import urequests
import cityid

# Enable On-Board LED
led = Pin("LED", Pin.OUT)

# Connect to WiFi
try:
    wlan.connect()
except KeyboardInterrupt:
    reset()

# API Request URL
URL = 'http://api.openweathermap.org/data/2.5/weather?q=' + cityid.city + ',' + cityid.country_code + '&APPID=' + secrets.openweather

led.on()
sleep(.5)
led.off()

# Retrieve weather data in json format
def get_weather(city, country_code, api_key, units='metric', lang='en'):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}&units={units}&lang={lang}"
    response = urequests.post(url)
    return response.json()

start = ticks_ms() - 1000

while(1):
    end = ticks_ms()
    
    # Waiting for 1 second between requests
    if(ticks_diff(end, start) > 1000):
        start = end
        
        weather_data = get_weather(cityid.city, cityid.country_code, secrets.openweather)
        
        main = weather_data.get('main')
        weather = weather_data.get('weather')
        sys = weather_data.get('sys')
        wind = weather_data.get('wind')
        
        print(f'Location: {weather_data["name"]},{sys["country"]}')
        print(f'Temperature: {main["temp"]}°C')
        print(f'Pressure: {main["pressure"]}hPa')
        print(f'Humidity: {main["humidity"]}%')
        print(f'Weather Discription: {weather[0]["description"]}')
        print(f'Wind: {wind["speed"]}m/s {wind["deg"]}°')
        print('\n\n')
        
        led.toggle()
        sleep(.01)
        led.toggle()
