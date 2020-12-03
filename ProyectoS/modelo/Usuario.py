from tkinter import StringVar #Para asociar los campos de texto con el compomente texto
from tkinter import IntVar #Para asociar los campos de numero con el compomente radio

class Usuario:

    def __init__(self):
        self.usuario = StringVar()
        self.contrasena = StringVar()
        self.correo = StringVar()
        self.lastUser = ""
        self.lastModification = StringVar()
        

    def limpiar(self):
        self.usuario.set("")
        self.contrasena.set("")
        self.correo.set("")

    def printInfo(self):
        print(f"Usuario:{self.usuario.get()}")
        print(f"Contraseña:{self.contrasena.get()}")
        print(f"Correo:{self.correo.get()}")
