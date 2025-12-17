from Stock.functions import *
from Caja.functions import *
from Caja.menus import *
from General.functions import *

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

def printInfoMesas(listaMesas,statsMesa,prodStats,dtc,pedidosVendidos,pedidosAnulados): 
    mesasVendidas = calcCantidadMesasSold(statsMesa)
    mesasAnuladas = calcCantidadMesasAnuladas(statsMesa)
    productosAnuladosSalon,productosAnuladosDelivery = calcCantidadProductosAnulados(prodStats)
    cantidadTotalVenida = mesasVendidas + pedidosVendidos

    print(f"""[Menu Principal > Caja > *Info Mesas*]
          
#########[ INFO MESAS ]#########
Cantidad Mesas LEVANTADAS, no cobradas (fixear logica) = {mesasVendidas}
Cantidad Deliveries Cobrados = {pedidosVendidos}
Porcentaje Salon/Delivery = {pct(mesasVendidas, cantidadTotalVenida)}% / {pct(pedidosVendidos, cantidadTotalVenida)}%
Mesas/Pedidos Anulados Salon/Delivery = {mesasAnuladas} / {pedidosAnulados}
Productos Anulados Salon/Delivery  = {productosAnuladosSalon} / {productosAnuladosDelivery}
          
Costo promedio por mesa = {dtc/(calcCantidadMesasSold(statsMesa) or 1)}$
          
        
1) Ver Estadisticas de Mesas
2) Ver Logs
X) Volver al menu anterior
          
##################################
""")
    

def printInfoStock(listaProductos,codigosProductosVendidos,prodStats):
    on = True
    while on:
        clearConsole()
        print("[Menu Principal > Caja > *Info Stock*]")
        print("")
        maxSold,minSold=calcProductosMasyMenosVendidos(listaProductos,codigosProductosVendidos)
        print(f"""##########[ INFO STOCK ]##########
{maxSold}
{minSold}

            
1) Ver lista comparativa de productos
2) Ver informacion de producto particular
X) Volver al menu anterior
##################################
""")
        choice = input("Ingrese una opcion: ")
        if choice == "1":
            listaComparativaProductos(listaProductos,codigosProductosVendidos,prodStats)
            input("Presione enter para volver al menu anterior.")
        elif choice == "2":
            pass
        elif choice == "X" or choice == "x":
            on = False
        else:
            print("Opcion invalida")
            input("Presione enter para continuar...")
    # {printProducts(listaProductos,codigosProductosVendidos)}

    
def listaComparativaProductos(listaProductos,codigosProductosVendidos,prodStats):
    clearConsole()
    print("[Menu Principal > Caja > Info Stock > *Lista Comparativa de Productos*]")
    print("")
    tabla = [
        ["NOMBRE DEL PRODUCTO", "STOCK",  "Vnt. SALON / DELIVERY" ,     "Anul. SALON / DELIVERY",  "% Stock Vendido", "% Stock Anulado", "% Stock Restante" ],
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


    
