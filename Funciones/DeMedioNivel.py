"""
Éste es un paquete dedicado a contener funciones de medio nivel, es decir, funciones que poseen cierta
complejidad y usan otras funciones de menor nivel.

Éste módulo posee las funciones:
:truncarElementosArreglo(confGeneral): Ésta función se encarga de truncar elementos; devuelve un arreglo
de elementos de configuración listos para usarse.

:convertirAMatriz(confVersEst1): Ésta función convierte y retorna una matriz de elementos a partir de
un arreglo que posee elementos en donde la información esta separada por coma

:encabezadoArchivoDeEjecucion(confGeneral, txt): Ésta función se encarga de escribir el encabezado de un
archivo por lotes de ejecución en serie para una máquina nada

:cuerpoArchivoEjecucion(confGeneral, confVersEst, txt, nroMaquina): Ésta función se encarga de escribir el
cuerpo de un archivo por lotes de ejecución en serie.

:pieArchivoEjecucion(confGeneral, confEjecucionVersEst, txt, nroMaquina): Ésta función se encarga de escribir
el pie de un archivo por lotes de ejecución en serie

:encabezadoArchivoPreparado(txt): Ésta función se encarga de escribir el encabezado de archivo por lotes
de preparacion de entorno

:cuerpoArchivoPreparado(confGeneral, confPreparadoVersEst, txt, nroMaquina): Ésta función se encarga de escribir
el cuerpo del archivo por lotes de preparado de entorno

:pieArchivoPreparado(txt): Se escribe el pie de archivo por lotes de preparado de entorno
"""

