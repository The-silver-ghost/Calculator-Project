from tkinter import *
from tkinter import ttk

class GUI:
    def __init__(self,root,frame):
        self.root = root
        self.frame = frame
    
    def main_screen(self):
        self.frame.grid()
        self.root.mainloop()
    
    