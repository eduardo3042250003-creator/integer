from conexionbd import conexion,cursor
class Clientes():
    def __init__(self,nombre,telefono,email, direccion, numDireccion, colonia, rfc, fechaRegistro, estatus):
        self._nombre = nombre
        self._telefono = telefono
        self._email = email
        self._direccion = direccion
        self._numDireccion = numDireccion
        self._colonia = colonia
        self._rfc = rfc
        self._fechaRegistro = fechaRegistro
        self._estatus = estatus
    #get y set
    #get

    def insertar(self):
        try:
            sql = "INSERT INTO clientes VALUES (null, %s,%s,%s, %s, %s, %s, %s, %s, %s)"
            valores = (self._nombre, self._telefono,self._email, self._direccion,self._numDireccion, self._colonia, self._rfc, self._fechaRegistro, self._estatus)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error detallado en SQL: {e}") 
            return False
    @staticmethod
    def consultarPorID(id :int):
        try:
            sql = "select * from clientes where id = %s"
            valores = (id,)
            cursor.execute(sql, valores)
            return cursor.fetchone()
        except:
            return []
    @staticmethod
    def consultarId():
        try:
            cursor.execute("select id from clientes")
            return cursor.fetchall()
        except:
            return []
    @staticmethod
    def consultar():
        try:
            sql = "select * from clientes"
            cursor.execute(sql,)
            return cursor.fetchall()
        except:
            return []
    @staticmethod
    def eliminar(id: int):
        try:
            sql = "delete from clientes where id= %s "
            valores =  (id,)
            cursor.execute(sql,valores)
            conexion.commit()
            return True
        except:
            return False
    def actualizar(self, id):
        try:
            sql = "UPDATE clientes SET nombre = %s, telefono = %s, email = %s, direccion =  %s,numDireccion	 = %s, colonia = %s,  rfc = %s, fechaRegistro = %s, estatus = %s WHERE id = %s"
            valores = (self._nombre, self._telefono,self._email, self._direccion,self._numDireccion,self._colonia, self._rfc, self._fechaRegistro, self._estatus, id)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False
    def cambiarEstatus(self,id,newEstatus):
        try:
            sql = "UPDATE clientes SET estatus = %s, WHERE id = %s"
            valores = (newEstatus, id)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except:
            return False
    

    @property
    def nombre(self):
        return self._nombre
    @property
    def telefono (self):
        return self._telefono
    @property
    def email(self):
        return self._email
    @property
    def direccion (self):
        return self._direccion
    @property
    def numDireccion(self):
        return self._numDireccion
    @property
    def colonia(self):
        return self._colonia
    @property
    def rfc (self):
        return self._rfc
    @property
    def fechaRegistro (self):
        return self._fechaRegistro
    @property
    def estatus(self):
        return self._estatus
    #set 
    @nombre.setter
    def nombre (self,nombre):
        self._nombre = nombre
    @telefono.setter
    def telefono (self,telefono):
        self._telefono = telefono
    @email.setter
    def email (self, email):
        self._email = email
    @direccion.setter
    def direccion(self,direccion):
        self._direccion = direccion
    @numDireccion.setter
    def numDireccion(self, numDireccion):
        self._numDireccion
    @colonia.setter
    def colonia(self, colonia):
        self._colonia = colonia
    @rfc.setter
    def rfc (self,rfc):
        self._rfc = rfc
    @fechaRegistro.setter
    def fechaRegistro (self,fechaRegistro):
        self._fechaRegistro = fechaRegistro
    @estatus.setter
    def estatus (self, estatus):
        self._estatus = estatus
