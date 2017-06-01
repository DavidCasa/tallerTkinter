from tkinter import * #Importar una libreria
class App:  #definir una clase
    def __init__(self, master): #definir una funcion
        #definir paneles para ordenar elementos
        frame = Frame(master)
        frame.pack()
        #declarar botones con los comandos llamando a funciones 
        self.button = Button(frame, text="SALIR",fg="red",command=frame.quit)
        #definir la posicion del boton
        self.button.pack(side=LEFT)
        self.slogan =Button(frame,text="ENTRAR",command=self.write_slogan)
        self.slogan.pack(side=LEFT)

    def write_slogan(self):
        #impresion del texto en el momento que la funcion es llamada
        print ("Estamos aprendiendo a usar Tkinter!, David Casa..!")

#llamada a la ventana y a sus componentes
root = Tk()
app = App(root)
root.mainloop()
