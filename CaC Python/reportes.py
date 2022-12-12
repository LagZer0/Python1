from controlErrores import validarOpcion
from crudTrabajador import obtenerTrabajadores


def mostrarDesocupadosPorEdad(nombreArchivo): 
    file= obtenerTrabajadores(nombreArchivo) #Esta variable tiene el listado de trabajadores osea [{},{},{}]
   
    if file == 0 :
        return 0
    nuevoListado = [] #Aqui van añadiendose los trabajadores a mostrar 
    print('Ingrese rango de edad de trabajadores desocupados a buscar')
    edadC = (validarOpcion('Desde :  '))
    edadF = (validarOpcion('Hasta :  '))
    contaEncontrados=0 #variable para saber cuantos hay y controlar la salida 

    for trabajador in file: 
        if int(trabajador['edad']) >= edadC and int(trabajador['edad']) < edadF and trabajador['estadoactual'] == 'Sin trabajo': # podria usar pertenencia con range(edadc,edadf+1)???
            contaEncontrados +=1
            nuevoListado.append(trabajador)
    if contaEncontrados == 0:
        return 0
    else:
        print(f"Se han encontrado {contaEncontrados} trabajadores\n")
        return nuevoListado
    
        
def mostrarSegunDato(nombreArchivo,datoBuscado):
    file= obtenerTrabajadores(nombreArchivo) #Esta variable tiene el listado de trabajadores osea [{},{},{}]
    
    if file == 0 :
        return 0
    nuevoListado = []
    contaEncontrado=0
    for trabajador in file:
        if trabajador['profesion'] == datoBuscado:
            contaEncontrado+=1
            nuevoListado.append(trabajador)
    if contaEncontrado == 0:
        return 0
    else:
        return nuevoListado



def mostrarEstadoTrabajador(nombreArchivo,datoBuscado):
    file= obtenerTrabajadores(nombreArchivo) #Esta variable tiene el listado de trabajadores osea [{},{},{}]
    
    if file == 0 :
        return 0
    nuevoListado = []
    contaEncontrado=0
    for trabajador in file:
        if trabajador['estadoactual'] == datoBuscado:
            contaEncontrado+=1
            nuevoListado.append(trabajador)
    if contaEncontrado == 0:
        return 0
    else:
        return nuevoListado