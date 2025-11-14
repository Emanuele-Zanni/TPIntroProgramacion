from General.functions import *
from Stock.validations import *

def addProducto(listaProductos):

    #! Validacion para todos los campos

    isProductValid = True
    p1,p2,p3,p4 = True, False, False, False

    while p1:
        clearConsole()
        print("[Menu Principal > Stock > *Agregar Producto*]")
        print("")
        codigo = input("Ingrese Código del producto: ")
        isCodeANumber,codigo = checkAndConvertToInt(codigo)

        if codigo == "x" or codigo == "X":
            input("Cancelando Carga de producto...")
            isProductValid = False
            p1 = False
        elif isCodeANumber:
            isReal = isCodeReal(listaProductos, codigo)
            if isReal:
                print("Código ya existe. Ingrese un nuevo código.")
                input("Presione enter para continuar...")
            else:
                p1 = False
                p2 = True
        else:
            print("El Código debe ser un numero entero. Ingrese un nuevo código.")
            input("Presione enter para continuar...")

    while p2:
        clearConsole()
        print("[Menu Principal > Stock > *Agregar Producto*]")
        print("")
        print(f"Código de producto: {codigo}")
        nombre = input("Ingrese Nombre del producto: ")
        # isNameANumber,_ = checkAndConvertToInt(nombre) #? Esta validacion puede eliminarse/modificarse dependiendo logica del negocio
        if nombre == "x" or nombre == "X":
            input("Cancelando Carga de producto...")
            isProductValid = False
            p2 = False
        elif nombre == "":
            print("El Nombre no puede estar vacio")
            input("Presione enter para continuar...")
        else:
            p2 = False
            p3 = True

    while p3:
        clearConsole()
        print("[Menu Principal > Stock > *Agregar Producto*]")
        print("")
        print(f"Código de producto: {codigo}")
        print(f"Nombre de producto: {nombre}")
        precio = input("Ingrese el precio del producto: ")
        isPrecioValid,precio = checkAndConvertToFloat(precio)
        if precio == "x" or precio == "X":
            input("Cancelando Carga de producto...")
            isProductValid = False
            p3 = False
        elif isPrecioValid:
            if precio <= 0:
                print("El Precio debe ser mayor a 0")
                input("Presione enter para continuar...")
            else:
                p3 = False
                p4 = True
        else:
            print("El Precio debe ser un numero. Ingrese un nuevo precio.")
            input("Presione enter para continuar...")

    while p4:
        clearConsole()
        print("[Menu Principal > Stock > *Agregar Producto*]")
        print("")
        print(f"Código de producto: {codigo}")
        print(f"Nombre de producto: {nombre}")
        print(f"Precio de producto: {precio}$")
        cantidad = input("Ingrese Cantidad en stock: ")
        isCantidadValid,cantidad = checkAndConvertToInt(cantidad)
        if cantidad == "x" or cantidad == "X":
            input("Cancelando Carga de producto...")
            isProductValid = False
            p4 = False
        elif isCantidadValid:
            if cantidad <= 0:
                print("La Cantidad debe ser mayor a 0")
                input("Presione enter para continuar...")
            else:
                p4 = False
        else:
            print("La Cantidad debe ser un numero entero. Ingrese una nueva cantidad.")
            input("Presione enter para continuar...")

    #* Validar Codigo, nombre (no repeat), precio > 0, cantidad=int

    if isProductValid:
        print(f"{nombre} fue agregado.")
        listaProductos.append([codigo, nombre, precio, cantidad])


def editProduct(listaProductos):
    codigo = int(input("Ingrese codigo de producto a editar:"))
    for producto in listaProductos:
        print(producto)
        if producto[0] == codigo:
            print(f"1. Código: {producto[0]}")
            print(f"2. Nombre: {producto[1]}")
            print(f"3. Precio: {producto[2]}")
            print(f"4. Cantidad: {producto[3]}")
            op = int(input("Que desea editar? "))
            #* Validar todos los casos de edicion
            #* Acomodar array con Sort < a >
            if op == 1:
                nuevo = int(input("Ingrese nuevo codigo: "))
                producto[0] = nuevo
            elif op == 2:
                nuevo = input("Ingrese nuevo nombre: ")
                producto[1] = nuevo
            elif op == 3:
                nuevo = float(input("Ingrese nuevo precio: "))
                producto[2] = nuevo
            elif op == 4:
                nuevo = int(input("Ingrese nueva cantidad: "))
                producto[3] = nuevo
            else:
                print("Opción inválida")

    return listaProductos

 
def deleteProduct(listaProductos):
    codigo = int(input("Ingrese codigo de producto a eliminar:"))
    #* Agregar confirmacion para delete
    for producto in listaProductos:
        if producto[0] == codigo:
            listaProductos.remove(producto)
            print(f"Producto con codigo {codigo} fue eliminado.")
        else:
            print(f"Producto con codigo {codigo} no encontrado.")
    return listaProductos

