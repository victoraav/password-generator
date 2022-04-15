from tkinter import *
from tkinter import ttk
import pyperclip
import random
import requests

root = Tk()

senhag = StringVar()
senhag2 = ""

def gerar():
    words_site = "https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt"

    response = requests.get(words_site)
    words = response.content.splitlines()
    numrandom = random.randint(0,40000)
    palavra_aleatoria = words[numrandom].decode("utf-8")
    simbolos = ["!","@","#","$","%","&","*"]

    numero_aleatorio = random.randint(0,9999)
    numero_gerado = str(numero_aleatorio)

    numero_simbolo = random.randint(0,6)
    simbolo_aleatorio = simbolos[numero_simbolo]

    senha = palavra_aleatoria.capitalize() + numero_gerado + simbolo_aleatorio
    global senhag
    global senhag2
    senhag.set(senha)
    senhag2 = senha
    return (senha)

def copiar():
    global senhag2
    pyperclip.copy(senhag2)

root.title("@victoraav - PassGen")
root.iconbitmap("lock.ico")

frm = ttk.Frame(root,padding=40)
frm.grid()

ttk.Label(frm,text="PASSWORD GENERATOR",font=("Impact",20)).grid(column=0,row=0)

ttk.Button(frm, text= "Generate", command= gerar).grid(column=0, row=3, pady=20)

ttk.Entry(frm,textvariable=senhag ,width=30).grid(column=0, row=4, pady=5)

ttk.Button(frm, text="Copy", width=5,command= copiar).grid(column=0, row=5)



root.mainloop()