# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import sys

safe = 1

GPIO_Nbr = 7
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_Nbr, GPIO.IN)

while True:
    if (GPIO.input(GPIO_Nbr)==1):
        safe = 0
        time.sleep(1) 
    elif(KeyboardInterrupt):
        GPIO.cleanup()
        sys.exit()
    else:
        safe = 1
    