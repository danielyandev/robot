import RPi.GPIO as gpio
import time


class MotorController:

    def __init__(self):
        self.tf = 0.03
        self.in1 = 7
        self.in2 = 11
        self.in3 = 13
        self.in4 = 15

    def setup(self):
        gpio.setmode(gpio.BOARD)
        gpio.setup(self.in1, gpio.OUT)
        gpio.setup(self.in2, gpio.OUT)
        gpio.setup(self.in3, gpio.OUT)
        gpio.setup(self.in4, gpio.OUT)

    def cleanup(self):
        gpio.cleanup()
        print('cleaned up');

    def output(self, pin, status):
        gpio.output(pin, status)

    def forward(self):
        self.setup()
        self.output(self.in1, False)
        self.output(self.in2, True)
        self.output(self.in3, True)
        self.output(self.in4, False)
        time.sleep(self.tf)
        self.cleanup()

    def reverse(self):
        self.setup()
        self.output(self.in1, True)
        self.output(self.in2, False)
        self.output(self.in3, False)
        self.output(self.in4, True)
        time.sleep(self.tf)
        self.cleanup()

    def turn_left(self):
        self.setup()
        self.output(self.in1, False)
        self.output(self.in2, True)
        self.output(self.in3, False)
        self.output(self.in4, False)
        time.sleep(self.tf)
        self.cleanup()

    def turn_right(self):
        self.setup()
        self.output(self.in1, True)
        self.output(self.in2, True)
        self.output(self.in3, True)
        self.output(self.in4, False)
        time.sleep(self.tf)
        self.cleanup()

    def pivot_left(self):
        self.setup()
        self.output(self.in1, False)
        self.output(self.in2, True)
        self.output(self.in3, False)
        self.output(self.in4, True)
        time.sleep(self.tf)
        self.cleanup()

    def pivot_right(self):
        self.setup()
        self.output(self.in1, True)
        self.output(self.in2, False)
        self.output(self.in3, True)
        self.output(self.in4, False)
        time.sleep(self.tf)
        self.cleanup()
