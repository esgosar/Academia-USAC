import os
from dotenv import load_dotenv
from email.message import EmailMessage
import smtplib
import ssl
import tkinter as tk
from tkinter import messagebox
import re
import json

def enviar_correo(email):
    try:
        load_dotenv()

        contraseña_encriptada = "Ejemplo"

        email_sender = "esgosarlavida@gmail.com"
        password = os.getenv("PASSWORD")  # Contraseña guardada en .env
        email_receiver = email

        subject = "Recuperación de contraseña"
        body = f"Su contraseña es {contraseña_encriptada}"

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
    recuperacion = tk.Tk()
    recuperacion.title("Recuperación de Contraseña")
    recuperacion.geometry("500x350")

    titulo = tk.Label(recuperacion, text="Recuperación de Contraseña", font=("Helvetica", 20, "bold"))
    titulo.pack(pady=20)

    usuario_label = tk.Label(recuperacion, text="Usuario:", font=("Helvetica", 14))
    usuario_label.pack()

    user_entry = tk.Entry(recuperacion, font=("Helvetica", 14))
    user_entry.pack()
    
    def enviar_nueva_contraseña():
        isUser = False
        if user_entry.get() == '':
            messagebox.showerror("Error", "Introduzca un correo")
            return
        
        # Si el usuario existe motrar mensaje. Revise su correo. y volver a la vista MainView
        with open("./users.json", "r") as f:  # Leer el JSON
            data = json.load(f)
            if user_entry.get() in data:
                isUser = True
    
        # Validar que el usuario esté registrdo y mostrar error de usuario no registrado
        if not isUser:
            messagebox.showinfo("Error", "Usuario no registrado")
            return
        else:
            enviar_correo(data[user_entry.get()]['Correo'])
            # Si el usuario este validado enviar correo con la contraseña


    enviar_button = tk.Button(recuperacion, text="Recuperar", font=("Helvetica", 14), command=enviar_nueva_contraseña)
    enviar_button.pack(pady=20)

    recuperacion.mainloop()

def correo_valido(email):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zAZ0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(patron, email) is not None

