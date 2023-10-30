import tkinter as tk
from tkinter import ttk

class CatView(tk.Frame):
    def __init__(self, master, switch_view):
        super().__init__(master)

        self.root = tk.Frame(self)
        self.root.pack(padx=50, pady=50, expand=True)
        self.switch_view = switch_view
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
        
         # Button at top-left
        self.top_left_button = tk.Button(self.barra_superior, text="Cerrar sesión", command=self.close_session)
        self.top_left_button.pack(side='left')


    def close_session(self):
        import sys
        import os
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
        from main_view import MainView  # Conditional import
        self.switch_view('MainView')
    
    
    def on_mosaico_click(self, nombre_area):
        print(f"Has hecho clic en la función: {nombre_area}")