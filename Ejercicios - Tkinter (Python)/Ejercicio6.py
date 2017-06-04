from tkinter import *
root = Tk()
v = IntVar()

v.set(1) # initializing the choice, i.e. Python

languages = [ ("Python",1), ("Perl",2), ("Java",3), ("C++",4), ("C",5)]

def ShowChoice():
    print (v.get())

Label(root, text="""Escoja un lenguaje de programación:""", justify = LEFT,
      padx = 20).pack()

for txt, val in languages:
    Radiobutton(root, text=txt, indicatoron =0, width = 20, padx = 20,
                variable=v, command=ShowChoice, value=val).pack(anchor=W)

mainloop()
