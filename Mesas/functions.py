from Stock.functions import *
from Mozos.functions import *
from General.functions import *
from Mozos.validations import *
from Mesas.validations import *
from Mesas.menus import *

def levantarMesa(listaMesas,listaMozos,listaProductos,stats,prodsTutorial):
            pedidosMesa = []
            mesaValida=False
            mozoValido=False
            isNumber=False

            #? Agregar posibilidad de cancelar la operacion en cualquier momento ingresando "X" o "x"
            #* Validar Mesa
            while mesaValida==False:
                clearConsole()
                print("[Menu Principal > Menu Mesas > Menu Salon > *Levantar Mesa*]\n")
                printMesasLibres(listaMesas)
                numMesa = input("• Ingrese el numero de mesa: ")
                isNumber,numMesa = checkAndConvertToInt(numMesa) 

                if isNumber:
                    mesaValida,error = isMesaValid(listaMesas,numMesa)
                    if mesaValida == False:
                        print(f"[ERROR] {error}")
                        input("Presione enter para continuar...")
                else:
                    print("El numero de mesa debe ser un numero entero")
                    input("Presione enter para continuar...")

            #* Validar Mozo
            while mozoValido==False:
                clearConsole()
                print("[Menu Principal > Menu Mesas > Menu Salon > *Levantar Mesa*]\n")
                print(f"Mesa Numero {numMesa}")
                numMozo = input("• Ingrese el numero de mozo: ")
                isNumber,numMozo = checkAndConvertToInt(numMozo)

                if isNumber:
                    mozoValido = isMozoValid(listaMozos,numMozo)
                    if mozoValido == False:
                        # print(f"Mozo {numMozo} no encontrado")
                        input("Presione enter para continuar...")
                else:
                    print("El numero de mozo debe ser un numero entero")
                    input("Presione enter para continuar...")

            #* Cargar productos (Probablemente haya que reworkearlo para mejorar UX, un submenu probablemente)
            # if mesaValida and mozoValido:
            cantidadProductos = 0
            cargaProductos = True
            if prodsTutorial:
                printCargaProdsTutorial()
            while cargaProductos:
                clearConsole()
                print("[Menu Principal > Menu Mesas > Menu Salon > *Levantar Mesa*]\n")
                print(f"Mesa numero {numMesa}")
                print(f"Mozo numero: {numMozo}")
                # print(f"Productos de la mesa:\n{pedidosMesa}") #! Esto reemplazarlo por un print de la lista de pedidos, la funcion ya hecha
                text=printProducts(listaProductos,pedidosMesa)
                print(f"[Productos de la mesa]:{text}\n")
                codigo = input("• Ingrese el codigo del item a cargar: ")

                if codigo == "x" or codigo == "X":
                    print("Mesa Levantada exitosamente!")
                    input("Presione enter para continuar...")
                    cargaProductos = False
                elif codigo == "?":
                    printCargaProdsTutorial()
                else:
                    isNumber,codigo = checkAndConvertToInt(codigo)

                    if isNumber:
                        producto = getProduct(listaProductos,codigo)
                        if producto != "":
                            pedidosMesa.append(producto[0])
                            cantidadProductos += 1
                        else:
                            # print("Codigo de producto no encontrado")
                            input("Presione enter para continuar...")
                    else:
                        print("El codigo del item debe ser un numero entero")
                        input("Presione enter para continuar...")
                    # total += producto[2]

            total = calculateTotal(listaProductos,pedidosMesa)
                
            
            ordenarBubble(pedidosMesa,"desc")
            #? usar listaMozos[numMozo-1] para guardar el nombre del mozo en vez del num
            listaMesas[numMesa-1] = [numMozo,pedidosMesa,False,total] #* Mesa levantada en listaMesas
            indice_mozo = buscar_indice(listaMozos, numMozo)
            if indice_mozo != -1:
                listaMozos[indice_mozo][2].append(numMesa)
            #* Actualizar Stats de Mesa particular
            print(numMesa-1)
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
        
