import gui
from tkinter import *
from tkinter import ttk

main_root = Tk()
main_root.title("Calculator")
tabs = ttk.Notebook(main_root)

gui.GUI(main_root,5,5,StringVar(main_root),StringVar(main_root),("Bodoni",12,"bold"),ttk.Frame(tabs),tabs,ttk.Frame(tabs)).main_screen()
