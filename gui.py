from tkinter import *


class GUI:
    def __init__(self,root,padding_x,padding_y):
        self.root = root
        self.padding_x = padding_x
        self.padding_y = padding_y
    
    def main_screen(self):
        #sets size for screen
        self.root.resizable(False,False)
        self.root["bg"] = "#575A5C"
        self.root.grid()
        

        #all buttons go here
        self.num_screen()
        self.buttons()

        #loops the screen until usr exit
        self.root.mainloop()
    
    def num_screen(self):
        #subject to change later
        Label(self.root,text="test",padx=10,pady=10,background="#575A5C").grid(row=0,column=1)
#need to work on the button sizes
    def buttons(self):
        Button(self.root,text="1", height=3,width=6,padx=10,pady=10).grid(row=1,column=0,padx=self.padding_x,pady=self.padding_y)
        Button(self.root,text="2", height=3,width=6,padx=10,pady=10).grid(row=1,column=1,padx=self.padding_x,pady=self.padding_y)
        Button(self.root,text="3", height=3,width=6,padx=10,pady=10).grid(row=1,column=2,padx=self.padding_x,pady=self.padding_y)
        Button(self.root,text="4", height=3,width=6,padx=10,pady=10).grid(row=2,column=0,padx=self.padding_x,pady=self.padding_y)
        Button(self.root,text="5", height=3,width=6,padx=10,pady=10).grid(row=2,column=1,padx=self.padding_x,pady=self.padding_y)
        Button(self.root,text="6", height=3,width=6,padx=10,pady=10).grid(row=2,column=2,padx=self.padding_x,pady=self.padding_y)
        Button(self.root,text="7", height=3,width=6,padx=10,pady=10).grid(row=3,column=0,padx=self.padding_x,pady=self.padding_y)
        Button(self.root,text="8", height=3,width=6,padx=10,pady=10).grid(row=3,column=1,padx=self.padding_x,pady=self.padding_y)
        Button(self.root,text="9", height=3,width=6,padx=10,pady=10).grid(row=3,column=2,padx=self.padding_x,pady=self.padding_y)
        Button(self.root,text="0", height=3,width=6,padx=10,pady=10).grid(row=4,column=0,padx=self.padding_x,pady=self.padding_y)
        Button(self.root,text="+", height=3,width=6,padx=10,pady=10).grid(row=2,column=3,padx=self.padding_x,pady=self.padding_y)
        Button(self.root,text="-", height=3,width=6,padx=10,pady=10).grid(row=2,column=4,padx=self.padding_x,pady=self.padding_y)
        Button(self.root,text="x", height=3,width=6,padx=10,pady=10).grid(row=3,column=3,padx=self.padding_x,pady=self.padding_y)
        Button(self.root,text="÷", height=3,width=6,padx=10,pady=10).grid(row=3,column=4,padx=self.padding_x,pady=self.padding_y)
        Button(self.root,text="^", height=3,width=6,padx=10,pady=10).grid(row=4,column=3,padx=self.padding_x,pady=self.padding_y)
        Button(self.root,text="(", height=3,width=6,padx=10,pady=10).grid(row=4,column=1,padx=self.padding_x,pady=self.padding_y)
        Button(self.root,text=")", height=3,width=6,padx=10,pady=10).grid(row=4,column=2,padx=self.padding_x,pady=self.padding_y)
        Button(self.root,text="=", height=3,width=6,padx=10,pady=10).grid(row=4,column=4,padx=self.padding_x,pady=self.padding_y)
        Button(self.root,text="C", height=3,width=6,padx=10,pady=10).grid(row=1,column=4,padx=self.padding_x,pady=self.padding_y)
        Button(self.root,text=".", height=3,width=6,padx=10,pady=10).grid(row=1,column=3,padx=self.padding_x,pady=self.padding_y)