##### EJERCICIO 8 #########
from tkinter import *

master = Tk()
#declaracion de una funcion
def var_states():
    print (" male: ",var1.get())
    print ("female: ",var2.get())

#impresion en un label en la ventana con el texto inscrito, y su respectiva posicion
Label(master, text="Indicar el sexo:").grid(row=0, sticky=W)
#declaracion de una variable
var1 = IntVar()

