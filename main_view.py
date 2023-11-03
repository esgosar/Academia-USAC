# MAIN SHOULD BE INSIDE SESSION DIRECTORY
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
from session import iniciar_sesion  # Import the iniciar_sesion function
from correo import vista_recuperacion
import json
import base64
import globals
from encryptor import Decrypt

class MainView(tk.Frame):
    def __init__(self, master, switch_view):
        super().__init__(master)  # This line ensures that MainView is properly initialized as a tk.Frame object (Use tk.Frame.__init__ directly)
        self.switch_view = switch_view

        self.incorrect_password_count = 0  # Initialize the incorrect password count
        
        self.master = master
        self.master.title("Facultad de Ingeniería")

        self.titulo = Label(master, text="Facultad de Ingeniería", font=("Helvetica", 40, "bold"))
        self.titulo.place(relx=0.5, rely=0.2, anchor='center')

        self.usuario_label = Label(master, text="Usuario:", font=("Helvetica", 16))
        self.usuario_label.place(relx=0.5, rely=0.4, anchor='center')
        self.usuario_entry = Entry(master, font=("Helvetica", 16))
        self.usuario_entry.place(relx=0.5, rely=0.45, anchor='center')

        self.contrasena_label = Label(master, text="Contraseña:", font=("Helvetica", 16))
        self.contrasena_label.place(relx=0.5, rely=0.55, anchor='center')
        self.contrasena_entry = Entry(master, show="*", font=("Helvetica", 16))
        self.contrasena_entry.place(relx=0.5, rely=0.6, anchor='center')

        self.iniciar_sesion_button = Button(master, text="Iniciar Sesión", font=("Helvetica", 16), command=self.login)
        self.iniciar_sesion_button.place(relx=0.5, rely=0.7, anchor='center')

        self.link = Label(master, text="Olvidé mi contraseña", fg="sky blue", font=("Helvetica", 14), cursor="hand2")
        self.link.place(relx=0.5, rely=0.9, anchor='center')
        self.link.bind("<Button-1>", lambda event:vista_recuperacion())

        self.abrir_registro = Button(self, text="Registrarse", font=("Helvetica",16),command=self.abrir_registro)
        self.abrir_registro.place(relx=0.5, rely=0.8, anchor='center')
        
    def wrap_iniciar_sesion(self):
        # Call the iniciar_sesion function once and store the result
        login_result = self.iniciar_sesion(self.usuario_entry, self.contrasena_entry)

        # Switch view based on the result of iniciar_sesion
        if login_result == 3:
            from sesion.admin.admin_view import AdminView  # Conditional import
            self.switch_view('AdminView')
        elif login_result == 1:
            from sesion.alumn.alumn_view import AlumnView  # Conditional import
            self.switch_view('AlumnView')
        elif login_result == 2:
            from sesion.cat.cat_view import CatView  # Conditional import
            self.switch_view('CatView')

    def login(self):
        isUser = False
        isPass = False
  
        if self.usuario_entry.get() == '' or self.contrasena_entry.get() == '':
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return
        
        # Leer el archivo JSON que contiene la información de los usuarios
        with open('./users.json', 'r') as f:
            data = json.load(f)
            #HERE SHOULD DECRYPT PASSWORD
            if self.usuario_entry.get() in data:
                isUser = True
                if self.contrasena_entry.get() == data[self.usuario_entry.get()]['password']:
                    isPass = True
                    self.incorrect_password_count = 0  # Reset the incorrect password count on successful login
                else:
                    self.incorrect_password_count += 1  # Increment the incorrect password count  

        if not isUser:
            messagebox.showerror("Error", "Usuario no registrado")
            return    
        else:
            if self.incorrect_password_count >= 3:
                globals.User().block(self.usuario_entry.get())
                messagebox.showerror("Error", 'Usuario bloqueado\n\nPara desbloquear su usuario contacte con el administrador')
                return
            elif not isPass:
                messagebox.showerror("Error", 'Contraseña incorrecta')
                return
            else:
                if data[self.usuario_entry.get()]['Confirmación'] == True:
                    globals.user_session = user # Iniciar sesión con este usuario
                    
                    #Cambio de vista
                    if data[user]['Tipo de usuario'] == "alumn":
                        return 1
                    elif data[user]['Tipo de usuario'] == "cat":
                        return 2
                    elif data[user]['Tipo de usuario'] == "admin":
                        return 3
        
    def abrir_registro(self):
        from registro.personal_data import PersonalDataView  # Conditional import
        self.switch_view('PersonalDataView')