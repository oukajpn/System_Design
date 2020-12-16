# -*- coding: utf-8 -*-
from time import sleep
import Detection
import Push_Pin
import RPi.GPIO as GPIO

health = 0

#stepper variables
DIR = 20
STEP = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, 1)

step_count = 200
delay = .001

def push(max_elevat,now_elevat,add_elevat):
    while(max_elevat > now_elevat):
        danger = Detection.detection()
        if(danger == 0):
            for x in range(step_count):
                GPIO.output(STEP, GPIO.LOW)
                sleep(delay)
                GPIO.output(STEP, GPIO.HIGH)
                sleep(delay)
            now_elevat -= add_elevat
            GPIO.cleanup()

def down(max_elevat,now_elevat,add_elevat):
    while(max_elevat > now_elevat):
        danger = Detection.detection()
        if(danger == 0):
            for x in range(step_count):
                GPIO.output(STEP, GPIO.HIGH)
                sleep(delay)
                GPIO.output(STEP, GPIO.LOW)
                sleep(delay)
            now_elevat -= add_elevat
            GPIO.cleanup()

def compression():
    global health
    max_elevat = 0
    now_elevat = 0
    add_elevat = 0
    pb_state = Push_Pin.detec_btn()
    pb_cnt = 0
    
    if(pb_state==1):
        if(pb_cnt == 0):
            pb_cnt = 1
            push(max_elevat,now_elevat,add_elevat)
            now_elevat = 0
            health = 1
        else:
            down(max_elevat,now_elevat,add_elevat)
            now_elevat = 0
            pb_cnt = 0