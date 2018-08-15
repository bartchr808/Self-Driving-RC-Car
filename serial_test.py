# Arduino modules
import serial
import time

# Establish the connection on a specific port
arduino = serial.Serial('/dev/cu.usbmodem1461', 9600)
time.sleep(1)  # give the connection a second to settle
#arduino.write("Hello from Python!")
while True:
    arduino.write(bytes(b'1'))
    time.sleep(0.5)
    arduino.write(bytes(b'2'))
    time.sleep(0.5)
