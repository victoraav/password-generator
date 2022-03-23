import random
import requests
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Password Generator - @victoraav")

frm = ttk.Frame(root,padding=40)
frm.grid()

ttk.Label(frm,text="PASSWORD GENERATOR",font=("Impact",20)).grid(column=0,row=0)


ttk.Checkbutton(frm, text=" Capital Letter").grid(column=0, row=1, sticky=SW)
ttk.Checkbutton(frm, text=" Special characters").grid(column=0, row=2, sticky=SW)



root.mainloop()