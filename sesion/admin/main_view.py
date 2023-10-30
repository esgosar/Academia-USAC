import tkinter as tk
from tkinter import ttk

class AdminView(tk.Frame):
    def create_widgets(self, master, switch_view):
        super().__init__(master)

        # Barra superior
        self.barra_superior = tk.Frame(self.root, bg="#87CEEB")
        self.barra_superior.pack(fill="x")

        self.nombre_usuario = "Nombre de Usuario"
        self.mensaje_bienvenida = tk.Label(self.barra_superior, text=f"¡Bienvenido, {self.nombre_usuario}!", font=("Helvetica", 12), bg="#87CEEB", fg="black")
        self.mensaje_bienvenida.pack(anchor='center')

        # Marco para los mosaicos
        self.mosaicos_frame = tk.Frame(self.root, bg="white")
        self.mosaicos_frame.pack()

        # Ancho y alto uniformes para los mosaicos
        ancho_mosaico = 200
        alto_mosaico = 200

        # Estilos para los cursos
        curso_style = {"bg": "white", "fg": "black", "font": ("Helvetica", 14, "bold")}
        cursos = [
            {"nombre": "Nuevos Profesores", "imagen": "math.png"},
            {"nombre": "Nuevos Cursos", "imagen": "history.png"},
            {"nombre": "Profesores registrados", "imagen": "python.png"},
            {"nombre": "Cursos", "imagen": "art.png"},
        ]

        for i, admin_data in enumerate(cursos):
            mosaico = ttk.Frame(self.mosaicos_frame, padding=10)
            mosaico.grid(row=i // 3, column=i % 3, padx=20, pady=10)

            # Crear etiqueta para el nombre del curso
            nombre_label = tk.Label(mosaico, text=admin_data["nombre"], **curso_style)
            nombre_label.pack()

            # Crear botón para inscribirse en el curso
            editar_button = tk.Button(mosaico, text="Editar", command=lambda curso=admin_data["nombre"]: self.on_mosaico_click(curso))
            editar_button.pack()
            
    def on_mosaico_click(self, editar):
        print(f"Has hecho clic : {editar}")