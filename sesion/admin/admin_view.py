import tkinter as tk
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from image_display import ImageViewerCanvas

class AssignCoursesModal(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.overrideredirect(True)  # Removes the title bar
        self.title("Assign Courses")
        self.geometry("600x500+%d+%d" % (self.winfo_screenwidth()/2 - 300, self.winfo_screenheight()/2 - 250))  # Centers the window and resizes it to 600x500

        # Create a frame for the  buttons
        self.button_frame = tk.Frame(self)
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor='w', pady=10, padx=20)

        # Create a title label
        self.title_label = tk.Label(self, text="Datos del Curso", font=("Helvetica", 24))
        self.title_label.pack(pady=20)  # Pack the title label with some vertical padding

        # Create a frame for the form
        self.form_frame = tk.Frame(self)
        self.form_frame.pack(fill=tk.BOTH, expand=True)

        # Center the form by using an additional frame
        self.center_frame = tk.Frame(self.form_frame)
        self.center_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Create labels and entries for each item
        self.labels_and_entries = {}
        items = ["Nombre", "Código", "Costo", "Horario", "Cupo", "Catedrático"]
        for i, item in enumerate(items):
            label = tk.Label(self.center_frame, text=item)
            entry = tk.Entry(self.center_frame)
            label.grid(row=i, column=0, sticky='e', padx=5, pady=5)
            entry.grid(row=i, column=1, sticky='w', padx=5, pady=5)
            self.labels_and_entries[item] = entry  # Store entry for

        # Create Close button
        self.close_button = tk.Button(self.button_frame, text="Cancelar", command=self.destroy)
        self.close_button.pack(side=tk.LEFT)

        # Create Siguiente button
        self.next_button = tk.Button(self.button_frame, text="Siguiente", command=self.on_next)
        self.next_button.pack(side=tk.RIGHT) 

        self.protocol("WM_DELETE_WINDOW", self.destroy)  # Handle the modal closure

    def on_next(self):
        print("siguiente")
        for item, entry in self.labels_and_entries.items():
            print(f"{item}: {entry.get()}")  # Print entered values to console
        self.destroy()


class AdminView(tk.Frame):
    def __init__(self, master, switch_view):
        super().__init__(master)
        self.root = tk.Frame(self, bg="grey")
        self.root.pack(expand=True, fill=tk.BOTH)
        self.switch_view = switch_view

        # Header
        self.header = tk.Frame(self.root, bg="white", height=60)
        self.header.pack(fill=tk.X, side=tk.TOP)

        self.header_text = tk.Label(self.header, text="Crear Curso", bg="white", fg="black", font=("Helvetica", 16))
        self.header_text.pack(side=tk.LEFT, padx=10)

        self.header_text.bind("<Button-1>", self.create_course)
        self.header_text.bind("<Enter>", lambda e: self.header_text.config(cursor="hand2"))
        self.header_text.bind("<Leave>", lambda e: self.header_text.config(cursor=""))

        # Create a label for closing session
        self.close_session_label = tk.Label(self.header, text="Cerrar sesión", bg="white", fg="black", font=("Helvetica", 16), cursor="hand2")
        self.close_session_label.pack(side=tk.RIGHT, padx=10)
        # Bind left-click event to close_session_label to trigger close_session method
        self.close_session_label.bind("<Button-1>", lambda e: self.close_session())

        # Border line
        self.border_line = tk.Frame(self.root, height=1, bg='black')
        self.border_line.pack(fill=tk.X, side=tk.TOP)

        # Body
        self.message_label = tk.Label(self.root, text="Sin cursos creados", bg="grey", fg="white", font=("Helvetica", 24))
        self.message_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
    def close_session(self):
        import sys
        import os
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
        from main_view import MainView  # Conditional import
        self.switch_view('MainView')

    def create_course(self, event):
        self.modal = AssignCoursesModal(self)