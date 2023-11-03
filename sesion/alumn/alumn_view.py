import tkinter as tk
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from image_display import ImageViewerCanvas

class CerrarSesionModal(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.overrideredirect(True)  # Removes the title bar
        
        # Adjust the dimensions as per your requirement
        width, height = 150, 20  # for example, 150x50
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight()
        x_offset, y_offset = screen_width - width + 40, height + 42
        self.geometry(f"{width}x{height}+{x_offset}+{y_offset}")
        
        # Create a label for the "Cerrar sesión" option with red text and a white background
        self.cerrar_sesion_label = tk.Label(self, text="Cerrar sesión", fg='red')
        self.cerrar_sesion_label.pack()
        
        # Bind the left mouse button click event to the on_cerrar_sesion method
        self.cerrar_sesion_label.bind("<Button-1>", lambda e: self.on_cerrar_sesion())
        
        # Change the cursor to a hand cursor when it hovers over the label
        self.cerrar_sesion_label.bind("<Enter>", lambda e: self.cerrar_sesion_label.config(cursor="hand2"))
        self.cerrar_sesion_label.bind("<Leave>", lambda e: self.cerrar_sesion_label.config(cursor=""))

        self.protocol("WM_DELETE_WINDOW", self.destroy)  # Handle the modal closure

    def on_cerrar_sesion(self):
        self.destroy()
        self.master.close_session()
        self.destroy()

class AlumnView(tk.Frame):
    def __init__(self, master, switch_view):
        super().__init__(master)
        self.root = tk.Frame(self, bg="grey")
        self.root.pack(expand=True, fill=tk.BOTH)
        self.switch_view = switch_view

        # Header
        self.header = tk.Frame(self.root, bg="white", height=60)
        self.header.pack(fill=tk.X, side=tk.TOP)

        self.header_text = tk.Label(self.header, text="Asignar Cursos", bg="white", fg="black", font=("Helvetica", 16))
        self.header_text.pack(side=tk.LEFT, padx=10)

        # Bind left-click event to header_text to trigger assign_courses method
        self.header_text.bind("<Button-1>", self.assign_courses)
        self.header_text.bind("<Enter>", lambda e: self.header_text.config(cursor="hand2"))
        self.header_text.bind("<Leave>", lambda e: self.header_text.config(cursor=""))

        self.profile_section = tk.Frame(self.header, bg="white")
        self.profile_section.pack(side=tk.RIGHT, padx=10, pady=10)

        # Create a menu with a single option "Cerrar sesión"
        self.menu = tk.Menu(self.profile_section, tearoff=0)
        self.menu.add_command(label="Cerrar sesión", command=self.close_session)

        # Bind right-click event to profile_section to display the menu
        self.profile_section.bind("<Button-1>", self.show_menu)
        self.profile_section.bind("<Enter>", lambda e: self.profile_section.config(cursor="hand2"))
        self.profile_section.bind("<Leave>", lambda e: self.profile_section.config(cursor=""))

        self.username = tk.Label(self.profile_section, text="Username", bg="white", fg="black", font=("Helvetica", 16))
        self.username.pack(side=tk.LEFT)
        # Bind the same events to username label
        self.username.bind("<Button-1>", self.show_menu)
        
        self.image_viewer_canvas = ImageViewerCanvas(master=self.profile_section, username='user', width=40, height=40)
        self.image_viewer_canvas.pack(side=tk.RIGHT, padx=10)
        # Bind the same events to image_viewer_canvas
        self.image_viewer_canvas.bind("<Button-1>", self.show_menu)

        # Border line
        self.border_line = tk.Frame(self.root, height=1, bg='black')
        self.border_line.pack(fill=tk.X, side=tk.TOP)

        # Body
        self.message_label = tk.Label(self.root, text="Sin cursos asignados", bg="grey", fg="white", font=("Helvetica", 24))
        self.message_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
    def show_menu(self, event):
        self.modal = CerrarSesionModal(master=self)
        # Optionally, set focus to the modal to ensure it stays on top
        self.modal.focus_set()

    def close_session(self):
        import sys
        import os
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
        from main_view import MainView  # Conditional import
        self.switch_view('MainView')

    def assign_courses(self, event=None):
        from sesion.alumn.assign_view import AssignView  # Conditional import
        self.switch_view('AssignView')
