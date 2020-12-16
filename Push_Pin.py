# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys

state = 0

GPIO_Nbr = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_Nbr, GPIO.IN)

while True:
    if (GPIO.input(GPIO_Nbr)==1):
        state = 1
        time.sleep(1) 
    elif(KeyboardInterrupt):
        GPIO.cleanup()
        sys.exit()
    else:
        state = 0
        