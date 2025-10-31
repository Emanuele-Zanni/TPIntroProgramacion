def cajaMenu():

    print("""
#########[ MENU CAJAS ]#########
1)Ver información general
2)Ver información de mozos 
3)Ver información de mesas 
4)Ver información de stock 
X)Volver al menu anterior 
#################################
""")

def printInfoMozos():
    print(f"""
#########[ INFO MOZOS]#########
*Estadisticas generales / leaderboard / podio*

*Estadisticas por mozo* (un input para elegir el num de mozo)
Cambios de mozos mesa = 
Mesas levantadas por mozos + porcentaje =
Deliveries realizados por mozos + porcentaje =
Dinero recaudado por mozo + porcentaje (Mostrar Salon y delivery por separado)=
Dinero anulado + porcentaje (Mostrar Salon y delivery por separado?) = 
total recaudado salon =
total recaudado delivery =
total de totales?? =
LOGS DE CADA MESA TOMADA???????????????????

lista de productos vendidos? c/u
-cantidad de prods vendidos total
-porcentaje de stock vendido en el dia
-prod mas vendido (por el mozo)
-prod menos vendido (por el mozo)
##################################
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
         
