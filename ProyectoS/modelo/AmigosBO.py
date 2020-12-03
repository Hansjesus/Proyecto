import mysql.connector # para instalarlo -> pip3 install mysql-connector 



class AmigosBO:

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
    def guardar(self, amigos):
        try:
            if(self.validar(amigos)):#se valida que tenga la información

                if(not self.exist(amigos)): #si no existe lo agrega
                    amigos.lastUser = "Hns"
                    insertSQL = "INSERT INTO Amigos (`nivel_de_amistad`, `pk_amigos`, `FK_cedulaOrigen`, `FK_cedulaDestino`, `lastUser`, `lastModificacion`) VALUES (%s, %s, %s, %s, %s, CURDATE())"
                    insertValores =  (amigos.nivel_de_amistad.get(), amigos.pk_amigos.get(),amigos.fk_cedulaOrigen.get(),amigos.fk_cedulaDestino.get(), amigos.lastUser)
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
    def exist(self , amigos):
        try:
            existe = False
            selectSQL = "Select * from Amigos where pk_amigos = " + amigos.pk_amigos.get()
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
    def validar (self, amigos):
        valido = True
        amigos.printInfo()
        if amigos.nivel_de_amistad.get() == "" :
            valido = False

        if amigos.pk_amigos.get() == "" :
            valido = False
        
        if amigos.fk_cedulaOrigen.get() == "" :
            valido = False

        if amigos.fk_cedulaDestino.get() == "" :
            valido = False


        return valido

    #*************************************************************************
    #Metodo para consultar toda la información de la base de datos
    #*************************************************************************
    def consultar(self ):
        try:
            selectSQL = "select * \
                        from amigos"
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
    def consultarAmigos(self, amigos):
        try:
            selectSQL = "Select * from Amigos where pk_amigos = " + amigos.pk_amigos.get()
            cursor = self.db.cursor()
            cursor.execute(selectSQL)
            personaBO = cursor.fetchone()
            if (personaBO) : #Metodo obtiene un solo registro o none si no existe información
                amigos.pk_amigos.set(personaBO[0])
                amigos.nivel_de_amistad.set(personaBO[1])
                amigos.fk_cedulaOrigen.set(personaBO[2])
                amigos.fk_cedulaDestino.set(personaBO[3])
            else:
                raise Exception("El código consultado no existe en la base de datos") 
            
        except mysql.connector.Error as e:
            print("Something went wrong: {}".format(e))
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e)) 

    #*************************************************************************
    #Metodo para eliminar a una persona de la base de datos
    #*************************************************************************
    def eliminar(self, amigos):
        try:
            deleteSQL = "delete  from Amigos where pk_amigos = " + amigos.pk_amigos.get()
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
    def modificar(self, amigos):
        try:
            if(self.validar(amigos)):#se valida que tenga la información

                if(self.exist(amigos)): #si  existe lo modifica
                    amigos.lastUser = "Hns"
                    updateSQL = "UPDATE Amigos  set `nivel_de_amistad` = %s, `FK_cedulaOrigen` = %s, `FK_cedulaDestino` = %s, `lastUser` = %s, `lastModificacion` = CURDATE() WHERE `pk_amigos` =  %s"
                    updateValores =  (amigos.nivel_de_amistad.get(),amigos.fk_cedulaOrigen.get(),amigos.fk_cedulaDestino.get(), amigos.lastUser, amigos.pk_amigos.get())
                    #print(insertValores)
                    cursor = self.db.cursor() #crea un cursos con la conexión lo que nos permite conectarnos a la base de datos
                    cursor.execute(updateSQL, updateValores) #ejecuta el SQL con las valores
                    self.db.commit() #crea un commit en la base de datos
                else:
                    raise Exception('El nivel_de_amistad indicado en el formulario no existe en la base de datos')  # si existe el registro con la misma cedual genera el error
            else:
                raise Exception('Los datos no fueron digitados por favor validar la información')  # si no tiene todos los valores de genera un error
        except mysql.connector.Error as e:
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e))