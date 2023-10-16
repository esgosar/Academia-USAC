from tkinter import *
from tkinter import ttk  # para el Checkbutton
from tkcalendar import DateEntry
from create_user import CreateAlumnDict, CreateCatdrDict, JSONBuilder
import json

# Crear una lista vacía para almacenar los widgets de tipo Entry
entry_widgets = []

def debugger():
    print("Yep!")

def new_alumn():
    # Obtener los valores ingresados en los campos de texto
    entry_values = [entry.get() for entry in entry_widgets]
    user = CreateAlumnDict(*entry_values)
    # Almacenar el usuario
    JSONBuilder(user)

def new_cat():
    # Obtener los valores ingresados en los cmapos de texto
    entry_values = [entry.get() for entry in entry_widgets]
    user = CreateCatdrDict(*entry_values)
    # Almacenar el usuario
    JSONBuilder(user)

def iniciar_sesion():
    # Obtener datos del usuario y contraseña
    user = usuario_entry.get()
    contrasena = contrasena_entry.get()
    isUser = False
    isPass = False

    # Leer el archivo JSON que contiene la información de los usuarios
    with open('./users.json', 'r') as f:
        data = json.load(f)
        for item in data:
            if user in item:
                isUser = True
                if item[user]['password'] == contrasena:
                    isPass = True
                    break

        # Manejo de errores para usuario y contraseña
        if not isUser:
            user_existn.pack()
        else:
            user_existn.pack_forget()
            if not isPass:
                pass_existn.pack()
            else:
                pass_existn.pack_forget()

            # Redireccionar la vista según el tipo de usuario
            if item[user]['tipo'] == "alumn":
                vista_alumno()
            elif item[user]['tipo'] == "cat":
                vista_catedra()
            elif item[user]['tipo'] == "admin":
                vista_admin()

def recuperar_pass():
    # Obtener datos del usuario y contraseña
    user = email_to_search.get()
    isUser = False

    # Leer el archivo JSON que contiene la información de los usuarios
    with open('./users.json', 'r') as f:
        data = json.load(f)
        for item in data:
            if user in item:
                isUser = True
    
        # Manejo de errores para usuario y contraseña
        if not isUser:
            user_existn.pack()
        else:
            user_existn.pack_forget()
            #wait_view()
            build_main_view()


def vista_alumno():
    global entry_widgets
    global titulo_alumno, sign_out_button

    entry_widgets = []  # Limpiar las entradas anteriores si las hay

    # Eliminar los widgets actuales
    for widget in ventana.winfo_children():
        widget.destroy()

    # Nueva etiqueta de título
    titulo_alumno = Label(ventana, text="Alumno", font=("Helvetica", 40, "bold"))
    titulo_alumno.place(relx=0.5, rely=0.1, anchor='center')

    # Botón para cerrar sesión
    sign_out_button = Button(ventana, text="Cerrar Sesión", font=("Helvetica", 16), command=build_main_view)
    sign_out_button.place(relx=0.5, rely=0.9, anchor='center')

def vista_admin():
    global entry_widgets
    global titulo_catedra, sign_out_button

    entry_widgets = []  # Limpiar las entradas anteriores si las hay

    # Eliminar los widgets actuales
    for widget in ventana.winfo_children():
        widget.destroy()

    # Nueva etiqueta de título
    titulo_catedra = Label(ventana, text="Admin", font=("Helvetica", 40, "bold"))
    titulo_catedra.place(relx=0.5, rely=0.1, anchor='center')

        # Nuevos campos de formulario
    campos = ["Usuario", "Nombre", "Apellido", "DPI", "Contraseña"]
    for index, campo in enumerate(campos):
        Label(ventana, text=campo, font=("Helvetica", 16)).place(relx=0.35, rely=0.2 + index*0.1, anchor='center')
        entry = Entry(ventana, font=("Helvetica", 16))
        entry.place(relx=0.65, rely=0.2 + index*0.1, anchor='center')
        entry_widgets.append(entry)  # Agregar a la lista

    # Botón de registro para el nuevo formulario
    registro_button = Button(ventana, text="Registrar", font=("Helvetica", 16), command=new_cat)
    registro_button.place(relx=0.6, rely=0.95, anchor='center')

    # Botón para cancelar y volver atrás
    sign_out_button = Button(ventana, text="Cancelar", font=("Helvetica", 16), command=build_main_view)
    sign_out_button.place(relx=0.4, rely=0.95, anchor='center')

def abrir_registro():
    global entry_widgets  # Declarar como global para modificarla
    entry_widgets = []  # Limpiar las entradas anteriores si las hay

    # Eliminar los widgets actuales (tener cuidado con este enfoque)
    for widget in ventana.winfo_children():
        widget.destroy()

    # Nuevo título para la página de registro
    titulo_registro = Label(ventana, text="Página de Registro", font=("Helvetica", 40, "bold"))
    titulo_registro.place(relx=0.5, rely=0.1, anchor='center')

    # Nuevos campos de formulario
    campos = ["Usuario","Nombre", "Apellido", "Fecha de Nacimiento", "Teléfono", "DPI", "Email", "Contraseña"]
    for index, campo in enumerate(campos):
        Label(ventana, text=campo, font=("Helvetica", 16)).place(relx=0.35, rely=0.2 + index*0.1, anchor='center')
        if campo == "Fecha de Nacimiento":
            entry = DateEntry(ventana, width=16, background="magenta3", foreground="white", bd=2)
        else:
            entry = Entry(ventana, font=("Helvetica", 16))

        entry.place(relx=0.65, rely=0.2 + index*0.1, anchor='center')
        entry_widgets.append(entry)  # Agregar a la lista

    # Botón de registro para el nuevo formulario
    registro_button = Button(ventana, text="Registrar", font=("Helvetica", 16), command=new_alumn)
    registro_button.place(relx=0.6, rely=0.95, anchor='center')

    # Botón para cancelar y volver atrás
    sign_out_button = Button(ventana, text="Cancelar", font=("Helvetica", 16), command=build_main_view)
    sign_out_button.place(relx=0.4, rely=0.95, anchor='center')
    
