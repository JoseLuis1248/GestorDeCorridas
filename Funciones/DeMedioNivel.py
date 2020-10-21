"""

"""

from Funciones.DeMenorNivel import *

def truncarElementosArreglo(confGeneral):
    """
    Ésta funcion transforma un arreglo: cada cadena de caracteres que conforma el arreglo
    se formatea para poseer solo el contenido luego del signo "="
    :param confGeneral: El arreglo con los elementos a truncar
    :return: Un arreglo de elementos (cadenas de texto) truncados
    """
    n = len(confGeneral)
    for i in range(n):
        elemento = formatearCadena(confGeneral[i])
        confGeneral[i] = elemento

def convertirAMatriz(confVersEst1):
    """
    Ésta función transforma un arreglo de cadenas de caracteres: cada cadena
    que posee informacion separada por coma se tranforma en un arreglo, de
    manera que se corvierte en una matriz de n x m elementos
    :param confVersEst1: El arreglo de cadenas de caracteres separados por comas
    :return: Una matriz de dos dimensiones
    """
    n = len(confVersEst1)
    for i in range(n):
        informacion = obtenerInfoSeparadaPorComa(confVersEst1[i])
        confVersEst1[i] = informacion

def encabezadoArchivoDeEjecucion(confGeneral, txt):
    """
    Ésta función escribe el encabezado de un archivo por lotes de ejecución automática
    común; refiriendo comun al hecho de que sirve para cualquier version estable
    :param confGeneral: El arreglo que posee la informacion de la configuracion general
    :param txt: El nombre (incluyendo direccion) del archivo donde se va a escribir la informacion
    :return: None
    """
    if(confGeneral[0] == "1"):
        p = 'echo SE MINIMIZARA LA VENTANA DE EJECUCION DEL ARCHIVO POR LOTES\n' + \
            'if "%1"=="done" goto runtime\n' + \
            'start "" /min %0 done\n' + \
            'exit\n' + \
            ':runtime\n' + \
            '\n'
    else:
        p = ""

    r = '@echo off\n' + \
        '\n' + \
        '{}'.format(p) + \
        'echo --------------------------------------------------------\n' + \
        'title ARCHIVO POR LOTES DE EJECUCION DE PROYECTO\n' + \
        'echo EJECUCION AUTOMATICA DE PROYECTO DE TEST COMPLETE\n' + \
        'echo --------------------------------------------------------\n' + \
        '\n'
    if(confGeneral[1] != ""):
        procesos = obtenerInfoSeparadaPorComa(confGeneral[1])
        for i in range(len(procesos)):
            p = 'echo CERRANDO PROCESO: {}\n'.format(procesos[i].upper()) + \
                'TASKKILL /IM "{}" /F /T\n'.format(procesos[i])
            r += p
        r += '\n'
    p = 'echo LA CONEXION REMOTA SE CERRARA...\n' + \
        'timeout {}\n'.format(confGeneral[3]) + \
        'for /f "skip=1 tokens=3" %%s in ("query user servertesting")' + \
        ' do (%windir%\System32' + '\\' + 't' + 'scon.exe %%s /dest:console)\n' + \
        'for /f "skip=1 tokens=3" %%s in ("query user testcomplete")' + \
        ' do (%windir%\System32' + '\\' + 't' + 'scon.exe %%s /dest:console)\n' + \
        '\n'
    r += p

    m = open(txt, "at")
    m.write(r)
    m.close()

