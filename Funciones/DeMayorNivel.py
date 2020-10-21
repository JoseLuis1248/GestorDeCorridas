"""

"""

from Funciones.DeMedioNivel import *

def generarArchivoDeProyectosPorMaquina(confGeneral, confEjecucionVersEst, nroMaquina):
    """
    Ésta función genera y exporta un archivo por lotes correspondiente a una version estable
    :param confGeneral: Arreglo de información con la configuración general
    :param confEjecucionVersEst: Matriz de dos dimensiones con la información de la configuración de la versión estable
    :param nroMaquina: Numero de maquina a preparar y de la cual exportar el archivo correspondiente
    :return: None
    """
    txt = "Exportacion/EjecucionEnSerie({})({}).txt".format(nroMaquina, confEjecucionVersEst[0][6])
    m = open(txt, "wt")
    m.close()
    encabezadoArchivoDeEjecucion(confGeneral, txt)
    cuerpoArchivoEjecucion(confGeneral, confEjecucionVersEst, txt, nroMaquina)

def generarArchivoDePreparadoPorVersion(confGeneral, confPreparadoVersEst, version):
    txt = "Exportacion/Preparacion({}).txt".format(version)
    m = open(txt, "wt")
    m.close()
    encabezadoArchivoPreparado(txt)
    cuerpoArchivoPreparado(confGeneral, confPreparadoVersEst, txt)
