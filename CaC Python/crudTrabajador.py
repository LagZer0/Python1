"""Este modulo contiene funciones para Alta-Baja-Modificacion del Trabajador"""
from controlErrores import validarOpcion, validarCaracter, validarCadena
import os
from vista import decorarEncontrado
import  msvcrt
from time import sleep


def obtenerTrabajadores(nombreArchivo): #recibe el nombre de archivo "Trabajadores.dat"

  try:
    
    if os.stat(nombreArchivo).st_size == 0: # Este metodo comprueba si el archivo contiene datos evaluado byte.
        print(f"El archivo {nombreArchivo} se encuentra vacio")
        print("Presione |Enter| para volver al menu principal")
        msvcrt.getch()
        #os.system("cls")
        return 0
    else:
        archivo = open(nombreArchivo,"r")
        listaDeTrabajadores=[]
        
        for linea in archivo.readlines():# devuelve en cada linea una lista 
            trabajador=linea.replace('\n','') #aca creo una variable, que es innecesaria? ......
            trabajador=trabajador.split(",")  
            trabajador = {
                "nombre":trabajador[0],
                "apellido":trabajador[1],
                "edad":trabajador[2],
                "dni":trabajador[3],
                "profesion":trabajador[4],
                "estadoactual":trabajador[5]
                }
            listaDeTrabajadores.append(trabajador) #esto tendria que ser [{},{},{}]
        archivo.close()
        return listaDeTrabajadores
            
  except FileNotFoundError:
    print("El archivo no existe para mostrar")
    respuestaUsuario= validarCaracter("""Desea ingresar un trabajador a la base de datos ? 

Presione |S| para agregar o |N| para volver al menu principal: """)
    if respuestaUsuario == 'S':
       return agregarTrabajador(nombreArchivo)
    elif respuestaUsuario == 'N':
       return 0  
    
    
def agregarTrabajador(nombreArchivo):
    
    listadoTrabajadores=[]
    nombre = validarCadena("Ingrese el nombre: ")
    apellido= validarCadena("Ingrese el apellido: ")
    edad=validarOpcion("Ingrese la edad del trabajador: ")
    dni=validarOpcion("Ingrese el documento de identidad: ")
    profesion=validarCadena("Ingrese la profesion: ")
    estadoactual=validarCaracter("Situacion Laboral? presione |S| para empleado |N| para desempleado ")
    
    if estadoactual=="S":
        estadoactual="Trabajando"
    else:
        estadoactual="Sin trabajo"    
    perfilTrabajador={
        "nombre":nombre,
        "apellido":apellido,
        "edad":edad,
        "dni":dni,
        "profesion":profesion,
        "estadoactual":estadoactual,
    }
    listadoTrabajadores.append(perfilTrabajador)
    archivo= open (nombreArchivo,"a")
    if os.stat(nombreArchivo).st_size == 0:
        datosTrabajador=f"{nombre},{apellido},{edad},{dni},{profesion},{estadoactual}"
        archivo.write(datosTrabajador)
        archivo.close()
    else:
        datosTrabajador=f"\n{nombre},{apellido},{edad},{dni},{profesion},{estadoactual}"
        archivo.write(datosTrabajador)
        archivo.close()
    print()
    print("El trabajador se ha ingresado correctamente")
    print()
    print("Presione una tecla para continuar")

    msvcrt.getch()
    os.system("cls")
    return listadoTrabajadores

