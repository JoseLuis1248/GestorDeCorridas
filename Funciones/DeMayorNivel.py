"""
Éste es un paquete dedicado a contener funciones de mayor nivel, es decir, funciones que no poseen mucha
complejidad pero si usan otras funciones de menor nivel.

Éste módulo contiene las funciones:
:generarArchivoDeProyectosPorMaquina(confGeneral, confEjecucionVersEst, nroMaquina, confPreparadoVersEst): Ésta
función se encarga de crear un archivo por lotes de ejecución en serie por cada máquina elegida

:generarArchivoDePreparadoPorVersion(confGeneral, confPreparadoVersEst, listaMaquinas): Ésta función se encarga
de crear un archivo por lotes de ejecución de preparación de entorno

:cargarDatosSistema(): Ésta función se encarga de reiniciar los arreglos, matrices locales dados en función
de la parametrización de los archivos de texto
"""

from Funciones.DeMedioNivel import *

def generarArchivoDeProyectosPorMaquina(confGeneral, confEjecucionVersEst, nroMaquina, confPreparadoVersEst):
    """
    Ésta función genera y exporta un archivo por lotes de ejecucion en serie de proyectos, correspondiente a una version estable
    :param confGeneral: Arreglo de información con la configuración general
    :param confEjecucionVersEst: Matriz de dos dimensiones con la información de la configuración de la versión estable
    :param nroMaquina: Numero de maquina a preparar y de la cual exportar el archivo correspondiente
    :return: None
    """
    ### En la siguiente estructura se establece el numero de la version estable (PARÁMETRO 6)
    if(confEjecucionVersEst[0][6] == "1"):
        # Según el numero de version estable, se crea variable que establece el nombre de la version
        version = confGeneral[17]
    else:
        # Según el numero de version estable, se crea variable que establece el nombre de la version
        version = confGeneral[18]

    ### En la siguiente estructura se busca el indice de fila de la maquina elegida en el archivo de preparador por versión
    ### esto se hace para extraer la ruta donde se exportará el archivo (PARÁMETRO 6)
    indice = 0
    for i in range(len(confPreparadoVersEst)):
        if(nroMaquina == confPreparadoVersEst[i][0]):
            indice = i
            break

    ### En la siguiente estructura se crea el archivo aunque no exista; esto es por el modo de apartura "wt"
    txt = "{}\Ejecucion({})({}).bat".format(confPreparadoVersEst[indice][6], nroMaquina, version)
    m = open(txt, "wt")
    m.close()

    ### En las siguientes lineas se crea el archivo, el encabezado primero, cuerpo y pie despues
    encabezadoArchivoDeEjecucion(confGeneral, txt)
    cuerpoArchivoEjecucion(confGeneral, confEjecucionVersEst, txt, nroMaquina)
    pieArchivoEjecucion(confGeneral, confEjecucionVersEst, txt, nroMaquina)


def generarArchivoDePreparadoPorVersion(confGeneral, confPreparadoVersEst, listaMaquinas):
    """
    Ésta función genera y exporta un archivo por lotes de preparacion de entorno, correspondiente a una version estable
    :param confGeneral: Arreglo de información con la configuración general
    :param confPreparadoVersEst: Matriz de dos dimensiones con la información de la configuración de la versión estable
    :param listaMaquinas: Lista de maquinas a preparar (nombradas como strings; por ejemplo: "31")
    :return: None
    """
    ### En la siguiente estructura se establece que version estable es la que se prepara, para conocer su nombre
    if(confPreparadoVersEst[0][5] == "1"):
        # Según el numero de version estable, se crea variable que establece el nombre de la version
        version = confGeneral[17]
    elif(confPreparadoVersEst[0][5] == "2"):
        # Según el numero de version estable, se crea variable que establece el nombre de la version
        version = confGeneral[18]

    ### En la siguiente estructura se crea el archivo aunque no exista; esto es por el modo de apartura "wt"
    txt = "{}\Preparacion({}).bat".format(confGeneral[19], version)
    m = open(txt, "wt")
    m.close()

    ### En las siguientes lineas se crea el archivo, el encabezado primero, cuerpo y pie despues
    encabezadoArchivoPreparado(txt)
    n = len(listaMaquinas)
    ### En la siguiente estructura, se agrega al cuerpo del archivo cuantas maquinas se hayan elegido para preparar
    for i in range(n):
        cuerpoArchivoPreparado(confGeneral, confPreparadoVersEst, txt, listaMaquinas[i])
    pieArchivoPreparado(txt)


def cargarDatosSistema():
    confGeneral = obtenerLineasDeArchivo("Configuraciones/confGeneral.txt")
    truncarElementosArreglo(confGeneral)
    confEjecucionVersEst1 = obtenerLineasDeArchivo("Configuraciones/confEjecucionVersEst1.txt")
    convertirAMatriz(confEjecucionVersEst1)
    confEjecucionVersEst2 = obtenerLineasDeArchivo("Configuraciones/confEjecucionVersEst2.txt")
    convertirAMatriz(confEjecucionVersEst2)
    confPreparadoVersEst1 = obtenerLineasDeArchivo("Configuraciones/confPreparadoVersEst1.txt")
    convertirAMatriz(confPreparadoVersEst1)
    confPreparadoVersEst2 = obtenerLineasDeArchivo("Configuraciones/confPreparadoVersEst2.txt")
    convertirAMatriz(confPreparadoVersEst2)

    return[confGeneral, confEjecucionVersEst1, confEjecucionVersEst2, confPreparadoVersEst1, confPreparadoVersEst2]
