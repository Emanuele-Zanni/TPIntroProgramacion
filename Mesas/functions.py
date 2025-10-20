from Stock.functions import *
from Mesas.validations import *
from Mozos.validations import *

def levantarMesa(listaMesas,listaMozos,listaProductos):
            pedidosMesa = []
            mesaValida=False
            mozoValido=False
            pedidoValido=False
            #* Type Mesa = NumeroMesa,MozoAsignado,"Pedidos",Disponible?(Boolean),MontoAPagar

            #* Validar Mesa con/sin funcion
            while mesaValida==False:
                numMesa = int(input("Ingrese el numero de mesa: "))

                mesaValida = isMesaValid(listaMesas,numMesa)

            #* Validar Mozo
            while mozoValido==False:
                numMozo = int(input("Ingrese el numero de mozo: "))

                mozoValido = isMozoValid(listaMozos,numMozo)

            item = 1
            total = 0
            producto = ""
            codigo = 0
            while codigo != -1:
                codigo = int(input("Ingrese el codigo del item a cargar (-1 para finalizar): "))
                producto = getProduct(listaProductos,codigo)
                if producto!= "":
                    pedidosMesa.append(producto[0])
                    total += producto[2]
                elif codigo == -1:
                    print("Mesa Levantada exitosamente!")
                
            
            listaMesas[numMesa-1] = [numMozo,pedidosMesa,False,total] #* usar listaMozos[numMozo-1] para guardar el nombre del mozo en vez del num
        
def anularMesa(listaMesas):
    print("Anular Mesa")
    isValid=True
    table = int(input("Seleccione la mesa a anular: "))

    isValid = isMesaReal(listaMesas,table)
    if isValid == False:
        print("Mesa no encontrada")
                            
    if isValid:
        isEmpty = isMesaEmpty(listaMesas,table)
        if isEmpty:
            isValid=False
                                
    if isValid:
        listaMesas[table-1] = [0,"",True,0]
        print("Mesa anulada exitosamente")

    elif isValid == False:
        print("Error al anular mesa")

def cobrarMesa(listaMesas):
    print("Cobrar Mesa")
    isValid=True
    table = int(input("Seleccione la mesa a cobrar: "))

    isValid = isMesaReal(listaMesas,table)
    if isValid == False:
        print("Mesa no encontrada")
                            
    if isValid:
        isEmpty = isMesaEmpty(listaMesas,table)
        if isEmpty:
            isValid=False
                                
    if isValid:
        listaMesas[table-1] = [0,"",True,0]
        print("Mesa cobrada exitosamente")

    elif isValid == False:
        print("Error al cobrar mesa")

def moverMesa(mesas):
    print("Mover Mesa")
    isValid = True

    tableOld = int(input("Seleccione la mesa a mover: ")) - 1

    # if isMesaReal(mesas,tableOld+1) == False:
    #     print("Mesa a mover no existe")
    #     isValid = False

    isValid = isMesaReal(mesas,tableOld+1)

    if isValid:
        if mesas[tableOld][2] == True:
            print("Mesa a mover vacia")
            isValid = False
        
    if isValid:
        tableNew = int(input("Seleccione la mesa destino: ")) - 1

    # if isValid:
    #     isMesaReal(mesas,tableNew+1) == False
    #     isValid = False
    if isValid:
        isValid = isMesaReal(mesas,tableNew)

    if isValid:
        if tableOld == tableNew:
            print("Mesa de origen y destino no pueden ser iguales")
            isValid = False

    if isValid:
        if mesas[tableNew][2] == False:
            print("Mesa destino ocupada")
            isValid = False

       
    if isValid:
        print("Mesa movida exitosamente")
        mesas[tableNew] = mesas[tableOld]
        mesas[tableOld] = [0,"",True,0]

    return mesas

def getMesa(listaMesas,mesa):
    return listaMesas[mesa-1]

def printMesa(listaMesas):
    numMesa = int(input("Ingrese la mesa a visualizar:"))
    isReal = isMesaReal(listaMesas,numMesa)
    mesa = listaMesas[numMesa-1]
    
     #* Ordenar productos por codigo menor a mayor

    if isReal:
            print(f"1. Mozo: {mesa[0]}")
            print(f"2. Pedidos: {mesa[1]}")
            print(f"3. Disponibilidad: {mesa[2]}")
            print(f"4. Valor total de Productos: {mesa[3]}$")

    return listaMesas



