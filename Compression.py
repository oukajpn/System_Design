# -*- coding: utf-8 -*-
from time import sleep
import Detection
import RPi.GPIO as GPIO

health = 0

motor_steps = 12500
delay = .001

def setup(DIR,STEP,btn1):
    global DIR
    global STEP
    global btn1
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DIR, GPIO.OUT)
    GPIO.setup(STEP, GPIO.OUT)
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
            GPIO.output(DIR, 0)
            while(max_elevat > now_elevat):
                GPIO.output(STEP, GPIO.HIGH)
                sleep(delay)
                GPIO.output(STEP, GPIO.LOW)
                sleep(delay)
                danger = Detection.OPEN_CLOSE_Detection
                GPIO.cleanup()
                max_elevat-=now_elevat
                if(danger == 1):
                    break

def down(max_elevat,now_elevat,add_elevat):
    while(max_elevat > now_elevat):
        danger = Detection.OPEN_CLOSE_Detection
        if(danger == 0):
            GPIO.output(DIR, 1)
            while(max_elevat > now_elevat):
                GPIO.output(STEP, GPIO.HIGH)
                sleep(delay)
                GPIO.output(STEP, GPIO.LOW)
                sleep(delay)
                danger = Detection.OPEN_CLOSE_Detection
                GPIO.cleanup()
                max_elevat-=now_elevat
                if(danger == 1):
                    break
            
        
def compression():
    global health
    max_elevat = motor_steps
    now_elevat = 0
    add_elevat = motor_steps/100
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