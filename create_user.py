import json

# Function to create a user dictionary
def CreateUserDict(username, nombre, apellido, fecha_nacimiento, telefono, dpi, email, password, user_type, confirmacion):
    return {
        username: {
            "nombre": nombre,
            "apellido": apellido,
            "fecha": fecha_nacimiento,
            "telf": telefono,
            "dpi": dpi,
            "email": email,
            "password": password,
            "tipo": user_type,
            "confirm": "true"
        }
    }

def JSONBuilder(usuario):
    # Read existing data
    with open('users.json', 'r') as f:
        try:
            users_list = json.load(f)
        except json.decoder.JSONDecodeError:  # Handles an empty or non-existent file
            users_list = []

    # Append new user data
    users_list.append(usuario)  # changed from user1 to user

    # Write the updated data back to the file
    with open('users.json', 'w') as f:
        json.dump(users_list, f, indent=4)