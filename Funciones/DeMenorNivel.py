"""
Éste paquete posee una serie de funciones básicas que si bien poseen cierta complejidad; no usan otras
funciones de menor nivel, ya que este es el menor.

Lista de funciones:
:validarCodigo(min, max, mensaje): Ésta función se encarga de validar un dato ingresado por el usuario

:formatearCadena(cadenaCompleta): Ésta función formatea una cadena de texto a partir del signo "="

:obtenerLineasDeArchivo(nombreArchivo): Ésta función trunca lineas de texto: elimina los caracteres de
salto de linea de un archivo de texto identificados como "\n"

:obtenerInfoSeparadaPorComa(cadena): Ésta función tranforma una linea de texto con parametros separados
por coma en un arreglo
"""

def validarCodigo(min, max, mensaje):
    """
    Ésta funcion valida el ingreso de un numero por pantalla
    :param min: Minimo aceptable para el ingreso del numero
    :param max: Maximo aceptable para el ingreso del numero
    :param mensaje: Mensaje entregado al usuario para ingresar el numero
    :return: El valor ingresado por el usuario, validodo entre los margenes
    """
    codigo = int(input(mensaje))
    while(codigo < min or codigo > max):
        codigo = int(input("Codigo ingresado incorrecto, debe ser >= " + str(min) + " y <= " + str(max) + ": "))
    return codigo

def formatearCadena(cadenaCompleta):
    """
    Ésta función retorna una cadena de texto truncada: a partir del signo "="
    es decir, retorna solo lo que esta por delante del signo "="
    :param cadenaCompleta: La cadena de texto a truncar
    :return: Una cadena de texto
    """
    n = len(cadenaCompleta)
    cadena = ""
    comienzaGravar = False
    for i in range(n):
        if(comienzaGravar):
            cadena += cadenaCompleta[i]
        if(cadenaCompleta[i] == "="):
            comienzaGravar = True
    return cadena

def obtenerLineasDeArchivo(nombreArchivo):
    """
    Ésta función retorna un arreglo de cadenas de caracteres, en donde cada elemento
    posee la informacion de cada cadena sin el salto de linea "\n" al final
    :param nombreArchivo: El archivo de texto del cual se quiere obtener la info
    :return: Un arreglo de cadenas de caracteres
    """
    configuracion = []
    m = open(nombreArchivo, "rt")
    ### Si bien el proximo ciclo parece tener condicion de ejecucion infinita, no es asi; existe una
    ### condicion de corte con una sentencia "break"
    while True:
        ### Lee una linea/fila completa del archivo de texto
        linea = m.readline()

        ### Si no existe mas dato, se corta el ciclo principal
        if(linea == ""):
            break

        ### Si el ultimo elemento de la linea de texto es "\n", se elimina
        if(linea[-1] == "\n"):
            linea = linea[:-1]

        configuracion.append(linea)
    m.close()
    return configuracion

def obtenerInfoSeparadaPorComa(cadena):
    """
    Ésta función retorna un arreglo de cadenas de caracteres con la informacion
    que estaba en la cadena (informacion separada por comas)
    :param cadena: La cadena con palabras separadas por comas
    :return: Un arreglo de cadenas de caracteres
    """
    informacion = []
    palabra = ""
    for c in cadena:
        ### Si es "," se terminó la palabra, se agrega entonces la misma al arreglo y se reinicia
        if c == ",":
            informacion.append(palabra)
            palabra = ""
        ### Si el caracter no es "," se está dentro de una palabra, asi que se agrega el caracter
        else:
            palabra += c
    informacion.append(palabra)
    return informacion
