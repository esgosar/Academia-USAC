from tkinter import *
from tkinter import ttk  # for the Checkbutton
from tkcalendar import DateEntry
from create_user import CreateUserDict, JSONBuilder
import json

# Create an empty list to store the Entry widgets
entry_widgets = []

def new_alumn():
    entry_values = [entry.get() for entry in entry_widgets]
    entry_values.append(tipo.alumn) #default
    entry_values.append("true") #condicional, verficar.
    user = CreateUserDict(*entry_values)
    #Store it
    JSONBuilder(user)

class tipo:
    alumn = "alumn"
    admin = "admin"
    catdr = "cat"

def iniciar_sesion():
    user = usuario_entry.get()
    contrasena = contrasena_entry.get()
    isUser = False
    isPass = False

    with open('./users.json', 'r') as f:
        data = json.load(f)
        for item in data:
            if user in item:
                isUser = True
                if item[user]['password'] == contrasena:
                    isPass = True
                    break
    
        # Manejo de errores
        if not isUser:
            user_existn.pack()
        else:
            user_existn.pack_forget()

        if not isPass:
            pass_existn.pack()
        else:
            pass_existn.pack_forget()
            # View fork
            if item[user]['tipo'] == tipo.alumn:
                vista_alumno()
            elif item[user]['tipo'] == tipo.admin:
                vista_catedra()
            elif item[user]['tipo'] == tipo.catdr:
                vista_admin()

def vista_alumno():
    global entry_widgets  # Declare as global to modify it
    entry_widgets = []  # Clear the previous entries if any

    # Destroy previous widgets
    titulo.destroy()
    usuario_label.destroy()
    usuario_entry.destroy()
    contrasena_label.destroy()
    contrasena_entry.destroy()
    iniciar_sesion_button.destroy()
    registrar_button.destroy()

    # New Title
    titulo_registro = Label(ventana, text="Alumno", font=("Helvetica", 40, "bold"))
    titulo_registro.place(relx=0.5, rely=0.1, anchor='center')

def vista_catedra():
    global entry_widgets  # Declare as global to modify it
    entry_widgets = []  # Clear the previous entries if any

    # Destroy previous widgets
    titulo.destroy()
    usuario_label.destroy()
    usuario_entry.destroy()
    contrasena_label.destroy()
    contrasena_entry.destroy()
    iniciar_sesion_button.destroy()
    registrar_button.destroy()

    # New Title
    titulo_registro = Label(ventana, text="Caterpiler", font=("Helvetica", 40, "bold"))
    titulo_registro.place(relx=0.5, rely=0.1, anchor='center')

def vista_admin():
    global entry_widgets  # Declare as global to modify it
    entry_widgets = []  # Clear the previous entries if any

    # Destroy previous widgets
    titulo.destroy()
    usuario_label.destroy()
    usuario_entry.destroy()
    contrasena_label.destroy()
    contrasena_entry.destroy()
    iniciar_sesion_button.destroy()
    registrar_button.destroy()

    # New Title
    titulo_registro = Label(ventana, text="administrator", font=("Helvetica", 40, "bold"))
    titulo_registro.place(relx=0.5, rely=0.1, anchor='center')

def abrir_registro():
    global entry_widgets  # Declare as global to modify it
    entry_widgets = []  # Clear the previous entries if any

    # Destroy previous widgets
    titulo.destroy()
    usuario_label.destroy()
    usuario_entry.destroy()
    contrasena_label.destroy()
    contrasena_entry.destroy()
    iniciar_sesion_button.destroy()
    registrar_button.destroy()

    # New Title
    titulo_registro = Label(ventana, text="Página de Registro", font=("Helvetica", 40, "bold"))
    titulo_registro.place(relx=0.5, rely=0.1, anchor='center')

    # New Form Fields
    campos = ["Usuario","Nombre", "Apellido", "Fecha de Nacimiento", "Teléfono", "DPI", "Email", "Contraseña"]
    for index, campo in enumerate(campos):
        Label(ventana, text=campo, font=("Helvetica", 16)).place(relx=0.35, rely=0.2 + index*0.1, anchor='center')
        if campo == "Fecha de Nacimiento":
            entry = DateEntry(ventana, width=16, background="magenta3", foreground="white", bd=2)
        else:
            entry = Entry(ventana, font=("Helvetica", 16))
                
        entry.place(relx=0.65, rely=0.2 + index*0.1, anchor='center')
        entry_widgets.append(entry)  # Append to the list

    # Register button for the new form
    registro_button = Button(ventana, text="Registrar", font=("Helvetica", 16), command=new_alumn)
    registro_button.place(relx=0.5, rely=0.95, anchor='center')
    

# Configuración de la ventana principal
ventana = Tk()
ventana.title("Facultad de Ingenieria")
ventana.attributes('-fullscreen', True)

# Título
font_style = ("Helvetica", 12)
titulo = Label(ventana, text="Facultad de Ingeniería", font=("Helvetica", 40, "bold"))
titulo.place(relx=0.5, rely=0.2, anchor='center')

# Usuario
usuario_label = Label(ventana, text="Usuario:", font=("Helvetica", 16))
usuario_label.place(relx=0.5, rely=0.4, anchor='center')
usuario_entry = Entry(ventana, font=("Helvetica", 16))
usuario_entry.place(relx=0.5, rely=0.45, anchor='center')

# Contraseña
contrasena_label = Label(ventana, text="Contraseña:", font=("Helvetica", 16))
contrasena_label.place(relx=0.5, rely=0.55, anchor='center')
contrasena_entry = Entry(ventana, show="*", font=("Helvetica", 16))
contrasena_entry.place(relx=0.5, rely=0.6, anchor='center')

# Botones
iniciar_sesion_button = Button(ventana, text="Iniciar Sesión", font=("Helvetica", 16), command=iniciar_sesion)
iniciar_sesion_button.place(relx=0.5, rely=0.7, anchor='center')

registrar_button = Button(ventana, text="Registrarse", font=("Helvetica", 16), command=abrir_registro)
registrar_button.place(relx=0.5, rely=0.8, anchor='center')

user_existn = Label(ventana, text="Usuario no registrado", font=font_style, fg="red")
user_existn.place(relx=0.5, rely=0.75, anchor='center')

pass_existn = Label(ventana, text="Contraseña incorrecta", font=font_style, fg="red")
pass_existn.place(relx=0.5, rely=0.8, anchor='center')

# Initially, hide them
user_existn.place_forget()
pass_existn.place_forget()

# Ejecutar la aplicación
ventana.mainloop()