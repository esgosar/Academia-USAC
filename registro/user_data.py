import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
import globals

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from add_profile_picture import ClickableImageCanvas  # Import the ClickableImageCanvas class
from check import isExplicityValidPassword

class UserDataView(tk.Frame):
    def __init__(self, master, switch_view):
        super().__init__(master)

        self.master = master
        self.switch_view = switch_view
        
        # Container frame with padding
        self.container = tk.Frame(self)
        self.container.pack(padx=50, pady=50, expand=True)

        # Title
        self.title_label = Label(self.container, text="Datos de Usuario", font=("Helvetica", 50))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky='ew')

        # ClickableImageCanvas
        self.image_canvas = ClickableImageCanvas(self.container)
        self.image_canvas.grid(row=1, column=0, columnspan=3, pady=(0, 20), sticky='ew')  # Placed between title and form

        # Centering columns
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_columnconfigure(1, weight=1)

    # Usuario
        self.usuario_entry = self.create_label_entry(2, "Usuario", hide=False)
    
    #Contraseña, Confirmar Contraseña
        self.contrasena_entry = self.create_label_entry(3, "Ejemplo1!", hide=True)
        self.confirmar_contrasena_entry = self.create_label_entry(4, "Ejemplo1!", hide=True)

        # Buttons
        self.left_button = Button(self.container, text="Cancelar", font=("Helvetica", 16), command=self.backward)
        self.left_button.grid(row=5, column=0, pady=20, sticky='w')  # Update row index

        self.right_button = Button(self.container, text="Siguiente", font=("Helvetica", 16), command=self.forward)
        self.right_button.grid(row=5, column=1, pady=20, sticky='e')  # Update row index

    def create_label_entry(self, row, text, hide=False):
        entry = Entry(self.container, font=("Helvetica", 16), width=30, show="*" if hide else "")
        entry.grid(row=row, column=0, columnspan=2, pady=5)
        self.on_entry_focus_out(None, entry, text)  # Set initial state
        entry.bind("<FocusIn>", lambda event, entry=entry, text=text: self.on_entry_focus_in(event, entry, text))
        entry.bind("<FocusOut>", lambda event, entry=entry, text=text: self.on_entry_focus_out(event, entry, text))
        return entry


    def passwords_match(self):
        return self.contrasena_entry.get() == self.confirmar_contrasena_entry.get()

    def on_entry_focus_in(self, event, entry, text):
        if entry.get() == text:
            entry.delete(0, tk.END)  # clear placeholder text
            entry.config(fg='black', font=("Helvetica", 16))  # restore normal color and font weight

    def on_entry_focus_out(self, event, entry, text):
        if not entry.get():
            entry.insert(0, text)  # restore placeholder text
            entry.config(fg='grey', font=("Helvetica", 16, 'italic'))  # change color to grey and font weight to italic

    def backward(self):
        import sys
        import os
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
        from main_view import MainView  # Conditional import
        self.switch_view('MainView')
    
    def forward(self):
        if self.usuario_entry.get() == 'Usuario' or self.contrasena_entry.get() == 'Contraseña':
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return  # Return early to prevent further processing
        elif globals.User().check(self.usuario_entry.get()):
            messagebox.showerror("Error", "Este usuario ya está registrado")
            return
        else:
            if  not self.passwords_match():
                messagebox.showerror("Error", "Las contraseñas no coinciden")
                return  # Return early to prevent further processing
            if isExplicityValidPassword(str(self.contrasena_entry.get())) == 1:
                messagebox.showerror("Error", "La contraseña debe tener al menos 8 caracteres")
                return  # Return early to prevent further processing
            elif isExplicityValidPassword(str(self.contrasena_entry.get())) == 2:
                messagebox.showerror("Error", "La contraseña debe tener al menos una letra mayúscula")
                return  # Return early to prevent further processing
            elif isExplicityValidPassword(str(self.contrasena_entry.get())) == 3:
                messagebox.showerror("Error", "La contraseña debe tener al menos un dígito")
                return  # Return early to prevent further processing
            elif isExplicityValidPassword(str(self.contrasena_entry.get())) == 4:
                messagebox.showerror("Error", "La contraseña debe tener al menos un símbolo")
                return  # Return early to prevent further processing
            elif isExplicityValidPassword(str(self.contrasena_entry.get())) == 5:
                globals.contrasena = self.contrasena_entry.get()
                globals.usuario = self.usuario_entry.get()
                globals.avatar = self.image_canvas.get()
    

        from registro.contact_data import ContactDataView
        self.switch_view('ContactDataView')
