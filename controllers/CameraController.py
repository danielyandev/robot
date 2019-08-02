import Adafruit_PCA9685
import time

from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from adafruit_motor import servo

class CameraController:
    
    def __init__(self):
        self.min = 0  # Min angle
        self.center = 100
        self.max = 180  # Max angle
        self.step = 10
        self.position = self.center
        self.channel = 0
        i2c = busio.I2C(SCL, SDA)
        # Create a simple PCA9685 class instance.
        self.pca = PCA9685(i2c)
        self.pca.frequency = 50
        self.camera = servo.Servo(self.pca.channels[self.channel])        
        self.setup()

    def setup(self):
        self.position = self.center
        self.move()

    def move(self):
        self.camera.angle = self.position
        print(self.position)

    def move_left(self):
        if self.position < self.max:
            self.position += self.step
            self.move()

    def move_right(self):
        if self.position > self.min:
            self.position -= self.step
            self.move()

    def move_center(self):
        return self.setup()
