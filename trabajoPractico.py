from abc import ABC, abstractmethod
import generar_contrasenia as g_c
def menu():
    print("Menú:")
    print("1. Ingresar como alumno")
    print("2. Ingresar como profesor")
    print("3. Ver cursos")
    print("4. Salir")

class Usuario(ABC):

    def __init__(self,nombre,apellido,email,contrasenia):
        self._nombre = nombre
        self._apellido = apellido
        self._mail = email
        self._contrasenia = contrasenia
    
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def validar_credenciales(self, email, contrasenia):
        pass    

class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia,legajo,anioInscripcion):
        super().__init__(nombre, apellido, email, contrasenia)
        self._legajo = legajo
        self._anio_inscripcion_carrera = anioInscripcion

    def __str__(self):
        return super().__str__()
    
    def matricular_en_curso(curso):
        pass
class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia,titulo,anioEgreso):
        super().__init__(nombre, apellido, email, contrasenia)
        self._titulo = titulo
        self._anio_egreso = anioEgreso

    def __str__(self):
        return super().__str__()
    
    def dictar_curso(curso):
        pass


class Curso():
    def __init__(self,nombre,contrasenia_matriculacion):
        self._nombre = nombre
        self._contrasenia_matriculacion = contrasenia_matriculacion
        
    def __str__(self) -> str:
        pass
    def generar_contrasenia(self) -> str:
        contraseña = g_c.generar_contrasenia
        return contraseña

    
