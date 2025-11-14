from General.functions import *
from Mozos.validations import *

def printInfoGeneral(mesas,mozos,productos,e,td,tc,ch,d):
    print(f"""[Menu Principal > Caja > *Info General*]

#########[ INFO GENERAL ]#########
Cantidad de Mesas = {len(mesas)}
Cantidad de Mozos = {len(mozos)}

efectivo = {e}$
tarjeta débito = {td}$
tarjeta crédito = {tc}$
cheque = {ch}$
deuda = {d}$
anulaciones = N/A
-----------------------------------------
Cantidad de dinero total = {e+td+tc+ch+d}$
##################################
""")

def printInfoMozos(): 
        print(f"""[Menu Principal > Caja > *Info Mozos*]
#########[ INFO MOZOS ]#########
*Estadisticas generales / leaderboard / podio =
            
1) Ver informacion de Mozo Partcular
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
        numMozo = input("Ingrese el numero de mozo: ")
        isNum,numMozo = checkAndConvertToInt(numMozo)

        if isNum:
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

def printInfoMozo(listaMozos,mozoStats,numMozo):
    print(f"""
#########[ INFO MOZO {numMozo} ]#########
Codigo de mozo = {numMozo}
Nombre/Apodo = {listaMozos[numMozo][1]}
Mesas Activas = {listaMozos[numMozo][2]}

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