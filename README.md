# pico_WeatherStation

A simple Raspberry Pi Pico W based implementation of a Weather Station.
It is built into 2 different Variants
- Variant 1: Using Sensors
- Variant 2: Using OpenWeathermap.org API

## Variant 1

### Hardware

BMP 180: It is an I2C based implementation of hardware used to detect Temperature, Pressure and Altitude. (Default: SDA = GPIO14 SCL = GPIO15)  
DHT11: It uses 1-Wire protocol to report Temperature and Humidity. (Default: DATA = GPIO28)  
Raspberry Pi Pico W: A Pi Pico with WiFi module is used to connect to the internet and process data.  

### Software

The Raspberry Pi Pico W running a python script is used to poll the serial port for data pulled from the sensors, and publishes the data to a ThingSpeak Channel.  
ThingSpeak is used to Visualise the Data.  

![ThingSpeak Charts](https://github.com/METACRYPT12/pico_WeatherStation/blob/master/img/ThingSpeak_Charts.png)

### Setup

The WiFi ssid and password must be updated in /lib/secrets.py for Pi Pico W to connect to the internet.  
A ThingSpeak Channel is Created after signing up and the following fields need to be added.  

![ThingSpeak Fields](https://github.com/METACRYPT12/pico_WeatherStation/blob/master/img/ThingSpeak_Fields.png)

Now the Write API key for the Channel is copied and updated in /lib/secrets.py

### Circuit Diagram

![Circuit Diagram](https://github.com/METACRYPT12/pico_WeatherStation/blob/master/img/Pinout_Diagram.jpg)

## Variant 2

### Hardware

No Hardware configuration is required to setup this Variant

### Software

The Raspberry Pi Pico W running a python script is used to poll the serial port for data pulled from OpenWeatherAPI.  

### Setup

The WiFi ssid and password must be updated in /lib/secrets.py for Pi Pico W to connect to the internet.  
An OpenWeatherMap API key needs to be generated and copied in /lib/secrets.py.  

## Auto-Start Instructions

Simply Copy the main.py for any of the two Variants you want to Auto-Start at boot.  
Additionally external power supply can be connected through VSYS to enable the user to push updates to the Pi Pico W on the go.  

## Future

A Display may be added later to the project.  
