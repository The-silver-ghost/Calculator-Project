import gui
from tkinter import *
from tkinter import ttk

main_root = Tk()
main_frame = ttk.Frame(main_root,height=600,width=600,)

gui.GUI(main_root,main_frame,5,5).main_screen()