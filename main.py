app=True
mainMenuVar=True
mesasMenuVar=False
mozosMenuVar=False
stockMenuVar=False
cajasMenuVar=False


#? Mesas manejadas como una Lista de LISTAS
mesas = [[0,[],True,0],[0,[],True,0],[0,[],True,0],[0,[],True,0],[0,[],True,0]] #*[mozoAsignado,"ListaPedidos",Disponible?,TotalMesa] (num de mesa = posicion en Lista)
mesasDelivery = [] #* mesas infinitas, mismo type de mesa pero SIN estado "disponible?", y numMesa modificado (un id)
# statsMesas = [[0,[[0,0]],0],[0,[[0,0]],0],[0,[[0,0]],0],[0,[[0,0]],0],[0,[[0,0]],0]]
statsMesas = [[0,[],0]]
#* MESA PARTICULAR: Veces levantada,mozosAsignados, productos cargados, productos anulados, plata recaudada, plata anulada
#* (array con numero de mozo + cantidad de veces que trabajaron en la mesa)

#* GENERALES: Mesas Movidas, Cambios de Mozo, [Mesas Cobradas, Mesas Anuladas, Productos Anulados, Productos Cargados] (Salon y Delivery),  

# Estructura de mozos: [ID, Nombre, [Lista de Mesas Asignadas], Total Recaudado]
mozos=[
    [1, "Mozo A", [], 0],
    [2, "Mozo B", [], 0],
    [3, "Mozo C", [], 0]
]
productos = [[1,"producto1",100,10],[2,"producto2",200,20],[3,"producto3",300,30],[4,"producto4",400,40],[5,"producto5",500,50]]

#******* Importaciones *********
from Mesas.menus import *
from Stock.menus import *
from General.menus import * 

from Mesas.functions import *
from Stock.functions import *
from General.functions import * #* hay que ver si es necesario o no
from Mozos.menus import *

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
            menu_mozos(mozos)
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
            clear_except_last(3)

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
                    #! Esto antes era solo "print(mesas)". Confirmar si se quiere una logica con while o pasa al Menu directamente
                    var="a"
                    while var != "":
                        limpiarConsola()
                        print(mesas)
                        var=input("Presione enter para volver al menu anterior")
                elif choice == "2": #* Levantar Mesa
                    levantarMesa(mesas,mozos,productos,statsMesas)
                elif choice == "3": #* Seleccionar Mesa
                    printMesa(mesas,productos)
                elif choice == "4": #* Cambiar Mozo
                    cambiarMozo(mesas,mozos)
                elif choice == "5": #* Mover Mesa 
                    moverMesa(mesas)
                elif choice == "6": #* Convertir Delivery/Salon
                    print("Convertir Delivery/Salon")
                    table = int(input("Seleccione la mesa a convertir: "))
                    print("Funcion para pushear mesa a lista de deliveries, ajustando los datos correspondientes (mozo, precios, etc)")
                elif choice == "7": #* Cobrar Mesa
                    cobrarMesa(mesas,mozos)
                elif choice == "8": #* Anular Mesa
                    anularMesa(mesas,mozos)
                elif choice == "X" or choice == "x": #* Volver al menu anterior
                    salonMenuVar=False
                else:
                    print("Opcion invalida")
                
        elif choice == "2":
                    print(mesasDelivery)
        elif choice == "3":
            var="a"
            while var != "":
                print("Estadisticas de Mesas")
                printMesaStats(statsMesas)
                var=input("Presione enter para volver al menu anterior") 
        elif choice == "4":
                    print("Configuracion de Mesas???")
        elif choice == "X" or choice == "x":
                    print("Volver al menu anterior")
                    mesasMenuVar=False
                    mainMenuVar=True
                    clear_except_last(3)
        else:
                    print("Opcion invalida")
                    clear_except_last(3)
         
    while stockMenuVar:
        stockMenu(productos)
        stockMenuVar=False
        mainMenuVar=True
         