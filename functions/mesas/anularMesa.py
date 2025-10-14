from functions.mesas.validations import *

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