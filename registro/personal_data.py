import tkinter as tk
from tkinter import Label, Entry, Button

class PersonalDataView(tk.Frame):
    def __init__(self, master, switch_view):
        super().__init__(master)
        self.master = master
        self.switch_view = switch_view

        # Title
        self.title_label = Label(self, text="Datos Personales", font=("Helvetica", 24))
        self.title_label.pack(anchor='w', padx=20, pady=(20, 10))  # Pack with padding

        # Nombres
        self.nombres_label = Label(self, text="Nombres", font=("Helvetica", 16))
        self.nombres_label.pack(anchor='w', padx=20)
        self.nombres_entry = Entry(self, font=("Helvetica", 16), width=30)
        self.nombres_entry.pack(anchor='w', padx=20, pady=5)

        # Apellidos
        self.apellidos_label = Label(self, text="Apellidos", font=("Helvetica", 16))
        self.apellidos_label.pack(anchor='w', padx=20)
        self.apellidos_entry = Entry(self, font=("Helvetica", 16), width=30)
        self.apellidos_entry.pack(anchor='w', padx=20, pady=5)

        # DPI
        self.dpi_label = Label(self, text="DPI", font=("Helvetica", 16))
        self.dpi_label.pack(anchor='w', padx=20)
        self.dpi_entry = Entry(self, font=("Helvetica", 16), width=30)
        self.dpi_entry.pack(anchor='w', padx=20, pady=5)

        # Fecha de Nacimiento
        self.fecha_label = Label(self, text="Fecha de Nacimiento", font=("Helvetica", 16))
        self.fecha_label.pack(anchor='w', padx=20)
        self.fecha_entry = Entry(self, font=("Helvetica", 16), width=30)
        self.fecha_entry.pack(anchor='w', padx=20, pady=5)

        # Buttons
        self.left_button = Button(self, text="Back", font=("Helvetica", 16))
        self.left_button.pack(side='left', padx=(20, 0), pady=20)

        self.right_button = Button(self, text="Next", font=("Helvetica", 16))
        self.right_button.pack(side='right', padx=(0, 20), pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    view = PersonalDataView(root, None)
    view.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
