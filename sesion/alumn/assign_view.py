import globals
import tkinter as tk
import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from image_display import ImageViewerCanvas
from notifications import Mail

course = globals.Course()

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

        if course.check(self.course_data['Código'], globals.user_session):
            # Create Delete button
            assign_button = tk.Button(self, text="Desasignar", command=self.unassign_course)
            assign_button.grid(row=i+1, column=0, columnspan=2, padx=5, pady=5)  
        else:
            # Create Delete button
            assign_button = tk.Button(self, text="Asignar", command=self.assign_course)
            assign_button.grid(row=i+1, column=0, columnspan=2, padx=5, pady=5)

    def unassign_course(self):
        course.unassign(self.course_data['Código'], globals.user_session)
        with open('./users.json', 'r') as f:
            data = json.load(f)

            if data[globals.user_session]:
                Mail().unassignation(
                data[globals.user_session]['Correo'],
                f"{data[globals.user_session]['Nombres']} {data[globals.user_session]['Apellidos']}",
                self.course_data['Nombre']
            )

        from sesion.alumn.assign_view import AssignView  # Conditional import
        self.admin_view.switch_view('AssignView')
        

    def assign_course(self):
        course.assign(self.course_data['Código'], globals.user_session)
        # Leer el archivo JSON que contiene la información de los usuarios
        with open('./users.json', 'r') as f:
            data = json.load(f)

            if data[globals.user_session]:
                Mail().assignation(
                data[globals.user_session]['Correo'],
                f"{data[globals.user_session]['Nombres']} {data[globals.user_session]['Apellidos']}",
                self.course_data['Nombre']
            )

        from sesion.alumn.assign_view import AssignView  # Conditional import
        self.admin_view.switch_view('AssignView')
        

class Header(tk.Frame):
    def __init__(self, master, switch_view, **kwargs):
        super().__init__(master, **kwargs)
        self.switch_view = switch_view
        self.config(bg="white", height=60)

        self.header_text = tk.Label(self, text="Cursos Asignados", bg="white", fg="black", font=("Helvetica", 16))
        self.header_text.pack(side=tk.LEFT, padx=10)

        # Bind left-click event to header_text to trigger assign_courses method
        self.header_text.bind("<Button-1>", self.back)
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

    def back(self, event=None):
        from sesion.alumn.alumn_view import AlumnView  # Conditional import
        self.switch_view('AlumnView')

class AssignView(tk.Frame):
    def __init__(self, master, switch_view):
        super().__init__(master)
        self.switch_view = switch_view
        self.root = tk.Frame(self, bg="grey")
        self.root.pack(expand=True, fill=tk.BOTH)
        # Header
        self.header = Header(self.root, self.switch_view, bg="white", height=60)
        self.header.pack(fill=tk.X, side=tk.TOP)

        self.display_courses()

    def display_courses(self):
        try:
            with open('courses.json', 'r') as f:
                courses_dict = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            courses_dict = {}

        self.body_frame = tk.Frame(self.root)
        self.body_frame.pack(fill=tk.BOTH, expand=True)

        for i, (course_code, course_data) in enumerate(courses_dict.items()):
            if not course.count(course_code) or globals.user_session in course_data['Alumnos']:
                course_frame = CourseFrame(self.body_frame, self, course_code, course_data)  # Pass self as the second argument
                row, col = divmod(i, 3)  # Arrange courses in a grid with 3 columns
                course_frame.grid(row=row, column=col, padx=10, pady=10)
