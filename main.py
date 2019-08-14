from controllers.KeyController import KeyController
from ui.TkinterUi import TkinterUi
from ui.WebUi import WebUi
import RPi.GPIO as gpio
import config.gpio as gpio_config


def setup_gpio():
    gpio.setmode(gpio.BCM)
    # motor controller
    gpio.setup(gpio_config.motor_controller['pin1'], gpio.OUT)
    gpio.setup(gpio_config.motor_controller['pin2'], gpio.OUT)
    gpio.setup(gpio_config.motor_controller['pin3'], gpio.OUT)
    gpio.setup(gpio_config.motor_controller['pin4'], gpio.OUT)

    # distance controller
    gpio.setup(gpio_config.distance_controller['trig'], gpio.OUT)
    gpio.setup(gpio_config.distance_controller['echo'], gpio.IN)


def run_web():
    ui = WebUi()
    ui.serve()


def run_tkinter():
    kc = KeyController()
    ui = TkinterUi()
    ui.root.bind("<KeyPress>", kc.key_pressed)
    ui.loop()
    gpio.cleanup()


#run_tkinter()
run_web()
