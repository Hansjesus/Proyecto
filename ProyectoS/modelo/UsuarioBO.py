import mysql.connector # para instalarlo -> pip3 install mysql-connector 



class UsuarioBO:

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
    def guardar(self, usuario):
        try:
            if(self.validar(usuario)):#se valida que tenga la información

                if(not self.exist(usuario)): #si no existe lo agrega
                    usuario.lastUser = "Hns"
                    insertSQL = "INSERT INTO Usuario (`PK_usuario`, `contrasena`, `correo`, `lastUser`, `lastModificacion`) VALUES (%s, %s, %s, %s, CURDATE())"
                    insertValores =  (usuario.usuario.get(),usuario.contrasena.get(),usuario.correo.get(), usuario.lastUser)
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
    def exist(self , usuario):
        try:
            existe = False
            selectSQL = "Select * from Usuario where PK_usuario = " + usuario.usuario.get()
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
    def validar (self, usuario):
        valido = True
        usuario.printInfo()
        if usuario.usuario.get() == "" :
            valido = False
        
        if usuario.contrasena.get() == "" :
            valido = False

        if usuario.correo.get() == "" :
            valido = False


        return valido

    #*************************************************************************
    #Metodo para consultar toda la información de la base de datos
    #*************************************************************************
    def consultar(self ):
        try:
            selectSQL = "select * \
                        from usuario" 
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
    def consultarUsuario(self, usuario):
        try:
            selectSQL = "Select * from Usuario where PK_usuario = " + usuario.usuario.get()
            cursor = self.db.cursor()
            cursor.execute(selectSQL)
            usuarioDB = cursor.fetchone()
            if (usuarioDB) : #Metodo obtiene un solo registro o none si no existe información
                usuario.usuario.set(usuarioDB[0]),
                usuario.contrasena.set(usuarioDB[1])
                usuario.correo.set(usuarioDB[2])
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
    def eliminar(self, usuario):
        try:
            deleteSQL = "delete  from Usuario where PK_usuario = " + usuario.usuario.get()
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
    def modificar(self, usuario):
        try:
            if(self.validar(usuario)):#se valida que tenga la información

                if(self.exist(usuario)): #si  existe lo modifica
                    usuario.lastUser = "Hns"
                    updateSQL = "UPDATE Usuario  set `contrasena` = %s, `correo` = %s, `lastUser` = %s, `lastModificacion` = CURDATE() WHERE `PK_usuario` =  %s"
                    updateValores =  (usuario.contrasena.get(),usuario.correo.get(), usuario.lastUser, usuario.usuario.get())
                    #print(insertValores)
                    cursor = self.db.cursor() #crea un cursos con la conexión lo que nos permite conectarnos a la base de datos
                    cursor.execute(updateSQL, updateValores) #ejecuta el SQL con las valores
                    self.db.commit() #crea un commit en la base de datos
                else:
                    raise Exception('La cédula indicada en el formulario no existe en la base de datos')  # si existe el registro con la misma cedual genera el error
            else:
                raise Exception('Los datos no fueron digitados por favor validar la información')  # si no tiene todos los valores de genera un error
        except mysql.connector.Error as e:
            raise Exception(str(e)) 
        except Exception as e: 
            raise Exception(str(e))