import tkinter as tk
import sys
import os
import json
import globals
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from image_display import ImageViewerCanvas

class CourseFrame(tk.Frame):
    def __init__(self, master, admin_view, course_code, course_data):
        super().__init__(master)
        self.admin_view = admin_view  # Store the admin_view argument as an instance variable
        self.config(borderwidth=1, relief="solid")
        self.course_data = course_data  # Store course_data as an instance variable

        #Display course code and name in a larger font
        name_label = tk.Label(self, text=f"{course_data['Código']} - {course_data['Nombre']}", font=("Helvetica", 18))
        name_label.grid(row=0, column=0, columnspan=2, sticky='w', padx=5, pady=5)

        # Display other course data
        for i, (key, value) in enumerate(course_data.items(), start=1):
            if key not in ['Código', 'Nombre', 'Alumnos']:  # skip
                label = tk.Label(self, text=(f"{key}" + "\t" + f"{value}"))
                label.grid(row=i, column=0, sticky='w', padx=5, pady=5)
        
        # Create a new button
        self.print_button = tk.Button(self, text="Ver curso", command=self.print_message)
        self.print_button.grid(row=i+2, column=0, columnspan=2, padx=5, pady=5)  # Adjust the row value accordingly

    def print_message(self):
        print("Move a la vista del alumno")

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

class Header(tk.Frame):
    def __init__(self, master, switch_view, **kwargs):
        super().__init__(master, **kwargs)
        self.switch_view = switch_view
        self.config(bg="white", height=60)

        self.header_text = tk.Label(self, text="Gestión de Cursos", bg="white", fg="black", font=("Helvetica", 16))
        self.header_text.pack(side=tk.LEFT, padx=10)

        # Bind left-click event to header_text to trigger assign_courses method
        self.header_text.bind("<Button-1>", self.assign_courses)
        self.header_text.bind("<Enter>", lambda e: self.header_text.config(cursor="hand2"))
        self.header_text.bind("<Leave>", lambda e: self.header_text.config(cursor=""))

        self.profile_section = tk.Frame(self, bg="white")
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
        
        self.image_viewer_canvas = ImageViewerCanvas(master=self.profile_section, username=globals.user_session, width=40, height=40)
        self.image_viewer_canvas.pack(side=tk.RIGHT, padx=10)
        # Bind the same events to image_viewer_canvas
        self.image_viewer_canvas.bind("<Button-1>", self.show_menu)

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

class AlumnView(tk.Frame):
    def __init__(self, master, switch_view):
        super().__init__(master)
        self.root = tk.Frame(self, bg="grey")
        self.root.pack(expand=True, fill=tk.BOTH)
        self.switch_view = switch_view

        # Header
        self.header = Header(self.root, self.switch_view, bg="white", height=60)
        self.header.pack(fill=tk.X, side=tk.TOP)

        # Body
        self.message_label = tk.Label(self.root, text="Sin cursos asignados", bg="white", fg="black", font=("Helvetica", 24))
        self.message_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Call the method to display assigned courses
        self.display_assigned_courses()

    def display_assigned_courses(self):
        try:
            with open('courses.json', 'r') as file:
                courses_dict = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            courses_dict = {}
        
        # Filter out the courses assigned to the current user
        assigned_courses = {k: v for k, v in courses_dict.items() if globals.user_session in v['Alumnos']}
        
        # Remove the no courses message if there are assigned courses
        if assigned_courses:
            self.message_label.place_forget()

            # Display assigned courses
            self.course_frames = []  # List to hold the CourseFrame instances
            self.body_frame = tk.Frame(self.root)  # Create a frame to hold the courses
            self.body_frame.pack(fill=tk.BOTH, expand=True)

            for i, (course_code, course_data) in enumerate(assigned_courses.items()):
                course_frame = CourseFrame(self.body_frame, self, course_code, course_data)  # Assuming CourseFrame is defined to handle displaying a course
                row, col = divmod(i, 3)  # Arrange courses in a grid with 3 columns
                course_frame.grid(row=row, column=col, padx=10, pady=10)
                self.course_frames.append(course_frame)  # Store the CourseFrame instance