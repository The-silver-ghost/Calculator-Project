import gui
from tkinter import *
from tkinter import ttk

main_root = Tk()
main_frame = ttk.Frame(main_root)
main_root.title("Calculator")
tabs = ttk.Notebook(main_frame)

gui.GUI(main_root,5,5,StringVar(main_root),StringVar(main_root),ttk.Frame(tabs),tabs,ttk.Frame(tabs),main_frame,StringVar(main_root),StringVar(main_root)).main_screen()
