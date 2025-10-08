app=True
mainMenu=True
mesasMenu=False
mozosMenu=False
Mozos=[]
Stock=[]

while app:
    while mainMenu:
        print("""
    1)Mesas
    2)Mozos
    3)Stock
    4)Cajas
    5)Finalizar Dia
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

    #* Type Mesa = NumeroMesa??(Se puede hacer implicito con la posicion del elemento en el array),
    #* MozoAsignado,"Pedidos",Disponible?(Boolean),MontoAPagar,
    # mesas = [{1,0,"",True,0},{2,0,"",True,0},{3,0,"",True,0},{4,0,"",True,0},{5,0,"",True,0}] #* Con Objetos + numMesa
    mesas = [{0,"",True,0},{0,"",True,0},{0,"",True,0},{0,"",True,0},{0,"",True,0}] #* Con Objetos sin numMesa

    #? Resolucion para el problema de mesas = tratarlas como listas de listas, o manejar objetos con campos nombrados,
    #? es decir, con {"clave" : valor}


    mesasDelivery = [] #* mesas infinitas, mismo type de mesa pero SIN estado "disponible?", y numMesa modificado (un id)
    pedidos = []

    while mesasMenu:
        print("""
    1)Ver mesas (Crear submenu?)
    2)Agregar pedido (Va a ser reemplazado por "Levantar Mesa")
    3)Ver pedidos (Esto vuela, implicito en Ver Mesas)
    11)Levantar Mesa
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
        #! LEVANTAR MESA
        elif choice=="11":
            pedidosMesa = []
            mesaValida=False
            mozoValido=False
            pedidoValido=False
            #* Type Mesa = NumeroMesa,MozoAsignado,"Pedidos",Disponible?(Boolean),MontoAPagar

            while mesaValida==False:
                numMesa = int(input("Ingrese el numero de mesa: "))

                for i in range(len(mesas)):
                    if mesas[numMesa-1] != mesas[i]:
                        print("Mesa no encontrada")
                    elif mesas[numMesa-1] == False: #* Disponible? = False
                        print("Mesa ocupada")
                    else:
                        mesaValida=True
                        # break

                for i in range(len(mozos)):
                    if mesas[numMesa-1] != mesas[i]:
                        print("Mesa no encontrada")
                    elif mesas[numMesa-1] == False: #* Disponible? = False
                        print("Mesa ocupada")
                    else:
                        mesaValida=True
                        # break

            
    
            numMozo = int(input("Ingrese el numero de mozo: "))
            pedidosMesa = input("Ingrese los pedidos: ")

            #* Esto reemplazar por funcion LevantarMesa()
            mesas[numMesa-1] = {numMozo,pedidosMesa,False,0}
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