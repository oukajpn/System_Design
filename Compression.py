# -*- coding: utf-8 -*-
from time import sleep
import Detection
import RPi.GPIO as GPIO
import spidev
import time
import subprocess

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

def push(limit_pressur,max_elevat,now_elevat,add_elevat):
    while(max_elevat > now_elevat):
        danger = Detection.OPEN_CLOSE_Detection
        now_pressur = pressure()
        if(danger == 0 and (limit_pressur>now_pressur)):
            GPIO.output(DIR, 0)
            while(max_elevat > now_elevat):
                GPIO.output(STEP, GPIO.HIGH)
                sleep(delay)
                GPIO.output(STEP, GPIO.LOW)
                sleep(delay)
                danger = Detection.OPEN_CLOSE_Detection
                GPIO.cleanup()
                max_elevat-=now_elevat
                if(danger == 1 or (limit_pressur<=now_pressur)):
                    break

def down(limit_pressur,max_elevat,now_elevat,add_elevat):
    while(max_elevat > now_elevat):
        danger = Detection.OPEN_CLOSE_Detection
        now_pressur = pressure()
        if(danger == 0 and (limit_pressur>now_pressur)):
            GPIO.output(DIR, 1)
            while(max_elevat > now_elevat):
                GPIO.output(STEP, GPIO.HIGH)
                sleep(delay)
                GPIO.output(STEP, GPIO.LOW)
                sleep(delay)
                danger = Detection.OPEN_CLOSE_Detection
                GPIO.cleanup()
                max_elevat-=now_elevat
                if(danger == 1 or (limit_pressur<=now_pressur)):
                    break
                
def pressure():
    spi = spidev.SpiDev()
    spi.open(0, 0)
    while True:
        res = spi.xfer2([0x68, 0x00])
        value = (res[0] * 256 + res[1]) & 0x3ff
        time.sleep(1)
        return(value)
            
def compression():
    max_elevat = motor_steps
    now_elevat = 0
    add_elevat = motor_steps/100
    limit_pressur = 250
    pb_state = detec_btn1()
    pb_cnt = 0
    
    if(pb_state==1):
        if(pb_cnt == 0):
            pb_cnt = 1
            push(limit_pressur,max_elevat,now_elevat,add_elevat)
            now_elevat = 0
        else:
            down(limit_pressur,max_elevat,now_elevat,add_elevat)
            now_elevat = 0
            pb_cnt = 0