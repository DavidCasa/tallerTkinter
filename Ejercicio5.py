############ EJERCICIO 5 #############
from tkinter import *
root = Tk()
v = IntVar()
v.set(1)  # initializing the choice, i.e. Python
#Hace un menú con los lenguajes de programación, con la primera opción ya señalada
#cada vez que se marque una opción se imprimirá el número de la posición que se marque
languages = [("Python",1),("Perl",2),("Java",3),("C++",4),("C",5)]
def ShowChoice():
    print (v.get())
#En un Label imprime un mensaje, donde sugiere que elija un lenguaje de programacion
Label(root, text="""Choose your favourite programming language:""",justify = LEFT,padx = 20).pack()
for txt, val in languages:Radiobutton(root, text=txt,padx = 30, variable=v, command=ShowChoice,value=val).pack(anchor=W)

mainloop()