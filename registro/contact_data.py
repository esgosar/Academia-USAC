import globals
from globals import CreateUser
import tkinter as tk
from tkinter import Label, Entry, Button

class ContactDataView(tk.Frame):
    def __init__(self, master, switch_view):
        super().__init__(master)

        self.master = master
        self.switch_view = switch_view

        # Container frame with padding
        self.container = tk.Frame(self)
        self.container.pack(padx=50, pady=50, expand=True)

        # Title
        self.title_label = Label(self.container, text="Datos de Contacto", font=("Helvetica", 50))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky='ew')

        # Centering columns
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_columnconfigure(1, weight=1)

        # Function to create label and entry pairs
        def create_label_entry(row, text):
            entry = Entry(self.container, font=("Helvetica", 16), width=30)
            entry.grid(row=row, column=0, columnspan=2, pady=5)
            self.on_entry_focus_out(None, entry, text)  # Set initial state
            entry.bind("<FocusIn>", lambda event, entry=entry, text=text: self.on_entry_focus_in(event, entry, text))
            entry.bind("<FocusOut>", lambda event, entry=entry, text=text: self.on_entry_focus_out(event, entry, text))
            return entry

        # Correo electrónico, Teléfono
        self.email_entry = create_label_entry(1, "Correo electrónico")
        self.phone_entry = create_label_entry(2, "Teléfono")

        # Buttons
        self.left_button = Button(self.container, text="Atrás", font=("Helvetica", 16), command=self.backward)
        self.left_button.grid(row=3, column=0, pady=20, sticky='w')  # Sticky 'w' to align to the left

        self.right_button = Button(self.container, text="Registrar", font=("Helvetica", 16), command=self.forward)
        self.right_button.grid(row=3, column=1, pady=20, sticky='e')

    def on_entry_focus_in(self, event, entry, text):
        if entry.get() == text:
            entry.delete(0, tk.END)  # clear placeholder text
            entry.config(fg='black', font=("Helvetica", 16))  # restore normal color and font weight

    def on_entry_focus_out(self, event, entry, text):
        if not entry.get():
            entry.insert(0, text)  # restore placeholder text
            entry.config(fg='grey', font=("Helvetica", 16, 'italic'))  # change color to grey and font weight to italic

    def backward(self):
        from registro.user_data import UserDataView
        self.switch_view('UserDataView')
    
    def forward(self):
        # Get the data from the entries
        globals.email = self.email_entry.get()
        globals.phone = self.phone_entry.get()

        CreateUser(globals.nombres, globals.apellidos, globals.dpi, globals.fecha_nacimiento, globals.avatar, globals.usuario, globals.contrasena, globals.email, globals.phone, "alumnn")

        from registro.success import SuccessView
        self.switch_view('SuccessView')