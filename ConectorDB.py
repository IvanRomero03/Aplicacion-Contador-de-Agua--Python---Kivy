import mysql.connector
import time
from datetime import datetime
# Conexion a la base de datos con la clase conector
# hostname: 'database-2.czklrrr38xte.us-east-1.rds.amazonaws.com'
# puerto: 3306
# user: 'admin'
# password: 'basededatos'
# database: 'RegistoUsuarios-Agua'

class BaseDeDatos:
    def __init__(self):
        self.DB = mysql.connector.connect(
            host="database-2.czklrrr38xte.us-east-1.rds.amazonaws.com",
            user="admin",
            passwd="basededatos",
            database="RegistoUsuarios-Agua"
        )
        self.cursor = self.DB.cursor()

    def verUsuarios(self):
        self.cursor.execute("SELECT * FROM usuarios;")
        usuarios = self.cursor.fetchall()
        return usuarios

    def verRegistros(self):
        self.cursor.execute("SELECT * FROM RegistrosAgua;")
        registros = self.cursor.fetchall()
        return registros

    def selectRegistrosUsuario(self, idUsuario:int):
        query = 'SELECT * FROM RegistrosAgua WHERE idUsuario ='+ str(idUsuario)+ ';'
        self.cursor.execute(query)
        registros = self.cursor.fetchall()
        return registros

    def insertarRegistro(self,idUsuario:int):
        query = "INSERT INTO RegistrosAgua(idUsuario) VALUES (" + str(idUsuario) + ");"
        self.cursor.execute(query)
        self.DB.commit()

    def insertarUsuario(self, nombre:str, correo:str, contrasena:str):
        query = "INSERT INTO usuarios(nombre, correo, contraseña) VALUES ("+ str(nombre) +", "+ str(correo) +", "+ str(contrasena) +");"
        self.cursor.execute(query)
        self.DB.commit()
    
    def selectRegistroUsuarioFecha(self, idUsuario:int, fechaInicio:datetime, fechaFin:datetime):
        fechaInicio.strftime("%Y-%m-%d %H:%M:%S")
        fechaFin.strftime("%Y-%m-%d %H:%M:%S")
        query = 'SELECT * FROM RegistrosAgua WHERE idUsuario = '+ str(idUsuario)+ ' AND RegistrosAguacol > \''+ str(fechaInicio) +'\' AND RegistrosAguacol > \''+ str(fechaFin) +'\';'
        self.cursor.execute(query)
        registros = self.cursor.fetchall()
        return registros
    def cerrar(self):
        self.DB.close()

def desplegarTabla(registros):
    for i in registros:
        print(i)

def demostracion():
    DB = BaseDeDatos()
    desplegarTabla(DB.verUsuarios())
    print('usuarios')

    desplegarTabla(DB.verRegistros())
    print('registros')

    desplegarTabla(DB.selectRegistrosUsuario(1))
    print('registros usuario')

    desplegarTabla(DB.selectRegistroUsuarioFecha(1, datetime(2020, 1, 1, 0, 0, 0), datetime.now()))
    print('registros usuario fecha')

    DB.cerrar()