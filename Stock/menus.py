from Stock.functions import *
from General.functions import *

def stockMenu(listaProductos):
    on = True
    while on:
        clearConsole()
        print("""
1)Ver productos
2)Añadir productos
3)Modificar productos
4)Eliminar productos
X)Volver al menú principal
""")

        choice = input("Ingrese una opción: ")

        if choice == "1":
            clearConsole()
            print("Ver productos")
            print(listaProductos)
        elif choice == "2":
            clearConsole()
            print("Añadir productos")
            addProducto(listaProductos)
        elif choice == "3":
            clearConsole()
            print("Modificar producto")
            editProduct(listaProductos)
        elif choice == "4":
            clearConsole()
            print("Eliminar productos")
            deleteProduct(listaProductos)
        elif choice == "x" or choice == "X":
            print("Volver al menú principal")
            on = False
        else:
            input("Opción inválida, presione enter para continuar...")