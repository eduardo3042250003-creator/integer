from tkinter import * 
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk 
from clientes import clientesbd
from tkcalendar import DateEntry
from cotizaciones import cotizacionbd
from materiales import materialesbd
from datetime import date, datetime, timedelta
from materiales.materilaes import MaterialesMVC

class CotizacionesMVC():
    def __init__(self, ventana, funcionMenu):
        self.ventana = ventana
        self.crearMenuSuperior = funcionMenu
        self.ventana.geometry("800x600")
        self.mostrarCotizacionesView()
    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()
    ##par llamar y tener conexion con el modulo de materiales
    def irAMaterialesMVC(self,cotizacion_id, tipo, id_mat):
        print("Tipo de acción:", tipo)
        MaterialesMVC(self.ventana, self.crearMenuSuperior, cotizacion_id, tipo,id_mat)
    def ejecutarTodoIns (self,datos,idcl,trabajadores,idTrabajadores):
        self.agregarCotizacionController(datos,idcl,trabajadores,idTrabajadores)
        self.borrarPantalla()
        self.mostrarCotizacionesView()
    def ejecutarTodoAct(self,datos,idcl,trabajadores,idTrabajadores):
        respuesta = messagebox.askyesno("advertencia", "seguro que deseas actualizar?")
        if respuesta:
            self.editarCotizacionController(datos,idcl,trabajadores,idTrabajadores)
            self.borrarPantalla()
            self.mostrarCotizacionesView()
        else:
            self.borrarPantalla()
            self.mostrarCotizacionesView()

    def mostrarCotizacionesView(self):
        self.borrarPantalla()
        contenedor = tk.Frame(self.ventana)
        contenedor.pack(fill="both", expand=True)

        self.crearMenuSuperior(contenedor)
        frame_principal = tk.Frame(contenedor)
        frame_principal.pack(fill="both", expand=True, padx=10, pady=10)
        frame_principal.grid_columnconfigure(0, weight=1, uniform="mitad")
        frame_principal.grid_columnconfigure(1, weight=1, uniform="mitad")
        frame_principal.grid_rowconfigure(0, weight=1)

        frame_izq = tk.Frame(frame_principal)
        frame_izq.grid(row=0, column=0, sticky="nsew", padx=(0, 5))

        Label(frame_izq, text="Cotizacion", font=("Arial", 12, "bold")).pack(anchor="w", pady=5)
        
        frame_tabla_cot = tk.Frame(frame_izq)
        frame_tabla_cot.pack(fill="both", expand=True, pady=5)
        
        columnas_cot = ("Id", "Cliente", "Total", "Descrip.", "Material")
        tabla_cot = ttk.Treeview(frame_tabla_cot, columns=columnas_cot, show="headings")
        

        datos_cot = self.mostrarCotizacionesController() 
        
        for col in columnas_cot:
            tabla_cot.heading(col, text=col)
            tabla_cot.column(col, width=70)
            
        if datos_cot:
            for item in datos_cot:
                tabla_cot.insert("", tk.END, values=item)
                
        tabla_cot.pack(side="top", fill="both", expand=True)
        tabla_cot.bind("<<TreeviewSelect>>", self.alSeleccionarCotizacion)
        
        # Botones de Cotizaciones
        frame_botones_cot = tk.Frame(frame_izq)
        frame_botones_cot.pack(fill="x", pady=10)
        
        Button(frame_botones_cot, text="Agregar", command=self.agregarCotizacionView).pack(side="right", padx=5)

        self.btnEditarCot = Button(frame_botones_cot, text="Editar", command=self.editarcotizacionesview)
        self.btnEditarCot.pack(side="right", padx=5)
        self.btnEditarCot.config(state=tk.DISABLED)