def main_view():
    global titulo, usuario_label, usuario_entry, contrasena_label, contrasena_entry
    global iniciar_sesion_button, registrar_button, user_existn, pass_existn

    # Título de la página principal
    titulo = Label(ventana, text="Facultad de Ingeniería", font=("Helvetica", 40, "bold"))
    titulo.place(relx=0.5, rely=0.2, anchor='center')

    # Etiqueta y entrada para el usuario
    usuario_label = Label(ventana, text="Usuario:", font=("Helvetica", 16))
    usuario_label.place(relx=0.5, rely=0.4, anchor='center')
    usuario_entry = Entry(ventana, font=("Helvetica", 16))
    usuario_entry.place(relx=0.5, rely=0.45, anchor='center')

    # Etiqueta y entrada para la contraseña
    contrasena_label = Label(ventana, text="Contraseña:", font=("Helvetica", 16))
    contrasena_label.place(relx=0.5, rely=0.55, anchor='center')
    contrasena_entry = Entry(ventana, show="*", font=("Helvetica", 16))
    contrasena_entry.place(relx=0.5, rely=0.6, anchor='center')

    # Botones para iniciar sesión y registrarse
    iniciar_sesion_button = Button(ventana, text="Iniciar Sesión", font=("Helvetica", 16), command=iniciar_sesion)
    iniciar_sesion_button.place(relx=0.5, rely=0.7, anchor='center')

    link = Label(ventana, text="Recuperar Contraseña o...", fg="white", font=("Helvetica", 16), cursor="hand2")
    link.place(relx=0.5, rely=0.75, anchor='center')
    link.bind("<Button-1>", lambda e: vista_recuperacion())

    registrar_button = Button(ventana, text="Registrarse", font=("Helvetica", 16), command=abrir_registro)
    registrar_button.place(relx=0.5, rely=0.8, anchor='center')

    # Etiquetas de error para usuario y contraseña
    user_existn = Label(ventana, text="Usuario no registrado", font=("Helvetica", 12), fg="red")
    user_existn.place(relx=0.5, rely=0.75, anchor='center')

    pass_existn = Label(ventana, text="Contraseña incorrecta", font=("Helvetica", 12), fg="red")
    pass_existn.place(relx=0.5, rely=0.8, anchor='center')

    # Inicialmente, ocultar las etiquetas de error
    user_existn.place_forget()
    pass_existn.place_forget()

def build_main_view():
    # Destruir los widgets actuales si los hay (tener cuidado con este enfoque)
    for widget in ventana.winfo_children():
        widget.destroy()

    # Reconstruir la vista principal (Esta función debería replicar los widgets de tu vista principal)
    main_view()  # Define esta función para contener el código de tu vista principal

def vista_recuperacion():
    global entry_widgets
    global titulo_catedra, registrar_button, sign_out_button, label, email_to_search, user_existn

    entry_widgets = []  # Limpiar las entradas anteriores si las hay

    # Eliminar los widgets actuales
    for widget in ventana.winfo_children():
        widget.destroy()

    # Nueva etiqueta de título
    titulo_catedra = Label(ventana, text="Recuperación de Contraseña", font=("Helvetica", 30, "bold"))
    titulo_catedra.place(relx=0.5, rely=0.1, anchor='center')

    label = Label(ventana, text="Usuario", font=("Helvetica", 16))
    label.place(relx=0.5, rely=0.4, anchor='center')
    email_to_search = Entry(ventana, font=("Helvetica", 16))
    email_to_search.place(relx=0.5, rely=0.5, anchor='center')

    # Botón de registro para el nuevo formulario
    registro_button = Button(ventana, text="Recuperar", font=("Helvetica", 16), command=recuperar_pass)
    registro_button.place(relx=0.6, rely=0.95, anchor='center')

    # Botón para cancelar y volver atrás
    sign_out_button = Button(ventana, text="Cancelar", font=("Helvetica", 16), command=build_main_view)
    sign_out_button.place(relx=0.4, rely=0.95, anchor='center')

    #Etiquetas de error para usuario
    user_existn = Label(ventana, text="Usuario no registrado", font=("Helvetica", 12), fg="red")
    user_existn.place(relx=0.5, rely=0.75, anchor='center')

    # Inicialmente, ocultar las etiquetas de error
    user_existn.place_forget()

# Configuración de la ventana principal
ventana = Tk()  # Crea una nueva ventana usando Tkinter
ventana.title("Academia USAC")  # Establece el título de la ventana
ventana.attributes('-fullscreen', True)  # Configura la ventana para que se abra en pantalla completa

# Construcción de la vista principal
main_view()  # Llama a la función que construye la vista principal

# Ejecutar la aplicación
ventana.mainloop()  # Inicia el bucle principal de la aplicación Tkinter