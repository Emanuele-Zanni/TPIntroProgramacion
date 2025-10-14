def moverMesa(mesas):
    print("Mover Mesa")
    tableOld = int(input("Seleccione la mesa a mover: ")) - 1

    if mesas[tableOld][2] == True:
        print("Mesa a mover vacia")
        
    tableNew = int(input("Seleccione la mesa destino: ")) - 1

    if mesas[tableNew][2] == False:
        print("Mesa destino ocupada")   

    mesas[tableNew] = mesas[tableOld]
    mesas[tableOld] = [0,"",True,0]

    print("Mesa movida exitosamente")

    return mesas