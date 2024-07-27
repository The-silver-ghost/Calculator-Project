from tkinter import *
from tkinter import ttk

class GUI:
    def __init__(self,root,frame,padding_x,padding_y):
        self.root = root
        self.frame = frame
        self.padding_x = padding_x
        self.padding_y = padding_y
    
    def main_screen(self):
        #sets size for screen
        self.root.resizable(False,False)
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
        self.button_addition()
        self.button_subtraction()
        self.button_multiplication()
        self.button_division()
        self.button_power()
        self.button_left_parenthesis()
        self.button_right_parenthesis()
        self.button_equal()
        self.button_clear()
        self.button_decimal()

        #loops the screen until usr exit
        self.root.mainloop()
    
    def num_screen(self):
        #subject to change later
        Label(self.frame,text="test",padx=10,pady=10).grid(row=0,column=1)
#need to work on the button sizes
    def button_1(self):
        Button(self.frame,text="1", height=3,width=6,padx=10,pady=10).grid(row=1,column=0,padx=self.padding_x,pady=self.padding_y)
    
    def button_2(self):
        Button(self.frame,text="2", height=3,width=6,padx=10,pady=10).grid(row=1,column=1,padx=self.padding_x,pady=self.padding_y)
    
    def button_3(self):
        Button(self.frame,text="3", height=3,width=6,padx=10,pady=10).grid(row=1,column=2,padx=self.padding_x,pady=self.padding_y)
    
    def button_4(self):
        Button(self.frame,text="4", height=3,width=6,padx=10,pady=10).grid(row=2,column=0,padx=self.padding_x,pady=self.padding_y)
    
    def button_5(self):
        Button(self.frame,text="5", height=3,width=6,padx=10,pady=10).grid(row=2,column=1,padx=self.padding_x,pady=self.padding_y)
    
    def button_6(self):
        Button(self.frame,text="6", height=3,width=6,padx=10,pady=10).grid(row=2,column=2,padx=self.padding_x,pady=self.padding_y)
    
    def button_7(self):
        Button(self.frame,text="7", height=3,width=6,padx=10,pady=10).grid(row=3,column=0,padx=self.padding_x,pady=self.padding_y)
    
    def button_8(self):
        Button(self.frame,text="8", height=3,width=6,padx=10,pady=10).grid(row=3,column=1,padx=self.padding_x,pady=self.padding_y)
    
    def button_9(self):
        Button(self.frame,text="9", height=3,width=6,padx=10,pady=10).grid(row=3,column=2,padx=self.padding_x,pady=self.padding_y)
    
    def button_0(self):
        Button(self.frame,text="0", height=3,width=6,padx=10,pady=10).grid(row=4,column=0,padx=self.padding_x,pady=self.padding_y)
    
    def button_addition(self):
        Button(self.frame,text="+", height=3,width=6,padx=10,pady=10).grid(row=2,column=3,padx=self.padding_x,pady=self.padding_y)
    
    def button_subtraction(self):
        Button(self.frame,text="-", height=3,width=6,padx=10,pady=10).grid(row=2,column=4,padx=self.padding_x,pady=self.padding_y)
    
    def button_multiplication(self):
        Button(self.frame,text="x", height=3,width=6,padx=10,pady=10).grid(row=3,column=3,padx=self.padding_x,pady=self.padding_y)
    
    def button_division(self):
        Button(self.frame,text="÷", height=3,width=6,padx=10,pady=10).grid(row=3,column=4,padx=self.padding_x,pady=self.padding_y)
    
    def button_power(self):
        Button(self.frame,text="^", height=3,width=6,padx=10,pady=10).grid(row=4,column=3,padx=self.padding_x,pady=self.padding_y)
    
    def button_left_parenthesis(self):
        Button(self.frame,text="(", height=3,width=6,padx=10,pady=10).grid(row=4,column=1,padx=self.padding_x,pady=self.padding_y)
    
    def button_right_parenthesis(self):
        Button(self.frame,text=")", height=3,width=6,padx=10,pady=10).grid(row=4,column=2,padx=self.padding_x,pady=self.padding_y)
    
    def button_equal(self):
        Button(self.frame,text="=", height=3,width=6,padx=10,pady=10).grid(row=4,column=4,padx=self.padding_x,pady=self.padding_y)
    
    def button_clear(self):
        Button(self.frame,text="C", height=3,width=6,padx=10,pady=10).grid(row=1,column=4,padx=self.padding_x,pady=self.padding_y)
    
    def button_decimal(self):
        Button(self.frame,text=".", height=3,width=6,padx=10,pady=10).grid(row=1,column=3,padx=self.padding_x,pady=self.padding_y)