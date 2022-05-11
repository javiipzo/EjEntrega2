
from ast import Continue, Pass
import time
import random
import threading
import tkinter as tk
from tkinter import *
from tkinter import ttk
from turtle import bgcolor
import filosofo 
import main

class ventana:
    root =tk.Tk()
    #create a basic tkinter interface
    root.title("Filosofos")
    root.geometry("720x580")
    root.columnconfigure(0, weight=0)
    root.columnconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)
    root.resizable(0,0)
    root.configure(background='#ffffff')

    #add 3 buttons on the bottom
    button1=ttk.Button(root,text="Iniciar",command=main.main())
    button1.grid(column=0,row=3)
    #create another button to exit the program
    button4=ttk.Button(root,text="Salir",command=quit)
    button4.grid(column=1,row=3)

    #create a frame to hold the buttons
    frame=ttk.Frame(root,relief=SUNKEN,borderwidth=5)
    frame.grid(column=0,row=2,columnspan=4,sticky=('N','S','E','W'))
    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.columnconfigure(3, weight=1)
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)
    frame.rowconfigure(3, weight=1)

    #create a frame on the first row that is 300 pixels wide and 400 pixels high
    frame1=ttk.Frame(root,width=500,height=260,relief=SUNKEN,borderwidth=5)
    frame1.grid(column=0,row=0,sticky=('N','S','E','W'))

    #create another frame on the second row that is 400 pixels wide and 360 pixels high
    frame2=ttk.Frame(root,width=500,height=260,relief=SUNKEN,borderwidth=5)
    frame2.grid(column=0,row=1,sticky=('N','S','E','W'))

    #create a frame on the second column and the first row that is 100 pixels wide and 260 pixels high
    frame3=ttk.Frame(root,width=300,height=260,relief=SUNKEN,borderwidth=5)
    frame3.grid(column=1,row=0,sticky=('N','S','E','W'))
    frame4=ttk.Frame(root,width=300,height=260,relief=SUNKEN,borderwidth=5)
    frame4.grid(column=1,row=1,sticky=('N','S','E','W'))

    frame1.columnconfigure(0, weight=1)
    frame1.columnconfigure(1, weight=1)
    frame1.columnconfigure(2, weight=1)
    frame1.columnconfigure(3, weight=1)
    frame1.rowconfigure(0, weight=1)
    frame1.rowconfigure(1, weight=1)
    frame1.rowconfigure(2, weight=1)
    frame1.rowconfigure(3, weight=1)

    #add a text on the frame on the first row and second column
    #add a text on the frame on the first row and second column
    text0=ttk.Label(frame3,text="Código de colores:",font=("Arial", 17, "bold"))
    text0.grid(column=0,row=0,sticky=('N','S','E','W'))


    text1=ttk.Label(frame3,text="Filósofo entra a comer",font=("Arial",15))
    text1.grid(column=0,row=2,sticky=('N','S','E','W'), padx = 20, pady = 10)
    color1 = tk.Label(frame3, background="pink", height = 1, width = 1)
    color1.place(relx=0.05, rely=0.17, anchor=tk.CENTER)
    color1.config(state="disable")

    text2=ttk.Label(frame3,text="Filosofo tiene un tenedor",font=("Arial",15))
    text2.grid(column=0,row=3,sticky=('N','S','E','W'), padx = 20, pady = 10)
    color2 = tk.Label(frame3, background="orange", height = 1, width = 1)
    color2.place(relx=0.05, rely=0.32, anchor=tk.CENTER)
    color2.config(state="disable")

    text3=ttk.Label(frame3,text="Filósofo esta comiendo",font=("Arial",15))
    text3.grid(column=0,row=4,sticky=('N','S','E','W'), padx = 20, pady = 10)
    color3 = tk.Label(frame3, background="blue", height = 1, width = 1)
    color3.place(relx=0.05, rely=0.48, anchor=tk.CENTER)
    color3.config(state="disable")

    text4=ttk.Label(frame3,text="Filósofo esta pensando",font=("Arial",15))
    text4.grid(column=0,row=5,sticky=('N','S','E','W'), padx = 20, pady = 10)
    color4 = tk.Label(frame3, background="grey", height = 1, width = 1)
    color4.place(relx=0.05, rely=0.62, anchor=tk.CENTER)
    color4.config(state="disable")

    text5=ttk.Label(frame3,text="Tenedor ocupado",font=("Arial",15))
    text5.grid(column=0,row=6,sticky=('N','S','E','W'), padx = 20, pady = 10)
    color5 = tk.Label(frame3, background="red", height = 1, width = 1)
    color5.place(relx=0.05, rely=0.77, anchor=tk.CENTER)
    color5.config(state="disable")

    text6=ttk.Label(frame3,text="Tenedor libre",font=("Arial",15))
    text6.grid(column=0,row=7,sticky=('N','S','E','W'), padx = 20, pady = 10)
    color6 = tk.Label(frame3, background="white", height = 1, width = 1)
    color6.place(relx=0.05, rely=0.93, anchor=tk.CENTER)


    text7=ttk.Label(frame4,text="Cuántas veces han comido:",font=("Arial", 15, "bold"))
    text7.grid(column=0,row=0,sticky=('N','S','E','W'))

    text8=ttk.Label(frame4,text="Filósofo 1:",font=("Arial",15))
    text8.grid(column=0,row=2,sticky=('N','S','E','W'))
    #create a text box next to text8 that will hold the number of times the philosopher 1 has eaten
    text8_1=ttk.Entry(frame4,width=14)
    text8_1.place(x=80,y=22)

    text9=ttk.Label(frame4,text="Filosofo 2:",font=("Arial",15))
    text9.grid(column=0,row=3,sticky=('N','S','E','W'))
    text9_1=ttk.Entry(frame4,width=14)
    text9_1.place(x=80,y=44)

    text10=ttk.Label(frame4,text="Filósofo 3:",font=("Arial",15))
    text10.grid(column=0,row=4,sticky=('N','S','E','W'))
    text10_1=ttk.Entry(frame4,width=14)
    text10_1.place(x=80,y=66)

    text11=ttk.Label(frame4,text="Filósofo 4:",font=("Arial",15))
    text11.grid(column=0,row=5,sticky=('N','S','E','W'))
    text11_1=ttk.Entry(frame4,width=14)
    text11_1.place(x=80,y=88)

    text12=ttk.Label(frame4,text="Filósofo 5:",font=("Arial",15))
    text12.grid(column=0,row=6,sticky=('N','S','E','W'))
    text12_1=ttk.Entry(frame4,width=14)
    text12_1.place(x=80,y=108)

    fil1 = tk.Label(frame1, text="Filósofo 1", background="white", height = 2, width = 7)
    fil1.place(x=190,y=25)
    fil1.config(state="disable")

    #create a text with grid
    fil2 = tk.Label(frame1, text="Filósofo 5", background="white", height = 2, width = 7)
    fil2.place(x=100,y=100)
    fil2.config(state="disable")

    #create a text with grid
    fil3 = tk.Label(frame1, text="Filósofo 2", background="white", height = 2, width = 7)
    fil3.place(x=290,y=80)
    fil3.config(state="disable")

    #create a text with grid
    fil4 = tk.Label(frame1, text="Filósofo 4", background="white", height = 2, width = 7)
    fil4.place(x=120,y=180)
    fil4.config(state="disable")

    #create a text with grid
    fil5 = tk.Label(frame1, text="Filósofo 3", background="white", height = 2, width = 7)
    fil5.place(x=260,y=160)
    fil5.config(state="disable")



    root.mainloop()






