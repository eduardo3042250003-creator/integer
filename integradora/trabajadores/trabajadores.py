from tkinter import * 
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk 
from clientes import clientesbd
from tkcalendar import DateEntry

from trabajadores import trabajadoresbd

class TrabajadoresMVC():
    def __init__(self, ventana, funcionMenu):
        self.ventana = ventana
        self.crearMenuSuperior = funcionMenu
        self.ventana.geometry("800x600")
        self.mostrarTrabajadoresView()
    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()
    def ejecutarTodoIns(self):
        self.agregarTrabajadoresController()
        self.borrarPantalla()
        self.agregarTrabajadoresView()
    def ejecutarTodoAct(self):
        respuesta = messagebox.askyesno("advertencia", "seguro que deseas actualizar?")
        if respuesta:
            self.editartrabajadoresController()
            self.borrarPantalla()
            self.mostrarTrabajadoresView()
        else:
            self.borrarPantalla()
            self.editarTrabajadoresView()
    def ejecutarTodobor(self):
        respuesta = messagebox.askyesno("advertencia", "seguro que deseas borrar?")
        if respuesta:
            self.borrarTrabajadoresController()
            self.borrarPantalla()
            self.mostrarTrabajadoresView()
        else:
            self.borrarPantalla()
            self.editarTrabajadoresView()
    def mostrarTrabajadoresView(self):
        self.borrarPantalla()
        contenedor = tk.Frame(self.ventana)
        contenedor.pack(fill="both", expand=True)
        self.crearMenuSuperior(contenedor)
        Label(contenedor, text="trabajadores").pack(anchor="w", padx=10, pady=5)
        frame_tabla = tk.Frame(contenedor)
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=5)
        columnas = ("id", "nombre", "apellido P", "apellido M", "username", "password","puesto", "telefono ", "email", "Estatus","fechaRegistro")
        tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
        datos = self.mostrarTrabajadoresController()
        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, width=80)
        if datos:
            for trabajador in datos:
                tabla.insert("", tk.END, values=trabajador)
        tabla.pack(side="top", fill="both", expand=True)
        tabla.bind("<<TreeviewSelect>>", self.alSeleccionar) 
        frame_botones = tk.Frame(contenedor)
        frame_botones.pack(fill="x", padx=10, pady=10)
        Button(frame_botones, text="agregar", command=self.agregarTrabajadoresView).pack(side="right", padx=5)
        self.ButtonEditar = Button(frame_botones, text="Editar", command=self.editarTrabajadoresView)
        self.ButtonEditar.pack(side="right", padx=5)
        self.ButtonEditar.config(state=tk.DISABLED)
    def alSeleccionar(self,event):
        seleccion = event.widget.selection()
        if seleccion:
            valores = event.widget.item(seleccion[0], "values")
            self.id_seleccionado = valores[0]
            self.ButtonEditar.config(state="normal")
    def agregarTrabajadoresView(self):
        self.borrarPantalla()
        contenedor = tk.Frame(self.ventana)
        contenedor.pack(fill="both", expand=True)
        self.crearMenuSuperior(contenedor)
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
        Label(frame_form, text="DATOS DEL TRABAJADOR", font=("Arial", 11, "bold")).pack(pady=5)
        Label(frame_form, text="ingrese el nombre del trabajador").pack(anchor="w", pady=2, padx=10)
        self.nombre = Entry(frame_form, width=40)
        self.nombre.focus()
        self.nombre.pack(fill="x", pady=2, padx=10)
        Label(frame_form, text="ingrese el apellido paterno del trabajador").pack(anchor="w", pady=2, padx=10)
        self.apellidoP = Entry(frame_form, width=40)
        self.apellidoP.pack(fill="x", pady=2, padx=10)
        Label(frame_form, text="ingrese el apellido materno del trabajador").pack(anchor="w", pady=2, padx=10)
        self.apellidoM = Entry(frame_form, width=40)
        self.apellidoM.pack(fill="x", pady=2, padx=10)
        Label(frame_form, text="username:").pack(anchor="w", pady=2, padx=10)
        self.username = Entry(frame_form, width=40)
        self.username.pack(fill="x", pady=2, padx=10)
        Label(frame_form, text="password:").pack(anchor="w", pady=2, padx=10)
        self.password = Entry(frame_form, width=40)
        self.password.pack(fill="x", pady=2, padx=10)
        Label(frame_form, text="puesto").pack(anchor="w", pady=2, padx=10)
        self.puesto = Entry(frame_form, width=40)
        self.puesto.pack(fill="x", pady=2, padx=10)
        Label(frame_form, text="ingrese la telefono del trabajador").pack(anchor="w", pady=2, padx=10)
        self.telefono = Entry(frame_form, width=40)
        self.telefono.pack(fill="x", pady=2, padx=10)       
        
        Label(frame_form, text="ingrese EL email del trabajador").pack(anchor="w", pady=2, padx=10)
        self.email = Entry(frame_form, width=40)
        self.email.pack(fill="x", pady=2, padx=10)
        
        Label(frame_form, text="ingrese el estatus del trabajador").pack(anchor="w", pady=2, padx=10)
        datos = ("activo", "inactivo")
        self.estatus = ttk.Combobox(frame_form, values=datos, state="readonly")
        self.estatus.pack(fill="x", pady=2, padx=10)
        self.estatus.current(0)      
        Label(frame_form, text="ingrese la fecha de registro del trabajador").pack(anchor="w", pady=2, padx=10)
        self.registro = DateEntry(frame_form, selectmode='day')
        self.registro.pack(fill="x", pady=2, padx=10)
        frame_botones = tk.Frame(frame_form)
        frame_botones.pack(pady=15)
        Button(frame_botones, text='agregar', command=self.ejecutarTodoIns).pack(side="left", padx=5)
        Button(frame_botones, text='::Regresar::', command=self.mostrarTrabajadoresView).pack(side="left", padx=5)   
    def editarTrabajadoresView(self):
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
        Label(frame_form, text=f"id seleccionado {self.id_seleccionado}").pack(anchor="w", pady=2, padx=10)
        Label(frame_form, text="nombre").pack(anchor="w", pady=2, padx=10)
        self.nombreAct = Entry(frame_form, width=40)
        self.nombreAct.pack(fill="x", pady=2, padx=10)
        Label(frame_form, text="apellido paterno").pack(anchor="w", pady=2, padx=10)
        self.apellidoPAct = Entry(frame_form, width=40)
        self.apellidoPAct.pack(fill="x", pady=2, padx=10)
        Label(frame_form, text="apellido materno").pack(anchor="w", pady=2, padx=10)
        self.apellidoMAct = Entry(frame_form, width=40)
        self.apellidoMAct.pack(fill="x", pady=2, padx=10)
        Label(frame_form, text="username").pack(anchor="w", pady=2, padx=10)
        self.usernameAct = Entry(frame_form, width=40)
        self.usernameAct.pack(fill="x", pady=2, padx=10)
        Label(frame_form, text="password").pack(anchor="w", pady=2, padx=10)
        self.passwordAct = Entry(frame_form, width=40, show="*")
        self.passwordAct.pack(fill="x", pady=2, padx=10)
        Label(frame_form, text="puesto").pack(anchor="w", pady=2, padx=10)
        self.puestoAct = Entry(frame_form, width=40)
        self.puestoAct.pack(fill="x", pady=2, padx=10)
        Label(frame_form, text="telefono").pack(anchor="w", pady=2, padx=10)
        self.telefonoAct = Entry(frame_form, width=40)
        self.telefonoAct.pack(fill="x", pady=2, padx=10)
        Label(frame_form, text="email").pack(anchor="w", pady=2, padx=10)
        self.emailAct = Entry(frame_form, width=40)
        self.emailAct.pack(fill="x", pady=2, padx=10)
        Label(frame_form, text="ingrese el estatus del cliente").pack(anchor="w", pady=2, padx=10)
        datos_estatus = ("activo", "inactivo")
        self.estatusAct = ttk.Combobox(frame_form, values=datos_estatus, state="readonly")
        self.estatusAct.pack(fill="x", pady=2, padx=10)
        self.estatusAct.current(0)  
        Label(frame_form, text="ingrese la fecha de registro del cliente").pack(anchor="w", pady=2, padx=10)
        self.registroAct = DateEntry(frame_form, selectmode='day')
        self.registroAct.pack(fill="x", pady=2, padx=10)
        frame_botones = tk.Frame(frame_form)
        frame_botones.pack(pady=15)
        Button(frame_botones, text='borrar', command=self.ejecutarTodobor).pack(side="left", padx=5)
        Button(frame_botones, text='Actualizar', command=self.ejecutarTodoAct).pack(side="left", padx=5)
        Button(frame_botones, text='Regresar', command=self.mostrarTrabajadoresView).pack(side="left", padx=5) 
        trabajador = self.buscarTrabajadorPorId(self.id_seleccionado)
        if trabajador:
          self.nombreAct.delete(0, "end")
          self.nombreAct.insert(0, trabajador[1])
          self.apellidoPAct.delete(0, "end")
          self.apellidoPAct.insert(0, trabajador[2])
          self.apellidoMAct.delete(0, "end")
          self.apellidoMAct.insert(0, trabajador[3])
          self.usernameAct.delete(0, "end")
          self.usernameAct.insert(0, trabajador[4])
          self.passwordAct.delete(0, "end")
          self.passwordAct.insert(0, trabajador[5])
          self.puestoAct.delete(0, "end")
          self.puestoAct.insert(0, trabajador[6])
          self.telefonoAct.delete(0, "end")
          self.telefonoAct.insert(0, trabajador[7])
          self.emailAct.delete(0, "end")
          self.emailAct.insert(0, trabajador[8])
          self.estatusAct.set(trabajador[9])
          self.registroAct.set_date(trabajador[10])

    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(title="::EXITO::", message="Accion como yo ...exitosa")
        else:
            messagebox.showerror(title='VERIFIQUE ', message="Esta accion no pudo realizarse con exito")

    def mostrarTrabajadoresController(self):
        return trabajadoresbd.Trabajadores.consultar()
    def agregarTrabajadoresController(self):
        trabajador = trabajadoresbd.Trabajadores(
            self.nombre.get(),
            self.apellidoP.get(),
            self.apellidoM.get(),
            self.username.get(),
            self.password.get(),
            self.puesto.get(),
            self.telefono.get(),
            self.email.get(),
            self.estatus.get(),
            self.registro.get_date()
        )
        respuesta = trabajador.insertar()
        self.respuesta_sql(respuesta)
        del trabajador
    def editartrabajadoresController(self):
        trabajador = trabajadoresbd.Trabajadores(
            self.nombreAct.get(),
            self.apellidoPAct.get(),
            self.apellidoMAct.get(),
            self.usernameAct.get(),
            self.passwordAct.get(),
            self.puestoAct.get(),
            self.telefonoAct.get(),
            self.emailAct.get(),
            self.estatusAct.get(),
            self.registroAct.get_date()
        )
        respuesta = trabajador.actualizar(self.id_seleccionado)
        self.respuesta_sql(respuesta)
        del trabajador

    def borrarTrabajadoresController(self):
        respuesta = trabajadoresbd.Trabajadores.eliminar(self.id_seleccionado)
        self.respuesta_sql(respuesta)
    def buscarTrabajadorPorId (self, id):
        return trabajadoresbd.Trabajadores.consultarPorID(id)