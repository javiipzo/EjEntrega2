import filosofo
import ventanaE
from ast import Continue, Pass
import time
import random
import threading
import tkinter as tk
from tkinter import *
from tkinter import ttk
from turtle import bgcolor
N = 5
TIEMPO_TOTAL = 3
def main():
    #PRUEBA TKINTER MAIN

    lista=[]
    for i in range(N):
        #add an object from class filosofo to the list
        
        lista.append(filosofo.filosofo())
#AGREGA UN FILOSOFO A LA LISTA
    for f in lista:
        f.start() #ES EQUIVALENTE A RUN()
        if f.estado[f.id] == 'COMIENDO':
            print('hola')
    for f in lista:
        f.join() #BLOQUEA HASTA QUE TERMINA EL THREAD

if __name__=="__main__":
    main()
