from abc import ABC, abstractmethod
import generar_contrasenia as g_c

lista_estudiantes = []
lista_profesores = []

def menuAlumno():
    opcionAlumno = 0
    while opcionAlumno != 3:
        print("\n.: Menú del Alumno :.")
        print("1. Matricularse a un curso")
        print("2. Ver curso")
        print("3. Volver al menú principal")
        
        opcionAlumno = int(input("Ingrese su opción: "))

        if opcionAlumno == 1:
            print("\nMatricularse a un curso...")
        elif opcionAlumno == 2:
            print("\nVer curso...")
        elif opcionAlumno == 3:
            print("\nVolviendo al menu principal... \n")
        else:
            print("\nOpción no válida. Intente nuevamente.")

def menu():
    
    opcion = 0
    while opcion != 4:
        print("Menu:")
        print("1. Ingresar como alumno")
        print("2. Ingresar como profesor")
        print("3. Ver cursos")
        print("4. Salir")
        opcion = int(input("\nSeleccione la opcion deseada: "))
        if opcion == 1:
            email_ingresado = str(input("Ingrese su mail: "))
            password_ingresado = str(input("Ingrese su contrasenia: "))
            estudiante = Estudiante.validar_credenciales(email_ingresado)
            if estudiante:
                estudiante = Estudiante.validar_credenciales(email_ingresado,password_ingresado)
                if estudiante:
                    menuAlumno()
                else:print("Error de ingreso...\n")
            else: print("\nDebe darse de alta en el alumnado...\n")

        elif opcion == 2:
            # Acciones para la opción 2
            print("Seleccionó la opción 2")

        elif opcion == 3:
            # Acciones para la opción 3
            print("Seleccionó la opción 3")
            
        elif opcion == 4:
            print("Salida exitosa...")
    
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
    def validar_credenciales(mail_a_validar=None, contrasenia_a_validar=None):
        if mail_a_validar is not None and contrasenia_a_validar is not None:
            # Correo y Contraseña
            for estudiante in lista_estudiantes:
                if estudiante._email == mail_a_validar and estudiante._contrasenia == contrasenia_a_validar:
                    return True
        elif mail_a_validar is not None:
            # Correo solamente
            for estudiante in lista_estudiantes:
                if estudiante._email == mail_a_validar:
                    return True
        elif contrasenia_a_validar is not None:
            # Contraseña solamente
            for estudiante in lista_estudiantes:
                if estudiante._contrasenia == contrasenia_a_validar:
                    return True
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
        
#Estudiantes
Pepe = Estudiante('Pepe','Quiroga','pepequiroga@gmail.com','pepe123',11223344,2015)
Raul = Estudiante('Raul','Gonzales','raulg@gmail.com','raul112',11335562,2016)

#Profesores
Sebastian = Profesor('Sebastian','Cabrera','sebastiancabrera@gmail.com','sebas123','Profesor de Literatura',2015)
Martin = Profesor('Martin','Martinez','martinmartinez@gmail.com','marto123','Profesor de Programacion',2011)

#Llamamos al menu principal

menu()


#programacion = Curso("ProgramacionII")
#programacion.generar_contrasenia()
