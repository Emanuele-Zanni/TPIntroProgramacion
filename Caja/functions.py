from General.functions import *
from Mozos.validations import *
from Mesas.functions import *
import Caja.menus as menus


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
        clearConsole()
        print(f"""[Menu Principal > Caja > *Info Mozos*]
              
#########[ INFO MOZOS ]#########
*Estadisticas generales / leaderboard / podio =
-Mostrar lista como la de INFO GENERAL, mostrar ingresos + porcentaje, mostrar mesas cobradas + porcentaje, mosrar pedidos cobrados + porcentaje
-Lista debe actuar como un top 3 de mozos
-Opcion "2)" para ver lista completa de TODOS los mozos rankeados?
              
1) Ver informacion de Mozo Particular
2) Ver lista comparativa COMPLETA de Mozos
X) Volver al Menu anterior
            
##################################
""")
        


def listaComparativaMozos(listaMozos, mozoStats):
    clearConsole()
    print("[Menu Principal > Caja > Info Mozos > *Lista Comparativa Mozos*]")
    print("")

    # ---------- Construcción de filas de datos ----------
    tabla = []

    total_mesas_vendidas = calcTotalMesasVendidas(mozoStats)
    total_pedidos_vendidos = calcTotalPedidosVendidos(mozoStats)

    total_mesas_anuladas = calcTotalMesasAnuladas(mozoStats)
    total_pedidos_anulados = calcTotalPedidosAnulados(mozoStats)

    total_costo_anulaciones = calcTotalCostoAnulaciones(mozoStats)

    total_cobrado_salon = calcTotalCobradoSalon(mozoStats)
    total_cobrado_delivery = calcTotalCobradoDelivery(mozoStats)
    total_cobrado_total = total_cobrado_salon + total_cobrado_delivery

    for i in range(len(listaMozos)):
        codigo = listaMozos[i][0]
        nombre = listaMozos[i][1]
        
        mesas_cobradas      = mozoStats[i][0][0]
        pedidos_cobrados    = mozoStats[i][1][0]

        cobrado_salon       = mozoStats[i][0][1]
        cobrado_delivery    = mozoStats[i][1][1]
        total_cobrado       = cobrado_salon + cobrado_delivery

        cant_anul_salon     = mozoStats[i][0][2]
        cant_anul_delivery  = mozoStats[i][1][2]

        dinero_anulado_salon    = mozoStats[i][0][3]
        dinero_anulado_delivery = mozoStats[i][1][3]
        total_anulado           = dinero_anulado_salon + dinero_anulado_delivery

        fila = [
            codigo,
            nombre,
            str(mesas_cobradas)     + f" ({pct(mesas_cobradas,     total_mesas_vendidas)}%)",
            str(pedidos_cobrados)   + f" ({pct(pedidos_cobrados,   total_pedidos_vendidos)}%)",
            str(cant_anul_salon)    + f" ({pct(cant_anul_salon,    total_mesas_anuladas)}%)",
            str(cant_anul_delivery) + f" ({pct(cant_anul_delivery, total_pedidos_anulados)}%)",
            f"{total_anulado}$"     + f" ({pct(total_anulado,      total_costo_anulaciones)}%)",
            f"{cobrado_salon}$"     + f" ({pct(cobrado_salon,      total_cobrado_salon)}%)",
            f"{cobrado_delivery}$"  + f" ({pct(cobrado_delivery,   total_cobrado_delivery)}%)",
            f"{total_cobrado}$"     + f" ({pct(total_cobrado,      total_cobrado_total)}%)"
        ]

        tabla.append(fila)

    # ---------- Header de 2 filas ----------
    header_row1 = [
        "Codigo", "Nombre", "Mesas", "Pedidos",
        "Anul.", "Anul.",
        "Total", "Cobrado", "Cobrado", "Total"
    ]
    header_row2 = [
        "", "Mozo", "Cobradas", "Cobrados",
        "Salon", "Delivery",
        "Anulado", "Salon", "Delivery", "Cobrado"
    ]

    # ---------- Cálculo de anchos por columna ----------
    cols = len(header_row1)
    col_widths = []

    for col in range(cols):
        max_len = len(header_row1[col])
        max_len = max(max_len, len(header_row2[col]))
        for fila in tabla:
            max_len = max(max_len, len(str(fila[col])))
        # pequeño padding para que no quede pegado
        col_widths.append(max_len + 2)

    def format_row(values):
        parts = []
        for i, val in enumerate(values):
            parts.append(str(val).ljust(col_widths[i]))
        return " | ".join(parts)

    total_width = sum(col_widths) + 3 * (cols - 1)

    print("-" * ((total_width - len(" MOZOS ")) // 2) + " MOZOS " + "-" * ((total_width - len(" MOZOS ")) // 2))

    # Header fila 1
    print(format_row(header_row1))
    # Header fila 2
    print(format_row(header_row2))
    print("-" * total_width)

    # Filas de datos
    for fila in tabla:
        print(format_row(fila))

    print("-" * total_width)
    print("")
    input("Ingrese enter para continuar...")


def calcTotalMesasVendidas(mozoStats):
    total = 0
    for i in range(len(mozoStats)):
        total += mozoStats[i][0][0]
    return total

def calcTotalPedidosVendidos(mozoStats):
    total = 0
    for i in range(len(mozoStats)):
        total += mozoStats[i][1][0]
    return total

def calcTotalMesasAnuladas(mozoStats):
    total = 0
    for i in range(len(mozoStats)):
        total += mozoStats[i][0][2]
    return total

def calcTotalPedidosAnulados(mozoStats):
    total = 0
    for i in range(len(mozoStats)):
        total += mozoStats[i][1][2]
    return total

def calcTotalCostoAnulaciones(mozoStats):
    total = 0
    for i in range(len(mozoStats)):
        total += mozoStats[i][0][3]
        total += mozoStats[i][1][3]
    return total

def calcTotalCobradoSalon(mozoStats):
    total = 0
    for i in range(len(mozoStats)):
        total += mozoStats[i][0][1]
    return total

def calcTotalCobradoDelivery(mozoStats):
    total = 0
    for i in range(len(mozoStats)):
        total += mozoStats[i][1][1]
    return total

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
        elif choice == "2":
            listaComparativaMozos(listaMozos,mozoStats)
        elif choice == "X" or choice == "x":
            on = False
        else:
            print("Opcion no valida")
            input("Presione enter para volver al menu anterior...")

    while mozosVar:
        clearConsole()
        print("[Menu Principal > Caja > Info Mozos > *Info Mozo Particular*]")
        print("")
        nombreMozo = input("Ingrese el codigo o nombre del mozo: ")
        isName,codigoMozo = isMozoNameValid(listaMozos,nombreMozo)
        isNum,numMozo = checkAndConvertToInt(nombreMozo)

        # print(f"Codigo de mozo = {codigoMozo}")
        # print(f"Numero de mozo = {numMozo}")

        if nombreMozo == "x" or nombreMozo == "X":
            print("El valor ingresado no puede estar vacio")
            input("Presione enter para continuar...")
            return


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

def infoMesasSubmenu(mesas,statsMesas,prodStats,dtc,pedidosVendidos,pedidosAnulados,listaProductos,logs):
    on = True
    while on:
        clearConsole()
        menus.printInfoMesas(mesas,statsMesas,prodStats,dtc,pedidosVendidos,pedidosAnulados)
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

def printMesaStats(listaMesas,statsMesas):
    clearConsole()
    print(f"[Menu Principal > Caja > Info Mesas > *Estadisticas por Mesa*]")
    print("")
    mesasVendidas = calcCantidadMesasSold(statsMesas)
    table = input("Ingrese el numero de mesa a visualizar: ")
    isNumber,table = checkAndConvertToInt(table)

    if table == "":
        print("El valor ingresado no puede estar vacio")
        input("Presione enter para continuar...")
        return
    elif isNumber == False:
        print("La opcion ingresada debe ser un numero")
        input("Presione enter para continuar...")
        return



    vecesLevantada = statsMesas[table-1][0]
    print(f"""
#########[ DATOS MESA {table} ]#########

Veces Levantada: {vecesLevantada}
Veces Anulada: {statsMesas[table-1][6]}
Dinero Recaudado en Mesa: {statsMesas[table-1][4]}$
Dinero Anulado en Mesa: {statsMesas[table-1][5]}$
Mozos Asignados:{printMozosMesa(statsMesas[table-1][1])}
Cant Productos Cargados: {statsMesas[table-1][2]}
Cant Productos Anulados: {statsMesas[table-1][3]}
Porcentaje de eleccion: {vecesLevantada*100 / (mesasVendidas or 1)}%
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
            print("[Menu Principal > Caja > Info Mesas > *Logs*]")
            print("")
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
       
def calcCantidadMesasSold(statsMesa):
    total = 0
    for i in range(len(statsMesa)):
        total += statsMesa[i][0]
    # print(f"total de mesas vendidas = {total}")
    return total

def calcCantidadMesasAnuladas(statsMesa):
    mesasAnuladas = 0
    for i in range(len(statsMesa)):
        mesasAnuladas += statsMesa[i][6]
    return mesasAnuladas

# def calcCantidadProductosAnulados(statsMesa):
#     total = 0
#     for i in range(len(statsMesa)):
#         total += statsMesa[i][3]
#     return total

def calcCantidadProductosAnulados(prodStats):
    cantAnuladaSalon = 0
    cantAnuladaDelivery = 0
    for i in range(len(prodStats)):
        cantAnuladaSalon += prodStats[i][1]
        cantAnuladaDelivery += prodStats[i][3]
    return cantAnuladaSalon,cantAnuladaDelivery

def calcProductosMasyMenosVendidos(listaProductos,listaProductosVendidos):
    CantidadProdsVendidos = len(listaProductosVendidos) #* Cantidad de productos vendidos total para calcular porcentajes

    if CantidadProdsVendidos == 0:
        return "Producto mas vendido: N/A","Producto menos vendido: N/A"
    
    #* Iterar la lista de codigos de productos desordenados para determinar productos unicos y guardarlos en uniqueProdList[]
    uniqueProdList = []
    for k in range(len(listaProductos)):
        uniqueProdList.append(listaProductos[k][0])

    #* Iterar nuevamente la lista con los codigos unicos y obtener la cantidad de veces que se vendio cada uno, y agruparlos en una lista (results) con Tuplas por cada Producto "[codigo, cantidad]"
    results = []
    quantity = 0
    for i in range(len(uniqueProdList)):
        for j in range(len(listaProductosVendidos)):
            if uniqueProdList[i] == listaProductosVendidos[j]:
                quantity += 1

            if j == len(listaProductosVendidos) - 1:
                aux = [uniqueProdList[i], quantity]
                results.append(aux)
                quantity = 0

    #* Determinar productos mas y menos vendidos
    masVendido=[]
    menosVendido=[]
    max=0
    min=0
    for i in range(len(results)):
        if results[i][1] > max:
            max = results[i][1]
            masVendido = [results[i]]
        elif results[i][1] == max:
            masVendido.append(results[i])

        if results[i][1] < min:
            min = results[i][1]
            menosVendido = [results[i]]
        elif results[i][1] == min:
            menosVendido.append(results[i])

    # print(f"RESULTADOS ==> {results}")
    # print(f"MAS VENDIDOS: {masVendido}")
    # print(f"MENOS VENDIDOS: {menosVendido}")

    #* Determinar producto mas vendido y devolver un texto con la info correcta segun el caso correspondiente (1 max vendido, 2 o 3 con mismo valor, 3 o mas con max valor)
    if len(masVendido) == 1: 
        item = getProduct(listaProductos, masVendido[0][0])
        masVendidoText = f"Producto mas vendido: '{item[1]}' x {masVendido[0][1]} veces ({masVendido[0][1] * 100 / CantidadProdsVendidos}% de los ingresos totales)"
    else:
        if len(masVendido) > 3:
            diff = len(masVendido) - 3
            masVendidoText = "Productos mas vendidos: "
            for i in range(len(masVendido)):
                item = getProduct(listaProductos, masVendido[i][0]) 
                if i == 0:
                    masVendidoText += f"'{item[1]}'"
                elif i != len(masVendido) - 1 and i < 3:
                    masVendidoText += f", '{item[1]}' "
            masVendidoText += f"y {diff} productos mas x {masVendido[i][1]} veces ({masVendido[i][1] * 100 / CantidadProdsVendidos}% de los ingresos totales)"
        else:
            masVendidoText = "Productos mas vendidos: "
            for i in range(len(masVendido)):
                item = getProduct(listaProductos, masVendido[i][0]) 
                if i == 0:
                    masVendidoText += f"'{item[1]}' "
                elif i == len(masVendido) - 1:
                    masVendidoText += f"y '{item[1]}'"
                else:
                    masVendidoText += f", '{item[1]}' "
            masVendidoText += f" x {masVendido[i][1]} veces ({masVendido[i][1] * 100 / CantidadProdsVendidos}% de los ingresos totales)"


    #* Determinar producto menos vendido y devolver un texto con la info correcta segun el caso correspondiente (1 min vendido, 2 o 3 con mismo valor, 3 o mas con min valor)
    if len(menosVendido) == 1: 
        item = getProduct(listaProductos, menosVendido[0][0])
        menosVendidoText = f"Producto menos vendido: '{item[1]}' x {menosVendido[0][1]} veces ({menosVendido[0][1] * 100 / CantidadProdsVendidos}% de los ingresos totales)"
    else:
        if len(menosVendido) > 3:
            diff = len(menosVendido) - 3
            menosVendidoText = "Productos menos vendidos: "
            for i in range(len(menosVendido)):
                item = getProduct(listaProductos, menosVendido[i][0])
                if i == 0:
                    menosVendidoText += f"'{item[1]}'"
                elif i != len(menosVendido) - 1 and i < 3:
                    menosVendidoText += f", '{item[1]}' "
            menosVendidoText += f"y {diff} productos mas x {menosVendido[i][1]} veces ({menosVendido[i][1] * 100 / CantidadProdsVendidos}% de los ingresos totales)"
        else:
            menosVendidoText = "Productos menos vendidos: "
            for i in range(len(menosVendido)):
                item = getProduct(listaProductos, menosVendido[i][0]) 
                if i == 0:
                    menosVendidoText += f"'{item[1]}'"
                elif i == len(menosVendido) - 1:
                    menosVendidoText += f"y '{item[1]}'"
                else:
                    menosVendidoText += f", '{item[1]}' "
            menosVendidoText += f" x {menosVendido[i][1]} veces ({menosVendido[i][1] * 100 / CantidadProdsVendidos}% de los ingresos totales)"
    
    return masVendidoText,menosVendidoText