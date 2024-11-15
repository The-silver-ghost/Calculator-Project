from tkinter import *
from tkinter import ttk
import ttkthemes
import Calculator.math_functions as math_functions

question_string_label = ' '
answer_string_label = " "
answer_button_var = ' '
quadratic_question_string_label = " "
quadratic_answer_string_label = " "
count = 0
num_list = []

class GUI:
    def __init__(self,root,padding_x,padding_y,question_string,answer_string,calc_tab,tabs,quadratic_tab,frame,question_string_quadratic,answer_string_quadratic,quadratic_string):
        self.root = root
        self.padding_x = padding_x
        self.padding_y = padding_y
        self.question_string = question_string
        self.answer_string = answer_string
        self.calc_tab = calc_tab
        self.tabs = tabs
        self.quadratic_tab = quadratic_tab
        self.frame = frame
        self.question_string_quadratic = question_string_quadratic
        self.answer_string_quadratic = answer_string_quadratic
        self.quadratic_string = quadratic_string

    def main_screen(self):
        #sets size for screen
        self.root.resizable(False,False)
        self.frame.grid()
        
        self.tabs.add(self.calc_tab, text = "Calculator")
        style = ttkthemes.ThemedStyle()
        style.theme_use("black")
        style.configure("TButton",font="Bodoni",padding=9,width=6,anchor="center")
        style.map("TButton",background=[("active","red")])
        style.configure("TLabel", font="Bodoni")
        self.tabs.grid(row=0,column=0)

        self.tabs.add(self.quadratic_tab, text = "Quadratic Eq")
        self.tabs.grid(row=0,column=1)
        

        #all buttons go here
        self.num_screen()
        self.buttons_calc_tab()
        self.num_screen_quadratic()
        self.equal_button_function_quadratic()
        self.buttons_quadratic_tab()


        #loops the screen until usr exit
        self.root.mainloop()
    
    def num_screen(self):
        questionLabel = ttk.Label(self.calc_tab,textvariable=self.question_string)
        questionLabel.grid(row=1,column=0,padx=self.padding_x,pady=self.padding_y,columnspan=4)

        answerLabel = ttk.Label(self.calc_tab,textvariable=self.answer_string)
        answerLabel.grid(row=2,column=1,padx=self.padding_x,pady=self.padding_y,columnspan=2)

        textLabel = ttk.Label(self.calc_tab,text="Answer:")
        textLabel.grid(row=2,column=0,padx=self.padding_x,pady=self.padding_y)

    def buttons_calc_tab(self):
        buttonOne = ttk.Button(self.calc_tab,text="1", command=lambda: self.text_from_button("1"))
        buttonOne.grid(row=4,column=0,padx=self.padding_x,pady=self.padding_y)

        buttonTwo = ttk.Button(self.calc_tab,text="2", command=lambda: self.text_from_button("2"))
        buttonTwo.grid(row=4,column=1,padx=self.padding_x,pady=self.padding_y)

        buttonThree = ttk.Button(self.calc_tab,text="3", command=lambda: self.text_from_button("3"))
        buttonThree.grid(row=4,column=2,padx=self.padding_x,pady=self.padding_y)

        buttonFour = ttk.Button(self.calc_tab,text="4", command=lambda: self.text_from_button("4"))
        buttonFour.grid(row=5,column=0,padx=self.padding_x,pady=self.padding_y)

        buttonFive = ttk.Button(self.calc_tab,text="5", command=lambda: self.text_from_button("5"))
        buttonFive.grid(row=5,column=1,padx=self.padding_x,pady=self.padding_y)

        buttonSix = ttk.Button(self.calc_tab,text="6", command=lambda: self.text_from_button("6"))
        buttonSix.grid(row=5,column=2,padx=self.padding_x,pady=self.padding_y)

        buttonSeven = ttk.Button(self.calc_tab,text="7", command=lambda: self.text_from_button("7"))
        buttonSeven.grid(row=6,column=0,padx=self.padding_x,pady=self.padding_y)

        buttonEight = ttk.Button(self.calc_tab,text="8", command=lambda: self.text_from_button("8"))
        buttonEight.grid(row=6,column=1,padx=self.padding_x,pady=self.padding_y)

        buttonNine = ttk.Button(self.calc_tab,text="9", command=lambda: self.text_from_button("9"))
        buttonNine.grid(row=6,column=2,padx=self.padding_x,pady=self.padding_y)

        buttonZero = ttk.Button(self.calc_tab,text="0", command=lambda: self.text_from_button("0"))
        buttonZero.grid(row=7,column=0,padx=self.padding_x,pady=self.padding_y)

        buttonAddition = ttk.Button(self.calc_tab,text="+", command=lambda: self.text_from_button("+"))
        buttonAddition.grid(row=3,column=0,padx=self.padding_x,pady=self.padding_y)

        buttonSubtraction = ttk.Button(self.calc_tab,text="-", command=lambda: self.text_from_button("-"))
        buttonSubtraction.grid(row=3,column=1,padx=self.padding_x,pady=self.padding_y)

        buttonMultiplication = ttk.Button(self.calc_tab,text="x", command=lambda: self.text_from_button("x"))
        buttonMultiplication.grid(row=3,column=2,padx=self.padding_x,pady=self.padding_y)

        buttonDivision = ttk.Button(self.calc_tab,text="÷", command=lambda: self.text_from_button("÷"))
        buttonDivision.grid(row=3,column=3,padx=self.padding_x,pady=self.padding_y)

        buttonPower = ttk.Button(self.calc_tab,text="^", command=lambda: self.text_from_button("^"))
        buttonPower.grid(row=4,column=3,padx=self.padding_x,pady=self.padding_y)

        buttonLeftParenthesis = ttk.Button(self.calc_tab,text="(", command=lambda: self.text_from_button("("))
        buttonLeftParenthesis.grid(row=7,column=1,padx=self.padding_x,pady=self.padding_y)

        buttonRightParenthesis = ttk.Button(self.calc_tab,text=")", command=lambda: self.text_from_button(")"))
        buttonRightParenthesis.grid(row=7,column=2,padx=self.padding_x,pady=self.padding_y)

        buttonEqual = ttk.Button(self.calc_tab,text="=", command=self.equal_button_function,width=36)
        buttonEqual.grid(row=8,column=0,padx=self.padding_x,pady=self.padding_y,columnspan=4)

        buttonClear = ttk.Button(self.calc_tab,text="C", command = self.clear_button_function)
        buttonClear.grid(row=6,column=3,padx=self.padding_x,pady=self.padding_y)

        buttonDecimal = ttk.Button(self.calc_tab,text=".", command=lambda: self.text_from_button("."))
        buttonDecimal.grid(row=5,column=3,padx=self.padding_x,pady=self.padding_y)
        
        buttonAns = ttk.Button(self.calc_tab,text="Ans", command=self.ans_button_function)
        buttonAns.grid(row=7,column=3,padx=self.padding_x,pady=self.padding_y)
    
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
        global answer_button_var
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
            answer_button_var = str(answer)
            question_string_label = " "
        except SyntaxError:
            self.answer_string.set("Syntax Error")
        except ZeroDivisionError:
            self.answer_string.set("Math Error: Division by 0")
        except TypeError:
            self.answer_string.set("Brackets are not counted as multiplication")
        
        answer_string_label = ' '
    
    def ans_button_function(self):
        global answer_button_var
        global question_string_label
        question_string_label += answer_button_var
        self.question_string.set(question_string_label)
    
    def buttons_quadratic_tab(self):
        buttonOne = ttk.Button(self.quadratic_tab,text="1",command= lambda: self.quadratic_buttons_function("1"))
        buttonOne.grid(row=3,column=0,padx=self.padding_x,pady=self.padding_y)

        buttonTwo = ttk.Button(self.quadratic_tab,text="2",command= lambda: self.quadratic_buttons_function("2"))
        buttonTwo.grid(row=3,column=1,padx=self.padding_x,pady=self.padding_y)

        buttonThree = ttk.Button(self.quadratic_tab,text="3",command= lambda: self.quadratic_buttons_function("3"))
        buttonThree.grid(row=3,column=2,padx=self.padding_x,pady=self.padding_y)

        buttonFour = ttk.Button(self.quadratic_tab,text="4",command= lambda: self.quadratic_buttons_function("4"))
        buttonFour.grid(row=4,column=0,padx=self.padding_x,pady=self.padding_y)

        buttonFive = ttk.Button(self.quadratic_tab,text="5",command= lambda: self.quadratic_buttons_function("5"))
        buttonFive.grid(row=4,column=1,padx=self.padding_x,pady=self.padding_y)

        buttonSix = ttk.Button(self.quadratic_tab,text="6",command= lambda: self.quadratic_buttons_function("6"))
        buttonSix.grid(row=4,column=2,padx=self.padding_x,pady=self.padding_y)

        buttonSeven = ttk.Button(self.quadratic_tab,text="7",command= lambda: self.quadratic_buttons_function("7"))
        buttonSeven.grid(row=5,column=0,padx=self.padding_x,pady=self.padding_y)

        buttonEight = ttk.Button(self.quadratic_tab,text="8",command= lambda: self.quadratic_buttons_function("8"))
        buttonEight.grid(row=5,column=1,padx=self.padding_x,pady=self.padding_y)

        buttonNine = ttk.Button(self.quadratic_tab,text="9",command= lambda: self.quadratic_buttons_function("9"))
        buttonNine.grid(row=5,column=2,padx=self.padding_x,pady=self.padding_y)

        buttonZero = ttk.Button(self.quadratic_tab,text="0",command= lambda: self.quadratic_buttons_function("0"))
        buttonZero.grid(row=6,column=0,padx=self.padding_x,pady=self.padding_y)

        buttonAddition = ttk.Button(self.quadratic_tab,text="+",command= lambda: self.quadratic_buttons_function("+"))
        buttonAddition.grid(row=3,column=3,padx=self.padding_x,pady=self.padding_y)

        buttonSubtraction = ttk.Button(self.quadratic_tab,text="-",command= lambda: self.quadratic_buttons_function("-"))
        buttonSubtraction.grid(row=4,column=3,padx=self.padding_x,pady=self.padding_y)

        buttonEqual = ttk.Button(self.quadratic_tab,text="=",command=self.equal_button_function_quadratic)
        buttonEqual.grid(row=6,column=2,padx=self.padding_x,pady=self.padding_y)

        buttonClear = ttk.Button(self.quadratic_tab,text="C",command=self.clear_button_function_quadratic)
        buttonClear.grid(row=6,column=1,padx=self.padding_x,pady=self.padding_y)

        buttonDecimal = ttk.Button(self.quadratic_tab,text=".",command= lambda: self.quadratic_buttons_function("."))
        buttonDecimal.grid(row=5,column=3,padx=self.padding_x,pady=self.padding_y)

    def num_screen_quadratic(self):
        quadraticQuestionLabel = ttk.Label(self.quadratic_tab,textvariable=self.question_string_quadratic)
        quadraticQuestionLabel.grid(row=1,column=0,padx=self.padding_x,pady=self.padding_y,columnspan=2)

        quadraticTextLabel = ttk.Label(self.quadratic_tab,textvariable=self.quadratic_string)
        quadraticTextLabel.grid(row=1,column=1,padx=self.padding_x,pady=self.padding_y)

        quadraticAnswerLabel = ttk.Label(self.quadratic_tab,textvariable=self.answer_string_quadratic)
        quadraticAnswerLabel.grid(row=2,column=0,padx=self.padding_x,pady=self.padding_y,columnspan=4)
    
    def quadratic_buttons_function(self,string):
        global quadratic_question_string_label
        quadratic_question_string_label += string
        self.question_string_quadratic.set(quadratic_question_string_label)
    
    def clear_button_function_quadratic(self):
        global quadratic_question_string_label
        global quadratic_answer_string_label
        global num_list
        global count
        quadratic_question_string_label = " "
        self.question_string_quadratic.set(quadratic_question_string_label)
        quadratic_answer_string_label = " "
        self.answer_string_quadratic.set(quadratic_answer_string_label)
        count = 1
        num_list = []
        self.quadratic_string.set("x²")
    
    def equal_button_function_quadratic(self):
        global count
        global quadratic_question_string_label
        global quadratic_answer_string_label
        global num_list

        
        if count == 0:
            self.quadratic_string.set("x²")
            count += 1
        elif count == 1:
            self.quadratic_string.set("x")
            num_list.append(quadratic_question_string_label)
            quadratic_question_string_label = " "
            self.question_string_quadratic.set(quadratic_question_string_label)
            count += 1

        elif count == 2:
            self.quadratic_string.set("")
            num_list.append(quadratic_question_string_label)
            quadratic_question_string_label = " "
            self.question_string_quadratic.set(quadratic_question_string_label)
            count += 1
        elif count == 3:
            self.quadratic_string.set("x²")
            num_list.append(quadratic_question_string_label)
            
            try:
                answer=math_functions.quadratic_calc(num_list)
                quadratic_answer_string_label = answer
                self.answer_string_quadratic.set(quadratic_answer_string_label)
            except ZeroDivisionError:
                quadratic_answer_string_label = "Math Error: Division By Zero"
                self.answer_string_quadratic.set(quadratic_answer_string_label)
            except ValueError:
                quadratic_answer_string_label = "Necessary Values Missing/Syntax Error"
                self.answer_string_quadratic.set(quadratic_answer_string_label)
            
            
            
            num_list.clear()
            quadratic_question_string_label = " "
            self.question_string_quadratic.set(quadratic_question_string_label)
            count = 0
            count += 1