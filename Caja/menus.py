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
    
def printInfoGeneral(mesas,mozos,stock,productos):
    print(f"""
#########[ INFO GENERAL ]#########
Cantidad de Mozos = {len(mozos)}
Cantidad de Mesas = {len(mesas)}
Cantidad de Stock = {stock}
Cantidad de Productos = {productos} 
Cantidad de dinero total = {productos}

efectivo
tarjeta débito
tarjeta crédito
cheque 

##################################
""")

def printInfoMozos():
    print(f"""
#########[ INFO MOZOS]#########
Cambios de mozos mesa = 

##################################
""")
    

def printInfoMesas(): 
    print(f"""
#########[ INFO MESAS ]#########
Cantidad de Delivery =
Cantidad de Mesas levantadas =
Cantidad de mesas usadas = 

##################################
""")

def printInfoStock():
    print(f"""
##########[ INFO STOCK ]##########

##################################
""")
         
