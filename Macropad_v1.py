from machine import Pin
import time

# 10, 11, 12, 13
# 6, 7, 8, 9

led = Pin(25, Pin.OUT)

button1 = Pin(10, Pin.IN, Pin.PULL_UP)
button2 = Pin(11, Pin.IN, Pin.PULL_UP)
button3 = Pin(12, Pin.IN, Pin.PULL_UP)
button4 = Pin(13, Pin.IN, Pin.PULL_UP)

button5 = Pin(6, Pin.IN, Pin.PULL_UP)
button6 = Pin(7, Pin.IN, Pin.PULL_UP)
button7 = Pin(8, Pin.IN, Pin.PULL_UP)
button8 = Pin(9, Pin.IN, Pin.PULL_UP)

delay = .11

shiftOrSpacePressed = False

while True:
    if button1.value() == 0: # Exit UI - ESC
        led.value(1)
        time.sleep(delay)
    elif button2.value() == 0: # Inventory - F1
        led.value(1)
        time.sleep(delay)
    elif button3.value() == 0: # Prayer - F2
        led.value(1)
        time.sleep(delay)
    elif button4.value() == 0: # Spellbook - F3
        led.value(1)
        time.sleep(delay)
    elif button5.value() == 0: # Shift
        led.value(1)
        shiftOrSpacePressed = True
        time.sleep(delay)
    elif button6.value() == 0: # Space
        led.value(1)
        shiftOrSpacePressed = True
        time.sleep(delay)
    elif button7.value() == 0: # Worn Equipment
        led.value(1)
        time.sleep(delay)
    elif button8.value() == 0: #Combat Options
        led.value(1)
        time.sleep(delay)
    elif shiftOrSpacePressed == True:
        shiftOrSpacePressed = False
        led.value(0)
    else:
        led.value(0)
