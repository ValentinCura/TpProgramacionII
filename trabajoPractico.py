#Modulos utilizados
from abc import ABC, abstractmethod
import generar_contrasenia as g_c
from datetime import date

#Listas vacias para almacenar estudiantes, profesores, y cursos respectivamente.
lista_estudiantes = []
lista_profesores = []
cursosTotales = []

#Menu Alumno
def menuAlumno(email_ingresado):
    opcionAlumno = 0
    while opcionAlumno != 4:
        print("\n.: Menú del Alumno :.")
        print("1. Matricularse a un curso")
        print("2. Desmatricularse a un curso")
        print("3. Ver cursos")
        print("4. Volver al menú principal")
        opcionAlumno = int(input("\nIngrese: "))

        if opcionAlumno == 1:
            if not cursosTotales:
                print("\nNo hay cursos disponibles.\n")
            else:
                print("\nCursos disponibles:")
                i=1
                for cursoIndividual in cursosTotales:
                    print(f"{i}. {cursoIndividual._nombre}")
                    i+=1
                opcionCurso = int(input("\nIngrese el curso que desea... "))
                if opcionCurso < 1 or opcionCurso > i-1:
                    print("\nIngrese correctamente.")
                else: 
                    indiceCurso = opcionCurso - 1
                    cursoSeleccionado = cursosTotales[indiceCurso]
                    for estudiante in lista_estudiantes:
                        if estudiante._email == email_ingresado:
                            estudiante.matricular_en_curso(cursoSeleccionado)
                            break

        elif opcionAlumno == 2:
            bandera = True
            for estudiante in lista_estudiantes:
                if estudiante._email == email_ingresado:
                    if not estudiante._mis_cursos:
                        bandera = False

                    else:
                        print(f"Cursos:")
                        i=1
                        for cursoInd in estudiante._mis_cursos:
                            print(f"{i}. {cursoInd._nombre}")
                            i += 1
                        indice = i-1
                        opcCurso = int(input("Seleccione curso...  "))
                        if opcCurso <= 0 or opcCurso > indice:
                            print(f"Error, no selecciono correctamente")
                        else:
                            curso_a_eliminar = estudiante._mis_cursos[opcCurso - 1]
                            estudiante._mis_cursos.remove(curso_a_eliminar)
                            print(f"Se ha desmatriculado del curso: {curso_a_eliminar._nombre}")
                    break
            if not bandera:
                print(f"\nUsted no se encuentra matriculado en ningun curso.")

        elif opcionAlumno == 3:
            bandera = True
            for estudiante in lista_estudiantes:
                if estudiante._email == email_ingresado:
                    if not estudiante._mis_cursos:
                        bandera = False

                    else:
                        print(f"Cursos:")
                        i=1
                        for cursoInd in estudiante._mis_cursos:
                            print(f"{i}. {cursoInd._nombre}")
                            i += 1
                        indice = i-1
                        opcCurso = int(input("Seleccione curso...  "))
                        if opcCurso <= 0 or opcCurso > indice:
                            print(f"Error, no selecciono correctamente")
                        else:
                            if not estudiante._mis_cursos[opcCurso - 1]._archivos:
                                print(f"Sin archivos")
                            else: 
                                print("Archivos:")
                                for archivo in estudiante._mis_cursos[opcCurso - 1]._archivos:
                                    print(archivo)
                                print()
                    break
            if not bandera:
                print(f"\nUsted no se encuentra matriculado en ningun curso.")
                
        elif opcionAlumno == 4:
            print("\nVolviendo al menu principal... \n")

        else:
            print("\nOpción no válida. Intente nuevamente.")
#Menu profesor
def menuProfesor(email_ingresado):
    opcionProfesor = 0
    while opcionProfesor != 3:
        print("\n.: Menú del Profesor :.")
        print("1. Dar un curso")
        print("2. Ver curso")
        print("3. Volver al menú principal")
        
        opcionProfesor = int(input("\nIngrese su opción: "))

        if opcionProfesor == 1:
            for profesor in lista_profesores:
                if profesor._email == email_ingresado: #Coincidencia del mail
                    profesor.dictar_curso()
                    break

        elif opcionProfesor == 2:
            for profesor in lista_profesores:
                if profesor._email == email_ingresado: #Coincidencia del mail
                    if not profesor._mis_cursos:
                        print(f"\nUsted no posee cursos dados de alta\n")
                    else: 
                        print(f"\nCursos: ")
                        i=1
                        for curso in profesor._mis_cursos:
                            print(f"{i}-{curso._nombre}")
                            i+=1
                        opcionCurso = int(input(f"\nSeleccione un curso: "))
                        if opcionCurso > len(profesor._mis_cursos) or opcionCurso <= 0:
                            print(f"\nError. Debe ingresar el numero correctamente\n")
                        else:
                            opcionCurso -= 1
                            cantidadArchivos = len(profesor._mis_cursos[opcionCurso]._archivos)
                            print(f"\nNombre: {profesor._mis_cursos[opcionCurso]._nombre}\nContrasenia: {profesor._mis_cursos[opcionCurso]._contrasenia_matriculacion}\nCodigo: {profesor._mis_cursos[opcionCurso]._codigo}\nCantidad de archivos: {cantidadArchivos}")

                            
                                             
                                             
                    break

        elif opcionProfesor == 3:
            print("\nVolviendo al menú principal... \n")

        else:
            print("\nOpción no válida. Intente nuevamente.")
