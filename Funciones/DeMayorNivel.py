"""

"""

from Funciones.DeMedioNivel import *

def generarArchivoDeProyectosPorMaquina(confGeneral, confEjecucionVersEst, nroMaquina, confPreparadoVersEst):
    """
    Ésta función genera y exporta un archivo por lotes de ejecucion de proyectos, correspondiente a una version estable
    :param confGeneral: Arreglo de información con la configuración general
    :param confEjecucionVersEst: Matriz de dos dimensiones con la información de la configuración de la versión estable
    :param nroMaquina: Numero de maquina a preparar y de la cual exportar el archivo correspondiente
    :return: None
    """
    if(confEjecucionVersEst[0][6] == "1"):
        version = confGeneral[17]
    else:
        version = confGeneral[18]
    indice = 0
    for i in range(len(confPreparadoVersEst)):
        if(nroMaquina == confPreparadoVersEst[i][0]):
            indice = i
            break
    txt = "{}\Ejecucion({})({}).bat".format(confPreparadoVersEst[indice][6], nroMaquina, version)
    m = open(txt, "wt")
    m.close()
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
    if(confPreparadoVersEst[0][5] == "1"):
        version = confGeneral[17]
    elif(confPreparadoVersEst[0][5] == "2"):
        version = confGeneral[18]
    txt = "{}\Preparacion({}).bat".format(confGeneral[19], version)
    m = open(txt, "wt")
    m.close()
    encabezadoArchivoPreparado(txt)
    n = len(listaMaquinas)
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
