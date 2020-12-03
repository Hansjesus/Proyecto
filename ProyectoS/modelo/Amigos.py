from tkinter import StringVar #Para asociar los campos de texto con el compomente texto
from tkinter import IntVar #Para asociar los campos de numero con el compomente radio

class Amigos:

    def __init__(self):
        self.pk_amigos = StringVar()
        self.nivel_de_amistad = StringVar()
        self.fk_cedulaOrigen = StringVar()
        self.fk_cedulaDestino = StringVar()
        self.lastUser = ""
        self.lastModificacion = StringVar()
        

    def limpiar(self):
        self.pk_amigos.set("")
        self.nivel_de_amistad.set("")
        self.fk_cedulaOrigen.set("")
        self.fk_cedulaDestino.set("")


    def printInfo(self):
        print(f"Nivel de Amistad:{self.pk_amigos.get()}")
        print(f"Amigos:{self.nivel_de_amistad.get()}")
        print(f"Cedula Origen:{self.fk_cedulaOrigen.get()}")
        print(f"CedulaDestino:{self.fk_cedulaDestino.get()}")