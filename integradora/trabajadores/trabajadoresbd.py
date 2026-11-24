from conexionbd import conexion,cursor
class Trabajadores():
    def __init__(self,nombre,apellido1,apellido2,username,password,puesto,telefono,email,estatus,fechaRegistro):
        self._nombre = nombre
        self._apellido1 = apellido1
        self._apellido2 = apellido2
        self._username = username
        self._password = password
        self._puesto  = puesto
        self._telefono = telefono
        self._email = email
        self._estatus = estatus
        self._fechaRegistro = fechaRegistro
    def insertar(self):
        try:
            sql = "INSERT INTO trabajadores VALUES (null, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s)"
            valores = (self._nombre, self._apellido1,self._apellido2, self._username, self._password, self._puesto, self._telefono, self._email, self._estatus, self._fechaRegistro)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error detallado en SQL: {e}") 
            return False
    @staticmethod
    def consultarPorID(id :int):
        try:
            sql = "select * from trabajadores where id = %s"
            valores = (id,)
            cursor.execute(sql, valores)
            return cursor.fetchone()
        except:
            return []
    @staticmethod
    def consultar():
        try:
            sql = "select * from trabajadores"
            cursor.execute(sql,)
            return cursor.fetchall()
        except:
            return []
    @staticmethod
    def validarLogin(username,password):
        try:
            sql = "SELECT username, password FROM trabajadores WHERE username = %s AND password = %s "
            valores = (username, password)
            cursor.execute(sql, valores)
            return cursor.fetchall()
        except:
            return []
    @staticmethod
    def eliminar(id: int):
        try:
            sql = "delete from trabajadores where id= %s "
            valores =  (id,)
            cursor.execute(sql,valores)
            conexion.commit()
            return True
        except:
            return False
    def actualizar(self, id):
        try:
            
            sql = "UPDATE trabajadores SET nombre = %s, apellido1 = %s, apellido2 = %s, username = %s, password = %s, 	puesto = %s, telefono = %s, email = %s, estatus = %s, fechaRegistro = %s WHERE id = %s"
            valores = (self._nombre, self._apellido1,self._apellido2, self._username, self._password, self._puesto, self._telefono, self._email, self._estatus, self._fechaRegistro, id)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre (self, nombre):
        self._nombre = nombre
    @property
    def apellido1(self):
        return self._apellido1
    @apellido1.setter
    def apellido1 (self, apellido1):
        self._apellido1 = apellido1
    @property
    def apellido2(self):
        return self._apellido2
    @apellido2.setter
    def apellido2 (self, apellido2):
        self._apellido2 = apellido2
    @property
    def username(self):
        return self._username
    @username.setter
    def username (self, username):
        self._username = username
    @property
    def puesto(self):
        return self._puesto
    @puesto.setter
    def puesto (self, puesto):
        self._puesto = puesto
    @property
    def telefono(self):
        return self._telefono
    @telefono.setter
    def telefono (self, telefono):
        self._telefono = telefono
    @property
    def email(self):
        return self._email
    @email.setter
    def email (self, email):
        self._email = email
    @property
    def estatus(self):
        return self._estatus
    @estatus.setter
    def estatus (self, estatus):
        self._estatus = estatus
    @property
    def fechaRegistro(self):
        return self._fechaRegistro
    @fechaRegistro.setter
    def fechaRegistro (self, fechaRegistro):
        self._fechaRegistro = fechaRegistro


    #set 
    @nombre.setter
    def nombre (self,nombre):
        self._nombre = nombre
        