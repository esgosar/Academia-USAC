import tkinter as tk
from tkcalendar import DateEntry
from tkinter import Label, Entry, Button

class PersonalDataView(tk.Frame):
    def __init__(self, master, switch_view):
        super().__init__(master)
        self.master = master
        self.switch_view = switch_view

        # Container frame with padding
        self.container = tk.Frame(self)
        self.container.pack(padx=50, pady=50, expand=True)

        # Title
        self.title_label = Label(self.container, text="Datos Personales", font=("Helvetica", 50))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky='ew')

        # Centering columns
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_columnconfigure(1, weight=1)

        # Function to create label and entry pairs
        def create_label_entry(row, text):
            if row == 4:  # Condition to check if it's the row for Fecha de Nacimiento
                entry = DateEntry(self.container, width=20, background="magenta3", foreground="white", bd=2, font=("Helvetica", 16))
            else:
                entry = Entry(self.container, font=("Helvetica", 16), width=30)
            
            entry.grid(row=row, column=0, columnspan=2, pady=5)
            if row != 4:  # Only bind these events if it's not a DateEntry
                self.on_entry_focus_out(None, entry, text)  # Set initial state
                entry.bind("<FocusIn>", lambda event, entry=entry, text=text: self.on_entry_focus_in(event, entry, text))
                entry.bind("<FocusOut>", lambda event, entry=entry, text=text: self.on_entry_focus_out(event, entry, text))
                
            return entry

        # Nombres, Apellidos, DPI, Fecha de Nacimiento
        self.nombres_entry = create_label_entry(1, "Nombres")
        self.apellidos_entry = create_label_entry(2, "Apellidos")
        self.dpi_entry = create_label_entry(3, "DPI")
        self.fecha_entry = create_label_entry(4, "Fecha de Nacimiento")

        # Buttons
        self.left_button = Button(self.container, text="Back", font=("Helvetica", 16))
        self.left_button.grid(row=5, column=0, pady=20, sticky='w')  # Sticky 'w' to align to the left

        self.right_button = Button(self.container, text="Next", font=("Helvetica", 16))
        self.right_button.grid(row=5, column=1, pady=20, sticky='w')

    def on_entry_focus_in(self, event, entry, text):
        if entry.get() == text:
            entry.delete(0, tk.END)  # clear placeholder text
            entry.config(fg='black', font=("Helvetica", 16))  # restore normal color and font weight

    def on_entry_focus_out(self, event, entry, text):
        if not entry.get():
            entry.insert(0, text)  # restore placeholder text
            entry.config(fg='grey', font=("Helvetica", 16, 'italic'))  # change color to grey and font weight to italic

if __name__ == "__main__":
    root = tk.Tk()
    view = PersonalDataView(root, None)
    view.pack(fill=tk.BOTH, expand=True)
    root.mainloop()
