class Contacto:
    """Informacion de un contacto.
    nombre  --str el cual tendra dicho nombre de usuario
    telefono    --int el cual tendra dicho numero de telefono
    email       --str el cual tedra el correo del usuario"""

    def __init__(self,nombre,telefono,email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return(F"Nombre: {self.nombre}, Telefono: {self.telefono}, Email: {self.email}")
    

usuario= Contacto("Paka",555_444_333,"esta@aqui.es")

print(usuario)
