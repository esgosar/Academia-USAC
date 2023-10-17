import tkinter as tk
from tkinter import Label, Entry, Button
from session import iniciar_sesion  # Import the iniciar_sesion function

class MainView:
    def __init__(self, master):
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

        self.link = Label(master, text="Recuperar Contraseña o...", fg="white", font=("Helvetica", 16), cursor="hand2")
        self.link.place(relx=0.5, rely=0.75, anchor='center')
        self.link.bind("<Button-1>", self.vista_recuperacion)

        self.registrar_button = Button(master, text="Registrarse", font=("Helvetica", 16), command=self.abrir_registro)
        self.registrar_button.place(relx=0.5, rely=0.8, anchor='center')

        self.error_message = Label(master, font=("Helvetica", 12), fg="red")
        self.error_message.place(relx=0.5, rely=0.75, anchor='center')
    


    """
        self.user_existn = Label(master, text="Usuario no registrado", font=("Helvetica", 12), fg="red")
        self.user_existn.place(relx=0.5, rely=0.75, anchor='center')

        self.pass_existn = Label(master, text="Contraseña incorrecta", font=("Helvetica", 12), fg="red")
        self.pass_existn.place(relx=0.5, rely=0.8, anchor='center')

        self.blocked_message = Label(master, text="Usuario bloqueado", font=("Helvetica", 12), fg="red")
        self.blocked_message.place(relx=0.5, rely=0.8, anchor='center')

        # Initially hide the error labels
        self.hide_error_labels()

    def hide_error_labels(self):
        self.user_existn.place_forget()
        self.pass_existn.place_forget()
        self.blocked_message.place_forget()

        # Redireccionar la vista según el tipo de usuario
        if item[user]['confirm'] == 'false':
            pass
        elif item[user]['confirm'] == 'true':
            if item[user]['tipo'] == "alumn":
                vista_alumno()
            elif item[user]['tipo'] == "cat":
                vista_catedra()
            elif item[user]['tipo'] == "admin":
                vista_admin()
    """

    def update_error_message(self, message):
        self.error_message.config(text=message)
        self.error_message.place(relx=0.5, rely=0.75, anchor='center')  # Show the error message
        
    def hide_error_message(self):
        self.error_message.place_forget()  # Hide the error message
        
    def wrap_iniciar_sesion(self):
        iniciar_sesion(self.usuario_entry, self.contrasena_entry, self.update_error_message, self)

    def reset_incorrect_password_count(self):
        self.incorrect_password_count = 0  # Reset the incorrect password count

    def vista_recuperacion():
        pass

    def abrir_registro():
        pass