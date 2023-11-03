# MAIN SHOULD BE INSIDE SESSION DIRECTORY
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
from session import iniciar_sesion  # Import the iniciar_sesion function
from correo import vista_recuperacion 

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

        self.iniciar_sesion_button = Button(master, text="Iniciar Sesión", font=("Helvetica", 16), command=self.wrap_iniciar_sesion)
        self.iniciar_sesion_button.place(relx=0.5, rely=0.7, anchor='center')

        self.link = Label(master, text="Olvidé mi contraseña", fg="sky blue", font=("Helvetica", 14), cursor="hand2")
        self.link.place(relx=0.5, rely=0.9, anchor='center')
        self.link.bind("<Button-1>", lambda event:vista_recuperacion())

        self.abrir_registro = Button(self, text="Registrarse", font=("Helvetica",16),command=self.abrir_registro)
        self.abrir_registro.place(relx=0.5, rely=0.8, anchor='center')

        self.error_message = Label(master, font=("Helvetica", 12), fg="red")
        self.error_message.place(relx=0.5, rely=0.75, anchor='center')

    def update_error_message(self, message):
        self.error_message.config(text=message)
        self.error_message.place(relx=0.5, rely=0.75, anchor='center')  # Show the error message
        
    def hide_error_message(self):
        self.error_message.place_forget()  # Hide the error message
        
    def wrap_iniciar_sesion(self):
        if iniciar_sesion(self.usuario_entry, self.contrasena_entry, self.update_error_message, self) == 3:
            from sesion.admin.admin_view import AdminView  # Conditional import
            self.switch_view('AdminView')
        elif iniciar_sesion(self.usuario_entry, self.contrasena_entry, self.update_error_message, self) == 1:
            from sesion.alumn.alumn_view import AlumnView  # Conditional import
            self.switch_view('AlumnView')
        elif iniciar_sesion(self.usuario_entry, self.contrasena_entry, self.update_error_message, self) == 2:
            from sesion.cat.cat_view import CatView  # Conditional import
            self.switch_view('CatView')
    
    def reset_incorrect_password_count(self):
        self.incorrect_password_count = 0  # Reset the incorrect password count

    def abrir_registro(self):
        from registro.personal_data import PersonalDataView  # Conditional import
        self.switch_view('PersonalDataView')
