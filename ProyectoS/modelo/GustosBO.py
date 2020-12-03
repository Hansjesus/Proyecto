import mysql.connector # para instalarlo -> pip3 install mysql-connector 



class GustosBO:

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
    def guardar(self, gustos):
        try:
            if(self.validar(gustos)):#se valida que tenga la información

                if(not self.exist(gustos)): #si no existe lo agrega
                    gustos.lastUser = "Hns"
                    insertSQL = "INSERT INTO Gustos (`PK_gustos`, `descripcion`, `FK_cedula`, `lastUser`, `lastModificacion`) VALUES (%s, %s, %s, %s, CURDATE())"
                    insertValores =  (gustos.gustos.get(),gustos.descripcion.get(),gustos.fk_cedula.get(), gustos.lastUser)
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
    def exist(self , gustos):
        try:
            existe = False
            selectSQL = "Select * from Gustos where PK_gustos = " + gustos.gustos.get()
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
    def validar (self, gustos):
        valido = True
        gustos.printInfo()
        if gustos.gustos.get() == "" :
            valido = False
        
        if gustos.descripcion.get() == "" :
            valido = False

        if gustos.fk_cedula.get() == "" :
            valido = False


        return valido

    #*************************************************************************
    #Metodo para consultar toda la información de la base de datos
    #*************************************************************************
    def consultar(self ):
        try:
            selectSQL = "select * \
                        from gustos" 
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
    def consultarGustos(self, gustos):
        try:
            selectSQL = "Select * from Gustos where PK_gustos = " + gustos.gustos.get()
            cursor = self.db.cursor()
            cursor.execute(selectSQL)
            gustosDB = cursor.fetchone()
            if (gustosDB) : #Metodo obtiene un solo registro o none si no existe información
                gustos.gustos.set(gustosDB[0]),
                gustos.descripcion.set(gustosDB[1])
                gustos.fk_cedula.set(gustosDB[2])
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
    def eliminar(self, gustos):
        try:
            deleteSQL = "delete  from Gustos where PK_gustos = " + gustos.gustos.get()
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
    def modificar(self, gustos):
        try:
            if(self.validar(gustos)):#se valida que tenga la información

                if(self.exist(gustos)): #si  existe lo modifica
                    gustos.lastUser = "Hns"
                    updateSQL = "UPDATE Gustos  set `descripcion` = %s, `FK_cedula` = %s, `lastUser` = %s, `lastModificacion` = CURDATE() WHERE `PK_gustos` =  %s"
                    updateValores =  (gustos.descripcion.get(),gustos.fk_cedula.get(), gustos.lastUser, gustos.gustos.get())
                    #print(insertValores)
                    cursor = self.db.cursor() #crea un cursos con la conexión lo que nos permite conectarnos a la base de datos
                    cursor.execute(updateSQL, updateValores) #ejecuta el SQL con las valores
                    self.db.commit() #crea un commit en la base de datos
                else:
                    raise Exception('Gusto indicado en el formulario no existe en la base de datos')  # si existe el registro con la misma cedual genera el error
            else:
                raise Exception('Los datos no fueron digitados por favor validar la información')  # si no tiene todos los valores de genera un error
        except mysql.connector.Error as e:
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e))