def anularMesa(listaMesas, listaMozos):
    print("Anular Mesa")
    isValid=True
    table = input("Seleccione la mesa a anular: ")
    isNumber,table = checkAndConvertToInt(table)

    if isNumber:
        isValid = isMesaReal(listaMesas,table)
        if isValid == False:
            print("Mesa no encontrada")
                                
        if isValid:
            isEmpty = isMesaEmpty(listaMesas,table)
            if isEmpty:
                isValid=False
                                    
        if isValid:
            listaMesas[table-1] = [0,"",True,0]
            id_mozo_asignado = listaMesas[table-1][0] # Obtiene el ID del mozo de esa mesa
            if id_mozo_asignado != 0:
                indice_mozo = buscar_indice(listaMozos, id_mozo_asignado)
                if indice_mozo != -1:
                    # mozo[2] es la lista de mesas
                    lista_mesas_mozo = listaMozos[indice_mozo][2]
                    
                    # Buscar la mesa para eliminarla de la lista del mozo
                    indice_mesa_en_mozo = -1
                    j = 0
                    while j < len(lista_mesas_mozo) and indice_mesa_en_mozo == -1:
                        if lista_mesas_mozo[j] == table: # 'table' es el numMesa (ej: 1, 2, 3)
                            indice_mesa_en_mozo = j
                        j += 1
                        
                    if indice_mesa_en_mozo != -1:
                        lista_mesas_mozo.pop(indice_mesa_en_mozo)   
            print("Mesa anulada exitosamente")

        elif isValid == False:
            print("Error al anular mesa")
    else:
        print("El numero de mesa debe ser un numero entero")
        input("Presione enter para continuar...")



def cobrarMesa(listaMesas, listaMozos, table,e,td,tc,ch,d):
    isValid=True
    # table = int(input("Seleccione la mesa a cobrar: "))

    isValid = isMesaReal(listaMesas,table)
    if isValid == False:
        print("Mesa no encontrada")
                            
    if isValid:
        isEmpty = isMesaEmpty(listaMesas,table)
        if isEmpty:
            isValid=False
                                
    if isValid:
        """Agregado para los mozos"""
        id_mozo_asignado = listaMesas[table-1][0] # Obtiene el ID del mozo de esa mesa
        if id_mozo_asignado != 0:
            indice_mozo = buscar_indice(listaMozos, id_mozo_asignado)
            if indice_mozo != -1:
                # mozo[2] es la lista de mesas
                lista_mesas_mozo = listaMozos[indice_mozo][2]
                
                # Buscar la mesa para eliminarla de la lista del mozo
                indice_mesa_en_mozo = -1
                j = 0
                while j < len(lista_mesas_mozo) and indice_mesa_en_mozo == -1:
                    if lista_mesas_mozo[j] == table: # 'table' es el numMesa (ej: 1, 2, 3)
                        indice_mesa_en_mozo = j
                    j += 1
                    
                if indice_mesa_en_mozo != -1:
                    lista_mesas_mozo.pop(indice_mesa_en_mozo)  

        hasPaid = False
        while hasPaid == False:
            metodoPagoMenu()
            choice = input("Seleccione el metodo de pago: ")
            
            total = listaMesas[table-1][3]
            print(f"Total: {total}")

            if choice == "1":
                print("Efectivo")
                e += total
                hasPaid = True
            elif choice == "2":
                print("debito")
                td += total
                hasPaid = True
            elif choice == "3":
                print("credito")
                tc += total
                hasPaid = True
            elif choice == "4":
                print("cheque")
                ch += total
                hasPaid = True
            elif choice == "5":
                print("deuda")
                d += total
                hasPaid = True
            elif choice == "x" or choice == "X":
                print("cancelar")
                isValid = False
                hasPaid = True
            else:
                print("Opcion no valida")
                input("Presione enter para continuar...")
        

        if isValid and hasPaid:
            print(f"Mesa {table} cobrada exitosamente (Total = {listaMesas[table-1][3]}$)")
            resetMesa(listaMesas,table)

        return e,td,tc,ch,d
    elif isValid == False:
        print("Error al cobrar mesa")

def resetMesa(listaMesas,table):
    listaMesas[table-1] = [0,[],True,0]

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

def printCargaProdsTutorial():
    clearConsole()
    print("Controles de la Carga de productos:\n")
    print("Ingrese 'x' para finalizar la carga de productos")
    print("Ingrese '-' antes del codigo de producto para eliminar el producto (ejemplo: -2 = Resta 1 producto de codigo 2)")
    print("Ingrese '*' despues del codigo de producto, seguido por un numero entero, para agregar esa cantidad de productos (ejemplo: 2*4 = Agrega 4 productos de codigo 2)")
    print("Puede tambien combinar simbolos de la siguiente manera: -2*4 = Resta 4 productos de codigo 2 de ser posible")
    print("\nIngrese '?' para volver a visualizar este tutorial")
    input("\nPresione cualquier tecla para cerrar el tutorial...")

