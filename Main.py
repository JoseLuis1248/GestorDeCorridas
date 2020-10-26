"""
MODULO EJECUTABLE: Este módulo contiene la definición de 'main', función que ejecuta el programa principal

Lista de funciones incluidos:
"""

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

    listaMaquinas = obtenerInfoSeparadaPorComa(confGeneral[12])

    ### Variables generales
    opcion = -1
    menu =  "\nMenu de opciones" + \
            "\n1. Preparar entorno para: VERSION ESTABLE 1 ({}) - MAQUINAS INGRESADAS MANUALMENTE".format(confGeneral[17]) + \
            "\n2. Preparar entorno para: VERSION ESTABLE 2 ({}) - MAQUINAS INGRESADAS MANUALMENTE".format(confGeneral[18]) + \
            "\n3. Generar archivos por lotes: VERSION ESTABLE 1 ({}) - MAQUINAS INGRESADAS MANUALMENTE".format(confGeneral[17]) + \
            "\n4. Generar archivos por lotes: VERSION ESTABLE 2 ({}) - MAQUINAS INGRESADAS MANUALMENTE".format(confGeneral[18]) + \
            "\n5. Reiniciar configuraciones por cambio de archivos" + \
            "\n0. Finalizar programa"

    ### Inicio de programa - Menu de opciones
    while opcion != 0:
        print(menu)
        opcion = validarCodigo(0, 5, "Ingrese una opcion de menu: ")

        if(opcion == 0):
            input("Programa finalizado...")
        elif(opcion == 1):
            listaDeMaquinas = input("Ingrese la lista de maquinas a preparar (separadas por coma, si espacios): ")
            listaFormateada = obtenerInfoSeparadaPorComa(listaDeMaquinas)
            generarArchivoDePreparadoPorVersion(confGeneral, confPreparadoVersEst1, listaFormateada)
        elif(opcion == 2):
            listaDeMaquinas = input("Ingrese la lista de maquinas a preparar (separadas por coma, si espacios): ")
            listaFormateada = obtenerInfoSeparadaPorComa(listaDeMaquinas)
            generarArchivoDePreparadoPorVersion(confGeneral, confPreparadoVersEst2, listaFormateada)
        elif(opcion == 3):
            listaDeMaquinas = input("Ingrese la lista de maquinas a configurar ejecucion en serie (separadas por coma, si espacios): ")
            listaFormateada = obtenerInfoSeparadaPorComa(listaDeMaquinas)
            for i in range(len(listaFormateada)):
                generarArchivoDeProyectosPorMaquina(confGeneral, confEjecucionVersEst1, listaFormateada[i], confPreparadoVersEst1)
        elif(opcion == 4):
            listaDeMaquinas = input("Ingrese la lista de maquinas a configurar ejecucion en serie (separadas por coma, si espacios): ")
            listaFormateada = obtenerInfoSeparadaPorComa(listaDeMaquinas)
            for i in range(len(listaFormateada)):
                generarArchivoDeProyectosPorMaquina(confGeneral, confEjecucionVersEst2, listaFormateada[i], confPreparadoVersEst2)
        elif(opcion == 5):
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
            print("Proceso finalizado correctamente.")

if __name__ == '__main__':
    main()
