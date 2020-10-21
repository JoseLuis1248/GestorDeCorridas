"""

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
    while True:
        linea = m.readline()
        if(linea == ""):
            break
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
        if c == ",":
            informacion.append(palabra)
            palabra = ""
        else:
            palabra += c
    informacion.append(palabra)
    return informacion
