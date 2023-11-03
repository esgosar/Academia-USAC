import tkinter as tk
import json
from globals import Course

class CourseFrame(tk.Frame):
    def __init__(self, master, course_code, course_data):
        super().__init__(master)
        self.config(borderwidth=1, relief="solid")

        #Display course code and name in a larger font
        name_label = tk.Label(self, text=f"{course_data['Código']} - {course_data['Nombre']}", font=("Helvetica", 18))
        name_label.grid(row=0, column=0, columnspan=2, sticky='w', padx=5, pady=5)

        # Display other course data
        for i, (key, value) in enumerate(course_data.items(), start=1):
            if key not in ['Código', 'Nombre', 'Alumnos']:  # skip
                label = tk.Label(self, text=(f"{key}" + "\t" + f"{value}"))
                label.grid(row=i, column=0, sticky='w', padx=5, pady=5)

        # Create Delete button
        assign_button = tk.Button(self, text="Asignar", command=self.assign_course)
        assign_button.grid(row=i+1, column=0, columnspan=2, padx=5, pady=5)

    def assign_course(self):
        print("Hello")

class AssignView(tk.Frame):
    def __init__(self, master, switch_view):
        super().__init__(master)
        self.switch_view = switch_view
        self.root = tk.Frame(self, bg="grey")
        self.root.pack(expand=True, fill=tk.BOTH)
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
            course_frame = CourseFrame(self.body_frame, course_code, course_data)
            row, col = divmod(i, 3)  # Arrange courses in a grid with 3 columns
            course_frame.grid(row=row, column=col, padx=10, pady=10)
