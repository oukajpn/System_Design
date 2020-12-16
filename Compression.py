# -*- coding: utf-8 -*-
from time import sleep
import Detection
import RPi.GPIO as GPIO

health = 0

motor_steps = 200
delay = .001

def setup(DIR,STEP,btn1):
    global DIR
    global STEP
    global btn1
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)
    GPIO.output(DIR, 1)
    GPIO.setup(btn1, GPIO.IN)
    
def detec_btn1():
    state = 0
    while True:
        if (GPIO.input(btn1)==1):
            state = 1
            return state
        else:
            state = 0
            return state

def push(max_elevat,now_elevat,add_elevat):
    while(max_elevat > now_elevat):
        danger = Detection.OPEN_CLOSE_Detection
        if(danger == 0):
            for x in range(motor_steps):
                GPIO.output(STEP, GPIO.LOW)
                sleep(delay)
                GPIO.output(STEP, GPIO.HIGH)
                sleep(delay)
            now_elevat -= add_elevat
            GPIO.cleanup()

def down(max_elevat,now_elevat,add_elevat):
    while(max_elevat > now_elevat):
        danger = Detection.OPEN_CLOSE_Detection
        if(danger == 0):
            for x in range(motor_steps):
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
    pb_state = detec_btn1()
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