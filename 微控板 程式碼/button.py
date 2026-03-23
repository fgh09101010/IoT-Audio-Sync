from machine import Pin
import time
 
gpio = 36
p = Pin(gpio, Pin.IN)


def stop_button():
    num=p.value()
    return num==0

