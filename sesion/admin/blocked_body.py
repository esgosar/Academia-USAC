from globals import Course
import tkinter as tk

class BlockedBody(tk.Frame):
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