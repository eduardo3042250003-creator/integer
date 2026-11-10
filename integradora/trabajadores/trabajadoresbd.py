from conexionbd import conexion,cursor
class trabajadores():
    def __init__(self,nombre,apellido1,apellido2,username,password,puesto,telefono,email,estatus,fechaRegistro,proyectoAsg):
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
        self._proyectoAsg =proyectoAsg

    def insertar(self):
        try:
            sql = "INSERT INTO trabajadores VALUES (null, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s)"
            valores = (self._nombre, self._apellido1,self._apellido2, self._username, self._password, self._puesto, self._telefono, self._email, self._estatus, self._fechaRegistro, self._proyectoAsg)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error detallado en SQL: {e}") 
            return False
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
            
            sql = "UPDATE trabajadores SET nombre = %s, apellido1 = %s, apellido2 = %s, username = %s, password = %s, 	puesto = %s, telefono = %s, estatus = %s, fechaRegistro = %s, 	proyectoAsg = %s,  WHERE id = %s"
            valores = (self._nombre, self._apellido1,self._apellido2, self._username, self._password, self._puesto, self._telefono, self._email, self._estatus, self._fechaRegistro, self._proyectoAsg, id)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False

        