
#? Variables de APP
app=True
cargaProdTutorial=False
#* Fin dia debe tener guardar TODA la DATA de CAJA + los LOGS en una lista, y eso seria un log de un dia
#? Variables de Menu
inicioDiaMenuVar=True
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
#? id(Determinado con posicion en Lista), hora de transaccion, [Mesa] (todos los datos de la mesa, mozo, productos, costo. Todo en ORDEN),Type (Salon o Delivery)
#* [time,"Delivery",metodoPagoElegido,listaMesas[pedido-1][2],listaMesas[pedido-1]]
logs=[] 

logsFinalDia = []


#? Variables de Mesas

mesas = [[0,[],True,0],[0,[],True,0],[0,[],True,0],[0,[],True,0],[0,[],True,0]] #*[mozoAsignado,"ListaProductos",Disponible?,TotalMesa] (num de mesa = posicion en Lista)
mesasDelivery = [] #* [numMozo Asignado,"ListaProductos",direccion,totalMesa]
statsMesas = [[0,[],0],[0,[],0],[0,[],0],[0,[],0],[0,[],0]] #* STATS MESA PARTICULAR: Veces levantada,mozosAsignados, productos cargados? (HACER LOGS aparte), productos anulados, plata recaudada, plata anulada
statsDelivery = [] #* (array con numero de mozo + cantidad de veces que trabajaron en la mesa)

#* GENERALES: Mesas Movidas, Cambios de Mozo, [Mesas Cobradas, Mesas Anuladas, Productos Anulados, Productos Cargados] (Salon y Delivery),  
#? Variables de Stock
listaProductosVendidos=[]

#* Estructura de productos: [codigo, Nombre, Precio, Stock]
productos = [[1,"producto1",100,10],[2,"producto2",200,20],[3,"producto3",300,30],[4,"producto4",400,40],[5,"producto5",500,50]]
prodStats = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] #* [Ventas Salon, Anulaciones Salon, Ventas Delivery, Anulaciones Delivery]
#? Variables de Mozos

#? Estructura de mozos: [ID, Nombre, [Lista de Mesas Asignadas], Total Recaudado????]
mozos=[[1, "Mozo A", [], 0],[2, "Mozo B", [], 0],[3, "Mozo C", [], 0]]

#? Estructura de Stats de los mozos:
#? [[Mesas Cobradas Salon, Dinero Salon, Anulaciones Salon, Dinero Anulado Salon],[Mesas Cobradas Delivery, Dinero Delivery, Anulaciones Delivery, Dinero Anulado Delivery]]
#! esta de abajo es la estructura vieja, la dejo x posibles bugs que haya que corregir
#* [[Mesas Cobradas Salon,Dinero,MesasDelivery,DineroDelivery],[Anulaciones Salon, Dinero Anulado Salon, Anulaciones Delivery,Dinero Anulado Delivery]]
mozoStats = [[[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0]],[[0,0,0,0],[0,0,0,0]]]



#******* Importaciones *********
from Mesas.menus import *
from Stock.menus import *
from General.menus import * 
from Mozos.menus import *
from Caja.menus import *
from Inicio.menus import *

from Mesas.functions import *
from Stock.functions import *
from General.functions import *
from Caja.functions import *
from Inicio.functions import *

from Mesas.validations import *
from Stock.validations import *
from Mozos.validations import *
#*******************************

while app:

    while inicioDiaMenuVar:
        inicioDiaMenuVar,mainMenuVar,app=Inicio()
        statsMesas,statsDelivery,mozoStats,listaProductosVendidos,cantPedidosVendidos,logs,ec,tdc,tcc,cc,dc,ecd,tdcd,tccd,ccd,dcd=resetAllStats(statsMesas,statsDelivery,mozoStats,listaProductosVendidos,cantPedidosVendidos,logs,ec,tdc,tcc,cc,dc,ecd,tdcd,tccd,ccd,dcd)

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
        elif choice=="5": #! Finalizar Dia
            print("Funcion para guardar TODA la info del dia en logsFinalDia")
            inicioDiaMenuVar=True
            mainMenuVar=False
        else:
            print("Opcion invalida")
            input("Presione enter para volver al menu anterior...")

    while mesasMenuVar: #! MESAS MENU
        clearConsole()
        mesasMenu()
        choice=input("Ingrese una opcion: ")

        if choice=="1": #! Ver Salon
            ec,tdc,tcc,cc,dc,dtc,cargaProdTutorial,listaProductosVendidos=Salon(mesas,mozos,productos,statsMesas,mozoStats,cargaProdTutorial,listaProductosVendidos,ec,tdc,tcc,cc,dc,dtc,logs)
        elif choice == "2": #! Ver Delivery
            ecd,tdcd,tccd,ccd,dcd,dtcd,cantPedidosVendidos=Delivery(mesasDelivery,mozos,productos,mozoStats,listaProductosVendidos,ecd,tdcd,tccd,ccd,dcd,dtcd,cargaProdTutorial,cantPedidosVendidos,logs)
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
        stockMenu(productos,prodStats)
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

        elif choice == "2":
            infoMozosSubmenu(mozos,mozoStats)
    
        elif choice =="3":
            infoMesasSubmenu(mesas,statsMesas,dtc,cantPedidosVendidos,productos,logs)
        elif choice=="4": 
            printInfoStock(productos,listaProductosVendidos,prodStats)
            input("Presione enter para volver al menu anterior...")
        elif choice == "X" or choice == "x": #* Volver al menu anterior
            cajasMenuVar=False
            mainMenuVar=True
        else:
            print("Opcion invalida")
            input("Presione enter para volver al menu anterior...")
    