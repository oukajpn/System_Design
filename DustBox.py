# -*- coding: utf-8 -*-
import time
import sys
import Compression
import RPi.GPIO as GPIO

DIR = 20
STEP = 21
btn1 = 6

Compression.setup(DIR,STEP,btn1)

while True:
    Compression.compression()
    time.sleep(1)
    if(KeyboardInterrupt):
        GPIO.cleanup()
        sys.exit()
 