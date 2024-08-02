from tkinter import *



class GUI:
    def __init__(self,root,padding_x,padding_y,question_string):
        self.root = root
        self.padding_x = padding_x
        self.padding_y = padding_y
        self.question_string = question_string
    
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
        questionLabel = Label(self.root,textvariable=self.question_string,padx=10,pady=10)
        questionLabel.grid(row=0,column=0,padx=self.padding_x,pady=self.padding_y,columnspan=6)

        answerLabel = Label(self.root,text=answer_string,padx=10,pady=10)
        answerLabel.grid(row=1,column=0,padx=self.padding_x,pady=self.padding_y,columnspan=6)

    def buttons(self):
        buttonOne = Button(self.root,text="1", command=lambda: self.text_from_button("1"),height=3,width=6,padx=10,pady=10)
        buttonOne.grid(row=2,column=0,padx=self.padding_x,pady=self.padding_y)
        self.txt = buttonOne.cget('text')

        buttonTwo = Button(self.root,text="2", command=lambda: self.text_from_button("2"),height=3,width=6,padx=10,pady=10)
        buttonTwo.grid(row=2,column=1,padx=self.padding_x,pady=self.padding_y)

        buttonThree = Button(self.root,text="3", command=lambda: self.text_from_button("3"),height=3,width=6,padx=10,pady=10)
        buttonThree.grid(row=2,column=2,padx=self.padding_x,pady=self.padding_y)

        buttonFour = Button(self.root,text="4", command=lambda: self.text_from_button("4"),height=3,width=6,padx=10,pady=10)
        buttonFour.grid(row=3,column=0,padx=self.padding_x,pady=self.padding_y)

        buttonFive = Button(self.root,text="5", command=lambda: self.text_from_button("5"),height=3,width=6,padx=10,pady=10)
        buttonFive.grid(row=3,column=1,padx=self.padding_x,pady=self.padding_y)

        buttonSix = Button(self.root,text="6", command=lambda: self.text_from_button("6"),height=3,width=6,padx=10,pady=10)
        buttonSix.grid(row=3,column=2,padx=self.padding_x,pady=self.padding_y)

        buttonSeven = Button(self.root,text="7", command=lambda: self.text_from_button("7"),height=3,width=6,padx=10,pady=10)
        buttonSeven.grid(row=4,column=0,padx=self.padding_x,pady=self.padding_y)

        buttonEight = Button(self.root,text="8", command=lambda: self.text_from_button("8"),height=3,width=6,padx=10,pady=10)
        buttonEight.grid(row=4,column=1,padx=self.padding_x,pady=self.padding_y)

        buttonNine = Button(self.root,text="9", command=lambda: self.text_from_button("9"),height=3,width=6,padx=10,pady=10)
        buttonNine.grid(row=4,column=2,padx=self.padding_x,pady=self.padding_y)

        buttonZero = Button(self.root,text="0", command=lambda: self.text_from_button("0"),height=3,width=6,padx=10,pady=10)
        buttonZero.grid(row=5,column=0,padx=self.padding_x,pady=self.padding_y)

        buttonAddition = Button(self.root,text="+", command=lambda: self.text_from_button("+"),height=3,width=6,padx=10,pady=10)
        buttonAddition.grid(row=3,column=3,padx=self.padding_x,pady=self.padding_y)

        buttonSubtraction = Button(self.root,text="-", command=lambda: self.text_from_button("-"),height=3,width=6,padx=10,pady=10)
        buttonSubtraction.grid(row=3,column=4,padx=self.padding_x,pady=self.padding_y)

        buttonMultiplication = Button(self.root,text="x", command=lambda: self.text_from_button("x"),height=3,width=6,padx=10,pady=10)
        buttonMultiplication.grid(row=4,column=3,padx=self.padding_x,pady=self.padding_y)

        buttonDivision = Button(self.root,text="÷", command=lambda: self.text_from_button("÷"),height=3,width=6,padx=10,pady=10)
        buttonDivision.grid(row=4,column=4,padx=self.padding_x,pady=self.padding_y)

        buttonPower = Button(self.root,text="^", command=lambda: self.text_from_button("^"),height=3,width=6,padx=10,pady=10)
        buttonPower.grid(row=5,column=3,padx=self.padding_x,pady=self.padding_y)

        buttonLeftParenthesis = Button(self.root,text="(", command=lambda: self.text_from_button("("),height=3,width=6,padx=10,pady=10)
        buttonLeftParenthesis.grid(row=5,column=1,padx=self.padding_x,pady=self.padding_y)

        buttonRightParenthesis = Button(self.root,text=")", command=lambda: self.text_from_button(")"),height=3,width=6,padx=10,pady=10)
        buttonRightParenthesis.grid(row=5,column=2,padx=self.padding_x,pady=self.padding_y)

        buttonEqual = Button(self.root,text="=", height=3,width=6,padx=10,pady=10)
        buttonEqual.grid(row=5,column=4,padx=self.padding_x,pady=self.padding_y)

        buttonClear = Button(self.root,text="C", command = self.clear_button,height=3,width=6,padx=10,pady=10)
        buttonClear.grid(row=2,column=4,padx=self.padding_x,pady=self.padding_y)

        buttonDecimal = Button(self.root,text=".", command=lambda: self.text_from_button("."),height=3,width=6,padx=10,pady=10)
        buttonDecimal.grid(row=2,column=3,padx=self.padding_x,pady=self.padding_y)
    
    def text_from_button(self,txt):
        global question_string_label
        question_string_label += txt
        self.question_string.set(question_string_label)
    
    def clear_button(self):
        global question_string_label
        question_string_label = ""
        self.question_string.set(question_string_label)

question_string_label = ''
answer_string = ""