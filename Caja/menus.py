def cajaMenu():

    print("""[Menu Principal > Caja]
          
#########[ MENU CAJAS ]#########
1)Ver información general
2)Ver información de mozos 
3)Ver información de mesas 
4)Ver información de stock 
5)Ver información de pagos
X)Volver al menu anterior 
#################################
""")
    

def printInfoMesas(): 
    print(f"""
#########[ INFO MESAS ]#########
*Estadisticas Mesas Generales*
Cantidad de Mesas existentes =
Cantidad de Mesas levantadas =
Cantidad de Delivery =
Porcentaje Salon/Delivery =
LOGS DE CADA MESA COBRADA???????????????????
          
Costo promedio por mesa =
Mesas mas utilizadas + porcentajes =
          
lista de stats de mesa
Buscador de stats de mesa (input con funcion nueva)
          
          
*Estadisticas por Mesa* (un input para elegir el num de mesa)
Cantidad de veces levantada + porcentaje =
Dinero recaudado + porcentaje =
          
*Estadisticas Delivery* (un input para ver delivery)
Cantidad de Delivery = 
Dinero recaudado + porcentaje =
          
##################################
""")

def printInfoStock():
    print(f"""
##########[ INFO STOCK ]##########
prod mas vendido?
prod menos vendido?
lista prods agotados
          

          
lista de Stats de prods
cantidad de veces vendido + porcentaje de stock vendido =
cantidad de veces anulado + porcentaje de stock anulado =
Buscador de stats de producto (input con funcion nueva)
##################################
""")
         
def printInfoPagos():
    print(f"""
#########[ INFO PAGOS ]######### 
Total en efectivo = {efectivoTotalCaja}
Total en tarjeta débito = {debitoTotalCaja}
Total en tarjeta crédito = {creditoTotalCaj}
Total en cheque = {chequeTotalCaja}
################################""")
