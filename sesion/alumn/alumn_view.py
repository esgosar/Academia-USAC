import tkinter as tk
from tkinter import ttk

class AlumnView(tk.Frame):
    def __init__(self, master, switch_view):
        super().__init__(master)

        self.root = tk.Frame(self)
        self.root.pack(padx=50, pady=50, expand=True)

        # Barra superior
        self.barra_superior = tk.Frame(self.root, bg="#87CEEB")
        self.barra_superior.pack(fill="x")

        self.nombre_usuario = "Ejemplo"
        self.mensaje_bienvenida = tk.Label(self.barra_superior, text=self.nombre_usuario, font=("Helvetica", 12), bg="#87CEEB", fg="black")
        self.mensaje_bienvenida.pack(side="right", padx=10, pady=10)

        self.cursos_button = tk.Button(self.root, text="Mis cursos", font=("Helvetica", 14), bg="blue", fg="white")
        self.cursos_button.pack(pady=10)

        # Marco para los mosaicos
        self.mosaicos_frame = tk.Frame(self.root, bg="white")
        self.mosaicos_frame.pack()

        # Ancho y alto uniformes para los mosaicos
        ancho_mosaico = 200
        alto_mosaico = 200

        # Estilos para los cursos
        curso_style = {"bg": "white", "fg": "black", "font": ("Helvetica", 14, "bold")}
        cursos = [
            {"nombre": "Matemáticas", "imagen": "math.png"},
            {"nombre": "Historia", "imagen": "history.png"},
            {"nombre": "Programación", "imagen": "python.png"},
            {"nombre": "Física Básica", "imagen": "art.png"},
            {"nombre": "Curso 5", "imagen": "image5.png"}  # Agrega más cursos si es necesario
        ]

        for i, curso_data in enumerate(cursos):
            mosaico = ttk.Frame(self.mosaicos_frame, padding=10)
            mosaico.grid(row=i // 3, column=i % 3, padx=20, pady=10)

            # Crear etiqueta para el nombre del curso
            nombre_label = tk.Label(mosaico, text=curso_data["nombre"], **curso_style)
            nombre_label.pack()

            # Crear botón para inscribirse en el curso
            inscribirse_button = tk.Button(mosaico, text="Inscribirse", command=lambda curso=curso_data["nombre"]: self.on_mosaico_click(curso))
            inscribirse_button.pack()
            
    def on_mosaico_click(self, curso):
        print(f"Has hecho clic en el curso: {curso}")
