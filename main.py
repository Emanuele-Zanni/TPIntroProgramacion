app=True
mainMenu=True
mesasMenu=False
mozosMenu=False
stockMenuVar=False
mozos=["mozo1","mozo2","mozo3"]

mesas = [[0,"",False,0],[0,"",True,0],[0,"",True,0],[0,"",True,0],[0,"",True,0]]

productos = [[1,"producto1",100,10],[2,"producto2",200,20],[3,"producto3",300,30],[4,"producto4",400,40]]
#*[mozoAsignado,"Pedidos",Disponible?,MontoAPagar] (num de mesa = posicion en Lista)
#? Mesas manejadas como una Lista de LISTAS

mesasDelivery = [] #* mesas infinitas, mismo type de mesa pero SIN estado "disponible?", y numMesa modificado (un id)
pedidos = [] #* xd? (creo q era solo para cumplir con consigna semana 2)

# from utils.isMesaValid import isMesaValid
from utils.isMozoValid import isMozoValid
# from utils.isMesaEmpty import isMesaEmpty

from functions.mesas.validations import *
from functions.mesas.levantarMesa import levantarMesa
from functions.mesas.cobrarMesa import cobrarMesa
from functions.mesas.anularMesa import anularMesa
from functions.mesas.moverMesa import moverMesa

from functions.stock.stockMenu import *


while app:
    while mainMenu:
        print("""
    1)Mesas (Casi hecho)
    2)Mozos (FALTA)
    3)Stock (WIP)
    4)Cajas (FALTA)
    5)Finalizar Dia (FALTA)
    """)

        choice=input("Ingrese una opcion: ")

        if choice=="1":
            print("Mesas")
            mesasMenu=True
            mainMenu=False
        elif choice=="2":
            print("Mozos")
            mozosMenu=True
            mainMenu=False
        elif choice=="3":
            print("Stock")
            stockMenuVar=True
            mainMenu=False
        elif choice=="4":
            print("Cajas")
        elif choice=="5":
            print("Finalizar Dia")
            mainMenu=False
        else:
            print("Opcion invalida")

    #* Submenu Mesas
    #* 1) Levantar Mesa 
    #* 2) Editar/Acceder Mesa => submenu => Mover Mesa, Cambiar Mozo, Editar Pedidos, Cobrar Mesa, Anular Mesa, Convertir a Delivery
    #* 3) Cobrar Mesa
    #* 4) Anular Mesa

    while mesasMenu:
        print("""
        1)Ver Salon
        2)Ver Delivery
        X)Volver al menu anterior
        """)
    
        choice=input("Ingrese una opcion: ")

        if choice=="1":
            salonMenu=True
            while salonMenu:
                #! Mostrar Mesas Salon + Mesas Delivery automaticamente arriba del Menu????
                # print: 3Mover mesa, 2Cambiar Mozo, 1Editar Pedidos, 5Cobrar Mesa,6 Anular Mesa, 4Convertir a Delivery/Salon
                print("""
            1)Ver Mesas (Mapeado automaticamente arriba del menu??) / Seleccionar Mesa
            2)Levantar Mesa
            3)Editar Mesa (Implicito dentro de "Seleccionar Mesa"?)
            4)Cambiar Mozo (Dentro de "Seleccionar Mesa"?) X
            5)Mover Mesa (Dentro y Fuera de "Seleccionar Mesa")
            6)Convertir Delivery/Salon (Dentro de "Seleccionar Mesa")
            7)Cobrar Mesa (Dentro y Fuera de "Seleccionar Mesa")
            8)Anular Mesa (Dentro y Fuera de "Seleccionar Mesa")
            X)Volver al menu anterior
            """)
                choice=input("Ingrese una opcion: ")
                if choice == "1":
                    print(mesas)
                elif choice == "2":
                    levantarMesa(mesas,mozos)
                elif choice == "3":
                    print("Editar Mesa")
                    print("Mesa especifica DATOS")
                    print("Menu de opciones GLOBALES (opciones previas) + ESPECIFICAS DE MESA")
                elif choice == "4":
                            print("Cambiar Mozo")
                            noErrors=True
                            table = int(input("Seleccione una mesa: "))
                            isValid = isMesaReal(mesas,table)
                            if isValid == False:
                                noErrors=False
                            
                            if noErrors == True:
                                isValid = isMesaEmpty(mesas,table) #! el nombre isValid aca es confuso, pero me facilita el manejo de los IFs
                                if isValid == True:
                                    print("Mesa vacia")
                                    noErrors=False
                            
                            if noErrors == True:
                                waiter = int(input("Seleccione el nuevo mozo a asignar: "))
                                isValid = isMozoValid(mozos,waiter)
                                if isValid == False:
                                    print("Mozo no encontrado")
                                    noErrors=False

                            if noErrors == True:
                                mesas[table-1][0] = waiter
                elif choice == "5": #! Cambiar breaks por whiles o por algo que no me devuelva al menu de "Ver Salon" y "Ver Delivery"
                    moverMesa(mesas)
                elif choice == "6":
                    print("Convertir Delivery/Salon")
                    table = int(input("Seleccione la mesa a convertir: "))
                    print("Funcion para pushear mesa a lista de deliveries, ajustando los datos correspondientes (mozo, precios, etc)")
                elif choice == "7":
                    cobrarMesa(mesas)
                elif choice == "8":
                    anularMesa(mesas)
                elif choice == "X" or choice == "x":
                    print("Volver al menu anterior")
                    salonMenu=False
                else:
                    print("Opcion invalida")
                
        elif choice == "2":
                    print(mesasDelivery)
        elif choice == "X" or choice == "x":
                    print("Volver al menu anterior")
                    mesasMenu=False
                    mainMenu=True
        else:
                    print("Opcion invalida")
         
    while stockMenuVar:
        stockMenu(productos)
        stockMenuVar=False
        mainMenu=True
         