def printMesa(listaMesas, listaProductos, numMesa, showAllProducts=False, maxShowProducts=3):
    if not isMesaReal(listaMesas, numMesa):
        return f"Error: Mesa {numMesa} no encontrada"

    mesa = listaMesas[numMesa - 1]
    inner = BOX_WIDTH - 2
    titulo = f"######### [ Mesa {numMesa} ] #########"

    top     = " " + "-" * (BOX_WIDTH - 2)
    sep_mid = _box_line("-" * inner, inner)
    bottom  = "|" + "_" * (BOX_WIDTH - 2) + "|"

    # ──────────────── CASO MESA VACÍA ────────────────
    if mesa[2] == True:  # disponible/vacía
        ALTURA = 7  # cantidad total de líneas dentro del cuadro
        lineas = [top]
        lineas.append(_box_line(titulo.center(inner), inner))
        lineas.append(sep_mid)
        # cuántas líneas agregar antes y después del texto
        vacias_arriba = (ALTURA - 3) // 2  # deja espacio arriba
        vacias_abajo = ALTURA - 3 - vacias_arriba
        for _ in range(vacias_arriba):
            lineas.append(_box_line("", inner))
        lineas.append(_box_line("MESA VACIA".center(inner), inner))
        for _ in range(vacias_abajo):
            lineas.append(_box_line("", inner))
        lineas.append(bottom)
        lineas.append("")  # salto final opcional
        return "\n".join(lineas)

    # costo total (si no lo tenés calculado, podés recalcularlo aquí)
    costo_total = mesa[3]

    lineas = []
    lineas.append(top)
    lineas.append(_box_line(titulo.center(inner), inner))
    lineas.append(sep_mid)
    lineas.append(_box_line(f"• Mozo: {mesa[0]}", inner))
    # lineas.append(_box_line(f"• Mesa disponible?: {mesa[2]}", inner))

    # Productos (múltiples líneas con precio a la derecha)
    lineas.append(_box_line("• Productos en mesa:", inner))

    codigos = mesa[1]
    prod_pairs = construir_lineas_productos_lr(listaProductos, codigos)

    if not prod_pairs:
        lineas.append(_box_line("  (sin productos)", inner))
    else:
        if showAllProducts == False:
            mostrar = prod_pairs[:maxShowProducts]
            restantes = len(prod_pairs) - len(mostrar)
            for left, price in mostrar:
                lineas.append(_box_line_lr(left, price, inner, min_gap=1))
            if restantes > 0:
                # esta línea es informativa, sin precio a la derecha
                lineas.append(_box_line(f" y {restantes} productos más...", inner))
        else:
            for left, price in prod_pairs:
                lineas.append(_box_line_lr(left, price, inner, min_gap=1))

    # Costo total (precio pegado a la derecha)
    lineas.append(sep_mid)
    lineas.append(_box_line_lr("• Total:", f"{costo_total}$", inner, min_gap=1))

    lineas.append(bottom)
    lineas.append("")  # salto final opcional

    return "\n".join(lineas)


def printMesas(listaMesas, listaProductos):
    clearConsole()
    bloques = [
        printMesa(listaMesas, listaProductos, i)
        for i in range(1, len(listaMesas) + 1)
    ]
    render_side_by_side(bloques, cols=4, padding=6)

def printMesasActivas(listaMesas):
    mesasActivas = []
    for i in range(len(listaMesas)):
        if listaMesas[i][2] == False:
            mesasActivas.append(i+1)
            
    text = f"Mesas Activas: {mesasActivas}"
    return mesasActivas,text


def printMesasLibres(listaMesas):
    mesasLibres = []
    for i in range(len(listaMesas)):
        if listaMesas[i][2] == True:
            mesasLibres.append(i+1)
    print(f"Mesas Disponibles: {mesasLibres}")
    


def printMozosMesa(stats):
    text = ""
    for i in range(len(stats)):
        text += f"\nMozo {stats[i][0]} x {stats[i][1]}"

    return text