def cuerpoArchivoEjecucion(confGeneral, confVersEst, txt, nroMaquina):
    """
    Ésta función escribe el cuerpo de un archivo por lotes general de uso comun, es decir
    usable para cualquier version estable
    :param confGeneral: Arreglo con la informacion de la configuracion general
    :param confVersEst: Matriz de informacion de la configuracion de proyectos de la version estable
    :param txt: Nombre del archivo (incluyendo direccion) donde se va a gravar la informacion
    :param nroMaquina: Numero de la maquina que se va a preparar y exportar archivo correspondiente
    :return: None
    """
    m = open(txt, "at")
    n = len(confVersEst)
    for i in range(n):
        if(confVersEst[i][3] == "1" and confVersEst[i][2] == nroMaquina):
            if(confVersEst[i][6] == "1"):
                if(confGeneral[7] == nroMaquina):
                    p = confGeneral[10]
                else:
                    p = confGeneral[8]
            elif(confVersEst[i][6] == "2"):
                if(confGeneral[7] == nroMaquina):
                    p = confGeneral[11]
                else:
                    p = confGeneral[9]
            r = 'echo INICIO DE PROYECTO {}'.format(confVersEst[i][1].upper()) + '\n' + \
                '"{}" "{}" /r '.format(confGeneral[4], confVersEst[i][5]) + \
                '/p:{} /e /SilentMode /Timeout:{}'.format(confVersEst[i][1], confVersEst[i][4]) + \
                ' /ExportLog:"{}{}'.format(p, confVersEst[i][0].upper()) + \
                '-{}({}).mht"\n'.format(confVersEst[i][1].upper(), confVersEst[i][2]) + \
                '\n' + \
                'echo TIEMPO DE ESPERA ENTRE CORRIDA\n' + \
                'timeout {}\n'.format(confGeneral[6])
            procesos = obtenerInfoSeparadaPorComa(confGeneral[5])
            for i in range(len(procesos)):
                p = 'echo CERRANDO PROCESO: {}\n'.format(procesos[i].upper()) + \
                    'TASKKILL /IM "{}" /F /T\n'.format(procesos[i])
                r += p
            r += 'echo DESCOMPRIMIENDO BASE DE DATOS COMUN\n' + \
                '"C:\Program Files\WinRAR\WinRAR.exe" x -o+ ' + \
                '"D:\RECURSOS_TC\BASESDEDATOS_TC\Inicial.rar" ' + \
                '"D:\RECURSOS_TC\BASESDEDATOS_TC"\n' + \
                '\n'
            m.write(r)
    m.close()

def encabezadoArchivoPreparado(txt):
    r = '@echo off\n' + \
        'echo --------------------------------------------------------\n' + \
        'title ARCHIVO POR LOTES DE PREPARADO DE ENTORNO\n' + \
        'echo EJECUCION AUTOMATICA DE PREPARACION DE ENTORNO EN MAQUINAS\n' + \
        'echo --------------------------------------------------------\n' + \
        '\n'
    m = open(txt, "at")
    m.write(r)
    m.close()

def cuerpoArchivoPreparado(confGeneral, confPreparadoVersEst, txt):
    m = open(txt, "at")
    n = len(confPreparadoVersEst)
    for i in range(n):
        if(confPreparadoVersEst[i][1] == "1" or confPreparadoVersEst[i][2] == "1"):
            if(confPreparadoVersEst[i][5] == "1"):
                bases = confGeneral[13]
                ejec = confGeneral[14]
            elif(confPreparadoVersEst[i][5] == "2"):
                bases = confGeneral[15]
                ejec = confGeneral[16]
            r = 'echo --------------------------------------------------------\n' + \
                'echo SE PREPARARA EL ENTORNO EN MAQUINA DE IP TERMINACION {}\n'.format(confPreparadoVersEst[i][0]) + \
                '\n'
            if(confPreparadoVersEst[i][1] == "1"):
                b = 'echo SE COPIARAN LAS BASES DE DATOS\n' + \
                    'timeout 2 /nobreak\n' + \
                    'XCOPY "{}*" "{}" /f /q /y\n'.format(bases, confPreparadoVersEst[i][3]) + \
                    '\n'
                r += b
            if(confPreparadoVersEst[i][2] == "1"):
                e = 'echo SE COPIARA EJECUTABLE DE TESTEO\n' + \
                    'timeout 2 /nobreak\n' + \
                    'XCOPY "{}*" "{}" /f /q /y\n'.format(ejec, confPreparadoVersEst[i][4]) + \
                    'echo --------------------------------------------------------\n' + \
                    '\n'
            else:
                e = 'echo --------------------------------------------------------\n' + \
                    '\n'
            r += e
            m.write(r)
    m.close()
