import os
import yagmail

# Create the yagmail client
yag = yagmail.SMTP(
    user='3354094580901@ingenieria.usac.edu.gt', 
    password=os.getenv("PASSWORD")
)

def notify_block(mail, name):
    contents = f'''
    <html>
        <body>
            <h1>{name},</h1>
            <p>
                Por seguridad, hemos bloqueado su cuenta debido a múltiples intentos fallidos de inicio de sesión.
                Para desbloquear su cuenta, por favor contacte con el administrador respondiendo a este correo.
            </p>
            <p>
                Atentamente,<br>
                El equipo de Soporte
            </p>
        </body>
    </html>
    '''

    yag.send(
        to=mail,
        subject='Bloqueo de Cuenta',
        contents=contents,
        headers={'From': 'Academia USAC <3354094580901@ingenieria.usac.edu.gt>'}
    )

notify_block('esgosar@icloud.com', "José Estuardo González Sarceño")