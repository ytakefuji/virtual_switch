# virtual_switch
This repository shows how to integrate artificial intelligence libraries such as mediapipe
with Arduino Nano.

Read the following site for hand gesture recognition:

https://github.com/ytakefuji/mediapipe_hand

Three Python programs (fingersw.py, fvsw.py, fvswt.py) are to control an LED.

fservo.py controls a servo by the tip of your index finger 
where the servo is connected to digital pin #2 on the Arduino.

# fingersw.py
fingersw.py works with 1_0LED.ino arduino.
You should install 1_0LED.ino on arduino Nano.
In fingersw.py, place the tip of your index finger on the upper left corner 
to toggle the LED lights..

# fvsw.py and fvswt.py
fvsw.py works with firmata arduino.

Firmata is a protocol for communicating with microcontrollers 
from software on a computer (or smartphone/tablet, etc).

You should install StandardFirmata for arduino Nano.

In firmata, getpin(X:Y:Z) is to set pin Y: analog 'a' or digital 'd' for X,
Y represents pin number, Z is pin type: 'i' for input,
'o' for output, 'p' for pwm, 's' for servo.

get_pin('d:2:s') means that pin#2 is used for digital servo.

# fvsw.py
In fvsw.py, when placing the tip of your index finger on the upper left corner, 
the LED will light up.

<img src=   width=540 height=480>

# fvswt.py
fvswt.py works with firmata arduino.
In fvswt.py, placing the tip of your index finger on the upper left corner 
toggles the LED-lighting.

# fservo.py
fservo.py works with firmata arduino.
In fservo.py, moving the tip of your index finger with the horizontal axis
can rotate the servo.
