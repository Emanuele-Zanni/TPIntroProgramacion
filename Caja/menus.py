from Stock.functions import *

def cajaMenu():

    print("""[Menu Principal > Caja]
          
#########[ MENU CAJAS ]#########
1) Ver información general
2) Ver información de mozos 
3) Ver información de mesas 
4) Ver información de stock 
X) Volver al menu anterior 
#################################
""")
    
def calcCantidadMesasSold(statsMesa):
    total = 0
    for i in range(len(statsMesa)):
        total += statsMesa[i][0]
    # print(f"total de mesas vendidas = {total}")
    return total


def printInfoMesas(listaMesas,statsMesa,dtc,pedidosVendidos): 
    mesasVendidas = calcCantidadMesasSold(statsMesa)
    cantidadTotalVenida = mesasVendidas + pedidosVendidos

    print(f"""
[Menu Principal > Caja > Info Mesas]
          
#########[ INFO MESAS ]#########
Cantidad de Mesas Salon LEVANTADAS, no cobradas (fixear logica) = {mesasVendidas}
Cantidad de Pedidos Delivery Cobrados = {pedidosVendidos}
Porcentaje Salon/Delivery = {mesasVendidas * 100 / (cantidadTotalVenida or 1)}% / {pedidosVendidos * 100 /(cantidadTotalVenida or 1)}%
Pedidos Anulados Salon/Delivery =
Productos Anulados Salon/Delivery  =
Costo total Anlaciones Salon/Delivery =
          
Costo promedio por mesa = {dtc/(calcCantidadMesasSold(statsMesa) or 1)}
Mesas mas utilizadas + porcentajes (top 3? funcion para calcular)=
          
          
*Estadisticas por Mesa* (un input para elegir el num de mesa)
Cantidad de veces levantada + porcentaje =
Dinero recaudado + porcentaje =

1)Ver Estadisticas de Mesas
2)Ver Logs
X)Volver al menu anterior
          
##################################
""")

def printInfoStock(listaProductos,codigosProductosVendidos):
    clearConsole()
    print(f"""
##########[ INFO STOCK ]##########
-Producto más vendido
-Producto menos vendido
-Total recaudado y cantidad de unidades vendidas
          
1)lista prods agotados
2)lista de Stats de prods / prods vendidos
cantidad de veces vendido + porcentaje de stock vendido =
cantidad de veces anulado + porcentaje de stock anulado =
2.1)Buscador de stats de producto (input con funcion nueva)
3)lista de todos los prods vendidos (comparacion stock inicio dia vs stock actual) ???? esto es lo mismo que la "2)"
{printProducts(listaProductos,codigosProductosVendidos)}
##################################""")
    
