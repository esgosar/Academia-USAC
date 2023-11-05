import os
import yagmail

class Mail:
    def __init__(self):
        self.yag = yagmail.SMTP(
            user='3354094580901@ingenieria.usac.edu.gt', 
            password=os.getenv("PASSWORD")
        )

    def block(self, mail, name):
        contents = f'''
            <html>
                <body>
                    <p>
                        {name},<br><br>
                        Por seguridad, hemos bloqueado su cuenta debido a múltiples intentos fallidos de inicio de sesión.
                        Para desbloquear su cuenta, por favor contacte con el administrador.<br><br>
                        Atentamente,<br>
                        El equipo de Soporte
                    </p>
                </body>
            </html>
            '''

        self.yag.send(
            to=mail,
            subject='Cuenta Bloqueada',
            contents=contents,
            headers={'From': 'Academia USAC <3354094580901@ingenieria.usac.edu.gt>'}
        )

    def confirm(self, mail, name):
        contents = f'''
            <html>
                <body>
                    <p>
                        {name},<br><br>
                        ¡Gracias por registrarse!<br><br>
                        Atentamente,<br>
                        El equipo de Soporte
                    </p>
                </body>
            </html>
            '''

        self.yag.send(
            to=mail,
            subject='Cuenta Registrada',
            contents=contents,
            headers={'From': 'Academia USAC <3354094580901@ingenieria.usac.edu.gt>'}
        )

    def recovery(self, mail, name, password):
        contents = f'''
            <html>
                <body>
                    <p>
                        {name},<br><br>
                        Hemos recibido una solicitud para restablecer su contraseña.<br>
                        Su contraseña es: {password}
                        Si no ha solicitado un restablecimiento de contraseña, ignore este correo electrónico.<br><br>
                        Atentamente,<br>
                        El equipo de Soporte
                    </p>
                </body>
            </html>
            '''

        self.yag.send(
            to=mail,
            subject='Recuperación de Contraseña',
            contents=contents,
            headers={'From': 'Academia USAC <3354094580901@ingenieria.usac.edu.gt>'}
        )

    def assignation(self, mail, name, course):
        contents = f'''
            <html>
                <body>
                    <p>
                        {name},<br><br>
                        Nos complace informarle que ha sido asignado al curso {course}.<br><br>
                        ¡Esperamos que disfrute su aprendizaje!<br><br>
                        Atentamente,<br>
                        El equipo de Coordinación Académica
                    </p>
                </body>
            </html>
            '''

        self.yag.send(
            to=mail,
            subject='Curso Asignado',
            contents=contents,
            headers={'From': 'Academia USAC <3354094580901@ingenieria.usac.edu.gt>'}
        )

    def unassignation(self, mail, name, course):
        contents = f'''
            <html>
                <body>
                    <p>
                        {name},<br><br>
                        Le confirmamos que ha eliminado el curso {course} de su lista de cursos asignados.<br><br>
                        Si tiene alguna pregunta o necesita asistencia, no dude en contactarnos.<br><br>
                        Atentamente,<br>
                        El equipo de Coordinación Académica
                    </p>
                </body>
            </html>
            '''

        self.yag.send(
            to=mail,
            subject='Curso Desasignado',
            contents=contents,
            headers={'From': 'Academia USAC <3354094580901@ingenieria.usac.edu.gt>'}
        )
