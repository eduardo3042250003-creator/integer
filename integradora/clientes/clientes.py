from tkinter import * 
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk 
from clientes import clientesbd
from tkcalendar import DateEntry

class ClientesMVC():
    def __init__(self, ventana, funcionMenu):
        self.ventana = ventana
        self.crearMenuSuperior = funcionMenu
        self.ventana.geometry("800x600")
        self.mostrarClientesView()

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def ejecutarTodoIns(self):
        self.agregarClientesController()
        self.borrarPantalla()
        self.agregarClientesView()

    def ejecutarTodoAct(self):
        respuesta = messagebox.askyesno("advertencia", "seguro que deseas actualizar?")
        if respuesta:
            self.editarClientesController()
            self.borrarPantalla()
            self.mostrarClientesView()
        else:
            self.borrarPantalla()
            self.editarClientesView()

    def mostrarClientesView(self):
        self.borrarPantalla()
        contenedor = tk.Frame(self.ventana)
        contenedor.pack(fill="both", expand=True)
        self.crearMenuSuperior(contenedor)
        
        Label(contenedor, text="clientes").pack(anchor="w", padx=10, pady=5)
        
        frame_tabla = tk.Frame(contenedor)
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=5)
        
        columnas = ("id", "nombre", "telefono", "email", "calle", "numero","colonia", "RFC", "registro", "Estatus")
        tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
        datos = self.mostrarClientesController()
        
        for col in columnas:
            tabla.heading(col, text=col)
            tabla.column(col, width=80)
            
        if datos:
            for cliente in datos:
                tabla.insert("", tk.END, values=cliente)
                
        tabla.pack(side="top", fill="both", expand=True)
        tabla.bind("<<TreeviewSelect>>", self.alSeleccionar)
        
        frame_botones = tk.Frame(contenedor)
        frame_botones.pack(fill="x", padx=10, pady=10)
        Button(frame_botones, text="agregar", command=self.agregarClientesView).pack(side="right", padx=5)
        self.ButtonEditar = Button(frame_botones, text="Editar", command=self.editarClientesView)
        self.ButtonEditar.pack(side="right", padx=5)
        self.ButtonEditar.config(state=tk.DISABLED)
    def alSeleccionar(self,event):
            seleccion = event.widget.selection()
            if seleccion:
                valores = event.widget.item(seleccion[0], "values")
                self.id_seleccionado = valores[0]
                self.ButtonEditar.config(state="normal")
   
    def agregarClientesView(self):
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
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=frame_form, anchor="nw")
        canvas.configure(yscrollcommand=barra.set)

        canvas.pack(side="left", fill="both", expand=True)
        barra.pack(side="right", fill="y")
        # ---------------------------------

        Label(frame_form, text="DATOS DEL CLIENTE", font=("Arial", 11, "bold")).pack(pady=5)
        Label(frame_form, text="ingrese el nombre del cliente").pack(anchor="w", pady=2, padx=10)
        self.nombre = Entry(frame_form, width=40)
        self.nombre.focus()
        self.nombre.pack(fill="x", pady=2, padx=10)
        
        Label(frame_form, text="ingrese el telefono del cliente").pack(anchor="w", pady=2, padx=10)
        self.telefono = Entry(frame_form, width=40)
        self.telefono.pack(fill="x", pady=2, padx=10)
        
        Label(frame_form, text="ingrese el email del cliente").pack(anchor="w", pady=2, padx=10)
        self.email = Entry(frame_form, width=40)
        self.email.pack(fill="x", pady=2, padx=10)
        
        Label(frame_form, text="calle:").pack(anchor="w", pady=2, padx=10)
        self.calle = Entry(frame_form, width=40)
        self.calle.pack(fill="x", pady=2, padx=10)
        
        Label(frame_form, text="numero").pack(anchor="w", pady=2, padx=10)
        self.numero = Entry(frame_form, width=40)
        self.numero.pack(fill="x", pady=2, padx=10)
        
        Label(frame_form, text="colonia").pack(anchor="w", pady=2, padx=10)
        self.colonia = Entry(frame_form, width=40)
        self.colonia.pack(fill="x", pady=2, padx=10)
        
        Label(frame_form, text="ingrese la RFC del cliente").pack(anchor="w", pady=2, padx=10)
        self.rfc = Entry(frame_form, width=40)
        self.rfc.pack(fill="x", pady=2, padx=10)       
        
        Label(frame_form, text="ingrese la fecha de registro del cliente").pack(anchor="w", pady=2, padx=10)
        self.registro = DateEntry(frame_form, selectmode='day')
        self.registro.pack(fill="x", pady=2, padx=10)
        
        Label(frame_form, text="ingrese el estatus del cliente").pack(anchor="w", pady=2, padx=10)
        datos = ("activo", "inactivo")
        self.estatus = ttk.Combobox(frame_form, values=datos, state="readonly")
        self.estatus.pack(fill="x", pady=2, padx=10)
        self.estatus.current(0)      
        
        frame_botones = tk.Frame(frame_form)
        frame_botones.pack(pady=15)
        Button(frame_botones, text='agregar', command=self.ejecutarTodoIns).pack(side="left", padx=5)
        Button(frame_botones, text='::Regresar::', command=self.mostrarClientesView).pack(side="left", padx=5)
        

    def editarClientesView(self):
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
        
        Label(frame_form, text="telefono").pack(anchor="w", pady=2, padx=10)
        self.telefonoAct = Entry(frame_form, width=40)
        self.telefonoAct.pack(fill="x", pady=2, padx=10)
        
        Label(frame_form, text="email").pack(anchor="w", pady=2, padx=10)
        self.emailAct = Entry(frame_form, width=40)
        self.emailAct.pack(fill="x", pady=2, padx=10)
        
        Label(frame_form, text="calle:").pack(anchor="w", pady=2, padx=10)
        self.calleAct = Entry(frame_form, width=40)
        self.calleAct.pack(fill="x", pady=2, padx=10)
        
        Label(frame_form, text="numero").pack(anchor="w", pady=2, padx=10)
        self.numeroAct = Entry(frame_form, width=40)
        self.numeroAct.pack(fill="x", pady=2, padx=10)
        
        Label(frame_form, text="colonia").pack(anchor="w", pady=2, padx=10)
        self.coloniaAct = Entry(frame_form, width=40)
        self.coloniaAct.pack(fill="x", pady=2, padx=10)
        
        Label(frame_form, text="RFC").pack(anchor="w", pady=2, padx=10)
        self.rfcAct = Entry(frame_form, width=40)
        self.rfcAct.pack(fill="x", pady=2, padx=10)
        
        Label(frame_form, text="ingrese la fecha de registro del cliente").pack(anchor="w", pady=2, padx=10)
        self.registroAct = DateEntry(frame_form, selectmode='day')
        self.registroAct.pack(fill="x", pady=2, padx=10)
        
        Label(frame_form, text="ingrese el estatus del cliente").pack(anchor="w", pady=2, padx=10)
        datos_estatus = ("activo", "inactivo")
        self.estatusAct = ttk.Combobox(frame_form, values=datos_estatus, state="readonly")
        self.estatusAct.pack(fill="x", pady=2, padx=10)
        self.estatusAct.current(0)  
        
        frame_botones = tk.Frame(frame_form)
        frame_botones.pack(pady=15)
        Button(frame_botones, text='Actualizar', command=self.ejecutarTodoAct).pack(side="left", padx=5)
        Button(frame_botones, text='Regresar', command=self.mostrarClientesView).pack(side="left", padx=5)
    
    
        cliente = self.buscarClientePorId(self.id_seleccionado)
        if cliente:
          self.nombreAct.delete(0, "end")
          self.nombreAct.insert(0, cliente[1])

          self.telefonoAct.delete(0, "end")
          self.telefonoAct.insert(0, cliente[2])

          self.emailAct.delete(0, "end")
          self.emailAct.insert(0, cliente[3])

          self.calleAct.delete(0, "end")
          self.calleAct.insert(0, cliente[4])

          self.numeroAct.delete(0, "end")
          self.numeroAct.insert(0, cliente[5])

          self.coloniaAct.delete(0, "end")
          self.coloniaAct.insert(0, cliente[6])

          self.rfcAct.delete(0, "end")
          self.rfcAct.insert(0, cliente[7])

          self.registroAct.set_date(cliente[8])
          self.estatusAct.set(cliente[9])


    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(title="::EXITO::", message="Accion como yo ...exitosa")
        else:
            messagebox.showerror(title='VERIFIQUE ', message="Esta accion no pudo realizarse con exito")
    def mostrarClientesController(self):
        return clientesbd.Clientes.consultar()
    def agregarClientesController(self):
        cliente1 = clientesbd.Clientes(
            self.nombre.get(), self.telefono.get(), self.email.get(), 
            self.calle.get(), self.numero.get(), self.colonia.get(), 
            self.rfc.get(), self.registro.get(), self.estatus.get()
        )
        respuesta = cliente1.insertar()
        self.respuesta_sql(respuesta)
        del cliente1

    def editarClientesController(self):
        cliente1 = clientesbd.Clientes(
            self.nombreAct.get(), self.telefonoAct.get(), self.emailAct.get(), 
            self.calleAct.get(), self.numeroAct.get(), self.coloniaAct.get(), 
            self.rfcAct.get(), self.registroAct.get(), self.estatusAct.get()
        )
        respuesta = cliente1.actualizar(self.id_seleccionado)
        self.respuesta_sql(respuesta)
        del cliente1
    def buscarClientePorId(self, cliente_id):
        cliente = clientesbd.Clientes.consultarPorID(cliente_id)
        return cliente