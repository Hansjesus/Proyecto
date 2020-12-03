from tkinter import StringVar #Para asociar los campos de texto con el compomente texto
from tkinter import IntVar #Para asociar los campos de numero con el compomente radio

class Telefono:

    def __init__(self):
        self.telefono = StringVar()
        self.codigo = StringVar()
        self.fk_cedula = StringVar()
        self.lastUser = ""
        self.lastModificacion = StringVar()
        

    def limpiar(self):
        self.telefono.set("")
        self.codigo.set("")
        self.fk_cedula.set("")


    def printInfo(self):
        print(f"Telefono:{self.telefono.get()}")
        print(f"Código:{self.codigo.get()}")
        print(f"Cedula:{self.fk_cedula.get()}")