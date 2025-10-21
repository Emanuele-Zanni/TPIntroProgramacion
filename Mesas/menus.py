from General.functions import *

def mesasMenu():
    # limpiarConsola()
    clear_except_last(3)
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
    clear_except_last(3)
    # print("\033[H\033[J", end="")

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
    