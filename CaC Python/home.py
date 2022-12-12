import msvcrt

import os
import time
from time import sleep

from controlErrores import validarOpcion, validarCadena

from crudTrabajador import agregarTrabajador, obtenerTrabajadores, modificarTrabajador, eliminarTrabajador

from vista  import decorarTitulos, decorarMenu, decorarMenuTrabajador, barra_tiempo, decorarListaTrabajador, decorarMenuReportes, decorarSaludo, listadoAlumnos

from reportes import mostrarDesocupadosPorEdad, mostrarSegunDato, mostrarEstadoTrabajador

os.system("cls")
os.system("cls")

barra_tiempo()


while True:
    
    os.system("cls")
    decorarTitulos("Menu Principal","#",50)
    decorarMenu()
    opcion = validarOpcion("Selecccione una opcion: ")
    os.system("cls")
    
    if opcion == 0:
        os.system("cls")
        print(decorarSaludo("Hasta pronto !!!"))
        time.sleep(2)
        break
    elif opcion == 1: ############### INICIO MENU GESTION ################

        os.system("cls")
        decorarTitulos("Gestion Trabajadores","#",50)
        decorarMenuTrabajador()
        print()
        opcion = validarOpcion("Selecccione una opcion: ")
        
        if opcion ==1:
            os.system("cls")
            decorarTitulos("Agregar Trabajador","#",50)
            agregarTrabajador("Trabajadores.dat")
        elif opcion == 2:
            os.system("cls")
            decorarTitulos("Modificar datos Trabajadores","#",50)
            Modificado = modificarTrabajador("Trabajadores.dat")
            if Modificado == 0:
                print("volviendo al menu principal")
                sleep(2)
            else:
                print()
                print("Los datos del trabajador han sido modificados exitosamente! ") 
                print("Presione una tecla para volver al menu principal")
                msvcrt.getch() 
                os.system("cls")              
        elif opcion == 3:
            os.system("cls")
            decorarTitulos("Eliminar Trabajador","#",50)
            print()
            eliminado= eliminarTrabajador("Trabajadores.dat")
            if eliminado == 0:
                print("volviendo al menu principal")
                sleep(2)
  
    #########  FIN DEL MENU GESTION TRABAJADORES  ###########        
  
    elif opcion == 2: ######### INICIO MENU REPORTES ############
        os.system("cls")
        decorarTitulos("Reportes","#",50)
        decorarMenuReportes()
        opcion = validarOpcion("Selecccione una opcion: ")
        
        if opcion == 1:
            os.system("cls")
            dato= 'Trabajando'
            lista= mostrarEstadoTrabajador("Trabajadores.dat",dato)
            if lista == 0:
                print("No hay trabajadores activos... ")
                print("volviendo al menu principal")
                sleep(2)
            else:
                print("cargando el listado....")
                sleep(1)
                decorarListaTrabajador(lista)
                print()
                print("Presione una tecla para volver al menu principal")
                msvcrt.getch()  
        elif opcion == 2:
            os.system("cls")
            dato= 'Sin trabajo'
            lista= mostrarEstadoTrabajador("Trabajadores.dat",dato)
            if lista == 0:
                print("No hay trabajadores desocupados... ")
                print("volviendo al menu principal")
                sleep(2)
            else:
                print("cargando el listado....")
                sleep(1)
                decorarListaTrabajador(lista)
                print()
                print("Presione una tecla para volver al menu principal")
                msvcrt.getch()   
        elif opcion == 3:    
            os.system("cls")
            lista= mostrarDesocupadosPorEdad("Trabajadores.dat")
            if lista == 0:
                print("No hay trabajadores con ese rango de edad... ")
                print("volviendo al menu principal")
                sleep(2)
            else:
                print("cargando el listado....")
                sleep(1)
                decorarListaTrabajador(lista)
                print()
                print("Presione una tecla para volver al menu principal")
                msvcrt.getch()
        elif opcion == 4:
            dato=validarCadena("Ingrese la profesion que desea buscar: ")
            os.system("cls")
            lista= mostrarSegunDato("Trabajadores.dat",dato)
            if lista == 0:
                print("No hay trabajadores con esa profesion... ")
                print("volviendo al menu principal")
                sleep(2)
            else:
                print("cargando el listado....")
                sleep(1)
                decorarListaTrabajador(lista)
                print()
                print("Presione una tecla para volver al menu principal")
                msvcrt.getch()     
     
     #########  FIN DEL MENU REPORTES TRABAJADORES  ###########     

    elif opcion == 3: # listado
           os.system("cls")
           lista=obtenerTrabajadores("Trabajadores.dat")
           if lista == 0:
                print("volviendo al menu principal")
                sleep(2)
           else:
                print("cargando el listado....")
                sleep(1)
                decorarListaTrabajador(lista)
                print()
                print("Presione una tecla para volver al menu principal")
                msvcrt.getch()
    elif opcion == 4: ##### ALUMNOS PARTICIPANTES
        os.system("cls")
        listadoAlumnos()
        print()
        print("Presione una tecla para volver al menu principal")
        msvcrt.getch()
    
    else:
        os.system("cls")
        print("Elija una opcion correcta")

