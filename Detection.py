# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
#import time
import sys

GPIO_Nbr = 7
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_Nbr, GPIO.IN)

def detection():
    safe = 1
    while True:
        if (GPIO.input(GPIO_Nbr)==1):
            safe = 0
            return safe
        elif(KeyboardInterrupt):
            GPIO.cleanup()
            sys.exit()
        else:
            safe = 1
            return safe
    