def getProduct(listaProductos, codigo):
    isFound = False
    for producto in listaProductos:
        if producto[0] == codigo and isFound == False:
            # print("Producto encontrado")
            # print(f"El precio de {producto[1]} es {producto[2]}")
            isFound = True
            return producto
        
    if isFound == False:
        print(f"Producto con codigo {codigo} no encontrado.")
        return ""

def printProducts(listaProductos,codigos):
    uniqueProdList = []
    for k in range(len(codigos)):
        if codigos[k] not in uniqueProdList:
            uniqueProdList.append(codigos[k])
            # print(f"Codigo {codigos[k]} guardado en lista")

    results = []
    quantity = 0
    for i in range(len(uniqueProdList)):
        for j in range(len(codigos)):
            if uniqueProdList[i] == codigos[j]:
                # print(uniqueProdList[i])
                quantity += 1

            if j == len(codigos) - 1:
                aux = [uniqueProdList[i], quantity]
                results.append(aux)
                quantity = 0
                # print("UniqueProdList: ",uniqueProdList[i])
                # print(results)  

    # print("Print Products:")
    text = ""
    ordenarBubble(results,"desc")
    for i in range(len(results)):
        item = getProduct(listaProductos, results[i][0]) #* Obtiene el producto de la lista orginal para mostrar el nombre
        # print(f"{item[1]} x {results[i][1]} unidades") 
        text += f"\n- {item[1]} x {results[i][1]} == {item[2] * results[i][1]}$"
    
    return text

def calculateTotal(listaProductos, codigos):
    total = 0
    for i in range(len(codigos)):
        item = getProduct(listaProductos, codigos[i]) #* Obtiene el producto de la lista orginal para mostrar el nombre
        total += item[2] #* Suma el precio del producto al total
    return total

#! Funciones meramente visuales de aca para abajo

#? Sin lineas entre productos
def printTablaProductos(listaProductos):
    """
    Muestra los productos en una tabla con formato de caja,
    y con el contenido centrado dentro de cada celda.
    Columnas: CODIGO | NOMBRE | PRECIO | CANTIDAD
    """
    if not listaProductos:
        print("No hay productos para mostrar.")
        return

    headers = ["CODIGO", "NOMBRE", "PRECIO", "CANTIDAD"]

    # calcular anchos máximos de cada columna (según datos y encabezados)
    col_widths = [
        max(len(str(row[i])) for row in listaProductos + [headers]) + 2
        for i in range(len(headers))
    ]

    # función para formatear una fila centrando el contenido
    def format_row(row):
        celdas = []
        for i, val in enumerate(row):
            text = str(val)
            celdas.append(text.center(col_widths[i]))  # centrado horizontal
        return "│ " + " │ ".join(celdas) + " │"

    # construir bordes de la caja
    total_width = sum(col_widths) + len(headers) * 3 + 1
    top_border    = "┌" + "─" * (total_width - 2) + "┐"
    mid_border    = "├" + "─" * (total_width - 2) + "┤"
    bottom_border = "└" + "─" * (total_width - 2) + "┘"

    # imprimir tabla
    print(top_border)
    print(format_row(headers))
    print(mid_border)
    for prod in listaProductos:
        print(format_row(prod))
    print(bottom_border)

#? Con lineas entre productos
# def printTablaProductos(listaProductos):
#     """
#     Muestra los productos en una tabla con formato de caja,
#     con contenido centrado y líneas internas suaves usando '-'.
#     """
#     if not listaProductos:
#         print("No hay productos para mostrar.")
#         return

#     headers = ["CODIGO", "NOMBRE", "PRECIO", "CANTIDAD"]

#     # calcular anchos máximos de columnas
#     col_widths = [
#         max(len(str(row[i])) for row in listaProductos + [headers]) + 2
#         for i in range(len(headers))
#     ]

#     # total del ancho de la tabla
#     total_width = sum(col_widths) + len(headers) * 3 + 1

#     # bordes principales
#     top_border    = "┌" + "─" * (total_width - 2) + "┐"
#     mid_border    = "├" + "─" * (total_width - 2) + "┤"
#     bottom_border = "└" + "─" * (total_width - 2) + "┘"

#     # separador suave entre filas (usando '-')
#     soft_row_sep  = "│" + "-" * (total_width - 2) + "│"

#     # formatear una fila (centrar el contenido)
#     def format_row(row):
#         celdas = []
#         for i, val in enumerate(row):
#             text = str(val)
#             celdas.append(text.center(col_widths[i]))
#         return "│ " + " │ ".join(celdas) + " │"

#     # imprimir tabla
#     print(top_border)
#     print(format_row(headers))
#     print(mid_border)
#     for idx, prod in enumerate(listaProductos):
#         print(format_row(prod))
#         if idx != len(listaProductos) - 1:  # no imprimir después de la última fila
#             print(soft_row_sep)
#     print(bottom_border)


