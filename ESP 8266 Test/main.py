# main.py -- put your code here!
import pcd8544_fb
from machine import Pin, SPI, PWM
import time

print('Hello world!')

def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('BreakfastBerry', 'N;9263k2')
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

do_connect()

buildin_led = Pin(2, Pin.OUT)
buildin_led.value(1) # turn off
time.sleep(1)
buildin_led.value(0) # turn on


spi = SPI(1)
spi.init(baudrate=2000000, polarity=0, phase=0)
cs = Pin(4)
dc = Pin(15)
rst = Pin(5)

# backlight on
bl = Pin(12, Pin.OUT, value=0)

# backlight dimming
bl_pwm = PWM(bl)
bl_pwm.freq(500)
bl_pwm.duty(0)    # off
bl_pwm.duty(128)  # dim

lcd = pcd8544_fb.PCD8544_FB(spi, cs, dc, rst)

def display_example(input_string):
    lcd.text('-NerdCave-', 0, 0, 1)
    lcd.text(input_string, 0, 12, 1)
    lcd.clear()
    lcd.show()
    time.sleep(2)

display_example('Hello World!')

