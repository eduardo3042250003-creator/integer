from conexionbd import conexion,cursor
class materiales():
    def __init__(self,nombre,descripcion, medida, precioU, comprado,cotizacion):
        self._nombre = nombre
        self._descripcion = descripcion
        self._medida = medida
        self._precioU = precioU 
        self._comprado = comprado
        self._cotizacion = cotizacion
    def insertar(self):
        try:
            sql = "INSERT INTO materiales VALUES (null, %s, %s, %s, %s, %s, %s, )"
            valores = (self._nombre, self._descripcion, self._medida, self._precioU, self._comprado, self._cotizacion)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error detallado en SQL: {e}") 
            return False
    @staticmethod
    def consultar():
        try:
            sql = "select * from materiales"
            cursor.execute(sql,)
            return cursor.fetchall()
        except:
            return []
    @staticmethod
    def eliminar(id: int):
        try:
            sql = "delete from materiales where id= %s "
            valores =  (id,)
            cursor.execute(sql,valores)
            conexion.commit()
            return True
        except:
            return False
    def actualizar(self, id):
        try:
            
            sql = "UPDATE materiales SET nombre = %s, descripcion = %s, medida = %s, precioU = %s, comprado = %s, 	cotizacion = %s, WHERE id = %s"
            valores = (self._nombre, self._descripcion, self._medida, self._precioU, self._comprado, self._cotizacion, id)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False

    #set y get`
    #get
    @property
    def nombre(self):
        return self.nombre
    @property
    def descripcion(self):
        return self.descripcion
    @property
    def medida(self):
        return self._medida
    @property
    def precioU(self):
        return self.precioU
    @property
    def comprado(self):
        return self._comprado
    @property
    def cotizacion(self):
        return self._cotizacion
    ##set
    @nombre.setter
    def nombre (self,nombre):
        self.nombre = nombre
    @descripcion.setter
    def descripcion (self,descripcion):
        self.descripcion = descripcion
    @medida.setter
    def medida (self, medida):
        self._medida = medida
    @precioU.setter 
    def precioU (self,precioU):
        self._precioU = precioU
    @comprado.setter
    def comprado(self, comprado):
        self._comprado = comprado
    @cotizacion.setter
    def cotizacion (self, cotizacion):
        self._cotizacion = cotizacion
