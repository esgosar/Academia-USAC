import globals
import tkinter as tk
from cryptography.fernet import Fernet
import base64

class CatBodyModal(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.overrideredirect(True)  # Removes the title bar
        self.title("CatBody Form")
        self.geometry("600x500+%d+%d" % (self.winfo_screenwidth()/2 - 300, self.winfo_screenheight()/2 - 250))  # Centers the window

        # Create a frame for the buttons
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10, padx=20)

        # Create a title label
        self.title_label = tk.Label(self, text="CatBody Data", font=("Helvetica", 24))
        self.title_label.pack(pady=20)

        # Create a frame for the form
        self.form_frame = tk.Frame(self)
        self.form_frame.pack(fill=tk.BOTH, expand=True)

        # Center the form using an additional frame
        self.center_frame = tk.Frame(self.form_frame)
        self.center_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Create labels and entries for each form item
        self.labels_and_entries = {}
        items = ["Usuario","Nombre", "Apellido", "DPI", "Contraseña", "Confirmar Contraseña"]
        for i, item in enumerate(items):
            label = tk.Label(self.center_frame, text=item)
            entry = tk.Entry(self.center_frame)
            label.grid(row=i, column=0, sticky='e', padx=5, pady=5)
            entry.grid(row=i, column=1, sticky='w', padx=5, pady=5)
            self.labels_and_entries[item] = entry

        # Create a Close button
        self.close_button = tk.Button(self.button_frame, text="Cancel", command=self.destroy)
        self.close_button.pack(side=tk.LEFT)

        # Create a Next button
        self.next_button = tk.Button(self.button_frame, text="Submit", command=self.on_submit)
        self.next_button.pack(side=tk.RIGHT)

        self.protocol("WM_DELETE_WINDOW", self.destroy)  # Handle the modal closure

    def on_submit(self):
        # Retrieve values from the Entry widgets and print them
        values = {item: entry.get() for item, entry in self.labels_and_entries.items()}
        for item, value in values.items():
            print(f"{item}: {value}")
            if item == "Nombre":
                globals.nombres = value
            elif item == "Apellido":
                globals.apellidos = value
            elif item == "DPI":
                globals.dpi = value
            elif item == "Contraseña":                
                globals.contrasena = value
            elif item == "Usuario":
                globals.usuario = value

        encrypted = globals.cipher_suite.encrypt(globals.contrasena.encode())
        base64_encrypted = base64.urlsafe_b64encode(encrypted).decode()
        globals.User().create(globals.nombres, globals.apellidos, globals.dpi, globals.fecha_nacimiento, globals.avatar, globals.usuario, base64_encrypted, globals.email, globals.phone, "cat")

        self.destroy()  # Close the modal after submission


class CatBody(tk.Frame):
    def __init__(self, master, switch_view):
        super().__init__(master)
        self.root = tk.Frame(self, bg="white")
        self.root.pack(expand=True, fill=tk.BOTH)
        self.switch_view = switch_view

        # Header
        self.header = tk.Frame(self.root, bg="white", height=60)
        self.header.pack(fill=tk.X, side=tk.TOP)

        # Create "Crear Curso" label
        self.crear_curso_label = self.create_header_label("Crear Curso", self.create_course)
        self.crear_curso_label.pack(side=tk.LEFT)

        # Separator
        self.separator1 = tk.Label(self.header, text=" | ", bg="white", fg="black")
        self.separator1.pack(side=tk.LEFT)

        # Create "Registrar de Profesor" label
        self.profesor_label = self.create_header_label("Registro de Profesor", self.registrar_profesor)
        self.profesor_label.pack(side=tk.LEFT)

        # Separator
        self.separator2 = tk.Label(self.header, text=" | ", bg="white", fg="black")
        self.separator2.pack(side=tk.LEFT)

        # Create "Notas" label
        self.notas_label = self.create_header_label("Notas", self.notas)
        self.notas_label.pack(side=tk.LEFT)

        # Separator
        self.separator3 = tk.Label(self.header, text=" | ", bg="white", fg="black")
        self.separator3.pack(side=tk.LEFT)

        # Create "Usuarios bloqueados" label
        self.bloqueados_label = self.create_header_label("Usuarios bloqueados", self.usuarios_bloqueados)
        self.bloqueados_label.pack(side=tk.LEFT)
        
        # Create a label for closing session
        self.close_session_label = tk.Label(self.header, text="Cerrar sesión", bg="white", fg="black", font=("Helvetica", 16), cursor="hand2")
        self.close_session_label.pack(side=tk.RIGHT, padx=10)
        # Bind left-click event to close_session_label to trigger close_session method
        self.close_session_label.bind("<Button-1>", lambda e: self.close_session())

        # Border line
        self.border_line = tk.Frame(self.root, height=1, bg='black')
        self.border_line.pack(fill=tk.X, side=tk.TOP)

        # Add a button to open the CatBodyModal
        self.add_modal_button = tk.Button(self.root, text="Open CatBody Form", command=self.open_catbody_modal)
        self.add_modal_button.pack(side=tk.BOTTOM, pady=10)  # Place at the bottom

    def open_catbody_modal(self):
        # This will create and show the CatBodyModal
        catbody_modal = CatBodyModal(self)
    
    def close_session(self):
            import sys
            import os
            sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
            from main_view import MainView  # Conditional import
            self.switch_view('MainView')

    def create_header_label(self, text, command):
        label = tk.Label(self.header, text=text, bg="white", fg="black", font=("Helvetica", 16), cursor="hand2")
        label.bind("<Button-1>", command)
        label.bind("<Enter>", lambda e: label.config(cursor="hand2"))
        label.bind("<Leave>", lambda e: label.config(cursor=""))
        return label

    def registrar_profesor(self, event):
        from sesion.admin.cat_body import CatBody  # Conditional import
        self.switch_view('CatBody')

    def notas(self, event):
        from sesion.admin.notes_body import NotesBody  # Conditional import
        self.switch_view('NotesBody')

    def usuarios_bloqueados(self, event):
        from sesion.admin.blocked_body import BlockedBody  # Conditional import
        self.switch_view('BlockedBody')

    def create_course(self, event):
        from sesion.admin.admin_view import AdminView  # Conditional import
        self.switch_view('AdminView')