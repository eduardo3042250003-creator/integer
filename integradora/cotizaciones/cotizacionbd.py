from conexionbd import conexion,cursor
class Cotizaciones():
    def __init__(self,numCotizacion, total,estado,revisado,ordenCompra,docOrden,tiempo,trabajadores, id_cliente, descripcion):
        self._numCotizacion = numCotizacion
        self._total = total
        self._estado = estado
        self._revisado = revisado
        self._ordenCompra = ordenCompra
        self._docOrden = docOrden
        self._tiempo = tiempo
        self._trabajadores = trabajadores
        self._id_cliente = id_cliente
        self._descripcion = descripcion

    def insertar(self):
        try:
            sql = "INSERT INTO cotizaciones VALUES ( %s, %s, %s, %s, %s, %s, %s,%s,%s, %s)"
            valores = (self._numCotizacion,self._total, self._estado, self._revisado, self._ordenCompra, self._docOrden, self._tiempo, self._trabajadores, self._id_cliente, self._descripcion)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error detallado en SQL: {e}") 
            return False  
    @staticmethod
    def consultar():
        try:
            sql = "select * from cotizaciones"
            cursor.execute(sql,)
            return cursor.fetchall()
        except:
            return [] 
    @staticmethod
    def eliminar(id: int):
        try:
            sql = "delete from cotizaciones where id= %s "
            valores =  (id,)
            cursor.execute(sql,valores)
            conexion.commit()
            return True
        except:
            return False
    def actualizar(self, id):
        try:
            
            sql = "UPDATE cotizaciones SET numCotizacion = %s, total = %s, estado = %s, revisado = %s, ordenCompra = %s, docOrdenCompra = %s, tiempo = %s, trabajadores = %s, id_cliente = %s, descripcion = %s WHERE id = %s"
            valores =(self._numCotizacion,self._total, self._estado, self._revisado, self._ordenCompra, self._docOrden, self._tiempo, self._trabajadores, self._id_cliente, self._descripcion, id)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False
       
    @property
    def numCotizacion(self):
        return self._numCotizacion
    @property
    def total(self):
        return self>self._total
    @property
    def estado (self):
        return self._estado
    @property
    def revisado(self):
        return self._revisado
    @property
    def ordenCompra(self):
        return self._ordenCompra
    @property
    def docOrden(self):
        return self._docOrden
    @property
    def tiempo(self):
        return self._tiempo
    @property
    def trabajadores(self):
        return self._trabajadores
    #SET
    @numCotizacion.setter
    def numCotizacion (self,numCotizacion):
        self._numCotizacion = numCotizacion
    @total.setter
    def total (self,total):
        self._total = total
    @estado.setter
    def estado (self,estado):
        self._estado = estado
    @revisado.setter
    def revisado (self,revisado):
        self._revisado = revisado
    @ordenCompra.setter
    def ordenCompra (self,ordenCompra):
        self._ordenCompra = ordenCompra
    @docOrden.setter
    def docOrden (self,docOrden):
        self._docOrden = docOrden
    @tiempo.setter
    def tiempo (self,tiempo):
        self._tiempo = tiempo
    @trabajadores.setter
    def tiempo (self,trabajadores):
        self._trabajadores = trabajadores








        