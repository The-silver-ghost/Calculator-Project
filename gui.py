from tkinter import *
import math_functions

question_string_label = ' '
answer_string_label = " "

class GUI:
    def __init__(self,root,padding_x,padding_y,question_string,answer_string,font_specification):
        self.root = root
        self.padding_x = padding_x
        self.padding_y = padding_y
        self.question_string = question_string
        self.answer_string = answer_string
        self.font_specification = font_specification
    
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

        answerLabel = Label(self.root,textvariable=self.answer_string,padx=10,pady=10)
        answerLabel.grid(row=1,column=0,padx=self.padding_x,pady=self.padding_y,columnspan=6)

    def buttons(self):
        buttonOne = Button(self.root,text="1", command=lambda: self.text_from_button("1"),height=3,width=6,padx=10,pady=10,font=self.font_specification)
        buttonOne.grid(row=2,column=0,padx=self.padding_x,pady=self.padding_y)
        self.txt = buttonOne.cget('text')

        buttonTwo = Button(self.root,text="2", command=lambda: self.text_from_button("2"),height=3,width=6,padx=10,pady=10,font=self.font_specification)
        buttonTwo.grid(row=2,column=1,padx=self.padding_x,pady=self.padding_y)

        buttonThree = Button(self.root,text="3", command=lambda: self.text_from_button("3"),height=3,width=6,padx=10,pady=10,font=self.font_specification)
        buttonThree.grid(row=2,column=2,padx=self.padding_x,pady=self.padding_y)

        buttonFour = Button(self.root,text="4", command=lambda: self.text_from_button("4"),height=3,width=6,padx=10,pady=10,font=self.font_specification)
        buttonFour.grid(row=3,column=0,padx=self.padding_x,pady=self.padding_y)

        buttonFive = Button(self.root,text="5", command=lambda: self.text_from_button("5"),height=3,width=6,padx=10,pady=10,font=self.font_specification)
        buttonFive.grid(row=3,column=1,padx=self.padding_x,pady=self.padding_y)

        buttonSix = Button(self.root,text="6", command=lambda: self.text_from_button("6"),height=3,width=6,padx=10,pady=10,font=self.font_specification)
        buttonSix.grid(row=3,column=2,padx=self.padding_x,pady=self.padding_y)

        buttonSeven = Button(self.root,text="7", command=lambda: self.text_from_button("7"),height=3,width=6,padx=10,pady=10,font=self.font_specification)
        buttonSeven.grid(row=4,column=0,padx=self.padding_x,pady=self.padding_y)

        buttonEight = Button(self.root,text="8", command=lambda: self.text_from_button("8"),height=3,width=6,padx=10,pady=10,font=self.font_specification)
        buttonEight.grid(row=4,column=1,padx=self.padding_x,pady=self.padding_y)

        buttonNine = Button(self.root,text="9", command=lambda: self.text_from_button("9"),height=3,width=6,padx=10,pady=10,font=self.font_specification)
        buttonNine.grid(row=4,column=2,padx=self.padding_x,pady=self.padding_y)

        buttonZero = Button(self.root,text="0", command=lambda: self.text_from_button("0"),height=3,width=6,padx=10,pady=10,font=self.font_specification)
        buttonZero.grid(row=5,column=0,padx=self.padding_x,pady=self.padding_y)

        buttonAddition = Button(self.root,text="+", command=lambda: self.text_from_button("+"),height=3,width=6,padx=10,pady=10,font=self.font_specification)
        buttonAddition.grid(row=3,column=3,padx=self.padding_x,pady=self.padding_y)

        buttonSubtraction = Button(self.root,text="-", command=lambda: self.text_from_button("-"),height=3,width=6,padx=10,pady=10,font=self.font_specification)
        buttonSubtraction.grid(row=3,column=4,padx=self.padding_x,pady=self.padding_y)

        buttonMultiplication = Button(self.root,text="x", command=lambda: self.text_from_button("x"),height=3,width=6,padx=10,pady=10,font=self.font_specification)
        buttonMultiplication.grid(row=4,column=3,padx=self.padding_x,pady=self.padding_y)

        buttonDivision = Button(self.root,text="÷", command=lambda: self.text_from_button("÷"),height=3,width=6,padx=10,pady=10,font=self.font_specification)
        buttonDivision.grid(row=4,column=4,padx=self.padding_x,pady=self.padding_y)

        buttonPower = Button(self.root,text="^", command=lambda: self.text_from_button("^"),height=3,width=6,padx=10,pady=10,font=self.font_specification)
        buttonPower.grid(row=5,column=3,padx=self.padding_x,pady=self.padding_y)

        buttonLeftParenthesis = Button(self.root,text="(", command=lambda: self.text_from_button("("),height=3,width=6,padx=10,pady=10,font=self.font_specification)
        buttonLeftParenthesis.grid(row=5,column=1,padx=self.padding_x,pady=self.padding_y)

        buttonRightParenthesis = Button(self.root,text=")", command=lambda: self.text_from_button(")"),height=3,width=6,padx=10,pady=10,font=self.font_specification)
        buttonRightParenthesis.grid(row=5,column=2,padx=self.padding_x,pady=self.padding_y)

        buttonEqual = Button(self.root,text="=", command=self.equal_button_function,height=3,width=6,padx=10,pady=10,font=self.font_specification)
        buttonEqual.grid(row=5,column=4,padx=self.padding_x,pady=self.padding_y)

        buttonClear = Button(self.root,text="C", command = self.clear_button_function,height=3,width=6,padx=10,pady=10,font=self.font_specification)
        buttonClear.grid(row=2,column=4,padx=self.padding_x,pady=self.padding_y)

        buttonDecimal = Button(self.root,text=".", command=lambda: self.text_from_button("."),height=3,width=6,padx=10,pady=10,font=self.font_specification)
        buttonDecimal.grid(row=2,column=3,padx=self.padding_x,pady=self.padding_y)
    
    def text_from_button(self,txt):
        global question_string_label
        if question_string_label[-1] == "x" and txt == "x":
            question_string_label += ""
        elif question_string_label[-1] == "÷" and txt == '÷':
            question_string_label += ""
        else:
            question_string_label += txt
        self.question_string.set(question_string_label)
    
    def clear_button_function(self):
        global question_string_label
        global answer_string_label
        question_string_label = " "
        self.question_string.set(question_string_label)
        answer_string_label = " "
        self.answer_string.set(answer_string_label)
    
    def equal_button_function(self):
        self.string_for_calc = self.question_string.get()
        global answer_string_label
        global question_string_label
        for symbol in self.string_for_calc:
            if symbol == "^":
                answer_string_label += "**"
            elif symbol == "÷":
                answer_string_label += "/"
            elif symbol == "x":
                answer_string_label += "*"
            else:
                answer_string_label += symbol
        try:
            answer = math_functions.regular_calc(answer_string_label)
            self.answer_string.set(answer)
        except SyntaxError:
            self.answer_string.set("Syntax Error")
        except ZeroDivisionError:
            self.answer_string.set("Math Error: Division by 0")
        except TypeError:
            self.answer_string.set("Brackets are not counted as multiplication")
        
        answer_string_label = ' '