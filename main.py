#* Variables de APP
app=True
#? Variables de Menu
mainMenuVar=True
mesasMenuVar=False 
mozosMenuVar=False
stockMenuVar=False
cajasMenuVar=False
#? Variables de Caja
ec=0 #* Efectivo Caja
tdc=0 #* Tarjeta Debito Caja
tcc=0  #* Tarjeta Credito Caja
cc=0 #* Cheques Caja
dc=0 #* Deuda Caja
#? Variables de Mesas

#? Variables de Stock

#? Variables de Mozos




#? Mesas manejadas como una Lista de LISTAS
mesas = [[0,[],True,0],[0,[],True,0],[0,[],True,0],[0,[],True,0],[0,[],True,0]] #*[mozoAsignado,"ListaPedidos",Disponible?,TotalMesa] (num de mesa = posicion en Lista)
mesasDelivery = [] #* mesas infinitas, mismo type de mesa pero SIN estado "disponible?", y numMesa modificado (un id)
# statsMesas = [[0,[[0,0]],0],[0,[[0,0]],0],[0,[[0,0]],0],[0,[[0,0]],0],[0,[[0,0]],0]]
statsMesas = [[0,[],0],[0,[],0],[0,[],0],[0,[],0],[0,[],0]]
#* MESA PARTICULAR: Veces levantada,mozosAsignados, productos cargados, productos anulados, plata recaudada, plata anulada
#* (array con numero de mozo + cantidad de veces que trabajaron en la mesa)

#* GENERALES: Mesas Movidas, Cambios de Mozo, [Mesas Cobradas, Mesas Anuladas, Productos Anulados, Productos Cargados] (Salon y Delivery),  

#? Estructura de mozos: [ID, Nombre, [Lista de Mesas Asignadas], Total Recaudado]
mozos=[
    [1, "Mozo A", [], 0],
    [2, "Mozo B", [], 0],
    [3, "Mozo C", [], 0]
]
# Estadistica de los mozos: [Veces levantadas, Dinero recaudado]
mozoStats = [[0,0,0],[0,0,0],[0,0,0]] 

productos = [[1,"producto1",100,10],[2,"producto2",200,20],[3,"producto3",300,30],[4,"producto4",400,40],[5,"producto5",500,50]]

#******* Importaciones *********
from Mesas.menus import *
from Stock.menus import *
from General.menus import * 
from Mozos.menus import *
from Caja.menus import *

from Mesas.functions import *
from Stock.functions import *
from General.functions import * #* hay que ver si es necesario o no
from Caja.functions import *

from Mesas.validations import *
from Stock.validations import *
from Mozos.validations import *
#*******************************


