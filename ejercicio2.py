
##### EJERCICIO 2 #########
from tkinter import *
master = Tk()
#Declarar una variable la cual contenga un mensaje
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
#imprimir en la ventana el mensaje
msg = Message(master, text = whatever_you_do)
#configurar el tipo de texto color de fondo de la venta.
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.pack( )
mainloop( )
