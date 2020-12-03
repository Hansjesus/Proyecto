import mysql.connector # para instalarlo -> pip3 install mysql-connector 



class TelefonoBO:

    #*************************************************************************
    #El constructor de la clase persona BO crea un objeto de conexion a la base de datos
    #*************************************************************************
    def __init__(self):
        #se crea la conexión con la base de datos
        self.db = mysql.connector.connect(host ="127.0.0.1", 
                                     user = "root", 
                                     password = "Hansgamb1n012345", 
                                     db ="red_social") 

    #*************************************************************************
    #Cuando el objeto es destruido por el interprete realiza la desconexion con la base de datos
    #*************************************************************************
    def __del__(self):
        self.db.close() #al destriurse el objeto cierra la conexion 
  
    #*************************************************************************
    #Metodo que guarda una persona en la base de datos
    #*************************************************************************
    def guardar(self, telefono):
        try:
            if(self.validar(telefono)):#se valida que tenga la información

                if(not self.exist(telefono)): #si no existe lo agrega
                    telefono.lastUser = "Hns"
                    insertSQL = "INSERT INTO Telefono (`PK_telefono`, `codigo`, `FK_cedula`, `lastUser`, `lastModificacion`) VALUES (%s, %s, %s, %s, CURDATE())"
                    insertValores =  (telefono.telefono.get(),telefono.codigo.get(),telefono.fk_cedula.get(), telefono.lastUser)
                    print(insertValores)
                    cursor = self.db.cursor() #crea un cursos con la conexión lo que nos permite conectarnos a la base de datos
                    cursor.execute(insertSQL, insertValores) #ejecuta el SQL con las valores
                    self.db.commit() #crea un commit en la base de datos
                else:
                    raise Exception('La cédula indicada en el formulario existe en la base de datos')  # si existe el registro con la misma cedual genera el error
            else:
                raise Exception('Los datos no fueron digitados por favor validar la información')  # si no tiene todos los valores de genera un error
        except mysql.connector.Error as e:
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e)) 
    
    #*************************************************************************
    #Metodo que verifica en la base de datos si la persona existe por cédula
    #*************************************************************************
    def exist(self , telefono):
        try:
            existe = False
            selectSQL = "Select * from P_Telefono where PK_telefono = " + telefono.telefono.get()
            cursor = self.db.cursor()
            cursor.execute(selectSQL)
            if (cursor.fetchone()) : #Metodo obtiene un solo registro o none si no existe información
                existe  = True

            return existe
            
        except mysql.connector.Error as e:
            print("Something went wrong: {}".format(e))
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e)) 


    #*************************************************************************
    #Metodo para validar al información que proviene de la vista
    #*************************************************************************
    def validar (self, telefono):
        valido = True
        telefono.printInfo()
        if telefono.telefono.get() == "" :
            valido = False
            
        if telefono.codigo.get() == "" :
            valido = False
        
        if telefono.fk_cedula.get() == "" :
            valido = False


        return valido

    #*************************************************************************
    #Metodo para consultar toda la información de la base de datos
    #*************************************************************************
    def consultar(self ):
        try:
            selectSQL = "select * \
                        from telefono" 
            cursor = self.db.cursor()
            cursor.execute(selectSQL)
            myresult = cursor.fetchall()
            final_result = [list(i) for i in myresult]
            return final_result
            
        except mysql.connector.Error as e:
            print("Something went wrong: {}".format(e))
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e)) 


    #*************************************************************************
    #Metodo para consultar la información de una persona
    #*************************************************************************
    def consultarTelefono(self, telefono):
        try:
            selectSQL = "Select * from Telefono where PK_telefono = " + telefono.telefono.get()
            cursor = self.db.cursor()
            cursor.execute(selectSQL)
            telefonoDB = cursor.fetchone()
            if (telefonoDB) : #Metodo obtiene un solo registro o none si no existe información
                telefono.telefono.set(telefonoDB[0]),
                telefono.codigo.set(telefonoDB[1])
                telefono.fk_cedula.set(telefonoDB[2])
            else:
                raise Exception("La cédula consultada no existe en la base de datos") 
            
        except mysql.connector.Error as e:
            print("Something went wrong: {}".format(e))
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e)) 

    #*************************************************************************
    #Metodo para eliminar a una persona de la base de datos
    #*************************************************************************
    def eliminar(self, telefono):
        try:
            deleteSQL = "delete  from Telefono where PK_telefono = " + telefono.telefono.get()
            cursor = self.db.cursor() #crea un cursos con la conexión lo que nos permite conectarnos a la base de datos
            cursor.execute(deleteSQL) #ejecuta el SQL con las valores
            self.db.commit() #crea un commit en la base de datos
        except mysql.connector.Error as e:
            print("Something went wrong: {}".format(e))
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e)) 



    #*************************************************************************
    #Metodo que guarda una persona en la base de datos
    #*************************************************************************
    def modificar(self, telefono):
        try:
            if(self.validar(telefono)):#se valida que tenga la información

                if(self.exist(telefono)): #si  existe lo modifica
                    telefono.lastUser = "Hns"
                    updateSQL = "UPDATE Telefono  set `FK_cedula` = %s, `codigo` = %s, `lastUser` = %s, `lastModificacion` = CURDATE() WHERE `PK_telefono` =  %s"
                    updateValores =  (telefono.fk_cedula.get(), telefono.codigo.get(), telefono.lastUser, telefono.telefono.get())
                    #print(insertValores)
                    cursor = self.db.cursor() #crea un cursos con la conexión lo que nos permite conectarnos a la base de datos
                    cursor.execute(updateSQL, updateValores) #ejecuta el SQL con las valores
                    self.db.commit() #crea un commit en la base de datos
                else:
                    raise Exception('El teléfono indicado en el formulario no existe en la base de datos')  # si existe el registro con la misma cedual genera el error
            else:
                raise Exception('Los datos no fueron digitados por favor validar la información')  # si no tiene todos los valores de genera un error
        except mysql.connector.Error as e:
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e))