from Stock.functions import *
from Mesas.validations import *
from Mozos.validations import *

def levantarMesa(listaMesas,listaMozos,listaProductos,stats):
            pedidosMesa = []
            mesaValida=False
            mozoValido=False

            #* Validar Mesa
            while mesaValida==False:
                numMesa = int(input("Ingrese el numero de mesa: "))

                mesaValida = isMesaValid(listaMesas,numMesa)

            #* Validar Mozo
            while mozoValido==False:
                numMozo = int(input("Ingrese el numero de mozo: "))

                mozoValido = isMozoValid(listaMozos,numMozo)

            #* Cargar pedidos
            item = 1
            producto = ""
            codigo = 0
            cantidadProductos = 0
            # total = 0
            while codigo != -1:
                codigo = int(input("Ingrese el codigo del item a cargar (-1 para finalizar): "))
                producto = getProduct(listaProductos,codigo)
                if producto!= "":
                    pedidosMesa.append(producto[0])
                    cantidadProductos += 1
                    # total += producto[2]
                elif codigo == -1:
                    print("Mesa Levantada exitosamente!")

            total = calculateTotal(listaProductos,pedidosMesa)
                
            
            #? usar listaMozos[numMozo-1] para guardar el nombre del mozo en vez del num
            listaMesas[numMesa-1] = [numMozo,pedidosMesa,False,total] #* Mesa levantada en listaMesas

            #* Actualizar Stats de Mesa particular
            stats[numMesa-1][0] += 1 #* Veces Levantada

            # stats[numMesa-1][1][0] = [numMozo,stats[numMesa-1][1][1] + 1] #* Mozos Asignados

            if len(stats[numMesa-1][1]) == 0:
                stats[numMesa-1][1].append([numMozo,1])
            else:
                waiterFound = False
                for i in range(len(stats[numMesa-1][1])):
                    if stats[numMesa-1][1][0][0] == numMozo:
                        stats[numMesa-1][1][0][1] += 1
                        waiterFound = True
                    elif i == len(stats[numMesa-1][1])-1 and waiterFound == False:
                        stats[numMesa-1][1].append([numMozo,1])
                

            # stats[numMesa-1][1][0][0] = numMozo
            # stats[numMesa-1][1][0][1] += 1 
            #? stats = [[0,[[0,0]],0],[0,[[0,0]],0],[0,[[0,0]],0],[0,[[0,0]],0],[0,[[0,0]],0]]
            #! 0,1,0,1

            stats[numMesa-1][2] += cantidadProductos  #* Cantidad de Productos cargados

        
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
        # totalCandela += listaMesas[table-1][3]
        listaMesas[table-1] = [0,"",True,0]
        print("Mesa cobrada exitosamente")

    elif isValid == False:
        print("Error al cobrar mesa")

def moverMesa(mesas,mesaMovidas):
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

        mesasMovidas += 1



    return mesas

def getMesa(listaMesas,mesa):
    return listaMesas[mesa-1]


def cambiarMozo(listaMesas,listaMozos):
    noErrors=True
    table = int(input("Seleccione una mesa: "))
    isValid = isMesaReal(listaMesas,table)
    if isValid == False:
        noErrors=False
                            
    if noErrors == True:
        isValid = isMesaEmpty(listaMesas,table) #! el nombre isValid aca es confuso, pero me facilita el manejo de los IFs
        if isValid == True:
            print("Mesa vacia")
            noErrors=False
                            
    if noErrors == True:
        waiter = int(input("Seleccione el nuevo mozo a asignar: "))
        isValid = isMozoValid(listaMesas,waiter)
        if isValid == False:
            print("Mozo no encontrado")
            noErrors=False

        if noErrors == True:
            listaMesas[table-1][0] = waiter

def printMesa(listaMesas,listaProductos):
    numMesa = int(input("Ingrese la mesa a visualizar:"))
    isReal = isMesaReal(listaMesas,numMesa)
    mesa = listaMesas[numMesa-1]

    products = printProducts(listaProductos,mesa[1]) #* Ordenar productos por codigo menor a mayor
    # total = calculateTotal(listaProductos,mesa[1]) #* Calcular total de la mesa


    if isReal:
            print(f"• Mozo: {mesa[0]}")
            print(f"• Mesa disponible?: {mesa[2]}")
            print(f"• Productos: {products}")
            print(f"• Valor total de Productos: {mesa[3]}$")

    return listaMesas

def printMozosMesa(stats):
    text = ""
    for i in range(len(stats)):
        text += f"\nMozo {stats[i][0]} x {stats[i][1]}"

    return text
