import gui
from tkinter import *


main_root = Tk()
main_root.title("Calculator")

gui.GUI(main_root,5,5,StringVar(main_root),StringVar(main_root)).main_screen()
