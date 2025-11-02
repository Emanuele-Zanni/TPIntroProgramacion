from General.functions import *
# from Mesas.functions import printMozosMesa

def mesasMenu():
    # limpiarConsola()
    # clear_except_last(1)
    print("""
[Menu Principal > Menu Mesas]

#########[ MENU MESAS ]#########
1)Ver Salon
2)Ver Delivery (NO HECHO)
3)Ver Estadisticas
4)Configuracion?? (NO HECHO)
X)Volver al menu anterior
#################################
""")
            
        
def salonMenu():
    # limpiarConsola()
    # clear_except_last(1)

    print("""
[Menu Principal > Menu Mesas > Menu Salon]
          
##########[ MENU SALON ]##########
1)Ver Mesas
2)Levantar Mesa
3)Seleccionar Mesa
X)Volver al menu anterior
#################################
""")
    
def seleccionarMesaMenu(numMesa):
    print(f"""
#########[ OPERACIONES MESA {numMesa} ]#########
1)Cobrar Mesa
2)Anular Mesa
3)Cambiar Mozo
4)Mover Mesa
5)Convertir hacia Delivery
X)Cancelar Operacion
#################################
""")
    
def metodoPagoMenu():
    print(f"""
#########[ Metodo de Pago ]#########
1)Efectivo
2)Tarjeta Debito 
3)Tarjeta Credito (10% de intere )
4)Cheque
5)Deuda
X)Cancelar Operacion
#################################
""")
    
def statsMenu(): #* Esto posiblemente lo borre mas adelante
    print("""
1)Ver Estadisticas Generales
2)Ver Estadisticas de Mesa
X)Volver al menu anterior
""")
    
# def printMesaStats(stats):

#     # for stat in range(len(stats)):
#     #     print(stat)

#     choice = int(input("Ingrese el numero de mesa a visualizar"))

#     print(f"""
# #########[ DATOS MESA {choice} ]#########
# Veces Levantada: {stats[choice-1][0]}
# Mozos Asignados:{printMozosMesa(stats[choice-1][1])}
# Cant Productos Cargados: {stats[choice-1][2]}
# Porcentaje de eleccion: algo%, que se divida la cant de veces levantada con el total de todas las mesas
# """)
    