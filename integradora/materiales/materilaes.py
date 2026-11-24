from tkinter import * 
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk 
from clientes import clientesbd
from tkcalendar import DateEntry
from cotizaciones import cotizacionbd
from materiales import materialesbd
class MaterialesMVC():
    def __init__(self, ventana, funcionMenu, cotizacion, tipo, id_mat):
        self.ventana = ventana
        self.crearMenuSuperior = funcionMenu
        self.tipo = tipo
        self.ventana.geometry("800x600")
        self.cotizacion = cotizacion
        self.id_mat = id_mat
        if self.tipo == "agregar":
            self.agregarMaterialesView()
        if self.tipo == "editar":
            self.editarMaterialesView()
        else:
            self.mostrarValidacionesview()
        

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()
    def regresarACotizaciones(self):
        from cotizaciones.cotizacion import CotizacionesMVC
        CotizacionesMVC(self.ventana, self.crearMenuSuperior)
    def ejecutarTodoIns(self):
        self.agregarMaterialesController()
        self.regresarACotizaciones()

    
    def ejecutarTodobor(self):
        respuesta = messagebox.askyesno("advertencia", "seguro que deseas actualizar?")
        if respuesta:
            self.editarMaterialesController()
            self.borrarPantalla()
            self.regresarACotizaciones()
        else:
            self.borrarPantalla()
            self.regresarACotizaciones()
    def ejecutarTodoAct(self):
        respuesta = messagebox.askyesno("advertencia", "seguro que deseas actualizar?")
        if respuesta:
            self.editarMaterialesController()
            self.borrarPantalla()
            self.regresarACotizaciones()
        else:
            self.borrarPantalla()
            self.regresarACotizaciones()

    def mostrarValidacionesview(self):
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
        datos = self.consultarCotID()
        self.estatus = ttk.Combobox(frame_izq, values=datos, state="readonly")
        self.estatus.pack(fill="x", pady=2, padx=10)
        self.estatus.current(0)      

    
        
        # Botones de Cotizaciones
        framesBtnIzq = tk.Frame(frame_izq)
        framesBtnIzq.pack(fill="x", pady=10)
        

        self.btnAplicar = Button(framesBtnIzq, text="Editar", command=self.editarcotizacionesview)
        self.btnAplicar.pack(side="right", padx=5)


