import tm1637
from machine import Pin


gpio_clk = 14
gpio_dio = 13
tm = tm1637.TM1637(clk=Pin(gpio_clk), dio=Pin(gpio_dio))

# 顯示計時器時間（格式化成 MM:SS）
def display_time(seconds):
    
    minutes = seconds // 60
    secs = seconds % 60
    s = "{:02d}{:02d}".format(minutes, secs)  # MM:SS 格式
    tm.show(s, True)  # 顯示時間並啟用冒號

def clear_display():
    tm.show("0000")  # 計時結束清零
