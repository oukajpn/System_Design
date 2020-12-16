from time import sleep
import RPi.GPIO as GPIO

direction = 20
step = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(direction, GPIO.OUT)
GPIO.setup(step, GPIO.OUT)
GPIO.output(direction, 1)

step_count = 5000
delay = .001

for x in range(step_count):
	GPIO.output(step, GPIO.HIGH)
	sleep(delay)
	GPIO.output(step, GPIO.LOW)
	sleep(delay)

GPIO.cleanup()