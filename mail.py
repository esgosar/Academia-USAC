import smtplib

sender = '3354094580901@ingenieria.usac.edu.gt'
recive = 'esgonsar@gmail.com'
import yagmail

# Create the yagmail client
yag = yagmail.SMTP(
    user='Academia USAC <3354094580901@ingenieria.usac.edu.gt>', 
    password='xihwoW-2kotmi-cihmib'
)

def notify_block():
    yag.send(
        to=recive,
        subject='Bloqueo de Cuenta',
        contents=
        '''
        Estimado usuario,

        Por seguridad, hemos bloqueado su cuenta debido a múltiples intentos fallidos de inicio de sesión. Para desbloquear su cuenta, por favor siga las instrucciones enviadas a su correo electrónico.

        Atentamente,
        El equipo de Soporte
        '''
    )


notify_block()