from controllers.CameraController import CameraController
from controllers.MotorController import MotorController


class KeyController:

    def __init__(self):
        self.motor_controller = MotorController()
        self.camera_controller = CameraController()
        
    def key_pressed(self, e):
        char = e.char.lower()
        if char == 'w':
            self.motor_controller.forward()
        elif char == 's':
            self.motor_controller.reverse()
        elif char == 'a':
            self.motor_controller.turn_left()
        elif char == 'd':
            self.motor_controller.turn_right()
        elif char == 'q':
            self.motor_controller.pivot_left()
        elif char == 'e':
            self.motor_controller.pivot_right()
        elif char == 'z':
            self.camera_controller.move_left()
        elif char == 'x':
            self.camera_controller.move_center()
        elif char == 'c':
            self.camera_controller.move_right()
        else:
            pass
