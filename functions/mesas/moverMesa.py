from functions.mesas.validations import isMesaReal

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