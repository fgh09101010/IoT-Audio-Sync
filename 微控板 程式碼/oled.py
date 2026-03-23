from machine import Pin, SoftI2C
import ssd1306
import time

DISPLAY_WIDTH = 128   
DISPLAY_HEIGHT = 64
gpio_sda = 21
gpio_scl = 22
 
# 初始化 I2C 和 OLED
i2cbus = SoftI2C(sda=Pin(gpio_sda), scl=Pin(gpio_scl))
display = ssd1306.SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, i2cbus)
  
def display_frequency(frequency,max_frequency,min_frequency):
    
    display.fill_rect(0, 45, DISPLAY_WIDTH, 10, 0)  # 清空頻率區域
    display.fill_rect(0, 60, DISPLAY_WIDTH, 10, 0)

    display.text(f'Freq: {frequency} Hz', 0, 45, 1)

    # 動態條形圖
    bar_length = int(((frequency-min_frequency) / (max_frequency-min_frequency)) * DISPLAY_WIDTH)  # 根據頻率計算條形圖長度
    display.fill_rect(0, 60, bar_length, 10, 1)  # 畫條形圖

    # 顯示屏幕更新
    display.show()
    
def display_song(song):
    # 清屏
    display.fill_rect(0, 0, DISPLAY_WIDTH, 10, 0)

    # 顯示標題和當前頻率
    display.text(f'song:{song}', 0, 0, 1)

    # 顯示屏幕更新
    display.show()
    
def display_time(t,total):
    
    display.fill_rect(0, 15, DISPLAY_WIDTH, 10, 0)  # 清空時間區域
    display.fill_rect(0, 30, DISPLAY_WIDTH, 10, 0)

    # 顯示標題和當前頻率
    display.text(f'time:{t} s', 0, 15)
    
    bar_length = int((total-t)/total * DISPLAY_WIDTH)  # 根據頻率計算條形圖長度
    display.fill_rect(0, 30, bar_length, 10, 1)  # 畫條形圖

    # 顯示屏幕更新
    display.show()
    
def clear_display():
    display.fill(0)  # 清空顯示屏，所有像素設為 0
    display.show()   # 更新顯示