from Funciones.DeMenorNivel import *
from datetime import datetime

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
    ### En la siguiente estructura se decide, según la configuración (PARAMETRO 0) si se incluye o no el bloque
    ### de código correspondiente al minimizado de ventana
    if(confGeneral[0] == "1"):
        p = 'echo SE MINIMIZARA LA VENTANA DE EJECUCION DEL ARCHIVO POR LOTES\n' + \
            'if "%1"=="done" goto runtime\n' + \
            'start "" /min %0 done\n' + \
            'exit\n' + \
            ':runtime\n' + \
            '\n'
    else:
        p = ""

    ### En la siguiente estructura se forma el archivo encabezado
    r = '@echo off\n' + \
        '\n' + \
        '{}'.format(p) + \
        'echo --------------------------------------------------------\n' + \
        'title ARCHIVO POR LOTES DE EJECUCION DE PROYECTO\n' + \
        'echo EJECUCION AUTOMATICA DE PROYECTO DE TEST COMPLETE\n' + \
        'echo --------------------------------------------------------\n' + \
        '\n'

    ### En la siguiente estructura se decide si se va a agregar el bloque de codigo correspondiente al cierre
    ### de procesos (PARAMETRO 1)
    if(confGeneral[1] != ""):
        procesos = obtenerInfoSeparadaPorComa(confGeneral[1])
        for i in range(len(procesos)):
            p = 'echo CERRANDO PROCESO: {}\n'.format(procesos[i].upper()) + \
                'TASKKILL /IM "{}" /F /T\n'.format(procesos[i])
            r += p
        r += '\n'

    ### En la siguiente estructura se agrega el bloque de codigo correspondiente al cierre de sesión. Se
    ### agregan 2 cadenas de cierre, una por el usuario "servertesting" y otra por el usuario "testcomplete"
    p = 'echo LA CONEXION REMOTA SE CERRARA...\n' + \
        'timeout {}\n'.format(confGeneral[3]) + \
        'for /f "skip=1 tokens=3" %%s in ' + "('query user servertesting')" + \
        ' do (%windir%\System32' + '\\' + 't' + 'scon.exe %%s /dest:console)\n' + \
        'for /f "skip=1 tokens=3" %%s in ' + "('query user testcomplete')" + \
        ' do (%windir%\System32' + '\\' + 't' + 'scon.exe %%s /dest:console)\n' + \
        '\n'
    r += p

    ### En el siguiente bloque se abre el archivo en modo escritura al final (at), se escribe en el mismo
    ### y se cierra
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
    ### En el siguiente ciclo se agrega de a uno por vez, cada bloque correspondiente a la ejecución de un proyecto
    ### y su tiempo de espera subsiguiente
    n = len(confVersEst)
    m = open(txt, "at")
    for i in range(n):
        ### Se corrobora que el proyecto esta habilitado (PARAMETRO 3) la version estable es la elegida y
        ### se corresponde el numero de maquina elegida
        if(confVersEst[i][3] == "1" and confVersEst[i][2] == nroMaquina):

            ### En el siguiente bloque se corrobora que version estable es (PARAMETRO 6); para buscar la ruta
            ### de exportacion en el archivo de configuracion general
            if(confVersEst[i][6] == "1"):
                ### En el siguiente bloque se compara: si el nombre de maquina resulta ser la maquina de exportacion
                ### especial (PARAMETRO 7), entonces se añadira al parametro "p" esta ruta
                if(confGeneral[7] == nroMaquina):
                    p = confGeneral[10]
                else:
                    p = confGeneral[8]
            elif(confVersEst[i][6] == "2"):
                ### En el siguiente bloque se compara: si el nombre de maquina resulta ser la maquina de exportacion
                ### especial (PARAMETRO 7), entonces se añadira al parametro "p" esta ruta
                if(confGeneral[7] == nroMaquina):
                    p = confGeneral[11]
                else:
                    p = confGeneral[9]

            ### En el siguiente bloque se crea parte del cuerpo de ejecucion de un proyecto
            r = 'echo INICIO DE PROYECTO {}'.format(confVersEst[i][1].upper()) + '\n' + \
                '"{}" "{}" /r '.format(confGeneral[4], confVersEst[i][5]) + \
                '/p:{} /e /SilentMode /Timeout:{}'.format(confVersEst[i][1], confVersEst[i][4]) + \
                ' /ExportLog:"{}{}'.format(p, confVersEst[i][0].upper()) + \
                '-{}({}).mht"\n'.format(confVersEst[i][1], confVersEst[i][2]) + \
                '\n' + \
                'echo TIEMPO DE ESPERA ENTRE CORRIDA\n' + \
                'timeout {}\n'.format(confGeneral[6])

            ### En el siguiente bloque se decide si se agrega o no (luego del bloque de ejecucion de proyecto)
            ### el cierre de procesos posterior (PARAMETRO 7)
            if(confVersEst[i][7] == "1"):
                ### En el siguiente ciclo se obtiene la serie de procesos de cierre entre proyectos (PARAMETRO 5)
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

def pieArchivoEjecucion(confGeneral, confEjecucionVersEst, txt, nroMaquina):
    """
    Ésta función escribe el pie de un archivo por lotes de ejecución en serie
    :param confGeneral: Arreglo con la información de la configuración general
    :param confEjecucionVersEst: Matriz de n x m con la información de la configuración por proyecto
    :param txt: Archivo txt donde se escribirá el texto
    :param nroMaquina: El numero de la maquina elegida
    :return:
    """
    ### En la siguiente estructura se establece de que version estable se trata (PARAMETRO 6) en funcion
    ### de ello se elige la ruta de exportacion de archivo aviso segun configuracion general (PARAMETRO 20,21)
    if(confEjecucionVersEst[0][6] == "1"):
        p = confGeneral[20]
    elif(confEjecucionVersEst[0][6] == "2"):
        p = confGeneral[21]

    ### En el siguiente bloque se abre el archivo en modo escritura al final (at), se escribe el pie en el
    ### archivo por lotes y se cierra el mismo
    r = 'echo SE EXPORTA ARCHIVO DE TERMINACION DE CORRIDAS\n' + \
        'Net View > "{}MAQUINA IP {} - EJECUCION FINALIZADA"\n'.format(p, nroMaquina) + \
        '\nEXIT\n'
    m = open(txt, "at")
    m.write(r)
    m.close()

