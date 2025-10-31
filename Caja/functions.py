def printInfoGeneral(mesas,mozos,productos,e,td,tc,ch,d):
    print(f"""
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
    print(f"""
#########[ INFO MOZOS]#########
*Estadisticas generales / leaderboard / podio =                 # qué mozo atendió
                                                                # cuánto recaudó la mesa
                                                                # sumarlo al mozo
    
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