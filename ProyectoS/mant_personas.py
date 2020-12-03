from tkinter import * 
from tkinter import font
from tkinter import messagebox as msg
from tkinter import ttk 

from tksheet import Sheet # para instalarlo -> pip3 install tksheet

from tkcalendar import Calendar, DateEntry # para instalarlo -> pip3 install tkcalendar

#Incluye el objeto de persona
from modelo import Persona

#Incluye el objeto de logica de negocio
from modelo import PersonoBO

import mant_telefonos 
import mant_amigos
import mant_gustos
import mant_usuarios


class Aplicacion:
    

    def __init__(self):
        #*************************************************************************
        #Crea un objeto TK
        #*************************************************************************
        self.raiz = Tk()
        self.raiz.title ("Mantenimiento de Personas")
        self.raiz.geometry('900x600') 

        #*************************************************************************
        #crea el menu de la pantalla
        #*************************************************************************
        menubar = Menu(self.raiz)
        self.raiz.config(menu=menubar)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Acerca de..")
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.raiz.quit)

        mantmenu = Menu(menubar, tearoff=0)
        mantmenu.add_command(label="Teléfonos", command=self.mostrar_mant_telefonos)
        mantmenu.add_command(label="Amigos", command=self.mostrar_mant_amigos)
        mantmenu.add_command(label="Gustos", command=self.mostrar_mant_gustos)
        mantmenu.add_command(label="Usuarios", command=self.mostrar_mant_usuarios)

        menubar.add_cascade(label="Archivo", menu=filemenu)
        menubar.add_cascade(label="Mantenimiento", menu=mantmenu)

        #*************************************************************************
        #crea un objeto tipo fuenta
        #*************************************************************************
        self.fuente = font.Font(weight="bold")

        #*************************************************************************
        #se crean atributos de la clase
        #*************************************************************************
        self.persona = Persona.Persona() #se crea el objeto de dominio para guardar la información
        self.insertando = True
       
        
        
        #*************************************************************************
        #se crean los campos de la pantalla telefono
        #*************************************************************************

        #Se coloca un label del titulo
        self.lb_tituloPantalla = Label(self.raiz, text = "MANTENIMIENTO DE PERSONAS", font = self.fuente)
        self.lb_tituloPantalla.place(x = 320, y = 20) #colocar por medio de espacion en pixeles de la parte superior de la pantalla considerando un eje x y un eje y
        
        #coloca en el formulario el campo y el label de cedula
        self.lb_cedula = Label(self.raiz, text = "Cedula:")
        self.lb_cedula.place(x = 100, y = 60)
        self.txt_cedula = Entry(self.raiz, textvariable=self.persona.cedula, justify="right")
        self.txt_cedula.place(x = 230, y = 60)

        #coloca en el formulario el campo y el label de nombre
        self.lb_nombre = Label(self.raiz, text = "Nombre:")
        self.lb_nombre.place(x = 100, y = 90)
        self.txt_nombre = Entry(self.raiz, textvariable=self.persona.nombre, justify="right", width=30)
        self.txt_nombre.place(x = 230, y = 90)

        #coloca en el formulario el campo y el label de apellido1
        self.lb_apellido1 = Label(self.raiz, text = "Primer apellido:")
        self.lb_apellido1.place(x = 100, y = 120)
        self.txt_apellido1 = Entry(self.raiz, textvariable=self.persona.apellido1, justify="right", width=30)
        self.txt_apellido1.place(x = 230, y = 120)


        #coloca en el formulario el campo y el label de apellido2
        self.lb_apellido2 = Label(self.raiz, text = "Segundo apellido:")
        self.lb_apellido2.place(x = 100, y = 150)
        self.txt_apellido2 = Entry(self.raiz, textvariable=self.persona.apellido2, justify="right", width=30)
        self.txt_apellido2.place(x = 230, y = 150)

        #coloca en el formulario el campo y el label de fecha nacimiento
        self.lb_fecha_nacimiento = Label(self.raiz, text = "Fecha nacimiento:")
        self.lb_fecha_nacimiento.place(x = 100, y = 180)
        self.txt_fechaNacimiento = Entry(self.raiz, textvariable=self.persona.fechaNacimiento, justify="right", width=30, state="readonly")
        self.txt_fechaNacimiento.place(x = 230, y = 180)
        self.bt_mostrarCalendario = Button(self.raiz, text="...", width=3, command = self.mostrarDatePicker)
        self.bt_mostrarCalendario.place(x = 510, y = 180)

        #coloca en el formulario el campo y el label de descripcion
        self.lb_descripcion = Label(self.raiz, text = "descripcion:")
        self.lb_descripcion.place(x = 100, y = 210)
        self.txt_descripcion = Entry(self.raiz, textvariable=self.persona.descripcion, justify="right", width=30)
        self.txt_descripcion.place(x = 230, y = 210) 

        #coloca en el formulario el campo y el label de observaciones
        self.lb_estado = Label(self.raiz, text = "estado:")
        self.lb_estado.place(x = 100, y = 250)
        self.txt_estado = Entry(self.raiz, textvariable=self.persona.estado, justify="right", width=30)
        self.txt_estado.place(x = 230, y = 250)

        #coloca en el formulario el campo y el label de observaciones
        self.lb_fk_usuario = Label(self.raiz, text = "Usuario:")
        self.lb_fk_usuario.place(x = 100, y = 280)
        self.txt_fk_usuario = Entry(self.raiz, textvariable=self.persona.fk_usuario, justify="right", width=30)
        self.txt_fk_usuario.place(x = 230, y = 280)

        #coloca los botones enviar y borrar
        self.bt_borrar = Button(self.raiz, text="Limpiar", width=15, command = self.limpiarInformacion)
        self.bt_borrar.place(x = 230, y = 350)

        self.bt_enviar = Button(self.raiz, text="Enviar", width=15, command = self.enviarInformacion)
        self.bt_enviar.place(x = 370, y = 350)

        #Se coloca un label del informacion
        self.lb_tituloPantalla = Label(self.raiz, text = "INFORMACIÓN INCLUIDA", font = self.fuente)
        self.lb_tituloPantalla.place(x = 190, y = 400) #colocar por medio de espacion en pixeles de la parte superior de la pantalla considerando un eje x y un eje y

        #*************************************************************************
        #tabla con informacion
        #*************************************************************************
        
        self.sheet = Sheet(self.raiz,
                           page_up_down_select_row = True,
                           #empty_vertical = 0,
                           column_width = 120,
                           startup_select = (0,1,"rows"),
                           #row_height = "4",
                           #default_row_index = "numbers",
                           #default_header = "both",
                           #empty_horizontal = 0,
                           #show_vertical_grid = False,
                           #show_horizontal_grid = False,
                           #auto_resize_default_row_index = False,
                           #header_height = "3",
                           #row_index_width = 100,
                           #align = "center",
                           #header_align = "w",
                            #row_index_align = "w",
                            #data = [[f"Row {r}, Column {c}\nnewline1\nnewline2" for c in range(50)] for r in range(1000)], #to set sheet data at startup
                            headers = ['Cédula', 'Nombre', 'Primer Ape.', 'Segundo Ape.', 'Fecha. Nacimiento', 'descripcion', 'estado', 'Usuario'],
                            #row_index = [f"Row {r}\nnewline1\nnewline2" for r in range(2000)],
                            #set_all_heights_and_widths = True, #to fit all cell sizes to text at start up
                            #headers = 0, #to set headers as first row at startup
                            #headers = [f"Column {c}\nnewline1\nnewline2" for c in range(30)],
                           #theme = "light green",
                            #row_index = 0, #to set row_index as first column at startup
                            #total_rows = 2000, #if you want to set empty sheet dimensions at startup
                            #total_columns = 30, #if you want to set empty sheet dimensions at startup
                            height = 195, #height and width arguments are optional
                            width = 720 #For full startup arguments see DOCUMENTATION.md
                            )
        #self.sheet.hide("row_index")
        #self.sheet.hide("header")
        #self.sheet.hide("top_left")
        self.sheet.enable_bindings(("single_select", #"single_select" or "toggle_select"
                                        
                                         "column_select",
                                         "row_select",
                                         "column_width_resize",
                                         "double_click_column_resize",
                                         #"row_width_resize",
                                         #"column_height_resize",
                                         "arrowkeys",
                                         "row_height_resize",
                                         "double_click_row_resize",
                                         "right_click_popup_menu",
                                         "rc_select",
                                         "rc_insert_column",
                                         "rc_delete_column",
                                         "rc_insert_row",
                                         "rc_delete_row"))
        #self.sheet.disable_bindings() #uses the same strings
        #self.sheet.enable_bindings()

        self.sheet.place(x = 20, y = 390)
        
        #coloca los botones cargar y eliminar
        self.bt_cargar = Button(self.raiz, text="Cargar", width=15, command = self.cargarInformacion)
        self.bt_cargar.place(x = 750, y = 385)

        self.bt_eliminar = Button(self.raiz, text="Eliminar", width=15, command = self.eliminarInformacion)
        self.bt_eliminar.place(x = 750, y = 425)
        
        self.cargarTodaInformacion()


        #*************************************************************************
        #se inicial el main loop de la pantalla
        #*************************************************************************
        self.raiz.mainloop()


    def mostrar_mant_telefonos(self):
        mant_telefonos.MantTelefonos(self.raiz)

    def mostrar_mant_amigos(self):
        mant_amigos.MantAmigos(self.raiz)

    def mostrar_mant_gustos(self):
        mant_gustos.MantGustos(self.raiz)

    def mostrar_mant_usuarios(self):
        mant_usuarios.MantUsuarios(self.raiz)


    #*************************************************************************
    #Metodo para consultar la información de la base de datos para 
    #cargarla en la tabla
    #*************************************************************************
    def cargarTodaInformacion(self):
        try:
            self.personaBo = PersonoBO.PersonaBO() #se crea un objeto de logica de negocio
            resultado = self.personaBo.consultar()

            self.sheet.set_sheet_data(resultado)
        except Exception as e: 
            msg.showerror("Error",  str(e)) #si se genera algun tipo de error muestra un mensache con dicho error

    #*************************************************************************
    #Metodo para cargar informacion
    #*************************************************************************
    def cargarInformacion(self):
        try:
            datoSeleccionado = self.sheet.get_currently_selected()
            cedula = (self.sheet.get_cell_data(datoSeleccionado[0],0))
            self.persona.cedula.set(cedula)
            self.personaBo = PersonoBO.PersonaBO() #se crea un objeto de logica de negocio
            self.personaBo.consultarPersona(self.persona) #se envia a consultar
            self.insertando = False
            msg.showinfo("Acción: Consultar persona", "La información de la persona ha sido consultada correctamente") # Se muestra el mensaje de que todo esta correcto
            
        except Exception as e: 
            msg.showerror("Error",  str(e)) #si se genera algun tipo de error muestra un mensache con dicho error

    #*************************************************************************
    #Metodo para cargar eliminar la informacion
    #*************************************************************************
    def eliminarInformacion(self):
        try:
            datoSeleccionado = self.sheet.get_currently_selected()
            cedula = (self.sheet.get_cell_data(datoSeleccionado[0],0))
            nombre = (self.sheet.get_cell_data(datoSeleccionado[0],1))

            resultado = msg.askquestion("Eliminar",  "¿Desear eliminar a "+nombre+" de la base de datos?")
            if resultado == "yes":
                self.persona.cedula.set(cedula)
                self.personaBo = PersonoBO.PersonaBO() #se crea un objeto de logica de negocio
                self.personaBo.eliminar(self.persona) #se envia a consultar
                self.cargarTodaInformacion()
                self.persona.limpiar()
        except Exception as e: 
            msg.showerror("Error",  str(e)) #si se genera algun tipo de error muestra un mensache con dicho error

    def printTxt(self, texto):
        print(texto)


    #*************************************************************************
    #Metodo para enviar la información a la base de datos 
    #*************************************************************************
    def enviarInformacion(self):
        try:
            self.personaBo = PersonoBO.PersonaBO() #se crea un objeto de logica de negocio
            if(self.insertando == True):
                self.personaBo.guardar(self.persona)
            else:
                self.personaBo.modificar(self.persona)
            
            self.cargarTodaInformacion()
            self.persona.limpiar() #se limpia el formulario

            if(self.insertando == True):
                msg.showinfo("Acción: Agregar persona", "La información de la persona ha sido incluida correctamente") # Se muestra el mensaje de que todo esta correcto
            else:
                msg.showinfo("Acción: Agregar modificar", "La información de la persona ha sido modificada correctamente") # Se muestra el mensaje de que todo esta correcto
        except Exception as e: 
            msg.showerror("Error",  str(e)) #si se genera algun tipo de error muestra un mensache con dicho error

    #*************************************************************************
    #Metodo para limpiar el formulario
    #*************************************************************************
    def limpiarInformacion(self):
        self.persona.limpiar() #llama al metodo de la clase persona para limpiar los atritudos de la clase
        self.insertando = True
        msg.showinfo("Acción del sistema", "La información del formulario ha sido eliminada correctamente") # muestra un mensaje indicando que se limpio el formulario


    #*************************************************************************
    #Metodo para mostrar un contro tipo datepicker
    #*************************************************************************
    def mostrarDatePicker(self):
        self.top = Toplevel(self.raiz)
        self.cal = Calendar(self.top, font="Arial 14", selectmode='day', locale='en_US',
                   year=2019, month=6, day=16)
        self.cal.pack(fill="both", expand=True)
        ttk.Button(self.top, text="Seleccionar", command = self.seleccionarFecha).pack()

    #*************************************************************************
    #Evento para obtener la fecha del datepicker
    #*************************************************************************
    def seleccionarFecha(self):
        self.persona.fechaNacimiento.set(self.cal.selection_get())

def main():
    Aplicacion()
    return 0

if __name__ == "__main__":
    main()