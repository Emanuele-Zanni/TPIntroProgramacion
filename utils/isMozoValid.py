def isMozoValid(listaMozos, numMozo):
    mozoValido=False
    for i in range(len(listaMozos)):
        if numMozo-1 != i and mozoValido==False:
            if i+1 == len(listaMozos):
                print(f"Mozo {numMozo} no encontrado")
        else:
            mozoValido=True
            # print("Mozo seleccionado exitosamente!")
            # print(f"Mozo numero {numMozo}: {listaMozos[numMozo-1]}")
            break

    return mozoValido