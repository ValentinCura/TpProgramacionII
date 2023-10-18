from abc import ABC, abstractmethod
import generar_contrasenia as g_c

lista_estudiantes = []
lista_profesores = []
def menu():
    print("Menú:")
    print("1. Ingresar como alumno")
    print("2. Ingresar como profesor")
    print("3. Ver cursos")
    print("4. Salir")

class Usuario(ABC):

    def __init__(self,nombre,apellido,email,contrasenia):
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena de texto.")
        if not isinstance(apellido, str):
            raise TypeError("El apellido debe ser una cadena de texto.")
        if not isinstance(email, str):
            raise TypeError("El email debe ser una cadena de texto.")
        if not isinstance(contrasenia, str):
            raise TypeError("La contraseña debe ser una cadena de texto.")
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia

    
    @abstractmethod
    def __str__(self):
        return f"Nombre: {self._nombre}\nApellido: {self._apellido}\nEmail: {self._email}\nContrasenia: {self._contrasenia}"

    @abstractmethod
    def validar_credenciales(self, mail_a_validar, contrasenia_a_validar):
        pass
            

class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia,legajo,anioInscripcion):
        super().__init__(nombre, apellido, email, contrasenia)
        self._legajo = legajo
        self._anio_inscripcion_carrera = anioInscripcion
        lista_estudiantes.append(self)

    def __str__(self):
        return "Soy un estudiante"
    def validar_credenciales(mail_a_validar, contrasenia_a_validar):
        for estudiante in lista_estudiantes:
            if estudiante._email == mail_a_validar and estudiante._contrasenia == contrasenia_a_validar:
                return True
            else:
                return False

    def matricular_en_curso(curso):
        pass
class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia,titulo,anioEgreso):
        super().__init__(nombre, apellido, email, contrasenia)
        self._titulo = titulo
        self._anio_egreso = anioEgreso
        lista_profesores.append(self)
    def __str__(self):
        return "Soy un profesor"
    
    def dictar_curso(curso):
        pass
    def validar_credenciales(mail_a_validar, contrasenia_a_validar):
        for profesor in lista_profesores:
            if profesor._email == mail_a_validar and profesor._contrasenia == contrasenia_a_validar:
                return True
            else:
                return False

class Curso():
    def __init__(self,nombre):
        self._nombre = nombre
        self._contrasenia_matriculacion = None
        
    def __str__(self) -> str:
        return f"Nombre del curso: {self._nombre}\nContrasenia: {self._contrasenia_matriculacion}"
    def generar_contrasenia(self) -> str:
        contrasenia = g_c.generar_contrasenia()
        self._contrasenia_matriculacion = contrasenia
        

Pepe = Estudiante('Pepe','Quiroga','pepequiroga@gmail.com','pepe123',11223344,2015)

validacion_pepe = Estudiante.validar_credenciales("pepequiroga@gmail.com",'pepe123')
print(validacion_pepe)

Sebastian = Profesor('Sebastian','Cabrera','sebastiancabrera@gmail.com','sebas123','Profesor de Literatura',2015)
validacion_Sebastian = Profesor.validar_credenciales("sebastiancabrera@gmail.com",'sebas123')
print(validacion_Sebastian)

#programacion = Curso("ProgramacionII")
#programacion.generar_contrasenia()
