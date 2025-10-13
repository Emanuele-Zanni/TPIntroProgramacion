def isMesaEmpty(listaMesas,numMesa):
    for i in range(len(listaMesas)):
        if listaMesas[numMesa-1][2] == True:
            # print("La mesa esta libre")
            return True
        else:
            # print("La mesa no esta libre")
            return False
