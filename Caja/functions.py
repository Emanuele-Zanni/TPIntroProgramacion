from General.functions import *
from Mozos.validations import *
from Mesas.functions import *
from Caja.menus import *

def printInfoGeneral(mesas,pedidos,mozos,productos,e,td,tc,ch,d,ed,tdd,tcd,chd,dd):
    mesasActivas,_ = printMesasActivas(mesas)
    print(f"""[Menu Principal > Caja > *Info General*]

############[ INFO GENERAL ]############
Mesas Activas = {len(mesasActivas)}/{len(mesas)}
Pedidos Activos = {len(pedidos)}
Cantidad de Mozos = {len(mozos)}
""")
    tabla = [
    ["Método de Pago",  "SALON",        "DELIVERY",       "TOTAL"],
    "SEPARADOR",
    ["Efectivo",        f"{e}$",        f"{ed}$",         f"{e+ed}$"],
    ["Tarjeta Débito",  f"{td}$",       f"{tdd}$",        f"{td+tdd}$"],
    ["Tarjeta Crédito", f"{tc}$",       f"{tcd}$",        f"{tc+tcd}$"],
    ["Cheque",          f"{ch}$",       f"{chd}$",        f"{ch+chd}$"],
    ["Deuda",           f"{d}$",        f"{dd}$",         f"{d+dd}$"],
    "SEPARADOR",
    ["Totales",f"{e+td+tc+ch+d}$",f"{ed+tdd+tcd+chd+dd}$",f"{(e+td+tc+ch+d) + (ed+tdd+tcd+chd+dd)}$"],
]
    print("-"*25,"Ingresos","-"*25)

    for fila in tabla:
        if fila == "SEPARADOR":
            print("-" * 60)
        else:
            print(f"{fila[0]:<18} | {fila[1]:<10} | {fila[2]:<10} | {fila[3]:<10}")
    print("")


def printInfoMozos(): 
        print(f"""[Menu Principal > Caja > *Info Mozos*]
#########[ INFO MOZOS ]#########
*Estadisticas generales / leaderboard / podio =
            
1) Ver informacion de Mozo Particular
X) Volver al Menu anterior
            
##################################
""")


def infoMozosSubmenu(listaMozos,mozoStats):
    on = True
    optionVar = True
    mozosVar = False
    while on:
        clearConsole()
        printInfoMozos()
        choice = input("Ingrese una opcion: ")
        if choice == "1":
            on = False
            mozosVar = True
        elif choice == "X" or choice == "x":
            on = False
        else:
            print("Opcion no valida")
            input("Presione enter para volver al menu anterior...")

    while mozosVar:
        clearConsole()
        nombreMozo = input("Ingrese el codigo o nombre del mozo: ")
        isName,codigoMozo = isMozoNameValid(listaMozos,nombreMozo)
        isNum,numMozo = checkAndConvertToInt(nombreMozo)

        # print(f"Codigo de mozo = {codigoMozo}")
        # print(f"Numero de mozo = {numMozo}")

        if isName:
            print(f"Codigo de mozo = {codigoMozo}")
            printInfoMozo(listaMozos,mozoStats,codigoMozo)
            mozosVar = False
            input("Presione enter para continuar...")
        elif isNum and isName == False:
            isValid = isMozoValid(listaMozos,numMozo)
            if isValid:
                printInfoMozo(listaMozos,mozoStats,numMozo
                )
                on = True
                mozosVar = False
                input("Presione enter para continuar...")
            else:
                print("Mozo no valido")
                input("Presione enter para volver al menu anterior...")
        else:
            print("La opcion ingresada es invalida")
            input("Presione enter para volver al menu anterior...")

def infoMesasSubmenu(mesas,statsMesas,dtc,cantPedidosVendidos,listaProductos,logs):
    on = True
    while on:
        clearConsole()
        printInfoMesas(mesas,statsMesas,dtc,cantPedidosVendidos)
        choice = input("Ingrese una opcion: ")
        if choice == "1": #! Ver Estadisticas de Mesa
            printMesaStats(mesas,statsMesas)
        elif choice == "2": #! Ver Logs de MESAS
            verLogs(listaProductos,logs)
        elif choice == "X" or choice == "x":
            on = False
        else:
            print("Opcion no valida")
            input("Presione enter para volver al menu anterior...")

def printInfoMozo(listaMozos,mozoStats,numMozo):
    print(f"""
#########[ INFO MOZO {numMozo} ]#########
Codigo de mozo = {listaMozos[numMozo-1][0]}
Nombre/Apodo = {listaMozos[numMozo-1][1]}
Mesas Activas = {listaMozos[numMozo-1][2]}

Cantidad de Mesas Cobradas = {mozoStats[numMozo-1][0][0]}
Cantidad de Deliveries Realizados = {mozoStats[numMozo-1][0][2]}

Total recaudado:
Salon = {mozoStats[numMozo-1][0][1]}$
Delivery = {mozoStats[numMozo-1][0][3]}$
------------------
Total = {mozoStats[numMozo-1][0][1] + mozoStats[numMozo-1][0][3]}$
Costo de Anulaciones = -{mozoStats[numMozo-1][1][1]+mozoStats[numMozo-1][1][3]}$

##################################
""")
    

