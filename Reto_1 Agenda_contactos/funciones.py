class Contacto:
    """Informacion de un contacto.
    Clase que representa un contacto con nombre, teléfono y email.

    nombre      --str -- nombre de usuario
    telefono    --str -- numero de telefono a futuro sera un --int--
    email       --str -- correo del usuario"""

    def __init__(self,nombre,telefono,email):
        """inicializa un nuevo contacto.

        Args:
        nombre      --str -- nombre de usuario
        telefono    --str -- numero de telefono
        email       --str -- correo del usuario"""

        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        """Devuelve los datos del contacto en una cadena.

        Return:
        --str--:Datos del contactos formateados."""

        return(F"Nombre: {self.nombre}, Telefono: {self.telefono}, Email: {self.email}")
    

#usuario= Contacto("Paka",555_444_333,"esta@aqui.es")   """borrar al finalizar"""

#print(usuario)                                         """borrar al finalizar"""

class GestorContactos:
    """Clase que gestiona una lista de contactos y almacena en un archivo .txt.
   
    Atributos:
    archivo     --str--: ruta del archivo txt.
    contactos   --lista[Contacto]--: Lista de objetos Contacto.
    """

    def __init__(self,archivo="contactos.txt"):
        """Inicia el gestor de carga de  los contactos en el archivo.txt
        Args:
        archivo --str--:nombre del archivo de almacenamiento (si quieres otro cambialo aqui)
        """
        self.archivo =archivo
        self.contactos = []
        self.cargar_contactos()
