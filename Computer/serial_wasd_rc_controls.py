# Arduino modules
import serial
import time
import pygame

# Constants
# Left
blue_on = bytes(b'2')
blue_off = bytes(b'1')
# Right
green_on = bytes(b'4')
green_off = bytes(b'3')
# Forward
red_on = bytes(b'6')
red_off = bytes(b'5')
# Backward
green_on2 = bytes(b'8')
green_off2 = bytes(b'7')

# Establish the connection on a specific port
arduino = serial.Serial('/dev/cu.usbmodem1461', 9600)
time.sleep(1)  # give the connection a second to settle

while True:

    arduino.write(blue_off)
    arduino.write(green_off)
    arduino.write(red_off)
    arduino.write(green_off2)

    my_in = input("Next command: ")

    if "a" in my_in:
        arduino.write(blue_on)
    elif "d" in my_in:
        arduino.write(green_on)
    if "w" in my_in:
        arduino.write(red_on)
    elif "s" in my_in:
        arduino.write(green_on2)
    
    # Turn off forward/backward, then let the left/right direction stay for 0.5 seconds while it coasts
    time.sleep(0.3)
    arduino.write(red_off)
    arduino.write(green_off2)
    time.sleep(0.5)
    arduino.write(blue_off)
    arduino.write(green_off)

