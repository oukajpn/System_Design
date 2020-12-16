# -*- coding: utf-8 -*-
from time import sleep
import Detection
import Push_Pin
import RPi.GPIO as GPIO

health = 0
danger = Detection.safe
max_elevat = 0
now_elevat = 0
add_elevat = 0
pb_state = Push_Pin.state
pb_cnt = 0

#stepper variables
DIR = 20
STEP = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, 1)

step_count = 200
delay = .001


if(pb_state==1):
    if(pb_cnt == 0):
        pb_cnt = 1
        while(max_elevat > now_elevat):
            if(danger == 0):
                for x in range(step_count):
                    GPIO.output(STEP, GPIO.HIGH)
                    sleep(delay)
                    GPIO.output(STEP, GPIO.LOW)
                    sleep(delay)
                now_elevat -= add_elevat
                GPIO.cleanup()
        now_elevat = 0
        health = 1
    else:
        while(max_elevat > now_elevat):
            if(danger == 0):
                for x in range(step_count):
                    GPIO.output(STEP, GPIO.HIGH)
                    sleep(delay)
                    GPIO.output(STEP, GPIO.LOW)
                    sleep(delay)
                now_elevat -= add_elevat
                GPIO.cleanup()
        now_elevat = 0
        pb_cnt = 0
    


'''
if(pb_state==1):
    if(pb_cnt == 0):
        pb_cnt = 1
        for comp in range(max_elevat,now_elevat,-(add_elevat)):
            if(danger == 0):
                for x in range(step_count):
                    GPIO.output(STEP, GPIO.HIGH)
                    sleep(delay)
                    GPIO.output(STEP, GPIO.LOW)
                    sleep(delay)
                GPIO.cleanup()
        health = 1
    else:
        for comp in range(max_elevat,now_elevat,-(add_elevat)):
            if(danger == 0):
                for x in range(step_count):
                    GPIO.output(STEP, GPIO.LOW)
                    sleep(delay)
                    GPIO.output(STEP, GPIO.HIGH)
                    sleep(delay)
                GPIO.cleanup()
        pb_cnt = 0
'''


'''
import RPi.GPIO as GPIO
from Stepper import Stepper
import Detection

health = 0
danger = Detection.safe
max_elevat = 0
now_elevat = 0
add_elevat = 0

#stepper variables
STEP = 22
DIR = 17
ENABLE = 23

testStepper = Stepper([STEP, DIR, ENABLE])

GPIO_Nbr = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_Nbr, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


if(danger == 0):
    if GPIO.input(GPIO_Nbr):
        for comp in range(max_elevat,now_elevat,-(add_elevat)):
            if(danger == 0):
                motor_steps = 3200
                testStepper.step(motor_steps, "right"); #steps, dir, speed, stayOn
                now_elevat += add_elevat
                #test stepper
        GPIO.cleanup()
        health += 1
'''