from abc import ABC, abstractmethod
import generar_contrasenia as g_c

lista_estudiantes = []
lista_profesores = []
cursosTotales = []
def menuAlumno(email_ingresado):
    opcionAlumno = 0
    while opcionAlumno != 3:
        print("\n.: Menú del Alumno :.")
        print("1. Matricularse a un curso")
        print("2. Ver curso")
        print("3. Volver al menú principal")
        opcionAlumno = int(input("Ingrese su opción: "))

        if opcionAlumno == 1:
            if not cursosTotales:
                print("\nNo hay cursos disponibles.\n")
            else:
                for cursoIndividual in cursosTotales:
                    print("Cursos disponibles:")
                    print(cursoIndividual._nombre)
                
        elif opcionAlumno == 2:
            print("\nVer curso...")

        elif opcionAlumno == 3:
            print("\nVolviendo al menu principal... \n")

        else:
            print("\nOpción no válida. Intente nuevamente.")

def menuProfesor(email_ingresado):
    opcionProfesor = 0
    while opcionProfesor != 3:
        print("\n.: Menú del Profesor :.")
        print("1. Dar un curso")
        print("2. Ver curso")
        print("3. Volver al menú principal")
        
        opcionProfesor = int(input("Ingrese su opción: "))

        if opcionProfesor == 1:
            print("\nMatricularse a un curso...")
            if martin._email == email_ingresado:
                martin.dictar_curso()

            elif juan._email == email_ingresado:
                
                juan.dictar_curso()
            else:
                sebastian.dictar_curso()



        elif opcionProfesor == 2:
            print("\nVer curso...")
        elif opcionProfesor == 3:
            print("\nVolviendo al menú principal... \n")
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
                    menuAlumno(email_ingresado)
                else:print("\nError de ingreso...\n")
            else: print("\nDebe darse de alta en el alumnado...\n")

        elif opcion == 2:
            email_ingresado = str(input("Ingrese su mail: "))
            password_ingresado = str(input("Ingrese su contrasenia: "))
            profesor = Profesor.validar_credenciales(email_ingresado)
            if profesor:
                profesor = Profesor.validar_credenciales(email_ingresado,password_ingresado)
                if profesor:
                    menuProfesor(email_ingresado)
                else:
                    print("\nError de ingreso...\n")
            else:
                print("\nDebe darse de alta en el profesorado...\n")


        elif opcion == 3:
            print("Seleccionó la opción 3")
            print("Materia: InglesI\tCarrera: Tecnicatura Universitaria en Programación")
            print("Materia: InglesII\tCarrera: Tecnicatura Universitaria en Programación")
            print("Materia: Laboratorio I\tCarrera: Tecnicatura Universitaria en Programación")
            print("Materia: Laboratorio II\tCarrera: Tecnicatura Universitaria en Programación")
            print("Materia: Programación I\tCarrera: Tecnicatura Universitaria en Programación")
            print("Materia: Programación II\tCarrera: Tecnicatura Universitaria en Programación")

            
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
        self._listaCursos = []

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
        self._cursosProfesor = []
        lista_profesores.append(self)
    def __str__(self):
        return "Soy un profesor"
    
    def dictar_curso(self):
        nombreCurso = str(input("Ingrese el nombre de su curso: "))
        cursoGenerado = Curso(nombreCurso)
        cursoGenerado.generar_contrasenia()
        cursosTotales.append(cursoGenerado)
        self._cursosProfesor.append(cursoGenerado)
        print(f"Curso generado exitosamente...")
        print(f"Nombre: {cursoGenerado._nombre}\nContraseña: {cursoGenerado._contrasenia_matriculacion}\n")

    def validar_credenciales(mail_a_validar=None, contrasenia_a_validar=None):
        if mail_a_validar is not None and contrasenia_a_validar is not None:
            # Correo y Contraseña
            for profesor in lista_profesores:
                if profesor._email == mail_a_validar and profesor._contrasenia == contrasenia_a_validar:
                    return True
        elif mail_a_validar is not None:
            # Correo solamente
            for profesor in lista_profesores:
                if profesor._email == mail_a_validar:
                    return True
        elif contrasenia_a_validar is not None:
            # Contraseña solamente
            for profesor in lista_profesores:
                if profesor._contrasenia == contrasenia_a_validar:
                    return True
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
sebastian = Profesor('Sebastian','Cabrera','sebastiancabrera@gmail.com','sebas123','Ingenieria De Sistemas',2015)
martin = Profesor('Martin','Martinez','martinmartinez@gmail.com','marto123','Tecnico superior en Programacion',2011)
juan = Profesor('Juan','Perez','juanperez@gmail.com','juan123','Desarrollador de Software',2013)
lista_profesores.append(sebastian)
lista_profesores.append(martin)
lista_profesores.append(juan)

#Ejemplo Curso


#Llamamos al menu principal

menu()