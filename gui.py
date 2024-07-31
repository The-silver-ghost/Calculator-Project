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
        Label(self.root,text="test",padx=10,pady=10,background="#575A5C").grid(row=0,column=1)

    def buttons(self):
        buttonOne = Button(self.root,text="1", height=3,width=6,padx=10,pady=10)
        buttonOne.grid(row=1,column=0,padx=self.padding_x,pady=self.padding_y)

        buttonTwo = Button(self.root,text="2", height=3,width=6,padx=10,pady=10)
        buttonTwo.grid(row=1,column=1,padx=self.padding_x,pady=self.padding_y)

        buttonThree = Button(self.root,text="3", height=3,width=6,padx=10,pady=10)
        buttonThree.grid(row=1,column=2,padx=self.padding_x,pady=self.padding_y)

        buttonFour = Button(self.root,text="4", height=3,width=6,padx=10,pady=10)
        buttonFour.grid(row=2,column=0,padx=self.padding_x,pady=self.padding_y)

        buttonFive = Button(self.root,text="5", height=3,width=6,padx=10,pady=10)
        buttonFive.grid(row=2,column=1,padx=self.padding_x,pady=self.padding_y)

        buttonSix = Button(self.root,text="6", height=3,width=6,padx=10,pady=10)
        buttonSix.grid(row=2,column=2,padx=self.padding_x,pady=self.padding_y)

        buttonSeven = Button(self.root,text="7", height=3,width=6,padx=10,pady=10)
        buttonSeven.grid(row=3,column=0,padx=self.padding_x,pady=self.padding_y)

        buttonEight = Button(self.root,text="8", height=3,width=6,padx=10,pady=10)
        buttonEight.grid(row=3,column=1,padx=self.padding_x,pady=self.padding_y)

        buttonNine = Button(self.root,text="9", height=3,width=6,padx=10,pady=10)
        buttonNine.grid(row=3,column=2,padx=self.padding_x,pady=self.padding_y)

        buttonZero = Button(self.root,text="0", height=3,width=6,padx=10,pady=10)
        buttonZero.grid(row=4,column=0,padx=self.padding_x,pady=self.padding_y)

        buttonAddition = Button(self.root,text="+", height=3,width=6,padx=10,pady=10)
        buttonAddition.grid(row=2,column=3,padx=self.padding_x,pady=self.padding_y)

        buttonSubtraction = Button(self.root,text="-", height=3,width=6,padx=10,pady=10)
        buttonSubtraction.grid(row=2,column=4,padx=self.padding_x,pady=self.padding_y)

        buttonMultiplication = Button(self.root,text="x", height=3,width=6,padx=10,pady=10)
        buttonMultiplication.grid(row=3,column=3,padx=self.padding_x,pady=self.padding_y)

        buttonDivision = Button(self.root,text="÷", height=3,width=6,padx=10,pady=10)
        buttonDivision.grid(row=3,column=4,padx=self.padding_x,pady=self.padding_y)

        buttonPower = Button(self.root,text="^", height=3,width=6,padx=10,pady=10)
        buttonPower.grid(row=4,column=3,padx=self.padding_x,pady=self.padding_y)

        buttonLeftParenthesis = Button(self.root,text="(", height=3,width=6,padx=10,pady=10)
        buttonLeftParenthesis.grid(row=4,column=1,padx=self.padding_x,pady=self.padding_y)

        buttonRightParenthesis = Button(self.root,text=")", height=3,width=6,padx=10,pady=10)
        buttonRightParenthesis.grid(row=4,column=2,padx=self.padding_x,pady=self.padding_y)

        buttonEqual = Button(self.root,text="=", height=3,width=6,padx=10,pady=10)
        buttonEqual.grid(row=4,column=4,padx=self.padding_x,pady=self.padding_y)

        buttonClear = Button(self.root,text="C", height=3,width=6,padx=10,pady=10)
        buttonClear.grid(row=1,column=4,padx=self.padding_x,pady=self.padding_y)

        buttonDecimal = Button(self.root,text=".", height=3,width=6,padx=10,pady=10)
        buttonDecimal.grid(row=1,column=3,padx=self.padding_x,pady=self.padding_y)
