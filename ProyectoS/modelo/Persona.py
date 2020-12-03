from tkinter import StringVar #Para asociar los campos de texto con el compomente texto
from tkinter import IntVar #Para asociar los campos de numero con el compomente radio

class Persona:

    def __init__(self):
        self.cedula = StringVar()
        self.nombre = StringVar()
        self.apellido1 = StringVar()
        self.apellido2 = StringVar()
        self.fechaNacimiento = StringVar()
        self.descripcion = StringVar()
        self.estado = StringVar()
        self.fk_usuario = StringVar()
        self.lastUser = ""
        self.lastModificacion = StringVar()
        

    def limpiar(self):
        self.cedula.set("")
        self.nombre.set("")
        self.apellido1.set("")
        self.apellido2.set("")
        self.fechaNacimiento.set("")
        self.descripcion.set("")
        self.estado.set("")
        self.fk_usuario.set("")

    def printInfo(self):
        print(f"Cedula:{self.cedula.get()}")
        print(f"Nombre:{self.nombre.get()}")
        print(f"Apellido1:{self.apellido1.get()}")
        print(f"Apellido2:{self.apellido2.get()}")
        print(f"Fecha Nacimiento:{self.fechaNacimiento.get()}")
        print(f"Descripcion:{self.descripcion.get()}")
        print(f"Estado:{self.estado.get()}")
        print(f"Usuario:{self.fk_usuario.get()}")

    
        