while app:
    while mainMenuVar: #* Main Menu
        clearConsole()
        mainMenu()
        choice=input("Ingrese una opcion: ")

        if choice=="1": #* Ver Mesas
            mesasMenuVar=True
            mainMenuVar=False
        elif choice=="2": #* Ver Mozos
            menu_mozos(mozos)
        elif choice=="3": #* Ver Stock
            stockMenuVar=True
            mainMenuVar=False
        elif choice=="4": #* Ver Cajas
            cajasMenuVar=True
            mainMenuVar=False
        elif choice=="5": #* Finalizar Dia o Config??
            print("Finalizar Dia")
            mainMenuVar=False
        else:
            print("Opcion invalida")
            input("Presione enter para volver al menu anterior...")
            # clear_except_last(3)

    while mesasMenuVar: #* Mesas Menu
        clearConsole()
        mesasMenu()
        choice=input("Ingrese una opcion: ")

        if choice=="1":
            salonMenuVar=True
            while salonMenuVar: 
                #! Mostrar Mesas Salon + Mesas Delivery automaticamente arriba del Menu????
                # print: 3Mover mesa, 2Cambiar Mozo, 1Editar Pedidos, 5Cobrar Mesa,6 Anular Mesa, 4Convertir a Delivery/Salon
                clearConsole()
                salonMenu()
                choice=input("Ingrese una opcion: ")

                if choice == "1": #* Ver Mesas
                    #! Esto antes era solo "print(mesas)". Confirmar si se quiere una logica con while o pasa al Menu directamente
                    # var="a"
                    # while var != "":
                        # limpiarConsola()
                        printMesas(mesas,productos)

                        var=input("Presione enter para volver al menu anterior")
                elif choice == "2": #* Levantar Mesa
                    levantarMesa(mesas,mozos,productos,statsMesas)
                elif choice == "3": #* Seleccionar Mesa
                    #! Mandar todo esto a una funcion "seleccionarMesa()" y 
                    clearConsole()
                    isEmpty=False
                    isReal=False
                    #* Manejar casos en donde la mesa no existe o no esta levantada
                    #! Mesa vacia se muestra con todo en 0, debe mostrarse como "Mesa Vacia"??? (Manejado indirectamente)
                    #! Mesa no existente rompe el programa, manejar ese caso
                    # mesasOcupadas = []
                    # for i in range(len(mesas)):
                    #     if mesas[i][2] == False:
                    #         mesasOcupadas.append(i+1)
                    # print(f"Mesas Activas: {mesasOcupadas}")
                    printMesasOcupadas(mesas)
                    numMesa = input("Ingrese la mesa a visualizar:")
                    isNumber,numMesa = checkAndConvertToInt(numMesa)
                    # numMesa = valor
                    # print(numMesa.isdigit())

                    if isNumber:
                        isReal = isMesaReal(mesas,numMesa)
                    # else:
                    #     isReal=False

                    if isReal: 
                        isEmpty = isMesaEmpty(mesas,numMesa)

                    if isReal and not isEmpty:
                        mesa = printMesa(mesas,productos,numMesa,True)
                        if isReal:
                            seleccionarMesaVar=True
                            while seleccionarMesaVar:
                                print(mesa)
                                seleccionarMesaMenu(numMesa)
                                choice = input("Ingrese una opcion: ")
                                if choice == "1": #* Cobrar Mesa

                                    #? [mozoStats]: Sumar +1 a la stat "veces levantada"
                                    numMozo = mesas[numMesa-1][0]   #* Obtiene el numero de mozo correspondiente a la mesa
                                    mozoStats[numMozo-1][0] += 1 #* Suma +1 a la Stat "veces levantada" de ese mozo
                                    
                                    #? [mozoStats]: Suma el costo total de la mesa a la stat "dinero recaudado"
                                    numMozo = mesas[numMesa-1][0]           # Dinero recaudado
                                    mozoStats[numMozo-1][1] += mesas[numMesa-1][3]  
                                          
                                    ec,tdc,tcc,cc,dc=cobrarMesa(mesas,mozos,numMesa,ec,tdc,tcc,cc,dc)
                                                

                                    input("Presione enter para volver al menu anterior...")
                                    seleccionarMesaVar=False
                                elif choice == "2": #* Anular Mesa
                                    anularMesa(mesas,mozos)
                                elif choice == "3": #* Cambiar Mozo
                                    cambiarMozo(mesas,mozos)
                                    #* Variable de cambio de mozo +1?
                                elif choice == "4": #* Mover Mesa
                                    moverMesa(mesas)
                                elif choice == "5": #* Convertir Delivery/Salon
                                    print("Convertir Delivery/Salon")
                                    table = int(input("Seleccione la mesa a convertir: "))
                                    print("Funcion para pushear mesa a lista de deliveries, ajustando los datos correspondientes (mozo, precios, ec)")
                                elif choice == "x" or choice == "X": #* Volver al menu anterior
                                    isReal=False
                                    seleccionarMesaVar=False
                                else:
                                    print("Opcion invalida")
                                    input("Presione enter para volver al menu anterior...")
                    elif isEmpty:
                        print(f"La Mesa {numMesa} esta vacia")
                        input("Presione enter para volver al menu anterior...")
                    elif isNumber == False:
                        print(f"La opcion ingresada debe ser un numero entero")
                        input("Presione enter para volver al menu anterior...")
                    else:
                        print(f"La Mesa {numMesa} no existe")
                        input("Presione enter para volver al menu anterior...")


                # elif choice == "4": #* Cambiar Mozo
                #     cambiarMozo(mesas,mozos)
                # elif choice == "5": #* Mover Mesa 
                #     moverMesa(mesas)
                # elif choice == "6": #* Convertir Delivery/Salon
                #     print("Convertir Delivery/Salon")
                #     table = int(input("Seleccione la mesa a convertir: "))
                #     print("Funcion para pushear mesa a lista de deliveries, ajustando los datos correspondientes (mozo, precios, ec)")
                # elif choice == "7": #* Cobrar Mesa
                #     cobrarMesa(mesas,mozos)
                # elif choice == "8": #* Anular Mesa
                    # anularMesa(mesas,mozos)
                elif choice == "X" or choice == "x": #* Volver al menu anterior
                    salonMenuVar=False
                else:
                    print("Opcion invalida")
                    input("Presione enter para volver al menu anterior...")
                
        elif choice == "2":
                    print(mesasDelivery)
        elif choice == "3":
            var="a"
            while var != "":
                print("Estadisticas de Mesas")
                clearConsole()
                printMesaStats(statsMesas)
                var=input("Presione enter para volver al menu anterior") 
        elif choice == "4":
                    print("Configuracion de Mesas???")
        elif choice == "X" or choice == "x":
                    print("Volver al menu anterior")
                    mesasMenuVar=False
                    mainMenuVar=True
        else:
                    print("Opcion invalida")
                    input("Presione enter para volver al menu anterior...")
         
    while stockMenuVar:
        stockMenu(productos)
        stockMenuVar=False
        mainMenuVar=True


    while cajasMenuVar:
        clearConsole()
        cajaMenu()
        choice = input("Ingrese una opcion: ")
        if choice == "1": #* Ver Informacion General
            clearConsole()
            printInfoGeneral(mesas,mozos,productos,ec,tdc,tcc,cc,dc) 
            input("Presione enter para volver al menu anterior...")
            # cantProductos{productos} 
            # cantDineroTotal 

        elif choice == "2":
            print("Ver informacion de Mozos")
    
        elif choice =="3":
            print("Ver informacion de Mesas")
            # mesasDelivery = 
            # cantidadMesasLevantadas = levantarMesa(mesas,mozos,productos,statsMesas)
            # cantidadMesasUsadas = cobrarMesa(mesas)
        elif choice=="4": 
            print("Ver información de Stock")
        elif choice == "X" or choice == "x": #* Volver al menu anterior
            cajasMenuVar=False
            mainMenuVar=True
        else:
            print("Opcion invalida")
            input("Presione enter para volver al menu anterior...")


#! TO DO:
#* Validaciones a todos los inputs, para no romper el programa (todos deben aceptar numeros o letras)
#* Agregar Mensaje de 2-pasos (presione enter para continuar...) despues de cada operacion
#* Agregar clearConsole() al inicio de cada menu segun corresponda
            
        
        

    
         