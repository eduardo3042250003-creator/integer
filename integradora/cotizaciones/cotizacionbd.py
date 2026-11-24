from conexionbd import conexion,cursor
class Cotizaciones():
    def __init__(self, total,estado,revisado,ordenCompra,docOrden,tiempo,trabajadores, id_cliente, descripcion):
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
            sql = "INSERT INTO cotizaciones VALUES (null, %s, %s, %s, %s, %s, %s,%s,%s, %s)"
            valores = (self._total, self._estado, self._revisado, self._ordenCompra, self._docOrden, self._tiempo, self._trabajadores, self._id_cliente, self._descripcion)
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
    def consultarCotId(id: int):
        try:
            sql = """
            SELECT
                cot.numCotizacion,
                cot.total,
                cot.estado,
                CONCAT_WS(' ', t.id, t.nombre, t.apellido1) AS revisado_por,
                cot.tiempo,
                cot.trabajadores,
                CONCAT_WS(' ', cli.id, cli.nombre) AS cliente,
                cot.descripcion
            FROM cotizaciones AS cot
            LEFT JOIN trabajadores AS t ON cot.revisado = t.id
            LEFT JOIN clientes AS cli ON cot.id_cliente = cli.id
            WHERE cot.numCotizacion = %s
            """
            cursor.execute(sql, (id,))
            return cursor.fetchone()
        except Exception as e:
            print("Error en consultarCotId:", e)
            return []
    @staticmethod
    def consultarNombres ():
        try:
            sql = "select id, nombre from clientes"
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
    @staticmethod
    def obtenerDatosTrab ():
        try:
            sql = "select id, nombre,apellido1 from trabajadores"
            cursor.execute(sql,)
            return cursor.fetchall()
        except:
            return [] 
    @staticmethod
    def consultarCot ():
        try:
            sql =   "SELECT c.numCotizacion,cl.nombre AS cliente, c.total, c.descripcion, c.ordenCompra FROM cotizaciones AS c LEFT JOIN clientes AS cl ON c.id_cliente = cl.id;"
            cursor.execute(sql,)
            return cursor.fetchall()
        except:
            return False


    

  
    def actualizar(self, id):
        try:
            
            sql = "UPDATE cotizaciones SET total = %s, estado = %s, revisado = %s, ordenCompra = %s , docOrdenCompra = %s,  tiempo = %s, trabajadores = %s, id_cliente = %s, descripcion = %s WHERE numCotizacion = %s"
            valores =(self._total, self._estado, self._revisado, self._ordenCompra, self._docOrden, self._tiempo, self._trabajadores, self._id_cliente, self._descripcion, id)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            
            return False
       
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








        