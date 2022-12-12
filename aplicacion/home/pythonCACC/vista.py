"""Este Modulo contiene las funciones a utilizar para decorar la salida del programa"""

from colorama import Fore, Style
import time
import pyfiglet # Esta libreria se instala con el comando PIP, pip install pyfiglet 


def decorarTitulos(frase,caracter, cantidad):
   from colorama import Fore
   print(Fore.CYAN+caracter*cantidad)
   print(Fore.WHITE+frase.center(50,"-"))
   print(Fore.CYAN+caracter*cantidad)

def decorarMenu():
   from colorama import Fore
   lineaDibujada="▄"*5+"█"+"▄"*44
   lineaDibujada2="▄"*50
   print(Fore.CYAN+lineaDibujada2)
   print(Fore.WHITE+"█ Nº █\t\t\t\t\tOpcion█")
   print(Fore.CYAN+lineaDibujada)
   listaDeOpciones={
      1:"Gestion de Trabajadores",
      2:"Reportes",
      3:"Listado de Trabajadores",
      4:"Autores del proyecto",
      0:"Salir"
      }
   
   for clave,valor in listaDeOpciones.items():
      print(Fore.WHITE+"█{:2}  █{:>40}█".format(clave,valor))
      print(Fore.CYAN+lineaDibujada) 
      
   print()   


def decorarMenuTrabajador():
   lineaDibujada="▄"*5+"█"+"▄"*44
   lineaDibujada2="▄"*50
   print(Fore.CYAN+lineaDibujada2)
   print(Fore.WHITE+"█ Nº █\t\t\t\t\tOpcion█")
   print(Fore.CYAN+lineaDibujada)
   listaDeOpciones={
      1:"Ingresar nuevo Trabajador",
      2:"Modificar datos Trabajador",
      3:"Eliminar trabajador",
      0:"Volver al menu principal"
      }
   
   for clave,valor in listaDeOpciones.items():
      print(Fore.WHITE+"█{:2}  █{:>40}█".format(clave,valor))
      print(Fore.CYAN+lineaDibujada) 
      
   print()   

def decorarMenuReportes():
   lineaDibujada="▄"*5+"█"+"▄"*44
   lineaDibujada2="▄"*50
   print(Fore.CYAN+lineaDibujada2)
   print(Fore.WHITE+"█ Nº █\t\t\t\t\tOpcion█")
   print(Fore.CYAN+lineaDibujada)
   listaDeOpciones={
      1:"Mostrar trabajadores Activos",
      2:"Mostrar trabajadores desocupados",
      3:"Mostrar desocupados en un rango de edad",
      4:"Mostrar trabajadores segun la profesion",
      0:"Volver al menu principal"
      }
   
   for clave,valor in listaDeOpciones.items():
      print(Fore.WHITE+"█{:2}  █{:>40}█".format(clave,valor))
      print(Fore.CYAN+lineaDibujada) 
      
   print()   


def decorarListaTrabajador(listado): #recibe la lista de diccionarios...
   encabezado = '{:10}{:10}{:10}{:10}{:10}{:10}'.format("NOMBRE","APELLIDO","EDAD","DNI","PROFESION","ESTADOACTUAL")
   print(Fore.WHITE+encabezado)
   for linea in listado:
      linea= '{:10}{:10}{:10}{:10}{:10}{:10}'.format(linea["nombre"],linea["apellido"],linea["edad"],linea["dni"],linea["profesion"],linea["estadoactual"])
      print(Fore.WHITE+linea)

def decorarEncontrado(per):
   encabezado = '{:10}{:10}{:10}{:10}{:10}{:10}'.format("NOMBRE","APELLIDO","EDAD","DNI","PROFESION","ESTADOACTUAL")
   print(Fore.WHITE+encabezado)
   per= '{:10}{:10}{:10}{:10}{:10}{:10}'.format(per["nombre"],per["apellido"],per["edad"],per["dni"],per["profesion"],per["estadoactual"])
   print(Fore.WHITE+per)


def decorarSaludo(saludo):
   saludofinal=pyfiglet.figlet_format(saludo)
   return saludofinal


def listadoAlumnos():
   print(Fore.LIGHTBLUE_EX+"PARTICIPARON DE ESTE PROYECTO LOS SIGUIENTES ALUMNOS: ")
   print()
   listadoParticipantes = [{1:'Gabriel',2:'Gonzalez'},{1:'Agustina',2:'Ferrini'},{1:'Coni',2:'Forgione'},{1:'Luis',2:'Giaccio'},{1:'Ariel',2:'Gonzalez'}]
   encabezado = '{:20}{:20}'.format("NOMBRE","APELLIDO")
   print(Fore.WHITE+encabezado)
   for alumno in listadoParticipantes:
      alumno = '{:20}{:20}'.format(alumno[1],alumno[2])
      print(Fore.CYAN+alumno)



limite = 45  ### cambia la velocidad a la que se hace la animacion de cargado

def barra_cargando(segmento,total,longitud):    ### funcion de barra de carga
   
    porcentaje = segmento / total
    completado = int(porcentaje * longitud)
    restante = longitud - completado
    barra = f"[{'#' * completado}{'^' * restante}{porcentaje:.2%}]"
    return barra

def temporizador_texto(texto):   ### fucion de presentacion del grupo 

    texto_convertido_a_lista = texto.split()
    for palabra in texto_convertido_a_lista:
        print(palabra, end=" ")
        time.sleep(.4)   ### temporidazor para que el bucle for se detenga X segundos


def barra_tiempo():
    print("")

    print(Fore.CYAN+Style.BRIGHT+"====================================")

    print("")
    
    temporizador_texto (Fore.WHITE+"Bienvenido a <CaC> Proyecto Grupo C")

    print("")
    print("")

    print(Fore.CYAN+Style.BRIGHT+"====================================")

    print("")
    print("")

    for i in range(limite + 1):
        time.sleep(0.05) ### temporizador para que el bucle for se detenga X segundos
        print(Fore.GREEN+Style.BRIGHT+barra_cargando(i,limite,40),end = "\r")

    print("")
    print("")



