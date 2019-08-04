import RPi.GPIO as gpio
import time
import config.gpio as gpio_config


class DistanceController:
    def __init__(self):
        self.trig = gpio_config.distance_controller['trig']
        self.echo = gpio_config.distance_controller['echo']
        
    def setup(self):
        gpio.setmode(gpio.BCM)
        gpio.setup(self.trig, gpio.OUT)
        gpio.setup(self.echo, gpio.IN)
        gpio.output(self.trig, False)
        #time.sleep(1)

    def check(self, measure='cm'):
        self.setup()
        
        gpio.output(self.trig, True)
        time.sleep(0.00001)
        gpio.output(self.trig, False)
        
        while gpio.input(self.echo) == 0:
            nosig = time.time()
            
        while gpio.input(self.echo) == 1:
            sig = time.time()
            
        tl = sig - nosig
        
        distance = None
        if measure == 'cm':
            distance = tl / 0.000058
        elif measure == 'inch':
            distance = tl / 0.000148
        else:
            print('invalid measure, supported cm and inch')
        
        print(distance)
        return distance
