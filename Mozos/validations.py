def isMozoValid(listaMozos, numMozo):
    mozoValido=False
    for i in range(len(listaMozos)):
        if numMozo-1 != i and mozoValido==False:
            if i+1 == len(listaMozos):
                # print(f"Mozo {numMozo} no encontrado")
                mozoValido=False
        else:
            mozoValido=True
            # print("Mozo seleccionado exitosamente!")
            # print(f"Mozo numero {numMozo}: {listaMozos[numMozo-1]}")

    return mozoValido

def isMozoNameValid(listaMozos, nombreMozo):
    mozoValido=False
    codigoMozo=""
    for i in range(len(listaMozos)):
        if nombreMozo == listaMozos[i][1] and mozoValido==False:
            mozoValido=True
            codigoMozo=listaMozos[i][0]

    return mozoValido,codigoMozo
