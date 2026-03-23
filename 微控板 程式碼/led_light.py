from machine import Pin
import neopixel
import time
 
gpio = 15
num_leds = 8
p = Pin(gpio)
led_strip = neopixel.NeoPixel(p, num_leds)
id_led=0
id_rgb=0
 
def show_leds(brightness):
    global id_led
    global id_rgb
    r=int((1-brightness)*10)
    g=0
    b=int(brightness*10)
    led_strip[id_led] = (r,g,b)
    id_led+=1
    if id_led==8:id_led=0
    id_rgb+=1
    if id_rgb==3:id_rgb=0
    led_strip.write()
 
 
def clear_leds():
    for i in range(num_leds):
        led_strip[i] = (0, 0, 0)
    led_strip.write()
 
 
