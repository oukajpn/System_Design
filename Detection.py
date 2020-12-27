# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO

GPIO_Nbr = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_Nbr, GPIO.IN)

def OPEN_CLOSE_Detection():
    safe = 1
    while True:
        if (GPIO.input(GPIO_Nbr)==1):
            safe = 0
            return safe
        else:
            safe = 1
            return safe
    
def OPEN_CLOSE_Detection_cnt():
    cnt = 0
    while True:
        if (GPIO.input(GPIO_Nbr)==1):
            cnt = 0
            return cnt
        else:
            cnt = 1
            return cnt