from tkinter import StringVar #Para asociar los campos de texto con el compomente texto
from tkinter import IntVar #Para asociar los campos de numero con el compomente radio

class Gustos:

    def __init__(self):
        self.gustos = StringVar()
        self.descripcion = StringVar()
        self.fk_cedula = StringVar()
        self.lastUser = ""
        self.lastModificacion = StringVar()
        

    def limpiar(self):
        self.gustos.set("")
        self.descripcion.set("")
        self.fk_cedula.set("")


    def printInfo(self):
        print(f"Gustos:{self.gustos.get()}")
        print(f"Nombre:{self.descripcion.get()}")
        print(f"Cedula:{self.fk_cedula.get()}")
