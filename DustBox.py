# -*- coding: utf-8 -*-
import time
import sys
import Compression
import RPi.GPIO as GPIO

while True:
    Compression.compression()
    time.sleep(1)
    if(KeyboardInterrupt):
        GPIO.cleanup()
        sys.exit()
 