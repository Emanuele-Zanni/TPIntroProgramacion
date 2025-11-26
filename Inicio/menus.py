def InicioDiaMenu():

    print("""----------- Inicio -----------
1) Iniciar Nuevo Dia
2) Ver resumen de dias previos 
X) Finalizar Programa
------------------------------""")
    
def printFinalLog(listaProductos,logs,id=1):

    return  f"""
-------------------[ LOG DIA {X} ]-------------------
* Mostrar tabla ingresos de INFO GENERAL
Hora de Facturacion: {logs[id-1][0]}
Salon/Delivery?: {logs[id-1][1]}


Productos de la Mesa:


Total de la Mesa: {logs[id-1][4][3]}$ | Metodo de pago: {logs[id-1][2]}
--------------------------------------------------
"""