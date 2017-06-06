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
Checkbutton(master, text="male", variable=var1).grid(row=1, sticky=W)
var2= IntVar()
Checkbutton(master, text="female", variable=var2).grid(row=2, sticky=W)
Button(master, text='Quit', command= master.quit).grid(row=3, sticky=W, padx=4)
Button(master, text='Show', command= var_states).grid(row=4, sticky=W, padx=4)
mainloop()

