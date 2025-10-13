def isMesaEmpty(listaMesas,numMesa):
    for i in range(len(listaMesas)):
        if listaMesas[numMesa-1][2] == True:
            # print("La mesa esta libre")
            return True
        else:
            # print("La mesa no esta libre")
            return False

def isMesaValid(listaMesas, numMesa):
    if numMesa > 0 and numMesa <= len(listaMesas):
        print(f"La mesa es valida")
        return True
    else:
        return False
    
def