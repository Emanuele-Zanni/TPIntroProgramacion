app=True
mainMenu=True
mesasMenu=False
mozosMenu=False
stockMenu=False
mozos=["mozo1","mozo2","mozo3"]

#* Type Mesa = NumeroMesa??(Se puede hacer implicito con la posicion del elemento en el array),
#* MozoAsignado,"Pedidos",Disponible?(Boolean),MontoAPagar,
# mesas = [{1,0,"",True,0},{2,0,"",True,0},{3,0,"",True,0},{4,0,"",True,0},{5,0,"",True,0}] #* Con Objetos + numMesa
mesasViejas = [{0,"",False,0},{0,"",True,0},{0,"",True,0},{0,"",True,0},{0,"",True,0}] #* Con Objetos sin numMesa
mesas = [[0,"",False,0],[0,"",True,0],[0,"",True,0],[0,"",True,0],[0,"",True,0]] #* Con Listas sin numMesa
#? Resolucion para el problema de mesas = tratarlas como listas de listas, o manejar objetos con campos nombrados,
#? es decir, con {"clave" : valor}

mesasDelivery = [] #* mesas infinitas, mismo type de mesa pero SIN estado "disponible?", y numMesa modificado (un id)
pedidos = [] #* xd? (creo q era solo para cumplir con consigna semana 2)

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

        print("""
    1)Ver Mesas/Salon (Crear submenu?)
    11)Levantar Mesa
    22)Ver Delivery
    33)Ver TODO
    
    2)Agregar pedido (Va a ser reemplazado por "Levantar Mesa")
    3)Ver pedidos (Esto vuela, implicito en Ver Mesas)
    X)Volver al menu principal
    """)

        choice=input("Ingrese una opcion: ")

        if choice=="1":
            print(mesas)
        elif choice=="2":
            on = True
            isDuplicate=False

            while on:
            # mesa = int(input("Ingrese el numero de mesa: "))
                pedido = input("Ingrese el pedido: ")

                for i in range(len(pedidos)):
                    if pedido == pedidos[i]:
                        isDuplicate=True
                        # break 

                if isDuplicate==False:
                    print("Pedido Agregado Exitosamente.")
                    pedidos.append(pedido)
                    on=False
                elif isDuplicate==True:
                    print("Error. Pedido duplicado")
                    isDuplicate=False
                    
                
        elif choice=="3":
            print(pedidos)
        #! FUNCION LEVANTAR MESA
        elif choice=="11":
            pedidosMesa = []
            mesaValida=False
            mozoValido=False
            pedidoValido=False
            #* Type Mesa = NumeroMesa,MozoAsignado,"Pedidos",Disponible?(Boolean),MontoAPagar

            #* Validar Mesa
            while mesaValida==False:
                numMesa = int(input("Ingrese el numero de mesa: "))
                tableFound=False

                for i in range(len(mesas)):
                    if numMesa-1 != i and tableFound==False:
                        if i+1 == len(mesas):
                            print("Mesa no encontrada")
                    elif mesas[numMesa-1][2] == False: #* Disponible? = False
                        tableFound=True
                        if i+1 == len(mesas):
                            print("Mesa ocupada")
                        # break
                    elif numMesa-1 == i and tableFound==False:
                        print("Mesa encontrada exitosamente")
                        mesaValida=True
                        tableFound=True
                        i = len(mesas)
                        # break

            while mozoValido==False:
                numMozo = int(input("Ingrese el numero de mozo: "))

                for i in range(len(mozos)):
                    if numMozo-1 != i:
                        if i+1 == len(mozos):
                            print("Mozo no encontrado")
                    else:
                        mozoValido=True
                        print("Mozo encontrado exitosamente")
                        print(f"Mozo numero {numMozo}: {mozos[numMozo-1]}")
                        # break

            item = "placeholder"
            while item != "":
                item = input("Ingrese un item o ingrese enter vacio para finalizar la carga: ")
                if item!= "":
                    pedidosMesa.append(item)
                else:
                    print("Carga de pedidos finalizada")
                
            #* Esto reemplazar por funcion LevantarMesa()
            mesas[numMesa-1] = [mozos[numMozo-1],pedidosMesa,False,0]
        #! EDITAR MESA
        elif choice=="12": 
        # print: Mover mesa, Cambiar Mozo, Editar Pedidos, Cobrar Mesa, Anular Mesa, Convertir a Delivery/Salon
            print("""
        1)Mover mesa
        2)Cambiar Mozo
        3)Editar Pedidos
        4)Conversion Delivery/Salon
        5)Anular Mesa (subir un nivel esta opcion?)
        6)Cobrar Mesa (subir un nivel esta opcion?)
        """) 

        elif choice=="X" or choice=="x":
            print("Volver al menu principal")
            mesasMenu=False
            mainMenu=True
        else:
            print("Opcion invalida")