import os
from dotenv import load_dotenv
from email.message import EmailMessage
import smtplib
import ssl
import tkinter as tk
from tkinter import messagebox
import re
import json

def enviar_correo(email, contraseña_encriptada):
    try:
        load_dotenv()

        contraseña_encriptada = ""

        email_sender = "esgosarlavida@gmail.com"
        password = os.getenv("PASSWORD")  # Contraseña guardada en .env
        email_receiver = "3651686290101@ingenieria.usac.edu.gt"

        subject = "Recuperación de contraseña"
        body = f"El usuario que requiere modificación de contraseña es {email}. Su nueva contraseña es {contraseña_encriptada}"

        em = EmailMessage()
        em.set_content(body)
        em["Subject"] = subject
        em["From"] = email_sender
        em["To"] = email_receiver

        context = ssl.create_default_context()

        # Servidor de Gmail
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, password)
            smtp.send_message(em)

        messagebox.showinfo("Éxito", "Se ha enviado la nueva contraseña")

    except smtplib.SMTPAuthenticationError as e:
        messagebox.showerror("Error", "Ocurrió un problema al enviar el correo")

def vista_recuperacion():
    
    def validar_contraseña(contraseña):
        # Función para validar la contraseña según tus criterios
        return (len(contraseña) >= 8 and
                any(c.isupper() for c in contraseña) and
                any(c.isdigit() for c in contraseña) and
                any(c in "!@#$%^&*." for c in contraseña))
    
    recuperacion = tk.Tk()
    recuperacion.title("Recuperación de Contraseña")
    recuperacion.geometry("500x350")

    titulo = tk.Label(recuperacion, text="Recuperación de Contraseña", font=("Helvetica", 20, "bold"))
    titulo.pack(pady=20)

    usuario_label = tk.Label(recuperacion, text="Ingrese su correo electrónico:", font=("Helvetica", 14))
    usuario_label.pack()

    correo_entry = tk.Entry(recuperacion, font=("Helvetica", 14))
    correo_entry.pack()

    new_contr_label = tk.Label(recuperacion, text="Nueva Contraseña:", font=("Helvetica", 14))
    new_contr_label.pack()

    new_contr_entry = tk.Entry(recuperacion, show="*", font=("Helvetica", 14))
    new_contr_entry.pack()

    confirmacion_contr_label = tk.Label(recuperacion, text="Confirmar Contraseña:", font=("Helvetica", 14))
    confirmacion_contr_label.pack()

    confirmacion_entry = tk.Entry(recuperacion, show="*", font=("Helvetica", 14))
    confirmacion_entry.pack()

    def enviar_nueva_contraseña():
        email = correo_entry.get()
        contrasena_nueva = new_contr_entry.get()
        confirmacion = confirmacion_entry.get()

        if not correo_valido(email):
            messagebox.showerror("Error", "Correo electrónico inválido")
            return

        if contrasena_nueva != confirmacion:
            messagebox.showerror("Error", "Las contraseñas no coinciden")
            return

        if not validar_contraseña(contrasena_nueva):
            messagebox.showerror("Error", "La contraseña no cumple con los requisitos (mínimo 8 caracteres, al menos 1 mayúscula, 1 número y 1 signo)")
            return

        try:
            with open("users.json", "r") as archivo:  # Leer el JSON
                datos = json.load(archivo)

            usuario_encontrado = False 

            for usuario in datos:
                if usuario["email"] == email:
                    usuario_encontrado = True
                    break

            if usuario_encontrado:
                enviar_correo(email, contrasena_nueva)
                messagebox.showinfo("Recuperar contraseña", "Se envió el correo al administrador")
                recuperacion.destroy()  # Cerrar la ventana de recuperación
            else:
                messagebox.showerror("Error", "No se encontró el correo en la base de datos")
        except FileNotFoundError:
            messagebox.showerror("Error", "No se encontró el archivo de usuarios 'users.json'")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

    enviar_button = tk.Button(recuperacion, text="Enviar Nueva Contraseña", font=("Helvetica", 14), command=enviar_nueva_contraseña)
    enviar_button.pack(pady=20)

    recuperacion.mainloop()

def correo_valido(email):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zAZ0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None

