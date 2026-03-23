from machine import Pin, PWM
import time

gpio_buzzer = 4  
buzzer = PWM(Pin(gpio_buzzer), freq=262, duty=0)

def buzz(frequency, duration,d):
    if frequency == 0:  # 休止符
        buzzer.duty(0)
    else:
        buzzer.freq(frequency)
        buzzer.duty(d)#0~1023
    time.sleep(duration)
    buzzer.duty(0)  # 停止蜂鳴器