#Menu Principal
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
            if not cursosTotales:
                print("\nNo hay cursos disponibles aun\n")
            else:
                cursosOrdenados = sorted(cursosTotales, key=lambda cursoIndividual: cursoIndividual._nombre)
                print(f"Cursos:\n")
                i=1
                for curso in cursosOrdenados:
                    print(f"{i} {curso._nombre}\t Carrera: Tecnicatura Universitaria en Programación")
                    i+=1
                print()
                
        elif opcion == 4:
            print("Salida exitosa...")
#Clase abstracta Usuario
class Usuario(ABC):

    def __init__(self,nombre: str, apellido: str, email: str, contrasenia: str):
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
#Clase estudiante
class Estudiante(Usuario):

    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str,legajo,anioInscripcion):
        super().__init__(nombre, apellido, email, contrasenia)
        self._legajo = legajo
        self._anio_inscripcion_carrera = anioInscripcion
        lista_estudiantes.append(self)
        self._mis_cursos = []

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

    def matricular_en_curso(self,curso):
        clave_curso = input("Ingrese la clave de matriculación del curso: ")

        if curso in self._mis_cursos:
            print("Usted ya se encuentra matriculado en este curso...")
        else:
            if curso._contrasenia_matriculacion == clave_curso:
                self._mis_cursos.append(curso)
                print("\nCurso añadido correctamente!")
            else:
                print("\nClave de matriculación incorrecta.")
    def desmatricular_curso(self,curso):
        pass
#Clase profesor
class Profesor(Usuario):

    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str,titulo: str,anioEgreso: int):
        super().__init__(nombre, apellido, email, contrasenia)
        self._titulo = titulo
        self._anio_egreso = anioEgreso
        self._mis_cursos = []
        lista_profesores.append(self)

    def __str__(self):
        return "Soy un profesor"
    
    def dictar_curso(self):
        nombreCurso = str(input("Ingrese el nombre de su curso: "))
        cursoGenerado = Curso(nombreCurso)
        bandera = True  #Validacion de no dar de alta dos o mas veces un mismo curso.
        for curso in cursosTotales:
            if curso._nombre == cursoGenerado._nombre:
                bandera = False 

        if bandera:
            
            añadir = int(input(f"Desea añadir archivos?\n1.Si\n2.No\n")) #Si bien no se aclara en la consigna, hicimos este apartado para añadir archivos.
            while añadir != 2:
                if añadir < 1 or añadir > 2:
                    print(f"\nError... Seleccione correctamente.")
                    añadir = int(input(f"Desea añadir archivos?\n1.Si\n2.No\n"))
                elif añadir == 1:
                    archivoNombre = 0 #Le damos un valor para iniciar el bucle
                    while archivoNombre != '2':
                        archivoNombre = input(f"\nIngrese el nombre del archivo que desee añadir, precione dos para salir:\n")
                        if archivoNombre != '2':
                            archivoFecha = date.today()
                            archivoFormato = str(input(f"Ingrese el formato: "))
                            archivoAñadido = Archivo(archivoNombre,archivoFecha,archivoFormato)
                            cursoGenerado.nuevo_archivo(archivoAñadido)
                        elif archivoNombre == '2':
                            print(f"\nSaliendo...")
                            añadir = 2    
            cursosTotales.append(cursoGenerado)
            self._mis_cursos.append(cursoGenerado)
            print(f"\nCurso generado exitosamente...")
            print(f"Nombre: {cursoGenerado._nombre}\nContraseña: {cursoGenerado._contrasenia_matriculacion}\nCodigo: {cursoGenerado._codigo}")
            if not cursoGenerado._archivos:
                print(f"Sin archivos")
            else:
                print(f"Archivos:\n")
                p = 1
                for archivoIndividual in cursoGenerado._archivos:
                    print(f"{p}- {archivoIndividual}")
                    p+=1
                    print()

        else: 
            print(f"\nEl curso ya se encuentra dado de alta.")  

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
#Clase Curso
class Curso:
    prox_cod: int = 1

    def __init__(self, nombre):
        self._nombre = nombre
        self._codigo = Curso.prox_cod 
        Curso.prox_cod += 1
        self._contrasenia_matriculacion = Curso.generar_contrasenia()  # Llama al método de clase para generar la contraseña
        self._archivos = []

    def __str__(self) -> str:
        return f"{self._nombre}\nCódigo: {self._codigo}\nContraseña: {self._contrasenia_matriculacion}"

    def nuevo_archivo(self, archivo):
        self._archivos.append(archivo)
        print(f"\nArchivos agregados correctamente.\n")

    @classmethod
    def generar_contrasenia(cls) -> str:
        return g_c.generar_contrasenia()
    
class Archivo():
    def __init__(self,nombre: str, date, formato: str) -> None:
        self._nombre = nombre
        self._fecha = date
        self._formato = formato

    def __str__(self) -> str:
        return f"{self._nombre}\nFecha: {self._fecha}\nFormato: {self._formato}"
        



#Instancias estudiantes
pepe = Estudiante('Pepe','Quiroga','pepequiroga@gmail.com','pepe123',11223344,2015)
raul = Estudiante('Raul','Gonzales','raulg@gmail.com','raul112',11335562,2016)
lista_estudiantes.append(pepe)
lista_estudiantes.append(raul)

#Instancias profesores
sebastian = Profesor('Sebastian','Cabrera','sebastiancabrera@gmail.com','sebas123','Ingenieria De Sistemas',2015)
martin = Profesor('Martin','Martinez','martinmartinez@gmail.com','marto123','Tecnico superior en Programacion',2011)
juan = Profesor('Juan','Perez','juanperez@gmail.com','juan123','Desarrollador de Software',2013)
lista_profesores.append(sebastian)
lista_profesores.append(martin)
lista_profesores.append(juan)
#Llamamos al menu principal
menu()