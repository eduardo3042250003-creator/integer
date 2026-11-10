from clientes import *
from clientes.clientes import ClientesMVC
from cotizaciones import cotizacionbd
from materiales import materialesbd
from proyectos import proyectosbd
from trabajadores import trabajadoresbd
import tkinter as tk
from tkinter import Tk,Label,Entry,Button
from tkinter import messagebox
from tkinter import ttk
class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("sistema paesa")
        self.ventana.geometry("400x300")


        self.loginView()
    def loginView (self):
        Label(self.ventana, text="login", font=("Arial", 36)).pack(pady=10)
        Label(self.ventana, text="USERNAME:").pack(pady=10)
        self.username = Entry(self.ventana)
        self.username.focus()
        self.username.pack(pady=5)
        Label(self.ventana, text="PASSWORD").pack(pady=10)
        self.password = Entry(self.ventana)
        self.password.pack(pady=5)
        Button(self.ventana, text='validar', command= self.login2).pack(pady=5)
        Button(self.ventana,text='salir',command=self.ventana.quit).pack(pady=5)

    def login2(self):
        
        respuesta = self.loginController()
        respuesta = True
        if respuesta:
            self.main()
        else:
            messagebox.showerror(title='ERROR', message="USUARIO INEXISTENTE... INTENTE DE NUEVO")
            self.borrarPantalla()
            self.loginView()

    def main(self):

        self.ventana.geometry("800x600")
        self.borrarPantalla()
        self.barra = tk.Scrollbar(self.ventana)
        self.barra.pack(fill="y", side="right")
        contenedor_main = tk.Frame(self.ventana)
        contenedor_main.pack(fill="both", expand=True)
        self.crear_menu_superior(contenedor_main) 
        Label(contenedor_main, text="PAESA", font=("Arial", 36)).pack(pady=200)
             
    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()
    def cerrarSesion(self):
        self.borrarPantalla()
        self.ventana.geometry("400x300")
        self.loginView()

    def crear_menu_superior(self, contenedor):
        barra_superior = tk.Frame(contenedor, height=30)
        barra_superior.pack(fill="x")
        btn_logout = tk.Button(barra_superior, text="Cerrar sesión", command=self.cerrarSesion)
        btn_logout.pack(side="right", padx=10, pady=2)
        menu = tk.Frame(contenedor, height=50)
        menu.pack(fill="x")
        menu.pack_propagate(False)
        opciones = ["Cotizaciones", "Validacion", "Proyectos", "Cobranzas", "Clientes"]
                
        for i in range(len(opciones)):
            menu.grid_columnconfigure(i, weight=1)
            
        for i, texto in enumerate(opciones):
            # Evaluamos si el botón actual es "Clientes"
            if texto == "Clientes":
                # Instanciamos la clase pasándole la ventana principal y llamamos al método
                accion = accion = self.irAClientes
            else:
                # Una acción temporal para los demás botones mientras los configuras
                accion = lambda t=texto: print(f"Módulo de {t} en construcción")

            btn = tk.Button(menu, text=texto, relief="solid", bd=1, command=accion)
            btn.grid(row=0, column=i, sticky="nsew")
            
        menu.grid_rowconfigure(0, weight=1)

    def irAClientes(self):
        # Instancias tu clase pasándole la ventana y la referencia del menú superior
        ClientesMVC(self.ventana, self.crear_menu_superior)
    ##controladores

    
    def loginController(self):
        credenciales = trabajadoresbd.trabajadores.validarLogin(self.username.get(),self.password.get())
        for credencial in credenciales:
            if credencial[0] == self.username.get() and credencial[1] == self.password.get():
                return True
                break
        else:
            return False
if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()