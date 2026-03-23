import time, utime
import buzzer
import _thread
import countdown
import oled
import button
import led_light



def begin_countdown(total_time):
    for remaining in range(total_time, -1, -1):
        if button.stop_button():
            clear_display()
            _thread.exit()
        countdown.display_time(remaining)
        oled.display_time(remaining, total_time) #oled
        time.sleep(1)  # 每秒更新一次
    countdown.clear_display()# 計時結束清零
    
def play_melody(melody,d=512):
    light=[i[0] for i in melody if i[0] != 0]
    max_light=max(light)*1.01
    min_light=min(light)*0.99
    for note, duration in melody:
        oled.display_frequency(note,max_light,min_light)
        rgb=(note-min_light)/(max_light-min_light)
        if rgb<0:rgb=0
        led_light.show_leds(rgb)
        buzzer.buzz(note, duration,d)
        
        if button.stop_button():
            led_light.clear_leds()
            oled.clear_display()
            _thread.exit()

    led_light.clear_leds()
    