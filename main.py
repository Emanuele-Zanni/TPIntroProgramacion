app=True
mainMenuVar=True
mesasMenuVar=False
mozosMenu=False
stockMenuVar=False
cajasMenuVar=False

#? Mesas manejadas como una Lista de LISTAS
mesas = [[0,[],True,0],[0,[],True,0],[0,[],True,0],[0,[],True,0],[0,[],True,0]] #*[mozoAsignado,"ListaPedidos",Disponible?,TotalMesa] (num de mesa = posicion en Lista)
mesasDelivery = [] #* mesas infinitas, mismo type de mesa pero SIN estado "disponible?", y numMesa modificado (un id)
statsMesas = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
#* MESA PARTICULAR: Veces levantada,mozosAsignados, productos cargados, productos anulados, plata recaudada, plata anulada
#* (array con numero de mozo + cantidad de veces que trabajaron en la mesa)

#* GENERALES: Mesas Movidas, Cambios de Mozo, [Mesas Cobradas, Mesas Anuladas, Productos Anulados, Productos Cargados] (Salon y Delivery),  

mozos=["mozo1","mozo2","mozo3"] 
productos = [[1,"producto1",100,10],[2,"producto2",200,20],[3,"producto3",300,30],[4,"producto4",400,40],[5,"producto5",500,50]]

#******* Importaciones *********
from Mesas.menus import *
from Stock.menus import *
from General.menus import *

from Mesas.functions import *
from Stock.functions import *
from General.functions import * #* hay que ver si es necesario o no

from Mesas.validations import *
from Stock.validations import *
from Mozos.validations import *
#*******************************


while app:
    while mainMenuVar: #* Main Menu
        mainMenu()
        choice=input("Ingrese una opcion: ")

        if choice=="1": #* Mesas
            mesasMenuVar=True
            mainMenuVar=False
        elif choice=="2": #* Mozos
            mozosMenu=True
            mainMenuVar=False
        elif choice=="3": #* Stock
            stockMenuVar=True
            mainMenuVar=False
        elif choice=="4": #* Cajas
            cajasMenuVar
            mainMenuVar=False
        elif choice=="5": #* Finalizar Dia o Config??
            print("Finalizar Dia")
            mainMenuVar=False
        else:
            print("Opcion invalida")

    while mesasMenuVar: #* Mesas Menu
        mesasMenu()
        choice=input("Ingrese una opcion: ")

        if choice=="1":
            salonMenuVar=True
            while salonMenuVar:
                #! Mostrar Mesas Salon + Mesas Delivery automaticamente arriba del Menu????
                # print: 3Mover mesa, 2Cambiar Mozo, 1Editar Pedidos, 5Cobrar Mesa,6 Anular Mesa, 4Convertir a Delivery/Salon
                salonMenu()
                choice=input("Ingrese una opcion: ")

                if choice == "1": #* Ver Mesas
                    print(mesas)
                elif choice == "2": #* Levantar Mesa
                    levantarMesa(mesas,mozos,productos)
                elif choice == "3": #* Seleccionar Mesa
                    printMesa(mesas,productos)
                elif choice == "4": #* Cambiar Mozo
                    cambiarMozo(mesas,mozos)
                elif choice == "5": #* Mover Mesa 
                    #! Cambiar breaks por whiles o por algo que no me devuelva al menu de "Ver Salon" y "Ver Delivery"
                    moverMesa(mesas)
                elif choice == "6": #* Convertir Delivery/Salon
                    print("Convertir Delivery/Salon")
                    table = int(input("Seleccione la mesa a convertir: "))
                    print("Funcion para pushear mesa a lista de deliveries, ajustando los datos correspondientes (mozo, precios, etc)")
                elif choice == "7": #* Cobrar Mesa
                    cobrarMesa(mesas)
                elif choice == "8": #* Anular Mesa
                    anularMesa(mesas)
                elif choice == "X" or choice == "x": #* Volver al menu anterior
                    salonMenuVar=False
                else:
                    print("Opcion invalida")
                
        elif choice == "2":
                    print(mesasDelivery)
        elif choice == "X" or choice == "x":
                    print("Volver al menu anterior")
                    mesasMenuVar=False
                    mainMenuVar=True
        else:
                    print("Opcion invalida")
         
    while stockMenuVar:
        stockMenu(productos)
        stockMenuVar=False
        mainMenuVar=True
         