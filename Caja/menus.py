from Stock.functions import *
from Caja.functions import *
from Caja.menus import *

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

def printInfoMesas(listaMesas,statsMesa,dtc,pedidosVendidos): 
    mesasVendidas = calcCantidadMesasSold(statsMesa)
    cantidadTotalVenida = mesasVendidas + pedidosVendidos

    print(f"""
[Menu Principal > Caja > Info Mesas]
          
#########[ INFO MESAS ]#########
Cantidad Mesas LEVANTADAS, no cobradas (fixear logica) = {mesasVendidas}
Cantidad Deliveries Cobrados = {pedidosVendidos}
Porcentaje Salon/Delivery = {mesasVendidas * 100 / (cantidadTotalVenida or 1)}% / {pedidosVendidos * 100 /(cantidadTotalVenida or 1)}%
Pedidos Anulados Salon/Delivery =
Productos Anulados Salon/Delivery  =
Costo total Anlaciones Salon/Delivery =
          
Costo promedio por mesa = {dtc/(calcCantidadMesasSold(statsMesa) or 1)}$

Mesas mas utilizadas + porcentajes (top 3? funcion para calcular)=
boton "3)" para ver lista de Mesas COMPLETA
          
        
1)Ver Estadisticas de Mesas
2)Ver Logs
X)Volver al menu anterior
          
##################################
""")

def printInfoStock(listaProductos,codigosProductosVendidos,prodStats):
    clearConsole()
    maxSold,minSold=calcProductosMasyMenosVendidos(listaProductos,codigosProductosVendidos)
    print(f"""
##########[ INFO STOCK ]##########
{maxSold}
{minSold}

          
1) Ver lista comparativa de productos
2) Ver informacion de producto particular
cantidad de veces vendido + porcentaje de stock vendido =
cantidad de veces anulado + porcentaje de stock anulado =
X)Volver al menu anterior
{printProducts(listaProductos,codigosProductosVendidos)}

##################################""")
    listaComparativaProductos(listaProductos,codigosProductosVendidos,prodStats)
    
def pct(parte, total):
    return parte * 100 / (total or 1)

    
def listaComparativaProductos(listaProductos,codigosProductosVendidos,prodStats):
    tabla = [
        ["PRODUCTO", "STOCK",  "Vnt. SALON / DELIVERY" ,     "Anul. SALON / DELIVERY",  "% Stock Vendido", "% Stock Anulado", "% Stock Restante" ],
        "SEPARADOR"
    ]

     # Construir las filas de productos
    for i in range(len(listaProductos)):
        # Ajustá estos índices según tu modelo real:
        # codigo         = listaProductos[i][0]   # código de producto
        nombre         = listaProductos[i][1]   # nombre del producto
        stock_inicial  = listaProductos[i][3] + prodStats[i][0] + prodStats[i][1] + prodStats[i][2] + prodStats[i][3]   #* Stock Actual + Stock Vendido + Stock Anulado + Stock Agregado?????
        stock_actual   = listaProductos[i][3]   # stock restante actual

        # Buscar ventas/anulaciones en salón y delivery
        vend_salon = prodStats[i][0]
        anul_salon = prodStats[i][1]
        vend_deliv = prodStats[i][2]
        anul_deliv = prodStats[i][3]
        # Totales
        total_vendido  = vend_salon + vend_deliv
        total_anulado  = anul_salon + anul_deliv

        # Porcentajes respecto al STOCK INICIAL
        porc_vendido   = pct(total_vendido, stock_inicial)
        porc_anulado   = pct(total_anulado, stock_inicial)
        porc_restante  = pct(stock_actual,  stock_inicial)

        fila = [
            nombre,
            str(stock_actual),
            f"{vend_salon} / {vend_deliv}",
            f"{anul_salon} / {anul_deliv}",
            f"{porc_vendido:.2f}%",
            f"{porc_anulado:.2f}%",
            f"{porc_restante:.2f}%",
        ]

        tabla.append(fila)

    # Ahora imprimimos (tu mismo formato)
    print("-"*35, "STOCK", "-"*35)

    for fila in tabla:
        if fila == "SEPARADOR":
            print("-" * 110)
        else:
            print(f"{fila[0]:<20} | "
                  f"{fila[1]:<7}  | "
                  f"{fila[2]:<22} | "
                  f"{fila[3]:<22} | "
                  f"{fila[4]:<16} | "
                  f"{fila[5]:<16} | "
                  f"{fila[6]:<16}")
    print("")


    
