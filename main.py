from controllers.KeyController import KeyController
from ui.TkinterUi import TkinterUi
from ui.WebUi import WebUi
import RPi.GPIO as gpio


def run_web():
    ui = WebUi()
    ui.serve()


def run_tkinter():
    kc = KeyController()
    ui = TkinterUi()
    ui.root.bind("<KeyPress>", kc.key_pressed)
    ui.loop()


#run_tkinter()
run_web()
