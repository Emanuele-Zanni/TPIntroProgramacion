from Stock.functions import *
from General.functions import *

def stockMenu(listaProductos):
    on = True
    while on:
        clearConsole()
        print("""[Menu Principal > Stock]
              
#########[ Menu Stock ]#########
1)Ver productos
2)Añadir productos
3)Modificar productos
4)Eliminar productos
X)Volver al menú principal
#################################
""")

        choice = input("Ingrese una opción: ")

        if choice == "1":
            clearConsole()
            # print("Ver productos")
            # print(listaProductos)
            printTablaProductos(listaProductos)
            input("Presione enter para continuar...")
        elif choice == "2":
            # clearConsole()
            addProducto(listaProductos)
        elif choice == "3":
            clearConsole()
            print("Modificar producto")
            editProduct(listaProductos)
            input("Presione enter para continuar...")
        elif choice == "4":
            clearConsole()
            print("Eliminar productos")
            deleteProduct(listaProductos)
            input("Presione enter para continuar...")
        elif choice == "x" or choice == "X":
            print("Volver al menú principal")
            on = False
        else:
            input("Opción inválida, presione enter para continuar...")