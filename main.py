app=True
mainMenu=True
mesasMenu=False
mozosMenu=False
stockMenu=False
mozos=["mozo1","mozo2","mozo3"]

mesas = [[0,"",False,0],[0,"",True,0],[0,"",True,0],[0,"",True,0],[0,"",True,0]]
#*[mozoAsignado,"Pedidos",Disponible?,MontoAPagar] (num de mesa = posicion en Lista)
#? Mesas manejadas como una Lista de LISTAS

mesasDelivery = [] #* mesas infinitas, mismo type de mesa pero SIN estado "disponible?", y numMesa modificado (un id)
pedidos = [] #* xd? (creo q era solo para cumplir con consigna semana 2)

from utils.isMesaValid import isMesaValid
from utils.isMozoValid import isMozoValid
from utils.isMesaEmpty import isMesaEmpty

from functions.mesas.levantarMesa import levantarMesa


while app:
    while mainMenu:
        print("""
    1)Mesas (Work in progress)
    2)Mozos (FALTA)
    3)Stock (FALTA)
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
            Mozos=True
            mainMenu=False
        elif choice=="3":
            print("Stock")
            Stock=True
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
        
    #     print("""
    # 1)Ver Mesas/Salon (Crear submenu? guardar opcion 11, 22 y 33)
    # 11)Levantar Mesa (verificar si funciona bien con Features STOCK y MOZOS)
    # 22)Ver Delivery (Crear funcion)
    # 33)Ver TODO (Crear funcion)
    
    # w2.1)Agregar pedido (Va a ser reemplazado por "Levantar Mesa")
    # w2.2)Ver pedidos (Esto vuela, implicito en Ver Mesas)
    # X)Volver al menu principal
    # """)
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
                            isValid = isMesaValid(mesas,table)
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
                            print("Mover Mesa")
                            tableOld = int(input("Seleccione la mesa a mover: ")) - 1

                            if mesas[tableOld][2] == True:
                                print("Mesa a mover vacia")
                                break

                            tableNew = int(input("Seleccione la mesa destino: ")) - 1

                            if mesas[tableNew][2] == False:
                                print("Mesa destino ocupada")
                                break

                            mesas[tableNew] = mesas[tableOld]
                            mesas[tableOld] = [0,"",True,0]

                elif choice == "6":
                            print("Convertir Delivery/Salon")
                            table = int(input("Seleccione la mesa a convertir: "))
                            print("Funcion para pushear mesa a lista de deliveries, ajustando los datos correspondientes (mozo, precios, etc)")
                elif choice == "7":
                            print("Cobrar Mesa")
                            isValid=True

                            table = int(input("Seleccione la mesa a cobrar: "))

                            isValid = isMesaValid(mesas,table)
                            if isValid == False:
                                print("Mesa no encontrada")
                            #! Individualizar validaciones.
                            if isValid:
                                isEmpty = isMesaEmpty(mesas,table)
                                if isEmpty:
                                    isValid=False
                            
                            if isValid:
                                mesas[table-1] = [0,"",True,0]
                                print("Mesa cobrada exitosamente")

                            elif isValid == False:
                                print("Error al cobrar mesa")
                            # Funcion para cobrar mesa, guardando los datos correspondientes (mozo, stock, caja, etc)
                elif choice == "8":
                            print("Anular Mesa")
                            table = int(input("Seleccione la mesa a anular: ")) - 1
                            print("Funcion para ANULAR mesa, guardando los datos correspondientes (mozo, stock, caja, etc)")
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

            
        # elif choice=="w2.1":
        #     on = True
        #     isDuplicate=False

        #     while on:
        #     # mesa = int(input("Ingrese el numero de mesa: "))
        #         pedido = input("Ingrese el pedido: ")

        #         for i in range(len(pedidos)):
        #             if pedido == pedidos[i]:
        #                 isDuplicate=True
        #                 # break 

        #         if isDuplicate==False:
        #             print("Pedido Agregado Exitosamente.")
        #             pedidos.append(pedido)
        #             on=False
        #         elif isDuplicate==True:
        #             print("Error. Pedido duplicado")
        #             isDuplicate=False
                    
                
        # elif choice=="w2.2":
        #     print(pedidos)
        # #! FUNCION LEVANTAR MESA
        # elif choice=="aaa":
        #     from functions.mesas.levantarMesa import levantarMesa
        #     levantarMesa(mesas,mozos)
        # elif choice=="11":
        #     pedidosMesa = []
        #     mesaValida=False
        #     mozoValido=False
        #     pedidoValido=False
            #* Type Mesa = NumeroMesa,MozoAsignado,"Pedidos",Disponible?(Boolean),MontoAPagar

            # from utils.isMesaValid import isMesaValid

            #* Validar Mesa con/sin funcion
            # while mesaValida==False:
            #     numMesa = int(input("Ingrese el numero de mesa: "))

            #     mesaValida = isMesaValid(mesas,numMesa)

                # tableFound=False
                # for i in range(len(mesas)):
                #     if numMesa-1 != i and tableFound==False:
                #         if i+1 == len(mesas):
                #             print("Mesa no encontrada")
                #     elif mesas[numMesa-1][2] == False: #* Disponible? = False
                #         tableFound=True
                #         if i+1 == len(mesas):
                #             print("Mesa ocupada")
                #         # break
                #     elif numMesa-1 == i and tableFound==False:
                #         print("Mesa encontrada exitosamente")
                #         mesaValida=True
                #         tableFound=True
                #         i = len(mesas)
                #         # break

            #* Validar Mozo
            # while mozoValido==False:
            #     numMozo = int(input("Ingrese el numero de mozo: "))

            #     mozoValido = isMozoValid(mozos,numMozo)

                # for i in range(len(mozos)):
                #     if numMozo-1 != i:
                #         if i+1 == len(mozos):
                #             print("Mozo no encontrado")
                #     else:
                #         mozoValido=True
                #         print("Mozo encontrado exitosamente")
                #         print(f"Mozo numero {numMozo}: {mozos[numMozo-1]}")
                #         # break

            # item = "placeholder" #!Modificar la condicion del while para deshacerse de este item
            # while item != "":
            #     item = input("Ingrese un item o ingrese enter vacio para finalizar la carga: ")
            #     if item!= "":
            #         pedidosMesa.append(item)
            #     else:
            #         print("Carga de pedidos finalizada")
                
            #! Esto reemplazar por funcion LevantarMesa()
            # mesas[numMesa-1] = [mozos[numMozo-1],pedidosMesa,False,0]
        #! EDITAR MESA
        # elif choice=="12": 
        # print: Mover mesa, Cambiar Mozo, Editar Pedidos, Cobrar Mesa, Anular Mesa, Convertir a Delivery/Salon
        #     print("""
        # 1)Mover mesa
        # 2)Cambiar Mozo
        # 3)Editar Pedidos
        # 4)Conversion Delivery/Salon
        # 5)Anular Mesa (subir un nivel esta opcion?)
        # 6)Cobrar Mesa (subir un nivel esta opcion?)
        # """) 

        # elif choice=="X" or choice=="x":
        #     print("Volver al menu principal")
        #     mesasMenu=False
        #     mainMenu=True
        # else:
        #     print("Opcion invalida")