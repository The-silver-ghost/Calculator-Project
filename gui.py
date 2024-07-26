from tkinter import *
from tkinter import ttk

class GUI:
    def __init__(self,root,frame):
        self.root = root
        self.frame = frame
    
    def main_screen(self):
        #sets size for screen
        self.frame.grid()

#all buttons go here
        self.num_screen()
        self.button_1()
        self.button_2()
        self.button_3()
        self.button_4()
        self.button_5()
        self.button_6()
        self.button_7()
        self.button_8()
        self.button_9()
        self.button_0()

#loops the screen until usr exit
        self.root.mainloop()
    
    def num_screen(self):
        #subject to change later
        ttk.Entry(self.frame).grid(row=0,column=1)
#need to work on the button sizes
    def button_1(self):
        ttk.Button(self.frame,text="1").grid(row=1,column=0)
    
    def button_2(self):
        ttk.Button(self.frame,text="2").grid(row=1,column=1)
    
    def button_3(self):
        ttk.Button(self.frame,text="3").grid(row=1,column=2)
    
    def button_4(self):
        ttk.Button(self.frame,text="4").grid(row=2,column=0)
    
    def button_5(self):
        ttk.Button(self.frame,text="5").grid(row=2,column=1)
    
    def button_6(self):
        ttk.Button(self.frame,text="6").grid(row=2,column=2)
    
    def button_7(self):
        ttk.Button(self.frame,text="7").grid(row=3,column=0)
    
    def button_8(self):
        ttk.Button(self.frame,text="8").grid(row=3,column=1)
    
    def button_9(self):
        ttk.Button(self.frame,text="9").grid(row=3,column=2)
    
    def button_0(self):
        ttk.Button(self.frame,text="0").grid(row=4,column=1)
    