"""
*Estadisticas por mozo* (un input para elegir el num de mozo)
Cambios de mozos mesa = 

LOGS DE CADA MESA TOMADA???????????????????

lista de productos vendidos? c/u
-cantidad de prods vendidos total
-porcentaje de stock vendido en el dia
-prod mas vendido (por el mozo)
-prod menos vendido (por el mozo)
"""

def printMesaStats(listaMesas,statsMesa):
    clearConsole()
    print(f"[Menu Principal > Caja > Info Mesas > *Estadisticas por Mesa*]")
    print("")
    mesasVendidas = calcCantidadMesasSold(statsMesa)
    table = input("Ingrese el numero de mesa a visualizar: ")
    isNumber,table = checkAndConvertToInt(table)



    vecesLevantada = statsMesa[table-1][0]
    print(f"""
#########[ DATOS MESA {table} ]#########
Veces Levantada: {vecesLevantada}
Veces Anulada??:
Mozos Asignados:{printMozosMesa(statsMesa[table-1][1])}
Cant Productos Cargados: {statsMesa[table-1][2]}
Porcentaje de eleccion: {vecesLevantada*100 / (mesasVendidas or 1)}%
algo%, que se divida la cant de veces levantada con el total de todas las mesas
""")
    input("Presione enter para continuar...")

def verLogs(listaProductos,logs):
    id = 1
    case = ""
    on = True
    while on:
        clearConsole()

        #* Esta estructura me ayuda a identificar el caso actual y asi poder mostrar las opciones correctas
        if len(logs) == 0:
            case = "noLog" #* Caso => No hay logs
        elif id == 1 and id == len(logs):
            case = "onlyLog" #* Caso => Solo hay 1 log
        elif id == len(logs):
            case = "maxLog" #* Caso => El log actual es el ultimo
        elif id == 1:
            case = "minLog" #* Caso => El log actual es el primero
        else:
            case = "commonLog" #* Caso => El log actual es comun, no tiene restricciones

        # print(f"Case Actual = {case}")

        
        if case == "noLog": #* Si no hay logs, no se muestra nada
            print("No hay logs para mostrar")
            input("Presione enter para continuar...")
            on = False
        else:
            print(f"""
[Menu Principal > Caja > Info Mesas > *Logs*]
[Viendo log {id} de {len(logs)}]
{printLog(listaProductos,logs,id)}""")
            
            #* Segun el caso, se muestran las opciones correspondientes
            if case == "maxLog":
                print(f"""1)Ver log Anterior
3)Ingresar ID de Log
X)Volver al menu anterior""")
            elif case == "minLog":
                print(f"""2)Ver log Siguiente
3)Ingresar ID de Log
X)Volver al menu anterior""")
            elif case == "onlyLog":
                print("X)Volver al menu anterior")
            else:
                print(f"""1)Ver log Anterior
2)Ver log Siguiente
3)Ingresar ID de Log
X)Volver al menu anterior""")
                
            #* Se ingresa la opcion y se restrigen los condicionales segun el caso del log actual para evitar errores
            choice = input("Ingrese una opcion: ")
            if choice == "1" and case != "minLog" and case != "onlyLog":
                id -= 1
            elif choice == "2" and case != "maxLog" and case != "onlyLog":
                id += 1
            elif choice == "3" and case != "onlyLog":
                id = input("Ingrese el ID del log a visualizar: ")
                isNumber,id = checkAndConvertToInt(id)
                #! falta validar que el id sea valido
            elif choice == "x" or choice == "X":
                on = False
            else:
                print("Opcion no valida")
                input("Presione enter para volver al menu anterior...")
    
def printLog(listaProductos,logs,id=1):

    tableOrAddress = printTableOrAddress(logs,id)
    return  f"""
-------------------[ LOG {id} ]-------------------
Hora de Facturacion: {logs[id-1][0]}
Salon/Delivery?: {logs[id-1][1]}
{tableOrAddress}

Productos de la Mesa:
{printProducts(listaProductos,logs[id-1][4][1])}

Total de la Mesa: {logs[id-1][4][3]}$ | Metodo de pago: {logs[id-1][2]}
--------------------------------------------------
"""

def printTableOrAddress(logs,id):
    if logs[id-1][1] == "Salon":
        return f"Mesa: {logs[id-1][3]} | Mozo: {logs[id-1][4][0]}"
    else:
        return f"Direccion: {logs[id-1][3]} | Mozo: {logs[id-1][4][0]}"