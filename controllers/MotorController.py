import RPi.GPIO as gpio
import time
import config.gpio as gpio_config
from controllers.DistanceController import DistanceController


class MotorController:

    def __init__(self):
        self.tf = 0.03
        self.pin1 = gpio_config.motor_controller['pin1']
        self.pin2 = gpio_config.motor_controller['pin2']
        self.pin3 = gpio_config.motor_controller['pin3']
        self.pin4 = gpio_config.motor_controller['pin4']
        self.distance_controller = DistanceController()

    def setup(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(self.pin1, gpio.OUT)
        gpio.setup(self.pin2, gpio.OUT)
        gpio.setup(self.pin3, gpio.OUT)
        gpio.setup(self.pin4, gpio.OUT)

    def cleanup(self):
        gpio.cleanup()

    def output(self, pin, status):
        gpio.output(pin, status)


    def forward(self):
        if self.distance_controller.distance < 20:
            self.stop()
            return False
        self.output(self.pin1, False)
        self.output(self.pin2, True)
        self.output(self.pin3, True)
        self.output(self.pin4, False)
        time.sleep(self.tf)
        self.stop()

    def reverse(self):
        self.output(self.pin1, True)
        self.output(self.pin2, False)
        self.output(self.pin3, False)
        self.output(self.pin4, True)
        time.sleep(self.tf)
        self.stop()

    def turn_left(self):
        self.output(self.pin1, False)
        self.output(self.pin2, True)
        self.output(self.pin3, False)
        self.output(self.pin4, False)
        time.sleep(self.tf)
        self.stop()

    def turn_right(self):
        self.output(self.pin1, True)
        self.output(self.pin2, True)
        self.output(self.pin3, True)
        self.output(self.pin4, False)
        time.sleep(self.tf)
        self.stop()

    def pivot_left(self):
        self.output(self.pin1, False)
        self.output(self.pin2, True)
        self.output(self.pin3, False)
        self.output(self.pin4, True)
        time.sleep(self.tf)
        self.stop()

    def pivot_right(self):
        self.output(self.pin1, True)
        self.output(self.pin2, False)
        self.output(self.pin3, True)
        self.output(self.pin4, False)
        time.sleep(self.tf)
        self.stop()
        
    def stop(self):
        gpio.output(self.pin1,  False)
        gpio.output(self.pin2, False)
        gpio.output(self.pin3, False)
        gpio.output(self.pin4, False)