def encabezadoArchivoPreparado(txt):
    """
    Ésta función escribe el encabezado de un archivo por lotes de preparado de entorno
    :param txt: El archivo donde se escribirá
    :return:
    """
    ### En el siguiente bloque se abre el archivo en modo escritura al final (at), se escribe y se cierra
    r = '@echo off\n' + \
        'echo --------------------------------------------------------\n' + \
        'title ARCHIVO POR LOTES DE PREPARADO DE ENTORNO\n' + \
        'echo EJECUCION AUTOMATICA DE PREPARACION DE ENTORNO EN MAQUINAS\n' + \
        'echo --------------------------------------------------------\n' + \
        '\n'
    m = open(txt, "at")
    m.write(r)
    m.close()

def cuerpoArchivoPreparado(confGeneral, confPreparadoVersEst, txt, nroMaquina):
    """
    Ésta función escribe el cuerpo de un archivo por lotes de prerarado de entorno en funcion de las maquinas elegidas
    :param confGeneral: Arreglo con la configuracion general
    :param confPreparadoVersEst: Matriz de n x m con la configuracion de cada maquina en particular
    :param txt: Archivo donde se escribirá
    :param nroMaquina: EL numero de maquina elegida
    :return:
    """
    ### En el siguiente bloque se abre el archivo txt en modo de escritura al final (at)
    m = open(txt, "at")
    n = len(confPreparadoVersEst)

    ### En el siguiente bloque de codigo se busca el indice i; es decir, se busca cual es la fila que coincide
    ### con el nro de maquina que se eligio
    for i in range(n):
        if(confPreparadoVersEst[i][0] == nroMaquina):
            break;

    ### En el siguiente bloque de codigo se ve si al menos existe una exportacion para la maquina deseada, es decir
    ### si al menos se exporta el reeemplazo de bases de datos o ejecutable (PARAMETROS 1, 2)
    if(confPreparadoVersEst[i][1] == "1" or confPreparadoVersEst[i][2] == "1"):
        ### En la siguiente estructura se establece cual es la version estable elegida, en funcion de ello, se
        ### establecen las rutas de copiado de bases de datos y ejecutable segun configuracion general
        if(confPreparadoVersEst[i][5] == "1"):
            bases = confGeneral[13]
            ejec = confGeneral[14]
        elif(confPreparadoVersEst[i][5] == "2"):
            bases = confGeneral[15]
            ejec = confGeneral[16]
        r = 'echo --------------------------------------------------------\n' + \
            'echo SE PREPARARA EL ENTORNO EN MAQUINA DE IP TERMINACION {}\n'.format(confPreparadoVersEst[i][0]) + \
            '\n'

        ### En la siguiente estructura se ve si esta habilitado el copiado de bases de datos (PARAMETRO 1)
        if(confPreparadoVersEst[i][1] == "1"):
            b = 'echo SE COPIARAN LAS BASES DE DATOS\n' + \
                'timeout 2 /nobreak\n' + \
                'XCOPY "{}*" "{}" /f /q /y\n'.format(bases, confPreparadoVersEst[i][3]) + \
                '\n'
            r += b

        ### En la siguiente estructura se ve si esta habilitado el copiado del ejecutable (PARAMETRO 2)
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

def pieArchivoPreparado(txt):
    """
    Ésta función escribe el pie de un archivo de texto de preparado de entorno
    :param txt: El nombre del archivo sobre el cual escribir
    :return:
    """
    m = open(txt, "at")
    r = 'echo LA PREPARACION DEL ENTORNO HA TERMINADO' + \
        '\npause' + \
        '\nexit'
    m.write(r)
    m.close()
