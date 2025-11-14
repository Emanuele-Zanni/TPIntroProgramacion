from General.functions import *
# from Mesas.functions import printMozosMesa

def mesasMenu():
    # limpiarConsola()
    # clear_except_last(1)
    print("""[Menu Principal > Mesas]

#########[ MENU MESAS ]#########
1)Ver Salon
2)Ver Delivery (NO HECHO)
3)Ver Estadisticas
4)Configurar cantidad de mesas
X)Volver al menu anterior
#################################
""")
            
        
def salonMenu():
    # limpiarConsola()
    # clear_except_last(1)

    print("""[Menu Principal > Mesas > Salon]
          
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
    
def tableSettingsMenu(mesas): #! VALIDACIONES GRALES
    print(f"Cantidad de mesas Actuales: {len(mesas)}")
    print("")
    value = input("Ingrese la nueva cantidad de mesas: ")
    isNumber,value = checkAndConvertToInt(value)

    if isNumber:
        newTableQuantity = value - len(mesas)

        if newTableQuantity < 0:
            #? Se usa la variable mode para que la proxima funcion sepa el tipo de operacion a realizar
            newTableQuantity = abs(newTableQuantity)
            if newTableQuantity > len(mesas):
                mode = -2
                print("No se puede eliminar mas mesas de las existentes") #! ?
                return mode,newTableQuantity
            elif newTableQuantity <= len(mesas):
                mode = -1
                return mode,newTableQuantity
                
            else:
                mode = 1
                return mode,newTableQuantity
        elif newTableQuantity > 0:
            mode = 1
            return mode,newTableQuantity
        elif newTableQuantity == 0:
            mode = 0
            return mode,newTableQuantity
        else:
            mode = 2
            return mode,newTableQuantity
    elif value == "":
        mode = 4
        newTableQuantity = 0
        return mode,newTableQuantity
    else:
        mode = 5
        newTableQuantity = 0
        return mode,newTableQuantity

    
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
    