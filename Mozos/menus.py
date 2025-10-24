from Mozos.functions import *
from General.functions import limpiarConsola

def menu_mozos(lista_mozos):
    on = True
    while on:
        # limpiarConsola()
        print("""
#######[ MENU MOZOS ]#######
1) Ver Mozos
2) Agregar Mozo
3) Eliminar Mozo
X) Volver al menú principal
#################################
""")
        choice = input("Ingrese una opcion: ")

        if choice == "1":

            mostrar_mozos(lista_mozos) 
            input("\nPresione enter para continuar...")
        elif choice == "2":

            agregar_mozo(lista_mozos)
            input("\nPresione enter para continuar...")
        elif choice == "3":

            eliminar_mozo(lista_mozos)
            input("\nPresione enter para continuar...")
        elif choice.lower() == "x":
            on = False
        else:
            print("Opción inválida")
            input("\nPresione enter para continuar...")
