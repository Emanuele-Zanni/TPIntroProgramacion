from General.functions import *

def buscar_indice(lista_mozos, id_mozo):
    indice_encontrado = -1
    i = 0
    while i < len(lista_mozos) and indice_encontrado == -1:
        if lista_mozos[i][0] == id_mozo:
            indice_encontrado = i
        i += 1
    return indice_encontrado

def mostrar_mozos(lista_mozos):
    """"Muestra una lista de todos los mozos con ID y nombre"""
    print("--- LISTA DE MOZOS ---")
    for i in range(len(lista_mozos)):
        mozo = lista_mozos[i]
        print(f"ID: {mozo[0]} - Nombre: {mozo[1]} - Mesas: {mozo[2]}")
    print("----------------------")

def agregar_mozo(lista_mozos):
    nameCheck = False
    nameEmpty = False

    nombre = input("Ingrese el nombre del nuevo mozo: ") #! Falta validacion por nombre vacio o numerico (debe ser un string NO vacio)
    #! Tambien se debe validar por nombres y IDs repetidos

    for i in range(len(lista_mozos)):
        if lista_mozos[i][1] == nombre:
            nameCheck = True
    if nombre == "":
        nameEmpty = True


    if nameCheck:
        print("El mozo ya existe")
        # input("Presione enter para continuar...")
    elif nameEmpty:
        print("El nombre del mozo no puede estar vacio")
        # input("Presione enter para continuar...")
    else:
        nuevo_id = 1
        if len(lista_mozos) > 0:
            nuevo_id = lista_mozos[-1][0] + 1
        
        # Estructura de lista de mozos: [ID, Nombre, [Mesas], Recaudado]

        nuevo_mozo = [nuevo_id, nombre, [], 0]
        lista_mozos.append(nuevo_mozo)
        print(f"Mozo {nombre} fue agregado")
        
        return lista_mozos

def eliminar_mozo(lista_mozos):
    print("[Menu Principal > Mozos > *Eliminar Mozo*]")
    print("")
    id_mozo = input("Ingrese el ID del mozo a eliminar: ")
    isNumber,id_mozo = checkAndConvertToInt(id_mozo)

    if isNumber:
        indice = buscar_indice(lista_mozos, id_mozo)
        if indice != -1:
            if len(lista_mozos[indice][2]) > 0:
                print(f"El mozo {lista_mozos[indice][1]} todavia tiene mesas asignadas.")
            else:
                nombre_eliminado = lista_mozos[indice][1]
                lista_mozos.pop(indice)
                print(f"Mozo {nombre_eliminado} eliminado exitosamente")
                input("Presione enter para continuar...")
        else:
            print("No se encontro un mozo con ese ID")
            input("Presione enter para continuar...")
        
        return lista_mozos
    else:
        if id_mozo == "":
            print("No se ingreso un ID")
            input("Presione enter para continuar...")
        else:
            print("El ID ingresado no es un numero")
            input("Presione enter para continuar...")
            

def agrupar_productos(codigos): #! Verificar si esto puede ser reemplazado por las funciones de bubbleSort
    """Toma una lista de codigos desordenada y la agrupa"""

    productos_unicos = []

    for k in range(len(codigos)):
        esta_en_lista = False
        for i in range(len(productos_unicos)):
            if codigos[k] == productos_unicos[i]:
                esta_en_lista = True
        
        if not esta_en_lista:
            productos_unicos.append(codigos[k])

    resultado = []

    for i in range(len(productos_unicos)):
        cantidad = 0
        for j in range(len(codigos)):
            if productos_unicos[i] == codigos[j]:
                cantidad += 1
        aux = [productos_unicos[i], cantidad]
        resultado.append(aux)

    return resultado


    