#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep


class Motor:
    def __init__(self, controlPins, freq=1000, dc=100):
        self.controlPins = controlPins
        self._freq = freq
        self._dc = dc
        print(controlPins)

        GPIO.setmode(GPIO.BOARD)
        for pin in controlPins.values():
            GPIO.setup(pin, GPIO.OUT)
        self.stop()

        self._pwm = GPIO.PWM(self.controlPins["pwm"], freq)
        self._pwm.start(dc)
    
    def forward(self):
        GPIO.output(self.controlPins["int1"], GPIO.HIGH)
        GPIO.output(self.controlPins["int2"], GPIO.LOW)

    def reverse(self):
        GPIO.output(self.controlPins["int1"], GPIO.LOW)
        GPIO.output(self.controlPins["int2"], GPIO.HIGH)

    def stop(self):
        GPIO.output(self.controlPins["int1"], GPIO.LOW)
        GPIO.output(self.controlPins["int2"], GPIO.LOW)

    def dc():
        
        def fget(self):
            return self._dc

        def fset(self, newDutyCycle):
            if newDutyCycle < 1 or newDutyCycle > 100 or type(newDutyCycle) != int:
                raise ValueError("Bad value")

            print("DC reset")
            self._pwm.ChangeDutyCycle(newDutyCycle)
            self._dc = newDutyCycle
        
        return locals()
    dc = property(**dc())

    def freq():

        def fget(self):
            return self._freq

        def fset(self, newFrecuency):
            self._pwm.ChangeFrequency(newFrecuency)
            self._freq = newFrecuency

        return locals()
    freq = property(**freq())

    def __del__(self):
        self._pwm.stop()
        GPIO.cleanup()
        print("stoped and cleaned up")

class Door(Motor):
    def __init__(self, controlPins):
        Motor.__init__(self, controlPins)

    def open(self):
        self.forward()
        sleep(2)
        self.stop()

    def close(self):
        self.reverse()
        sleep(2)
        self.stop()

motor1 = {"int1": 31,"int2": 29,"pwm": 33}
motor2 = {"int1": 11,"int2": 13,"pwm": 12}
