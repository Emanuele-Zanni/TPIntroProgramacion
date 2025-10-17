from functions.stock.funciones import *

def stockMenu(listaProductos):
    on = True
    while on:
        print("""
            1)Ver productos
            2)Añadir productos
            3)Modificar productos
            4)Eliminar productos
            X)Volver al menú principal
            """)

        choice = input("Ingrese una opción: ")

        if choice == "1":
            print("Ver productos")
            print(listaProductos)
        elif choice == "2":
            print("Añadir productos")
            addProducto(listaProductos)
        elif choice == "3":
            print("Modificar producto")
            editProduct(listaProductos)
        elif choice == "4":
            print("Eliminar productos")
            deleteProduct(listaProductos)
        elif choice == "x" or choice == "X":
            print("Volver al menú principal")
            on = False
        else:
            print("Opción inválida")