def editMesasQuantity(listaMesas,statsMesas):
    mode,tableValue = tableSettingsMenu(listaMesas)
    # print(tableValue)

    newListaMesas = []
    newStatsMesas = []
    error = False

    if mode == 1:
        for i in range(tableValue):
            listaMesas.append([0,[],True,0])
            statsMesas.append([0,[],0])
    elif mode == -1:
        # print("Ingresando en caso de ELIMINAR MESAS")
        newListaMesas = listaMesas.copy()
        newStatsMesas = statsMesas.copy()
        for i in range(tableValue):

            if listaMesas[len(listaMesas)-1-i][2] == False:
                error = True

            if error == False:
                newListaMesas.pop()
                newStatsMesas.pop()

    elif mode == 0:
        print(f"No se realizaron cambios, la cantidad de mesas actual ya es {len(listaMesas)}")
        input("Presione cualquier tecla para continuar...")
    elif mode == 2:
        print("Error general en la funcion")
    elif mode == -2:
        print(f"No se puede eliminar mas mesas de las existentes")
        input("Presione cualquier tecla para continuar...")
    elif mode == 4:
        error = ""
        print("No se puede ingresar un valor vacio")
    elif mode == 5:
        error = ""
        print("El valor ingresado no es un numero")


    if error == False:
            if mode == -1:
                listaMesas = newListaMesas
                statsMesas = newStatsMesas
            print("Cambio realizado con exito")
            input("Presione cualquier tecla para continuar...")
            return listaMesas, statsMesas
    elif error:
            print("Error, las mesas a eliminar deben estar vacias")
            input("Presione cualquier tecla para continuar...")
            return listaMesas, statsMesas
    else:
        input("Presione cualquier tecla para continuar...")
        return listaMesas, statsMesas




#! Este conjunto de Funciones tienen fines meramente esteticos y se encargan de formatear el texto y datos para una mejor visualizacion
#* Esta variable determina el ancho de los printMesa()
BOX_WIDTH = 32 # BOX_WIDTH = 41

#* Esta funcion se encarga de ajustar el texto a la anchura de la caja
#? Utiliza el metodo ljust() de Python para alinear el texto a la izquierda y utiliza operaciones de Slicing ([:inner])
def _fit(texto, inner):
    if len(texto) <= inner:
        return texto.ljust(inner)
    if inner <= 1:
        return "…"[:inner]
    return texto[:inner-1] + "…"

#* Esta funcion se encarga de construir una linea junto con sus barras verticales "|" y acomoda dentro suyo el texto (inner)
def _box_line(texto, inner):
    return f"|{_fit(texto, inner)}|"

#* Esta funcion hace lo mismo que _box_line() pero divide su ancho en 2 columnas para poder lograr la separacion entre el nombre del producto y su precio
def _box_line_lr(left, right, inner, min_gap=1, padding_right=2):
    right = str(right)
    espacio_left = inner - len(right) - min_gap - padding_right
    if espacio_left < 0:
        right = _fit(right, inner)
        return f"|{right}|"
    left_fit = _fit(left, espacio_left)
    return f"|{left_fit}{' ' * min_gap}{right}{' ' * padding_right}|"

#* Se encarga de construir las lineas de los productos, separando el nombre del producto de su precio para poder utilizarlo en conjunto con _box_line_lr()
def construir_lineas_productos_lr(listaProductos, codigos):
    conteo = {}
    for c in codigos:
        conteo[c] = conteo.get(c, 0) + 1

    lineas = []
    for codigo, cant in conteo.items():
        item = getProduct(listaProductos, codigo)  # item[1]=nombre, item[2]=precio_unit
        nombre = str(item[1])
        subtotal = item[2] * cant
        left = f"- {nombre} x {cant}"
        price = f"{subtotal}$"
        lineas.append((left, price))
    return lineas

#* Se encarga de imprimir los bloques de texto de las mesas uno al lado del otro, toma como parametros una lista de bloques de texto, la cantidad de columnas y el padding entre ellas
def render_side_by_side(bloques, cols=4, padding=4):
    if not bloques:
        return

    for start in range(0, len(bloques), cols):
        grupo = bloques[start:start + cols]

        # 1) Separar cada bloque del grupo en líneas
        cols_lines = [b.rstrip("\n").splitlines() for b in grupo]

        # 2) Igualar alturas (rellenar con líneas vacías)
        max_alto = max((len(c) for c in cols_lines), default=0)
        for c in cols_lines:
            c += [""] * (max_alto - len(c))

        # 3) Calcular anchos por columna (para alinear)
        anchos = [max((len(linea) for linea in c), default=0) for c in cols_lines]

        # 4) Imprimir línea por línea la fila actual (las 'cols' columnas)
        for fila in range(max_alto):
            partes = []
            for col_idx, c in enumerate(cols_lines):
                partes.append(c[fila].ljust(anchos[col_idx] + padding))
            print("".join(partes))

        # 5) Línea en blanco opcional entre filas de columnas
        print()
#!-------------------------------------------------------------------------------------------