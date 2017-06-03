############## EJERCICIOS 4 ################
from tkinter  import *
root = Tk()
v = IntVar()
#Es un pequeño menú, en el cual se aplica Radiobuttons para hacer la selección de opciones
Label(root,
      text="""Choose a programming language:""",
      justify = LEFT,
      padx = 20).pack()
Radiobutton(root,
            text="Python",
            padx = 20,
            variable=v,
            value=1).pack(anchor=W)
Radiobutton(root,
            text="Perl",
            padx = 20,
            variable=v,
            value=2).pack(anchor=W)

mainloop()