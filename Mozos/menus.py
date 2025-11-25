from Mozos.functions import *
from General.functions import *

def menu_mozos(lista_mozos,mozoStats):
    on = True
    while on:
        clearConsole()
        print("""[Menu Principal > Mozos]
              
#######[ MENU MOZOS ]#######
1) Ver Mozos
2) Agregar Mozo
3) Eliminar Mozo
X) Volver al menú principal
#################################
""")
        choice = input("Ingrese una opcion: ")

        if choice == "1":
            clearConsole()
            mostrar_mozos(lista_mozos) 
            input("\nPresione enter para continuar...")
        elif choice == "2":
            clearConsole()
            agregar_mozo(lista_mozos,mozoStats)
            input("Presione enter para continuar...")
        elif choice == "3":
            clearConsole()
            eliminar_mozo(lista_mozos,mozoStats)
        elif choice.lower() == "x":
            on = False
        else:
            print("Opción inválida")
            input("\nPresione enter para continuar...")