#---------------------------------- MATRIALES DERECHA--------------------------------
        frame_der = tk.Frame(frame_principal)
        frame_der.grid(row=0, column=1, sticky="nsew", padx=(5, 0))

        Label(frame_der, text="materiales", font=("Arial", 12, "bold")).pack(anchor="w", pady=5)
        
        frame_tabla_mat = tk.Frame(frame_der)
        frame_tabla_mat.pack(fill="both", expand=True, pady=5)
        
        columnas_mat = ("ID", "Material", "Descrip.", "Can.", "Prec", "Total","estatus")
        self.tabla_mat = ttk.Treeview(frame_tabla_mat, columns=columnas_mat, show="headings")
        
        datos_mat = ""
        
        for col in columnas_mat:
            self.tabla_mat.heading(col, text=col)
            self.tabla_mat.column(col, width=65)
            
        if datos_mat:
            for item in datos_mat:
                self.tabla_mat.insert("", tk.END, values=item)
                
        self.tabla_mat.pack(side="top", fill="both", expand=True)
        self.tabla_mat.bind("<<TreeviewSelect>>", self.alSeleccionaraplicar)
        
        # Botones de Materiales
        frame_botones_mat = tk.Frame(frame_der)
        frame_botones_mat.pack(fill="x", pady=10)
        
       
        self.btnAgregarMat = Button(frame_botones_mat, text="Agregar", command=lambda: self.irAMaterialesMVC(self.id_cot_seleccionado,"agregar",None))
        self.btnAgregarMat.pack(side="right", padx=5)
        self.btnAgregarMat.config(state=tk.DISABLED)

        self.btnEditarMat = Button(frame_botones_mat, text="Editar", command=lambda: self.irAMaterialesMVC(self.id_cot_seleccionado,"editar",self.id_mat_seleccionado))
        self.btnEditarMat.pack(side="right", padx=5)
        self.btnEditarMat.config(state=tk.DISABLED)

    def agregarMaterialesView (self):
        self.borrarPantalla()
        contenedor = tk.Frame(self.ventana)
        contenedor.pack(fill="both", expand=True)
        self.crearMenuSuperior(contenedor)

        # --- CONFIGURACIÓN DEL SCROLL ---
        canvas = tk.Canvas(contenedor)
        barra = tk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
        
        frame_form = tk.Frame(canvas)
        frame_form.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=frame_form, anchor="nw")
        canvas.configure(yscrollcommand=barra.set)
        canvas.pack(side="left", fill="both", expand=True)
        barra.pack(side="right", fill="y")
        # ---------------------------------

        Label(frame_form, text="DATOS DE LOS MATERIALES", font=("Arial", 11, "bold")).pack(pady=5)
        Label(frame_form, text="ingrese el nombre del material").pack(anchor="w", pady=2, padx=10)
        self.nombre = Entry(frame_form, width=40)
        self.nombre.focus()
        self.nombre.pack(fill="x", pady=2, padx=10)
        
        Label(frame_form, text="ingrese la descripción del material").pack(anchor="w", pady=2, padx=10)
        self.descripcion = Entry(frame_form, width=40)
        self.descripcion.pack(fill="x", pady=2, padx=10)

        Label(frame_form, text="medida:").pack(anchor="w", pady=2, padx=10)
        self.medida = Entry(frame_form, width=40)
        self.medida.pack(fill="x", pady=2, padx=10)
        
        Label(frame_form, text="ingrese el precio del material").pack(anchor="w", pady=2, padx=10)
        self.precio = Entry(frame_form, width=40)
        self.precio.pack(fill="x", pady=2, padx=10)
        Label(frame_form, text="ingrese la cantidad del material").pack(anchor="w", pady=2, padx=10)
        self.cantidad = Entry(frame_form, width=40)
        self.cantidad.pack(fill="x", pady=2, padx=10)


        
        frame_botones = tk.Frame(frame_form)
        frame_botones.pack(pady=15)
        Button(frame_botones, text='agregar', command= self.ejecutarTodoIns).pack(side="left", padx=5)
        Button(frame_botones, text='::Regresar::', command=self.regresarACotizaciones).pack(side="left", padx=5)



        #_---------------------------- metodo editar --------------------------------
    def editarMaterialesView (self):
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


        Label(frame_form, text="nombre").pack(anchor="w", pady=2, padx=10)
        self.nombreAct = Entry(frame_form, width=40)
        self.nombreAct.pack(fill="x", pady=2, padx=10)
        
        Label(frame_form, text="descripcion").pack(anchor="w", pady=2, padx=10)
        self.descripcionAct = Entry(frame_form, width=40)
        self.descripcionAct.pack(fill="x", pady=2, padx=10)
        
        Label(frame_form, text="medida").pack(anchor="w", pady=2, padx=10)
        self.medidaAct = Entry(frame_form, width=40)
        self.medidaAct.pack(fill="x", pady=2, padx=10)
        
        Label(frame_form, text="precio").pack(anchor="w", pady=2, padx=10)
        self.precioAct = Entry(frame_form, width=40)
        self.precioAct.pack(fill="x", pady=2, padx=10)
        
        Label(frame_form, text="cantidad").pack(anchor="w", pady=2, padx=10)
        self.cantidadAct = Entry(frame_form, width=40)
        self.cantidadAct.pack(fill="x", pady=2, padx=10)
        
        
        frame_botones = tk.Frame(frame_form)
        frame_botones.pack(pady=15)
        Button(frame_botones, text='Borrar', command=self.ejecutarTodobor).pack(side="left", padx=5)
        Button(frame_botones, text='Actualizar', command=self.ejecutarTodoAct).pack(side="left", padx=5)
        Button(frame_botones, text='Regresar', command=self.regresarACotizaciones).pack(side="left", padx=5)
        material = self.buscarMaterialesPorId(self.id_mat)
        if material:
          self.nombreAct.delete(0, "end")
          self.nombreAct.insert(0, material[1])
          self.descripcionAct.delete(0, "end")
          self.descripcionAct.insert(0, material[2])
          self.medidaAct.delete(0, "end")
          self.medidaAct.insert(0, material[3])
          self.precioAct.delete(0, "end")
          self.precioAct.insert(0, material[4])
          self.cantidadAct.delete(0, "end")
          self.cantidadAct.insert(0, material[5])
    



    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(title="::EXITO::", message="Accion como yo ...exitosa")
        else:
            messagebox.showerror(title='VERIFIQUE ', message="Esta accion no pudo realizarse con exito")

        #controladores


    def agregarMaterialesController(self):
        
        nombre = self.nombre.get()
        descripcion = self.descripcion.get()
        medida = self.medida.get()
        precio = self.precio.get()
        cantidad = self.cantidad.get()
        cotizacion = self.cotizacion

        comprado = "pediente"
        materiales = (nombre, descripcion, medida, precio, cantidad,comprado, cotizacion)

        if nombre and descripcion and medida and precio and cantidad is not None:
            materiales = materialesbd.Materiales(*materiales)
            respuesta = materiales.insertar()
            
        else:
            respuesta = False
        self.respuesta_sql(respuesta)
        del materiales
    def buscarMaterialesPorId (self, id_mat):  
        material = materialesbd.Materiales.consultarPorID(id_mat)
        return material
    def editarMaterialesController (self):
        material1 = materialesbd.Materiales(self.nombreAct.get(), self.descripcionAct.get(), self.medidaAct.get(), self.precioAct.get(), self.cantidadAct.get(), "", "")
        respuesta = material1.actualizar(self.id_mat)
        self.respuesta_sql(respuesta)
        del material1


    def consultarCotID (self):
        return materialesbd.Materiales.consultarCotId()
            