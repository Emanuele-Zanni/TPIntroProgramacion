productos = []
def menu():
    """"Se muestra el menu"""
    print("MENU DE STOCK")
    print("1- Ver productos")
    print("2- Añadir productos")
    print("3- Editar productos")
    print("4- Eliminar productos")
    print("5- Salir")

def ver_productos():
    print("Lista de productos")
    if not productos:
        print("No hay productos")
    else:
         for i in range(len(productos)):
             producto = productos[i]
             print(f"{i}. {producto[0]} - Precio: ${producto[1]} - Stock: {producto[2]}")

def seleccionar_producto():
    ver_productos()
    if not productos:
        return None
    
    indice_valido = False
    indice_seleccionado = -1

    # Bucle mientras indice_valido sea False
    while not indice_valido:
        indice = int(input("Ingresa el numero del producto: "))
        if 0 <= indice < len(productos):
            indice_seleccionado = indice
            indice_valido = True
        else:
            print("Este numero no esta en la lista")
    return indice_seleccionado

def add_producto():
    print("Añadir producto")
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad en stock: "))
    
    productos.append([nombre, precio, cantidad])

    print(f"{nombre} fue agregado.")

def editar_producto():
    print("Editar producto")
    indice = seleccionar_producto()
    if indice is not None:
        producto_actual = productos[indice]
        print(f"Editando {producto_actual[0]}")
        
        # Se piden nuevos valores

        nuevo_nombre = input(f"Nuevo nombre ({producto_actual[0]}): ")
        nuevo_precio = float(input(f"Nuevo precio (${producto_actual[1]}): "))
        nueva_cantidad = int(input(f"Nueva cantidad ({producto_actual[2]}): "))

        if nuevo_nombre :
            productos[indice][0] = nuevo_nombre
        if nuevo_precio :
            productos[indice][1] = nuevo_precio
        if nueva_cantidad :
            productos[indice][2] = nueva_cantidad
        
        print("Producto actualizado")

def eliminar_producto():
    print("Eliminar producto")
    indice = seleccionar_producto()

    if indice is not None:
        producto_eliminado = productos.pop(indice)
        print (f"El producto {producto_eliminado[0]} fue eliminado")

def main():
    salir = False
    while not salir:
        menu()
        opcion = int(input("Elige una opcion: "))

        if opcion == 1:
            ver_productos()
        elif opcion == 2:
            add_producto()
        elif opcion == 3:
            editar_producto()
        elif opcion == 4:
            eliminar_producto()
        elif opcion == 5:
            print ("Chau")
            salir = True
        else:
            print("Opcion no valida")

main()
print(productos)