#---------------------------------- MATRIALES DERECHA--------------------------------
        frame_der = tk.Frame(frame_principal)
        frame_der.grid(row=0, column=1, sticky="nsew", padx=(5, 0))

        Label(frame_der, text="materiales", font=("Arial", 12, "bold")).pack(anchor="w", pady=5)
        
        frame_tabla_mat = tk.Frame(frame_der)
        frame_tabla_mat.pack(fill="both", expand=True, pady=5)
        
        columnas_mat = ("ID", "Material", "Descrip.", "Can.", "Prec", "Total")
        self.tabla_mat = ttk.Treeview(frame_tabla_mat, columns=columnas_mat, show="headings")
        
        datos_mat = ""
        
        for col in columnas_mat:
            self.tabla_mat.heading(col, text=col)
            self.tabla_mat.column(col, width=65)
            
        if datos_mat:
            for item in datos_mat:
                self.tabla_mat.insert("", tk.END, values=item)
                
        self.tabla_mat.pack(side="top", fill="both", expand=True)
        self.tabla_mat.bind("<<TreeviewSelect>>", self.alSeleccionarMaterial)
        
        # Botones de Materiales
        frame_botones_mat = tk.Frame(frame_der)
        frame_botones_mat.pack(fill="x", pady=10)
        
       
        self.btnAgregarMat = Button(frame_botones_mat, text="Agregar", command=lambda: self.irAMaterialesMVC(self.id_cot_seleccionado,"agregar",None))
        self.btnAgregarMat.pack(side="right", padx=5)
        self.btnAgregarMat.config(state=tk.DISABLED)

        self.btnEditarMat = Button(frame_botones_mat, text="Editar", command=lambda: self.irAMaterialesMVC(self.id_cot_seleccionado,"editar",self.id_mat_seleccionado))
        self.btnEditarMat.pack(side="right", padx=5)
        self.btnEditarMat.config(state=tk.DISABLED)
    def agregarCotizacionView(self):
        self.borrarPantalla()
        contenedor = tk.Frame(self.ventana)
        contenedor.pack(fill="both", expand=True)
        self.crearMenuSuperior(contenedor)
        # --- CONFIGURACIÓN DEL SCROLL ---
        canvas = tk.Canvas(contenedor)
        barra = tk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
        frame_form = tk.Frame(canvas)
        frame_form.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=frame_form, anchor="nw")
        canvas.configure(yscrollcommand=barra.set)

        canvas.pack(side="left", fill="both", expand=True)
        barra.pack(side="right", fill="y")
        Label(frame_form, text="DATOS DE LA COTIZACIÓN", font=("Arial", 11, "bold")).pack(pady=5)
        datos,idcl = self.consultarClientes()
    
        Label(frame_form, text="selecione cliente").pack(anchor="w", pady=2, padx=10)
        self.idcliente = ttk.Combobox(frame_form, values=datos, state="readonly")
        
        self.idcliente.pack(fill="x", pady=2, padx=10)

        trabajadores,idTrabajadores =  self.consultartrabajadores()
        
        self.revisado = ttk.Combobox(frame_form, values=trabajadores, state="readonly")
        self.revisado.pack(fill="x", pady=2, padx=10)
        
        Label(frame_form, text="ingrese la fecha estimada de entrega").pack(anchor="w", pady=2, padx=10)
        self.registro = DateEntry(frame_form, selectmode='day')
        self.registro.pack(fill="x", pady=2, padx=10)

        Label(frame_form, text="presupuesto del cliente").pack(anchor="w", pady=2, padx=10)
        self.presupuesto = Entry(frame_form, width=40)
        self.presupuesto.pack(fill="x", pady=2, padx=10)
        
        Label(frame_form, text="ingrese cuantos empleados necesita").pack(anchor="w", pady=2, padx=10)
        self.numEmpleados = Entry(frame_form, width=40)
        self.numEmpleados.pack(fill="x", pady=2, padx=10)

        Label(frame_form, text="ingrese descripcion del proyecto:").pack(anchor="w", pady=2, padx=10)
        self.descripcion = Entry(frame_form, width=40)
        self.descripcion.pack(fill="x", pady=2, padx=10)
        
        frame_botones = tk.Frame(frame_form)
        frame_botones.pack(pady=15)
        Button(frame_botones, text='agregar', command=lambda: self.ejecutarTodoIns(datos,idcl,trabajadores,idTrabajadores)).pack(side="left", padx=5)
        Button(frame_botones, text='::Regresar::', command=self.mostrarCotizacionesView).pack(side="left", padx=5)
    def editarcotizacionesview(self):
        self.borrarPantalla()
        contenedor = tk.Frame(self.ventana)
        contenedor.pack(fill="both", expand=True)
        self.crearMenuSuperior(contenedor)
        canvas = tk.Canvas(contenedor)
        barra = tk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
        frame_form = tk.Frame(canvas)
        frame_form.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=frame_form, anchor="nw")
        canvas.configure(yscrollcommand=barra.set)
        canvas.pack(side="left", fill="both", expand=True)
        barra.pack(side="right", fill="y")

        Label(frame_form, text="editar cotizacion", font=("Arial", 11, "bold")).pack(pady=5)
        datos,idcl = self.consultarClientes()
    
        Label(frame_form, text="selecione cliente").pack(anchor="w", pady=2, padx=10)
        self.idclienteAct = ttk.Combobox(frame_form, values=datos, state="readonly")
        
        self.idclienteAct.pack(fill="x", pady=2, padx=10)

        trabajadores,idTrabajadores =  self.consultartrabajadores()
        
        self.revisadoAct = ttk.Combobox(frame_form, values=trabajadores, state="readonly")
        self.revisadoAct.pack(fill="x", pady=2, padx=10)
        Label(frame_form, text="ingrese la fecha estimada de entrega").pack(anchor="w", pady=2, padx=10)
        """
        self.registroAct = DateEntry(frame_form, selectmode='day')
        self.registroAct.pack(fill="x", pady=2, padx=10)
        """
        self.registroAct = DateEntry(frame_form, selectmode='day')
        self.registroAct.pack(fill="x", pady=2, padx=10)

        Label(frame_form, text="presupuesto del cliente").pack(anchor="w", pady=2, padx=10)
        self.presupuestoAct = Entry(frame_form, width=40)
        self.presupuestoAct.pack(fill="x", pady=2, padx=10)
        
        Label(frame_form, text="ingrese cuantos empleados necesita").pack(anchor="w", pady=2, padx=10)
        self.numEmpleadosAct = Entry(frame_form, width=40)
        self.numEmpleadosAct.pack(fill="x", pady=2, padx=10)

        Label(frame_form, text="ingrese descripcion del proyecto:").pack(anchor="w", pady=2, padx=10)
        self.descripcionAct = Entry(frame_form, width=40)
        self.descripcionAct.pack(fill="x", pady=2, padx=10)

        frame_botones = tk.Frame(frame_form)
        frame_botones.pack(pady=15)
        Button(frame_botones, text='Borrar',state=DISABLED, command=None).pack(side="left", padx=5)
        Button(frame_botones, text='Actualizar', command=lambda: self.ejecutarTodoAct(datos,idcl,trabajadores,idTrabajadores)).pack(side="left", padx=5)
        Button(frame_botones, text='Regresar', command=self.mostrarCotizacionesView).pack(side="left", padx=5)
        cotizacion1 = self.buscarcotizacionPorId(self.id_cot_seleccionado)

        if cotizacion1:
                    
                    self.idclienteAct.set(cotizacion1[6])
                    print(cotizacion1[6])
                    self.revisadoAct.set(cotizacion1[3])
        

                    self.registroAct.set_date( cotizacion1[4])
                    self.presupuestoAct.delete(0, "end")
                    self.presupuestoAct.insert(0, cotizacion1[2])
                    self.numEmpleadosAct.delete(0, "end")
                    self.numEmpleadosAct.insert(0, cotizacion1[5])
                    self.descripcionAct.delete(0, "end")
                    self.descripcionAct.insert(0, cotizacion1[7])

        #self.registroAct.set_date(trabajador[10])
        

    def alSeleccionarCotizacion(self, event):
        seleccion = event.widget.selection()
        if seleccion:
            valores = event.widget.item(seleccion[0], "values")
            self.id_cot_seleccionado = valores[0]
            self.btnEditarCot.config(state="normal")
            self.btnAgregarMat.config(state="normal")
            for fila in self.tabla_mat.get_children():
                self.tabla_mat.delete(fila)
            materiales = self.buscarMaterialesPorId(self.id_cot_seleccionado)
            if materiales:
                for mat in materiales:
                    self.tabla_mat.insert("", tk.END, values=mat)

    def alSeleccionarMaterial(self, event):
        seleccion = event.widget.selection()
        if seleccion:
            valores = event.widget.item(seleccion[0], "values")
            self.id_mat_seleccionado = valores[0]
            self.btnEditarMat.config(state="normal")
    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(title="::EXITO::", message="Accion como yo ...exitosa")
        else:
            messagebox.showerror(title='VERIFIQUE ', message="Esta accion no pudo realizarse con exito")
    #controladores
    def buscarcotizacionPorId (self,numCot):
        print(numCot)
        cotizacion = cotizacionbd.Cotizaciones.consultarCotId(numCot)
        print(cotizacion)

        dias = cotizacion[4]
        fecha_estimada = date.today() + timedelta(days=dias)
        
        cotizacion_tupla = (cotizacion[0],cotizacion[1], cotizacion[2], cotizacion[3],fecha_estimada, cotizacion[5], cotizacion[6], cotizacion[7])
        print (fecha_estimada)
        return cotizacion_tupla

    def mostrarCotizacionesController (self):
        return cotizacionbd.Cotizaciones.consultarCot()
    
    def buscarMaterialesPorId(self, id):
        materiales = materialesbd.Materiales.consultarId(id)

        if not materiales:
                    return []
        materiales_con_total = []
        for fila in materiales:
            precio_u = float(fila[4])
            cantidad = float(fila[5])
            total = precio_u * cantidad
            fila_formateada = (fila[0], fila[1], fila[2], fila[5], fila[4], total,)
            materiales_con_total.append(fila_formateada)
            print()

        return materiales_con_total


    def consultarClientes (self):
        datos =  cotizacionbd.Cotizaciones.consultarNombres()
        clientes = []
        ids = []
        if not datos:
            return ["sin valores"], []
        for dato in datos:
            clientes.append(f"{dato[0]} {dato[1]}")
            ids.append(dato[0])
        return clientes, ids
    def consultartrabajadores (self):
        datos = cotizacionbd.Cotizaciones.obtenerDatosTrab()
        
        trabajadores = []
        ids = []
        if not datos:
            return ["sin valores"], []

        for dato in datos:
            nombres = f"{dato[0]} {dato[1]} {dato[2]}"
            trabajadores.append(nombres)
            ids.append(dato[0])
        return trabajadores, ids
    def agregarCotizacionController (self,datos,idcl,trabajadores,idTrabajadores):

        for i in range(len(datos)):
            if self.idcliente.get() == datos[i]:
                id = idcl [i]

                break
        for i in range(len(trabajadores)):
            if self.revisado.get() == trabajadores[i]:
                rev = idTrabajadores[i]
                break
        fechaRegi = self.registro.get_date()
        hoy = date.today()
        tiempo = (fechaRegi - hoy).days
        cotizacion1 = cotizacionbd.Cotizaciones(self.presupuesto.get(),"nuevo",rev,None,None, tiempo, self.numEmpleados.get(),id, self.descripcion.get() )
        respuesta = cotizacion1.insertar()
        self.respuesta_sql(respuesta)
        del cotizacion1

    def editarCotizacionController (self,datos,idcl,trabajadores,idTrabajadores):
        fechaRegi = self.registroAct.get_date()
        hoy = date.today()
        tiempo = (fechaRegi - hoy).days
        for i in range(len(datos)):
            if self.idclienteAct.get() == datos[i]:
                id = idcl [i]

                break
        for i in range(len(trabajadores)):
            if self.revisadoAct.get() == trabajadores[i]:
                rev = idTrabajadores[i]
                break
        
        cotizacion1 = cotizacionbd.Cotizaciones(self.presupuestoAct.get(),"nuevo",rev,None,None,tiempo, self.numEmpleadosAct.get(),id, self.descripcionAct.get() )
        respuesta = cotizacion1.actualizar(self.id_cot_seleccionado)
        self.respuesta_sql(respuesta)
        
        del cotizacion1


