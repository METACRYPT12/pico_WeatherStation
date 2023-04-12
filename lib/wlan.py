import network
import secrets
from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT)

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.disconnect()
    wlan.connect(secrets.ssid, secrets.password)
    while(wlan.isconnected() == False):
        led.on()
        sleep(.02)
        led.off()
        sleep(.05)
        led.on()
        sleep(.02)
        led.off()
        sleep(1)