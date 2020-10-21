"""
MODULO EJECUTABLE: Este módulo contiene la definición de 'main', función que ejecuta el programa principal

Lista de funciones incluidos:
"""
__author__ = 'Grupo:77371,89208,89201'

from Funciones.DeMayorNivel import *

def main():
    """
    Ésta es la función principal de ejecución del programa
    :return: None
    """
    ### Carga en memoria de de los archivos de texto de configuraciones
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

    ### Variables generales
    opcion = -1
    menu =  "\nMenu de opciones" + \
            "\n1. Preparar entorno para: VERSION ESTABLE 1 - TODAS LAS MAQUINAS" + \
            "\n2. Preparar entorno para: VERSION ESTABLE 2 - TODAS LAS MAQUINAS" + \
            "\n3. Generar archivos por lotes: VERSION ESTABLE 1 - TODAS LAS MAQUINAS" + \
            "\n4. Generar archivos por lotes: VERSION ESTABLE 2 - TODAS LAS MAQUINAS" + \
            "\n0. Finalizar programa"

    ### Inicio de programa - Menu de opciones
    while opcion != 0:
        print(menu)
        opcion = validarCodigo(0, 4, "Ingrese una opcion de menu: ")

        if(opcion == 0):
            input("Programa finalizado...")
        elif(opcion == 1):
            generarArchivoDePreparadoPorVersion(confGeneral, confPreparadoVersEst1, "1")
        elif(opcion == 2):
            generarArchivoDePreparadoPorVersion(confGeneral, confPreparadoVersEst2, "2")
        elif(opcion == 3):
            versiones = obtenerInfoSeparadaPorComa(confGeneral[12])
            for i in range(len(versiones)):
                generarArchivoDeProyectosPorMaquina(confGeneral, confEjecucionVersEst1, versiones[i])
        elif(opcion == 4):
            versiones = obtenerInfoSeparadaPorComa(confGeneral[12])
            for i in range(len(versiones)):
                generarArchivoDeProyectosPorMaquina(confGeneral, confEjecucionVersEst2, versiones[i])

if __name__ == '__main__':
    main()
