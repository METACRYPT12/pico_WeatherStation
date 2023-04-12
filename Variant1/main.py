from machine import Pin, I2C, reset
from time import sleep, ticks_ms, ticks_diff
from bmp085 import BMP180
from PicoDHT22 import PicoDHT22
import wlan
import secrets
import urequests

# Enable On-Board LED
led = Pin("LED", Pin.OUT)

# Initialize DHT11
dht = PicoDHT22(Pin(28,Pin.IN,Pin.PULL_UP),dht11=True)

# Setting up I2C pins for BMP180
i2c = I2C(1, sda = Pin(14), scl = Pin(15))

# Configuring BMP180
bmp = BMP180(i2c)
bmp.oversample = 2
bmp.sealevel = 1013.25

# Connect to WiFi
try:
    wlan.connect()
except KeyboardInterrupt:
    reset()

# API POST URL
URL = 'https://api.thingspeak.com/update?api_key=%s' % secrets.thingspeak

led.on()
sleep(.5)
led.off()

start = ticks_ms() - 15000

while(1):
    end = ticks_ms()
    
    # Waiting for 15 seconds between requests
    if(ticks_diff(end, start) > 15000):
        start = end
        
        Temp, humidity = dht.read()
        temp = (bmp.temperature + Temp) / 2
        press = bmp.pressure
        altitude = bmp.altitude
        
        finalURL = URL +"&field1=%s&field2=%s&field3=%s&field4=%s" % (temp, press, altitude, humidity)
        request = urequests.post(finalURL)
        request.close()
        
        print("Temperature: {0:5.2f}°C\nPressure: {1:5.2f}hPa\nAltitude: {2:5.2f}m\nHumidity: {3}%".format(temp, press, altitude, humidity))
        print("\n\n")
        
        led.toggle()
        sleep(.01)
        led.toggle()
