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
    codigo = input("Ingrese codigo de producto a editar:")
    for producto in listaProductos:
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
            print(f"El precio de {producto[1]} es {producto[2]}")
            return producto
        else:
            return print(f"Producto con codigo {codigo} no encontrado.")
        