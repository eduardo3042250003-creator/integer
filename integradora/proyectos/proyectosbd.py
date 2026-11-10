from conexionbd import conexion,cursor
from datetime import datetime

class Proyectos():
    def __init__(self,fechaInico,fechaFinal,cometarios,estatus,ordenProyectos,estatusCob,fechaEntrega,fechapago,totalPgar):
        self._fechaInico = fechaInico
        self._fechaFinal = fechaFinal
        self._cometarios = cometarios
        self._estatus = estatus
        self._ordenProyectos = ordenProyectos
        self._estatusCob = estatusCob
        self._fechaEntrega = fechaEntrega
        self._fechapago = fechapago
        self._totalPgar = totalPgar


    def insertar(self):
        try:
            sql = "INSERT INTO proyectos VALUES ( %s, %s, %s, %s, %s, %s, %s,%s,%s)"
            valores = (self._fechaInico, self._fechaFinal, self._cometarios, self._estatus, self._ordenProyectos,self._estatusCob, self._fechaEntrega, self._fechapago, self._totalPgar)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error detallado en SQL: {e}") 
            return False  
    @staticmethod
    def consultar():
        try:
            sql = "select * from proyectos"
            cursor.execute(sql,)
            return cursor.fetchall()
        except:
            return [] 
    @staticmethod
    def eliminar(id: int):
        try:
            sql = "delete from proyectos where id= %s "
            valores =  (id,)
            cursor.execute(sql,valores)
            conexion.commit()
            return True
        except:
            return False
    def actualizar(self, id):
        try:
            
            sql = "UPDATE proyectos SET fechaInicio = %s, fechaFinal = %s, comentarios = %s, estatus = %s, ordenProyecto = %s,estatusCob = %s, fechaEntrega = %s, fechaPago = %s, totalPagar = %s, WHERE id = %s"
            valores =(self._fechaInico, self._fechaFinal, self._cometarios, self._estatus, self._ordenProyectos,self._estatusCob, self._fechaEntrega, self._fechapago, self._totalPgar,  id)
            cursor.execute(sql, valores)
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return False
    @property
    def fechaInicio(self):
        return self._fechaInico
    #set 
    @fechaInicio.setter
    def nombre (self,fechaInicio):
        self._fechaInicio = fechaInicio 
    @property
    def fechaFinal(self):
        return self._fechaFinal
    #set 
    @fechaInicio.setter
    def nombre (self,fechaFinal):
        self._fechaFinal = fechaFinal
    @property
    def cometarios(self):
        return self._cometarios
    #set 
    @cometarios.setter
    def cometarios (self,cometarios):
        self._cometarios = cometarios 
    @property
    def estatus(self):
        return self._estatus
    #set 
    @estatus.setter
    def estatus (self,estatus):
        self._estatus = estatus
    @property
    def ordenProyecto (self):
        return self._ordenProyecto
    @ordenProyecto.setter
    def ordenProyecto (self, ordenProyecto):
        self._ordenProyecto = ordenProyecto
    @property
    def estatusCob (self):
        return self._estatusCob
    @estatusCob.setter
    def estatusCob (self, estatusCob):
        self._estatusCob = estatusCob
    @property
    def fechaEntrega (self):
        return self._fechaEntrega
    @fechaEntrega.setter
    def fechaEntrega (self, fechaEntrega):
        self._fechaEntrega = fechaEntrega
    @property
    def fechaPago (self):
        return self._fechaPago
    @fechaPago.setter
    def fechaPago (self, fechaPago):
        self._fechaPago = fechaPago
    @property
    def totalPagar (self):
        return self._totalPagar
    @totalPagar.setter
    def totalPagar (self, totalPagar):
        self._totalPagar = totalPagar
    @property
    def totalPagar (self):
        return self._totalPagar
    @totalPagar.setter
    def totalPagar (self, totalPagar):
        self._totalPagar = totalPagar


 