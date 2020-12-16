# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
#import time
import sys

GPIO_Nbr = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_Nbr, GPIO.IN)

def detec_btn():
    state = 0
    while True:
        if (GPIO.input(GPIO_Nbr)==1):
            state = 1
            return state
        elif(KeyboardInterrupt):
            GPIO.cleanup()
            sys.exit()
        else:
            state = 0
            return state