from General.functions import *
from Mesas.functions import *

def mesasMenu():
    limpiarConsola()
    # clear_except_last(1)
    print("""
#########[ MENU MESAS ]#########
1)Ver Salon
2)Ver Delivery (NO HECHO)
3)Ver Estadisticas (NO HECHO)
4)Configuracion (NO HECHO)
X)Volver al menu anterior
#################################
""")
            
def statsMenu():
    print("""
1)Ver Estadisticas Generales
2)Ver Estadisticas de Mesa
X)Volver al menu anterior
""")
        
def salonMenu():
    limpiarConsola()
    # clear_except_last(1)

    print("""
##########[ MENU SALON ]##########
1)Ver Mesas
2)Levantar Mesa
3)Seleccionar Mesa
4)Cambiar Mozo (Dentro de "Seleccionar Mesa"?)
5)Mover Mesa
6)Convertir Delivery/Salon (Dentro de "Seleccionar Mesa")
7)Cobrar Mesa (falta CAJA)
8)Anular Mesa (falta CAJA)
X)Volver al menu anterior
#################################
""")
    
def printMesaStats(stats):

    # for stat in range(len(stats)):
    #     print(stat)

    choice = int(input("Ingrese el numero de mesa a visualizar"))

    print(f"""
#########[ DATOS MESA {choice} ]#########
Veces Levantada: {stats[choice-1][0]}
Mozos Asignados:{printMozosMesa(stats[choice-1][1])}
Cant Productos Cargados: {stats[choice-1][2]}
Porcentaje de eleccion: algo%, que se divida la cant de veces levantada con el total de todas las mesas
""")
    