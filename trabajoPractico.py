Mati Danunzio
matidanunzio
En línea



Mensaje directo

Valen Cura
ALIAS
Neymar Junior 7.5m
Buscar

Chat de
1 mensaje nuevo desde las 10:27
Marcar como leído

Valen Cura
Valen Cura#2522
Este es el comienzo de tu historial de mensajes directos con Valen Cura.

1 servidor en común

Eliminar amigo

Bloquear
10 de mayo de 2023

Valen Cura — 10/05/2023 21:55
mati
[21:56]
venite al chat del grupo si estas al pedo
12 de mayo de 2023

Valen Cura — 12/05/2023 15:16
#include<stdio.h> #include<stdlib.h> num = 1; int main(){     int i,num;     for (i=1;i<=20;i++)     {         printf(num);         num = num+2;      }     system("pause");     return 0; }
27 de julio de 2023

Valen Cura — 27/07/2023 18:32
pasame el sv
15 de agosto de 2023
Tienes una llamada perdida de 
Valen Cura
 que ha durado unos segundos.
 — 15/08/2023 20:26
Valen Cura
 ha iniciado una llamada que ha durado un minuto.
 — 15/08/2023 20:44
3 de octubre de 2023
Valen Cura
 ha iniciado una llamada que ha durado unos segundos.
 — 03/10/2023 19:06
18 de octubre de 2023

Valen Cura — 18/10/2023 14:37
from abc import ABC, abstractmethod import generar_contrasenia as g_c  lista_estudiantes = [] lista_profesores = [] def menu():     print("Menú:")     print("1. Ingresar como alumno")     print("2. Ingresar como profesor")     print("3. Ver cursos")     print("4. Salir")  class Usuario(ABC):      def init(self,nombre,apellido,email,contrasenia):         if not isinstance(nombre, str):             raise TypeError("El nombre debe ser una cadena de texto.")         if not isinstance(apellido, str):             raise TypeError("El apellido debe ser una cadena de texto.")         if not isinstance(email, str):             raise TypeError("El email debe ser una cadena de texto.")         if not isinstance(contrasenia, str):             raise TypeError("La contraseña debe ser una cadena de texto.")         self._nombre = nombre         self._apellido = apellido         self._email = email         self._contrasenia = contrasenia           @abstractmethod     def str(self):         ret
[14:37]
from abc import ABC, abstractmethod
import generar_contrasenia as g_c

lista_estudiantes = []
lista_profesores = []
def menu():
Expandir
message.txt
4 KB

Valen Cura — 18/10/2023 19:49
from abc import ABC, abstractmethod
import generar_contrasenia as g_c

lista_estudiantes = []
lista_profesores = []

Expandir
message.txt
6 KB

Mati Danunzio — 18/10/2023 20:01
from abc import ABC, abstractmethod
import generar_contrasenia as g_c

lista_estudiantes = []
lista_profesores = []

Expandir
message.txt
6 KB
19 de octubre de 2023

Valen Cura — 19/10/2023 15:18
from abc import ABC, abstractmethod
import generar_contrasenia as g_c

lista_estudiantes = []
lista_profesores = []
cursosTotales = []
Expandir
message.txt
9 KB

Valen Cura — 19/10/2023 15:59
from abc import ABC, abstractmethod
import generar_contrasenia as g_c

lista_estudiantes = []
lista_profesores = []
cursosTotales = []
Expandir
message.txt
10 KB

Mati Danunzio — 19/10/2023 16:21
from abc import ABC, abstractmethod
import generar_contrasenia as g_c

lista_estudiantes = []
lista_profesores = []
cursosTotales = []
Expandir
message.txt
10 KB
20 de octubre de 2023

Valen Cura — 20/10/2023 15:52
from abc import ABC, abstractmethod
import generar_contrasenia as g_c

lista_estudiantes = []
lista_profesores = []
cursosTotales = []
Expandir
message.txt
12 KB
22 de octubre de 2023

Valen Cura — 22/10/2023 15:04
#Modulos utilizados
from abc import ABC, abstractmethod
import generar_contrasenia as g_c

#Listas vacias para almacenar estudiantes, profesores, y cursos respectivamente.
lista_estudiantes = []
Expandir
message.txt
12 KB
24 de octubre de 2023

Valen Cura — ayer a las 14:04
https://github.com/ValentinCura/TpProgramacionII
GitHub
GitHub - ValentinCura/TpProgramacionII
Contribute to ValentinCura/TpProgramacionII development by creating an account on GitHub.
[14:07]

TpProgramacionII.zip
96.64 KB

Mati Danunzio — ayer a las 14:09

TrabajoPracticoProgramacionII.pdf
15.56 KB

Valen Cura — ayer a las 21:11
discord?

