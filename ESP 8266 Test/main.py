# main.py -- put your code here!
import pcd8544_fb
from machine import Pin, SPI, PWM
import time

def lcd_init():
    spi = SPI(1)
    spi.init(baudrate=2000000, polarity=0, phase=0)
    cs = Pin(4)
    dc = Pin(15)
    rst = Pin(5)
    lcd = pcd8544_fb.PCD8544_FB(spi, cs, dc, rst)

    # backlight on
    bl = Pin(12, Pin.OUT, value=0)

    # backlight dimming
    bl_pwm = PWM(bl)
    bl_pwm.freq(500)
    bl_pwm.duty(512)  # dim

    return lcd

lcd = lcd_init()

# def do_connect():
#     import network
#     wlan = network.WLAN(network.STA_IF)
#     wlan.active(True)
#     if not wlan.isconnected():
#         print('connecting to network...')
#         lcd.text('WIFI...', 0, 0, 1)
#         lcd.clear()
#         lcd.show()
#         wlan.connect('BreakfastBerry', 'N;9263k2')
#         while not wlan.isconnected():
#             pass
#     lcd.fill(0) # clear screen
#     lcd.text('WIFI Conn', 0, 0, 1)
#     lcd.clear()
#     lcd.show()
#     print('network config:', wlan.ifconfig())

# do_connect()

# import ntptime
# try:
#     ntptime.settime()
# except:
#     raise Exception("npttime.settime() failed. No network connection.")

def display_example(input_string):
    lcd.fill(0) # clear screen
    lcd.text('MicroPy', 0, 0, 1)
    lcd.text(input_string, 0, 12, 1)
    lcd.clear()
    lcd.show()
    time.sleep(2)

display_example('ESP 8266')

from icons import *

def draw_icon(x_pos, col_pos, data_upper, data_lower):
    if col_pos >= 5:
        raise ValueError('col_pos must be less than 5, rather than {}'.format(col_pos))
    
    if x_pos > 67:
        # Assume that the icon is 16 pixels wide
        raise ValueError('x_pos must be less than or equal to 67, rather than {}'.format(x_pos))

    lcd.position(x_pos, col_pos)
    lcd.data(data_upper)
    lcd.position(x_pos, col_pos + 1)
    lcd.data(data_lower)

def draw_status_bar_bubble():
    lcd.fill_rect(4, 32, 34, 16, 1)
    lcd.show() 
    draw_icon(0, 4, icon_squircle_l_upper, icon_squircle_l_lower)
    draw_icon(38, 4, icon_squircle_r_upper, icon_squircle_r_lower) 

def draw_status_bar_icon(wifi_status, sync_status):

    if wifi_status == -1:
        draw_icon(4, 4, icon_wifi_disabled_upper, icon_wifi_disabled_lower)
    elif wifi_status == 0:
        draw_icon(4, 4, icon_wifi0_upper, icon_wifi0_lower)
    elif wifi_status == 1:
        draw_icon(4, 4, icon_wifi1_upper, icon_wifi1_lower)
    elif wifi_status == 2:
        draw_icon(4, 4, icon_wifi2_upper, icon_wifi2_lower)
    elif wifi_status == 3:
        draw_icon(4, 4, icon_wifi3_upper, icon_wifi3_lower)
    elif wifi_status == 4:
        draw_icon(4, 4, icon_wifi4_upper, icon_wifi4_lower)
    else:
        draw_icon(4, 4, icon_wifi_not_connected_upper, icon_wifi_not_connected_lower)
        raise ValueError('wifi_status must be between -1 and 4, rather than {}'.format(wifi_status))
    
    if sync_status == 0:
        draw_icon(22, 4, icon_device_check_upper, icon_device_check_lower)
    elif sync_status == 1:
        draw_icon(22, 4, icon_device_error_upper, icon_device_error_lower)
    else:
        draw_icon(22, 4, icon_device_disabled_upper, icon_device_disabled_lower)
        raise ValueError('sync_status must be 0 or 1, rather than {}'.format(sync_status))

draw_status_bar_bubble()
draw_status_bar_icon(4, 0)

def wifi_animation(x_pos, col_pos):
    draw_icon(x_pos, col_pos, icon_wifi1_upper, icon_wifi1_lower)
    time.sleep(0.5)
    draw_icon(x_pos, col_pos, icon_wifi2_upper, icon_wifi2_lower)
    time.sleep(0.5)
    draw_icon(x_pos, col_pos, icon_wifi3_upper, icon_wifi3_lower)
    time.sleep(0.55)
    draw_icon(x_pos, col_pos, icon_wifi4_upper, icon_wifi4_lower)
    time.sleep(0.70)
    draw_icon(x_pos, col_pos, icon_wifi3_upper, icon_wifi3_lower)
    time.sleep(0.55)
    draw_icon(x_pos, col_pos, icon_wifi2_upper, icon_wifi2_lower)
    time.sleep(0.5)
    draw_icon(x_pos, col_pos, icon_wifi1_upper, icon_wifi1_lower)
    time.sleep(0.5)
    draw_icon(x_pos, col_pos, icon_wifi0_upper, icon_wifi0_lower)
    time.sleep(0.5)

def getSeattleTime(UTC_OFFSET=-8):
    print(time.localtime())
    return time.gmtime(time.time() + UTC_OFFSET * 3600)

def getSeattleTimeFormatted(UTC_OFFSET=-8):
    time = getSeattleTime(UTC_OFFSET)
    return "{}:{}".format(("0" + str(time[3 ]))[-2:], ("0" + str(time[4]))[-2:])

print(getSeattleTimeFormatted())

def draw_time():
    lcd.text(getSeattleTimeFormatted(), 44, 36, 1)
    lcd.show()
    lcd.clear()

draw_time()
draw_status_bar_bubble()
draw_status_bar_icon(4, 0)