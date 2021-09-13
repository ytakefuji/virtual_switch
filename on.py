# led-on or led-off
import serial
from time import sleep
s=serial.Serial("COM3",9600)
s.flush()
s.write(str('1').encode())
s.flush()
