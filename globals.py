#import os
import json

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

def CreateCourse(codigo, nombre, costo, horario, cupo, cat):
    with open('courses.json', 'r') as f:
        try:
            courses_dict = json.load(f)
        except json.decoder.JSONDecodeError:  # Handles an empty or non-existent file
            courses_dict = {}
            
    # Add new user data
    courses_dict[codigo] = {
        "nombre": nombre,
        "costo": costo,
        "horario": horario,
        "cupo": cupo,
        "cat": cat
    }

    # Write the updated data back to the file
    with open('courses.json', 'w') as f:
        json.dump(courses_dict, f, indent=4)