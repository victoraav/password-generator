import random
import requests
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("@victoraav - PassGen")
root.iconbitmap("lock.ico")

frm = ttk.Frame(root,padding=40)
frm.grid()

ttk.Label(frm,text="PASSWORD GENERATOR",font=("Impact",20)).grid(column=0,row=0)


ttk.Checkbutton(frm, text=" Capital Letter").grid(column=0, row=1, sticky=SW)
ttk.Checkbutton(frm, text=" Special characters").grid(column=0, row=2, sticky=SW)

ttk.Button(frm, text= "Generate").grid(column=0, row=3, pady=20)

ttk.Entry(frm, width=30).grid(column=0, row=4, pady=5)
ttk.Button(frm, text="Show", width=5).grid(column=0, row=5)
ttk.Button(frm, text="Copy", width=5).grid(column=0, row=6)



root.mainloop()