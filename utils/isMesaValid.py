def isMesaValid(listaMesas,numMesa):
    mesaValida=False
    tableFound=False
    for i in range(len(listaMesas)):
        if numMesa-1 != i and tableFound==False:
            if i+1 == len(listaMesas):
                print(f"Mesa {numMesa} no encontrada")
        elif listaMesas[numMesa-1][2] == False: #* Disponible? = False
                        tableFound=True
                        if i+1 == len(listaMesas):
                            print(f"Mesa {numMesa} ocupada")
                        # break
        elif numMesa-1 == i and tableFound==False:
                        # print("Mesa seleccionada exitosamente!")
                        mesaValida=True
                        tableFound=True
                        i = len(listaMesas)
                        # break

    return mesaValida
