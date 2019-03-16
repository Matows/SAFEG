#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

class Motor:
    def __init__(self, out={"int1":31,"int2":29,"ena":33}, freq=1000, dc=100):
        self.out = out

        GPIO.setmode(GPIO.BOARD)
        for pin in out.values():
            GPIO.setup(pin, GPIO.OUT)

        self._pwm = GPIO.PWM(self.out["ena"], freq)
        self._pwm.start(dc)
    
    def forward(self):
        GPIO.output(self.out["int1"], GPIO.HIGH)
        GPIO.output(self.out["int2"], GPIO.LOW)

    def reverse(self):
        GPIO.output(self.out["int1"], GPIO.LOW)
        GPIO.output(self.out["int2"], GPIO.HIGH)

    def stop(self):
        GPIO.output(self.out["int1"], GPIO.LOW)
        GPIO.output(self.out["int2"], GPIO.LOW)

    def dc():
        
        def fget(self):
            return self._dc

        def fset(self, newDutyCycle):
            if newDutyCycle < 1 or newDutyCycle > 100 or type(newDutyCycle) != int:
                raise ValueError("Bad value")

            GPIO.output(self.out["ena"], newDutyCycle)
            self._dc = newDutyCycle
        
        return locals()
    dc = property(**dc())

    def freq():

        def fget(self):
            return self._freq

        def fset(self, newFrecuency):
            GPIO.output(self.out["ena"], newFrecuency)
            self._freq = newFrecuency

        return locals()
    freq = property(**freq())

    def __del__(self):
        self._pwm.stop()
        GPIO.cleanup()
        print("stoped and cleaned up")