def modificarTrabajador(nombreArchivo):
    noEncontrado=True
    file= obtenerTrabajadores(nombreArchivo) #Esta variable tiene el listado de trabajadores osea [{},{},{}]
    
    if file == 0 :
        return 0
    
    dniTrabajador=str(validarOpcion("ingrese el dni del trabajador: "))

    for linea in file: # recorrer la lista de diccionarios para buscar el dni
                    
        if dniTrabajador == linea['dni']:# comparar con el dni ingresado por el usuario
            print(f"El dni {dniTrabajador} se ha encontrado !!\n")
            decorarEncontrado(linea)
            encontrado=linea
            noEncontrado=False
            print()
            #print(encontrado)#esta variable contiene un diccionario con los datos del trabajador {nombre: pepe, apellido:.....}
         
    if noEncontrado:   #controlando la salida, si el trabajador no existe 
        print(f"El dni {dniTrabajador} no existe o se ingresado incorrectamente")
        return 0    
    while True:
        datoModificar=validarOpcion('''Que dato desea modificar?: 
        [1] para modificar "nombre" 
        [2] para modificar "apellido"
        [3] para modificar "edad"
        [4] para modificar "dni"
        [5] para modificar "profesion"
        [6] para modificar "estadoactual" 
        [0] para cancelar 
        Elija una opcion:  ''')
        if datoModificar == 1:
            print(f"desea modificar el nombre del trabajador {encontrado['nombre']} ?")
            #ACA PODRIA PONER UN INPUT PARA QUE ME INGRESE SI O NO, PERO TENGO SUEÑO...
            encontrado['nombre']=validarCadena("Ingrese el nuevo nombre: ")
            print(f"El trabajador ahora se llama {encontrado['nombre']}")
            #print(file) #aca estaria el listado de diccionario ya modificado
            break
        elif datoModificar == 2:
            print(f"desea modificar el apellido del trabajador {encontrado['apellido']} ?")
            encontrado['apellido']=validarCadena("Ingrese el nuevo apellido: ")
            print(f"El trabajador ahora se llama {encontrado['apellido']}") # deberia usar una funcion ????
            break
        elif datoModificar == 3:
            print(f"desea modificar la edad del trabajador {encontrado['nombre']} ?")
            encontrado['edad']=validarOpcion("Ingrese la nueva edad: ")
            print(f"El trabajador ahora tiene {encontrado['edad']} anios")
            break
        elif datoModificar == 4:
            print(f"desea modificar el dni del trabajador {encontrado['nombre']} ?")
            encontrado['dni']=validarOpcion("Ingrese el nuevo dni: ")
            print(f"El documento de identidad del trabajador ahora es {encontrado['dni']} ")
            break
        elif datoModificar == 5:
            print(f"desea modificar la profesion del trabajador {encontrado['nombre']} ?")
            encontrado['profesion']=validarOpcion("Ingrese la nueva profesion: ")
            print(f"El trabajador ahora tiene {encontrado['profesion']} ")
            break
        elif datoModificar == 6:
            print(f"desea modificar la profesion del trabajador {encontrado['nombre']} ?")
            encontrado['estadoactual']=validarCaracter("Situacion Laboral? presione |S| para empleado |N| para desempleado ")
            if encontrado['estadoactual'] == "S":
                encontrado['estadoactual'] = "Trabajando"
                break
            else:
                encontrado['estadoactual'] ="Sin trabajo"
                print(f"El estado actual del trabajador ahora es: {encontrado['estadoactual']} ")
                break
        elif datoModificar == 0:
            print("Cancelando operacion.... ")
            sleep(1)
            os.system("cls")
            return 0
        else:
            print("Ha ingresado una opcion incorrecta")
            sleep(1)
            os.system("cls")    
    
    nuevoListadoTrabajador=[] #crear una nueva lista para almacenar el trabajador con datos modificados  
    
    for lineaModificada in file: #recorrer para agregar todas las lineas nuevamente.
        trabajadorModificado=f"\n{lineaModificada['nombre']},{lineaModificada['apellido']},{lineaModificada['edad']},{lineaModificada['dni']},{lineaModificada['profesion']},{lineaModificada['estadoactual']}"
        nuevoListadoTrabajador.append(trabajadorModificado)
    nuevoListadoTrabajador[0]=nuevoListadoTrabajador[0].replace("\n","")#reemplazar el primer salto de linea
    f= open(nombreArchivo,"w") # abrir el archivo "Trabajadores.dat" modo write 
    f.writelines(nuevoListadoTrabajador) # se sobreescribe el archivo con la nueva lista trabajador 
    f.close()

def eliminarTrabajador(nombreArchivo):
    file= obtenerTrabajadores(nombreArchivo) #Esta variable tiene el listado de trabajadores osea [{},{},{}]
    
    if file == 0 :
        return 0
    dniTrabajador=input("ingrese el dni del trabajador: ")
    indice=0
    for linea in file: # recorrer la lista de diccionarios para buscar el dni
        
        if dniTrabajador == linea['dni']:# comparar con el dni ingresado por el usuario
            print(f"El dni {dniTrabajador} se ha encontrado !!\n")
            decorarEncontrado(linea)
            encontrado=linea
            print()
            print(f"Desea eliminar el trabajador {encontrado['nombre']} ? ")
            print()
            respuestaUsuario= validarCaracter("Presione |S| para eliminar o |N| para volver al menu principal: ")
            print()
            if respuestaUsuario == 'S':
                file.pop(indice)
                #print(file)
                break       
            elif respuestaUsuario == 'N':
                break  
        indice+=1
    else:
        print(f"El dni {dniTrabajador} no existe o se ingresado incorrectamente")
        return 0
    if len(file) == 0:
        f= open(nombreArchivo,"w") # abrir el archivo "Trabajadores.dat" modo write 
        f.writelines("") # se sobreescribe el archivo con la nueva lista trabajador 
        f.close()
        return f"El archivo {nombreArchivo} se encuentra vacio"
    else:
        nuevoListadoTrabajador=[] #crear una nueva lista para actualizar la lista 
        for lineaModificada in file: #recorrer para agregar todas las lineas nuevamente.
            trabajadorModificado=f"\n{lineaModificada['nombre']},{lineaModificada['apellido']},{lineaModificada['edad']},{lineaModificada['dni']},{lineaModificada['profesion']},{lineaModificada['estadoactual']}"
            nuevoListadoTrabajador.append(trabajadorModificado)
        nuevoListadoTrabajador[0]=nuevoListadoTrabajador[0].replace("\n","")#reemplazar el primer salto de linea
        f= open(nombreArchivo,"w") # abrir el archivo "Trabajadores.dat" modo write 
        f.writelines(nuevoListadoTrabajador) # se sobreescribe el archivo con la nueva lista trabajador 
        f.close()








