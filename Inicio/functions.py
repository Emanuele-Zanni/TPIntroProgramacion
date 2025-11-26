from Inicio.menus import *
from General.functions import *

def Inicio():
    on = True

    while on:
        clearConsole()
        InicioDiaMenu()

        option = input("Ingrese una opcion: ")
        if option == "1":
            on = False
            return False,True,True
        elif option == "2":
            print("Logs dias anteriores")
        elif option == "x" or option == "X":
            on = False
            return False,False
        else:
            print("Opcion invalida")

def resetAllStats(statsMesas,statsDelivery,mozoStats,listaProductosVendidos,cantPedidosVendidos,logs,ec,tdc,tcc,cc,dc,ecd,tdcd,tccd,ccd,dcd):
    #? Variables de Caja
    #* --Salon--
    ec=0 #* Efectivo Caja
    tdc=0 #* Tarjeta Debito Caja
    tcc=0  #* Tarjeta Credito Caja
    cc=0 #* Cheques Caja
    dc=0 #* Deuda Caja
    #* --Delivery--
    ecd=0 #* Efectivo Caja Delivery
    tdcd=0 #* Tarjeta Debito Delivery
    tccd=0 #* Tarjeta Credito Delivery
    ccd=0 #* Cheques Caja Delivery
    dcd=0 #* Deuda Caja Delivery

    cantPedidosVendidos=0 #* Cantidad de deliveries vendidos
    #* --Logs--
    logs=[]

    #? Variables de Mesas
    newStatsMesas = []
    for i in range(len(statsMesas)):
        newStatSlot = [0,[],0]
        newStatsMesas.append(newStatSlot)
    statsMesas = newStatsMesas

    statsDelivery = []

    #? Variables de Stock
    listaProductosVendidos=[]

    newMozoStats = []
    for i in range(len(mozoStats)):
        newStatSlot = [[0,0,0,0],[0,0,0,0]]
        newMozoStats.append(newStatSlot)
    mozoStats = newMozoStats

    return statsMesas,statsDelivery,mozoStats,listaProductosVendidos,cantPedidosVendidos,logs,ec,tdc,tcc,cc,dc,ecd,tdcd,tccd,ccd,dcd