Mati Danunzio — ayer a las 21:54
nuuu me baño y me voy a dormir un ñosue
25 de octubre de 2023
NUEVO

Valen Cura — hoy a las 10:27
#Modulos utilizados
from abc import ABC, abstractmethod
import generar_contrasenia as g_c

#Listas vacias para almacenar estudiantes, profesores, y cursos respectivamente.
lista_estudiantes = []
Expandir
message.txt
15 KB

Enviar mensaje a @Valen Cura
﻿




 para seleccionar

Valen Cura
Valen Cura#2522
MIEMBRO DE DISCORD DESDE
19 jun 2017
NOTA

TRANSMITIENDO EN EL GRAN SERVIDOR
Compartiendo su pantalla

Viendo una transmisión

1 servidor en común
#Modulos utilizados
from abc import ABC, abstractmethod
import generar_contrasenia as g_c

#Listas vacias para almacenar estudiantes, profesores, y cursos respectivamente.
lista_estudiantes = []
lista_profesores = []
cursosTotales = []

#Menu Alumno
def menuAlumno(email_ingresado):
    opcionAlumno = 0
    while opcionAlumno != 3:
        print("\n.: Menú del Alumno :.")
        print("1. Matricularse a un curso")
        print("2. Ver cursos")
        print("3. Volver al menú principal")
        opcionAlumno = int(input("Ingrese su opción: "))

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
            for estudiante in lista_estudiantes:
                if estudiante._email == email_ingresado:
                    if not estudiante._mis_cursos:
                        print(f"\nUsted no se encuentra matriculado en ningun curso.")

                    else:
                        print(f"Cursos:")
                        i=1
                        for cursoInd in estudiante._mis_cursos:
                            print(f"{i}. {cursoInd._nombre}")
                            i += 1
                        indice = i-1
                        opcCurso = int(input("Seleccione curso... "))
                        if opcCurso <= 0 or opcCurso > indice:
                            print(f"Error, no selecciono correctamente")
                        else:
                            if not estudiante._mis_cursos[opcCurso - 1]._archivos:
                                print(f"Sin archivos")
                            else: 
                                print("Archivos:")
                                for archivo in estudiante._mis_cursos[opcCurso - 1]._archivos:
                                    print(archivo)
                    break


        elif opcionAlumno == 3:
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
                            print(f"\nNombre: {profesor._mis_cursos[opcionCurso]._nombre}\nContrasenia: {profesor._mis_cursos[opcionCurso]._contrasenia_matriculacion}")
                            
                                             
                                             
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
#Clase estudiante
class Estudiante(Usuario):

    def __init__(self, nombre, apellido, email, contrasenia,legajo,anioInscripcion):
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
#Clase profesor
class Profesor(Usuario):

    def __init__(self, nombre, apellido, email, contrasenia,titulo,anioEgreso):
        super().__init__(nombre, apellido, email, contrasenia)
        self._titulo = titulo
        self._anio_egreso = anioEgreso
        self._mis_cursos = []
        #lista_profesores.append(self)

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
            cursoGenerado.generar_contrasenia()
            añadir = int(input(f"Desea añadir archivos?\n1.Si\n2.No\n")) #Si bien no se aclara en la consigna, hicimos este apartado para añadir archivos.
            while añadir != 2:
                if añadir < 1 or añadir > 2:
                    print(f"\nError... Seleccione correctamente.")
                    añadir = int(input(f"Desea añadir archivos?\n1.Si\n2.No\n"))
                elif añadir == 1:
                    archivo = 0 #Le damos un valor para iniciar el bucle
                    while archivo != '2':
                        archivo = input(f"\nIngrese el nombre del archivo que desee añadir, precione dos para salir:\n")
                        if archivo != '2':
                            cursoGenerado._archivos.append(archivo)
                        elif archivo == '2':
                            print(f"\nSaliendo...")
                            añadir = 2    
            cursosTotales.append(cursoGenerado)
            self._mis_cursos.append(cursoGenerado)
            print(f"\nCurso generado exitosamente...")
            print(f"Nombre: {cursoGenerado._nombre}\nContraseña: {cursoGenerado._contrasenia_matriculacion}")
            if not cursoGenerado._archivos:
                print(f"Sin archivos")
            else:
                print(f"Archivos:")
                for archivoIndividual in cursoGenerado._archivos:
                    print(archivoIndividual)

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
class Curso():
    
    def __init__(self,nombre):
        self._nombre = nombre
        self._contrasenia_matriculacion = None
        self._archivos = []
        
    def __str__(self) -> str:
        return f"{self._nombre}\nContrasenia: {self._contrasenia_matriculacion}"
    def generar_contrasenia(self) -> str:
        contrasenia = g_c.generar_contrasenia()
        self._contrasenia_matriculacion = contrasenia
        
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
