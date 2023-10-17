import json

def iniciar_sesion(usuario_entry, contrasena_entry, update_error_message, count):
    # Obtener datos del usuario y contraseña
    user = usuario_entry.get()
    contrasena = contrasena_entry.get()
    isUser = False
    isPass = False
  
    # Leer el archivo JSON que contiene la información de los usuarios
    with open('./users.json', 'r') as f:
        data = json.load(f)
        for item in data:
            if user in item:
                isUser = True
                if item[user]['password'] == contrasena:
                    isPass = True
                    count[0] = 0  # Reset counter on successful login
                    break
                else:
                    count[0] += 1

    if not isUser:
        update_error_message('Usuario no registrado')
    else:
        update_error_message('')  # Clear the error message or hide it
        if not isPass:
            if count[0] >= 3:
                UserStatus(user, False)
                update_error_message('Usuario bloqueado')
            else:
                update_error_message('Contraseña incorrecta')