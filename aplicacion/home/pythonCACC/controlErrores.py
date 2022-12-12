"""Este modulo contiene funciones que controlan los errores que ingresa el usuario"""

def validarOpcion(leyenda):
  while True:
    try:
      numero=int(input(leyenda))
      break
    except ValueError:
      print("Solo se debe ingresar numeros enteros !! ")
  return numero


def validarCaracter(pregunta):
  
  while True:
    try:
      caracter=(input(pregunta))
      caracter=caracter.upper()
      if caracter in ("S","N"):
        break
    except:
      print("Error: Debe presionar las teclas |S| o |N|")

  return caracter


def validarCadena(leyenda):

  while True:
    
      nombre=(input(leyenda))
      if nombre.isalpha():
        break
      else:  
        print("Solo se permiten nombres reales")
      
  return nombre

  