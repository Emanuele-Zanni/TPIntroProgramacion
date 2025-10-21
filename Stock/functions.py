def addProducto(listaProductos):
    print("Añadir producto")
    codigo = int(input("Ingrese Código del producto: "))
    nombre = input("Ingrese Nombre del producto: ")
    precio = float(input("IngresePrecio del producto: "))
    cantidad = int(input("Ingrese Cantidad en stock: "))

    #* Validar Codigo, nombre (no repeat), precio > 0, cantidad=int

    
    listaProductos.append([codigo, nombre, precio, cantidad])

    print(f"{nombre} fue agregado.")

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
    for producto in listaProductos:
        if producto[0] == codigo:
            # print(f"El precio de {producto[1]} es {producto[2]}")
            return producto

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


    


        

    