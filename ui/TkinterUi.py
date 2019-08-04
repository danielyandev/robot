from tkinter import *
from PIL import ImageTk, Image
import cv2


class TkinterUi:

    def __init__(self):
        self.root = Tk()
        self.root.geometry("250x250")
        # Create a frame
        self.app = Frame(self.root, bg="white")
        self.app.grid()
        # Create a label in the frame
        self.lmain = Label(self.app)
        self.lmain.grid()
        # Capture from camera
        self.cap = cv2.VideoCapture(0)

    # function for video streaming
    def video_stream(self):
        _, frame = self.cap.read()
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)
        self.lmain.after(1, self.video_stream)

    def loop(self):
        #self.video_stream()
        self.root.mainloop()
