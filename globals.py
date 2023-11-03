#import os
import json

user_session = ''

nombres = ''
apellidos = ''
dpi = ''
fecha_nacimiento = ''
avatar = ''
usuario = ''
contrasena = ''
email = ''
phone = ''
user_type = ''

def CreateUser(nombres, apellidos, dpi, fecha_nacimiento, avatar, usuario, contrasena, email, phone, user_type):
    # Read existing data
    with open('users.json', 'r') as f:
        try:
            users_dict = json.load(f)
        except json.decoder.JSONDecodeError:  # Handles an empty or non-existent file
            users_dict = {}
    
    # Add new user data
    users_dict[usuario] = {
        "nombres": nombres,
        "apellidos": apellidos,
        "dpi": dpi,
        "nacimiento": fecha_nacimiento,
        "avatar": avatar,
        "password": contrasena,
        "email": email,
        "phone": phone,
        "tipo": user_type,
        "confirm": False  # la cuenta se crea pero esta bloqueada por defecto
    }
    
    # Write the updated data back to the file
    with open('users.json', 'w') as f:
        json.dump(users_dict, f, indent=4)

class Course:
    def __init__(self, filename='courses.json'):
        self.filename = filename

    def create(self, codigo, nombre, coste, horario, cupo, cat):
        with open(self.filename, 'r') as f:
            try:
                courses_dict = json.load(f)
            except json.decoder.JSONDecodeError:  # Handles an empty or non-existent file
                courses_dict = {}
        
        # Add new course data
        courses_dict[codigo] = {
            "Código": codigo,
            "Nombre": nombre,
            "Coste": coste,
            "Horario": horario,
            "Cupo": cupo,
            "Cat.": cat,
            "Alumnos": []  # Initialize an empty list for items
        }

        # Write the updated data back to the file
        with open(self.filename, 'w') as f:
            json.dump(courses_dict, f, indent=4)

    def assign(self, codigo, item):
        with open(self.filename, 'r') as f:
            try:
                courses_dict = json.load(f)
            except json.decoder.JSONDecodeError:
                raise ValueError(f'No course found with codigo: {codigo}')
        
        if codigo not in courses_dict:
            raise ValueError(f'No course found with codigo: {codigo}')

        # Append item to the course's Items list
        courses_dict[codigo]['Alumnos'].append(item)

        # Write the updated data back to the file
        with open(self.filename, 'w') as f:
            json.dump(courses_dict, f, indent=4)
    
    def check(self, codigo, item):
        with open(self.filename, 'r') as f:
            try:
                courses_dict = json.load(f)
            except json.decoder.JSONDecodeError:
                raise ValueError(f'No course found with codigo: {codigo}')

        if codigo not in courses_dict:
            raise ValueError(f'No course found with codigo: {codigo}')

        return item in courses_dict[codigo]['Alumnos']
    
    def delete(self, codigo):
        try:
            with open(self.filename, 'r') as file:
                courses_dict = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            courses_dict = {}

        courses_dict.pop(codigo, None)

        with open(self.filename, 'w') as file:
            json.dump(courses_dict, file, indent=4)