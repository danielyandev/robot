from controllers.KeyController import KeyController
from ui.TkinterUi import TkinterUi
from ui.WebUi import WebUi

def runWeb():
    ui = WebUi()
    ui.serve()
    
def runTkinter():
    kc = KeyController()
    ui = TkinterUi()
    ui.root.bind("<KeyPress>", kc.key_pressed)
    ui.loop()
    
runTkinter()

