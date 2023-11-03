from globals import Course
import tkinter as tk
import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from image_display import ImageViewerCanvas

course = Course()

class CourseFrame(tk.Frame):
    def __init__(self, master, admin_view, course_code, course_data):
        super().__init__(master)
        self.admin_view = admin_view
        self.config(borderwidth=1, relief="solid")
        
        # Display course code and name in a larger font
        name_label = tk.Label(self, text=f"{course_data['Código']} - {course_data['Nombre']}", font=("Helvetica", 18))
        name_label.grid(row=0, column=0, columnspan=2, sticky='w', padx=5, pady=5)

        # Display other course data
        for i, (key, value) in enumerate(course_data.items(), start=1):
            if key not in ['Código', 'Nombre', 'Alumnos']:  # skip
                label = tk.Label(self, text=(f"{key}" + "\t" + f"{value}"))
                label.grid(row=i, column=0, sticky='w', padx=5, pady=5)
        
        # Create Delete button
        delete_button = tk.Button(self, text="Delete", command=lambda: self.delete_course(course_code))  # Assumes delete_course method exists
        delete_button.grid(row=i+1, column=0, columnspan=2, padx=5, pady=5)

    def delete_course(self, course_code):
        course.delete(course_code)  # Call the function to delete the course from the JSON file
        self.admin_view.switch_view('AdminView')  # Update the view
    
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
        items = ["Código", "Nombre", "Costo", "Horario", "Cupo", "Catedrático"]
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
        # Retrieve values from the Entry widgets
        codigo = self.labels_and_entries["Código"].get()
        nombre = self.labels_and_entries["Nombre"].get()
        costo = int(self.labels_and_entries["Costo"].get())
        horario = self.labels_and_entries["Horario"].get()
        cupo = int(self.labels_and_entries["Cupo"].get())
        cat = self.labels_and_entries["Catedrático"].get()
        # Call CreateCourse to store the values
        course.create(codigo, nombre, costo, horario, cupo, cat)
        self.master.switch_view('AdminView')
        self.destroy()


class AdminView(tk.Frame):
    def __init__(self, master, switch_view):
        super().__init__(master)
        self.root = tk.Frame(self, bg="white")
        self.root.pack(expand=True, fill=tk.BOTH)
        self.switch_view = switch_view

        # Header
        self.header = tk.Frame(self.root, bg="white", height=60)
        self.header.pack(fill=tk.X, side=tk.TOP)

        # Create "Crear Curso" label
        self.crear_curso_label = self.create_header_label("Crear Curso", self.create_course)
        self.crear_curso_label.pack(side=tk.LEFT)

        # Separator
        self.separator1 = tk.Label(self.header, text=" | ", bg="white", fg="black")
        self.separator1.pack(side=tk.LEFT)

        # Create "Registrar de Profesor" label
        self.profesor_label = self.create_header_label("Registrar de Profesor", self.registrar_profesor)
        self.profesor_label.pack(side=tk.LEFT)

        # Separator
        self.separator2 = tk.Label(self.header, text=" | ", bg="white", fg="black")
        self.separator2.pack(side=tk.LEFT)

        # Create "Notas" label
        self.notas_label = self.create_header_label("Notas", self.notas)
        self.notas_label.pack(side=tk.LEFT)

        # Separator
        self.separator3 = tk.Label(self.header, text=" | ", bg="white", fg="black")
        self.separator3.pack(side=tk.LEFT)

        # Create "Usuarios bloqueados" label
        self.bloqueados_label = self.create_header_label("Usuarios bloqueados", self.usuarios_bloqueados)
        self.bloqueados_label.pack(side=tk.LEFT)
        
        # Create a label for closing session
        self.close_session_label = tk.Label(self.header, text="Cerrar sesión", bg="white", fg="black", font=("Helvetica", 16), cursor="hand2")
        self.close_session_label.pack(side=tk.RIGHT, padx=10)
        # Bind left-click event to close_session_label to trigger close_session method
        self.close_session_label.bind("<Button-1>", lambda e: self.close_session())

        # Border line
        self.border_line = tk.Frame(self.root, height=1, bg='black')
        self.border_line.pack(fill=tk.X, side=tk.TOP)

        # Call method to check courses and get the courses dictionary
        courses_dict = self.check_courses_and_display_message()

        # Conditionally display courses based on whether courses_dict is empty
        if courses_dict:
            self.display_courses(courses_dict)
        else:
            self.display_no_courses_message()

    def close_session(self):
        import sys
        import os
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
        from main_view import MainView  # Conditional import
        self.switch_view('MainView')

    def create_course(self, event):
        self.modal = AssignCoursesModal(self)
    
    def check_courses_and_display_message(self):
        try:
            with open('courses.json', 'r') as f:
                courses_dict = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):  # Handles a non-existent or empty file
            courses_dict = {}

        return courses_dict  # Return the courses_dict

    def display_courses(self, courses_dict):
        self.body_frame = tk.Frame(self.root)
        self.body_frame.pack(fill=tk.BOTH, expand=True)

        for i, (course_code, course_data) in enumerate(courses_dict.items()):
            course_frame = CourseFrame(self.body_frame, self, course_code, course_data)
            row, col = divmod(i, 3)  # Arrange courses in a grid with 3 columns
            course_frame.grid(row=row, column=col, padx=10, pady=10)
    
    def display_no_courses_message(self):
        self.message_label = tk.Label(self.root, text="Sin cursos creados", bg="white", fg="grey", font=("Helvetica", 24))
        self.message_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def create_header_label(self, text, command):
        label = tk.Label(self.header, text=text, bg="white", fg="black", font=("Helvetica", 16), cursor="hand2")
        label.bind("<Button-1>", command)
        label.bind("<Enter>", lambda e: label.config(cursor="hand2"))
        label.bind("<Leave>", lambda e: label.config(cursor=""))
        return label

    def registrar_profesor(self, event):
        print("Registrar de Profesor clicked")

    def notas(self, event):
        print("Notas clicked")

    def usuarios_bloqueados(self, event):
        print("Usuarios bloqueados clicked")

    def create_course(self, event):
        print("Crear Curso clicked")
