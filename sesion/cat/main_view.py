import tkinter as tk
from tkinter import ttk

class CatView:
    def __init__(self, root):
        self.root = root
        self.root.title("Panel de Profesor")
        self.root.geometry("600x400")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Barra superior
        self.barra_superior = tk.Frame(self.root, bg="#87CEEB")
        self.barra_superior.pack(fill="x")

        self.nombre_usuario = "Nombre del Profesor"
        self.mensaje_bienvenida = tk.Label(self.barra_superior, text=f"¡Bienvenido, {self.nombre_usuario}!", font=("Helvetica", 12), bg="#87CEEB", fg="black")
        self.mensaje_bienvenida.pack(anchor='center')

        # Marco para los mosaicos
        self.mosaicos_frame = tk.Frame(self.root, bg="white")
        self.mosaicos_frame.pack()

        # Ancho y alto uniformes para los mosaicos
        ancho_mosaico = 200
        alto_mosaico = 200

        # Estilos para las áreas
        area_style = {"bg": "white", "fg": "black", "font": ("Helvetica", 14, "bold")}
        areas_profesor = [
            {"nombre": "Mis Cursos", "imagen": "math.png"},
            {"nombre": "Registro de Notas", "imagen": "history.png"},
        ]

        for i, area_data in enumerate(areas_profesor):
            mosaico = ttk.Frame(self.mosaicos_frame, padding=10)
            mosaico.grid(row=i // 2, column=i % 2, padx=20, pady=10)

            # Crear etiqueta para el nombre del área de profesor
            nombre_label = tk.Label(mosaico, text=area_data["nombre"], **area_style)
            nombre_label.pack()

            # Crear botón para acceder al área
            acceder_button = tk.Button(mosaico, text="Acceder", command=lambda area=area_data["nombre"]: self.on_mosaico_click(area))
            acceder_button.pack()
            
    def on_mosaico_click(self, nombre_area):
        print(f"Has hecho clic en la función: {nombre_area}")