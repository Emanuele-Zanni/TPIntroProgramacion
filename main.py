
#? Variables de APP
app=True
cargaProdTutorial=True
logsFinalDia = []
#* Fin dia debe tener guardar TODA la DATA de CAJA + los LOGS en una lista, y eso seria un log de un dia
#? Variables de Menu
mainMenuVar=True
mesasMenuVar=False 
mozosMenuVar=False
stockMenuVar=False
cajasMenuVar=False
#? Variables de Caja
#* --Salon--
ec=0 #* Efectivo Caja
tdc=0 #* Tarjeta Debito Caja
tcc=0  #* Tarjeta Credito Caja
cc=0 #* Cheques Caja
dc=0 #* Deuda Caja
dtc=0 #* Dinero Total Caja
#* --Delivery--
ecd=0 #* Efectivo Caja Delivery
tdcd=0 #* Tarjeta Debito Delivery
tccd=0 #* Tarjeta Credito Delivery
ccd=0 #* Cheques Caja Delivery
dcd=0 #* Deuda Caja Delivery
dtcd=0 #* Dinero Total Caja Delivery

cantPedidosVendidos=0 #* Cantidad de deliveries vendidos
#* --Logs--
logs=[]
#? id(venta numero = ??. Determinado con posicion en Lista), hora de transaccion, [Mesa] (todos los datos de la mesa, mozo, productos, costo. Todo en ORDEN)
#? Type (Salon o Delivery)
#! Crear en caja un MAP para el log entero, mostrar de a 1 en 1 y poner opciones de "siguente log","log anterior" y "Elegir log id"

#? Variables de Mesas

mesas = [[0,[],True,0],[0,[],True,0],[0,[],True,0],[0,[],True,0],[0,[],True,0]] #*[mozoAsignado,"ListaProductos",Disponible?,TotalMesa] (num de mesa = posicion en Lista)
mesasDelivery = [] #* [numMozo Asignado,"ListaProductos",direccion,totalMesa]
statsMesas = [[0,[],0],[0,[],0],[0,[],0],[0,[],0],[0,[],0]] #* STATS MESA PARTICULAR: Veces levantada,mozosAsignados, productos cargados? (HACER LOGS aparte), productos anulados, plata recaudada, plata anulada
statsDelivery = [] #* (array con numero de mozo + cantidad de veces que trabajaron en la mesa)

#* GENERALES: Mesas Movidas, Cambios de Mozo, [Mesas Cobradas, Mesas Anuladas, Productos Anulados, Productos Cargados] (Salon y Delivery),  
#? Variables de Stock
listaProductosVendidos=[]
#? Variables de Mozos

#? Estructura de mozos: [ID, Nombre, [Lista de Mesas Asignadas], Total Recaudado]
mozos=[[1, "Mozo A", [], 0],[2, "Mozo B", [], 0],[3, "Mozo C", [], 0]]

#? Estructura de Stats de los mozos:
#? [[Mesas Cobradas Salon, Dinero Salon, Anulaciones Salon, Dinero Anulado Salon],[Mesas Cobradas Delivery, Dinero Delivery, Anulaciones Delivery, Dinero Anulado Delivery]]
#! esta de abajoes la estructura vieja, la dejo x posibles bugs que haya que corregir
#* [[Mesas Cobradas Salon,Dinero,MesasDelivery,DineroDelivery],[Anulaciones Salon, Dinero Anulado Salon, Anulaciones Delivery,Dinero Anulado Delivery]]
mozoStats = [[[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0]]]

productos = [[1,"producto1",100,10],[2,"producto2",200,20],[3,"producto3",300,30],[4,"producto4",400,40],[5,"producto5",500,50]]

#******* Importaciones *********
from Mesas.menus import *
from Stock.menus import *
from General.menus import * 
from Mozos.menus import *
from Caja.menus import *

from Mesas.functions import *
from Stock.functions import *
from General.functions import *
from Caja.functions import *

from Mesas.validations import *
from Stock.validations import *
from Mozos.validations import *
#*******************************

while app:
    while mainMenuVar: #* Menu Principal
        clearConsole()
        mainMenu()
        choice=input("Ingrese una opcion: ")

        if choice=="1": #* Ver Mesas
            mesasMenuVar=True
            mainMenuVar=False
        elif choice=="2": #* Ver Mozos
            menu_mozos(mozos,mozoStats)
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

    while mesasMenuVar: #! Mesas Menu
        clearConsole()
        mesasMenu()
        choice=input("Ingrese una opcion: ")

        if choice=="1": #! Ver Salon
            ec,tdc,tcc,cc,dc,dtc,cargaProdTutorial,listaProductosVendidos=Salon(mesas,mozos,productos,statsMesas,mozoStats,cargaProdTutorial,listaProductosVendidos,ec,tdc,tcc,cc,dc,dtc,logs)
        elif choice == "2": #! Ver Delivery
            ecd,tdcd,tccd,ccd,dcd,dtcd,cantPedidosVendidos=Delivery(mesasDelivery,mozos,productos,mozoStats,ecd,tdcd,tccd,ccd,dcd,dtcd,cargaProdTutorial,cantPedidosVendidos,logs)
        elif choice == "3": #! Configurar Cantidad de Mesas
            clearConsole()
            print("[Menu Principal > Mesas > Salon > *Configurar Mesas*]")
            print("")
            mesas,statsMesas = editMesasQuantity(mesas,statsMesas)
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
            printInfoGeneral(mesas,mesasDelivery,mozos,productos,ec,tdc,tcc,cc,dc,ecd,tdcd,tccd,ccd,dcd) 
            input("Presione enter para volver al menu anterior...")
            # cantProductos{productos} 
            # cantDineroTotal 

        elif choice == "2":
            infoMozosSubmenu(mozos,mozoStats)
    
        elif choice =="3":
            infoMesasSubmenu(mesas,statsMesas,dtc,cantPedidosVendidos,productos,logs)
        elif choice=="4": 
            printInfoStock(productos,listaProductosVendidos)
            input("Presione enter para volver al menu anterior...")
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
    