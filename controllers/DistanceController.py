import RPi.GPIO as gpio
import time
import config.gpio as gpio_config
import threading


class DistanceController:
    def __init__(self):
        self.trig = gpio_config.distance_controller['trig']
        self.echo = gpio_config.distance_controller['echo']
        self.distance = 0
        self.set_interval(self.set_distance, 0.5)
        
    def setup(self):
        # gpio.setmode(gpio.BCM)
        # gpio.setup(self.trig, gpio.OUT)
        # gpio.setup(self.echo, gpio.IN)
        gpio.output(self.trig, False)
        time.sleep(0.5)


    def check(self, measure='cm'):
        self.setup()
        
        gpio.output(self.trig, True)
        # Wait 10us
        time.sleep(0.00001)
        gpio.output(self.trig, False)
        nosig = time.time()
        sig = 0
            
        while gpio.input(self.echo) == 0:
            nosig = time.time()
        
        
        while gpio.input(self.echo) == 1:
            sig = time.time()
            
        tl = sig - nosig
        
        distance = None
        if measure == 'cm':
            distance = round(tl / 0.000058)
        elif measure == 'inch':
            distance = round(tl / 0.000148)
        else:
            print('invalid measure, supported cm and inch')
        
        print(distance)
        return distance
        
    def set_interval(self, func, sec):
        def func_wrapper():
            self.set_interval(func, sec)
            func()
        t = threading.Timer(sec, func_wrapper)
        t.start()
        return t

    def set_distance(self):
        self.distance = self.check()
            

