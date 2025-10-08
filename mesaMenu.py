#* Type Mesa = NumeroMesa??(Se puede hacer implicito con la posicion del elemento en el array),
#* MozoAsignado,"Pedidos",Disponible?(Boolean),MontoAPagar,

#! mesas debe estar declarado en MAIN
# mesas = [{1,0,"",True,0},{2,0,"",True,0},{3,0,"",True,0},{4,0,"",True,0},{5,0,"",True,0}] #* Con Objetos + numMesa
mesas = [{0,"",True,0},{0,"",True,0},{0,"",True,0},{0,"",True,0},{0,"",True,0}] #* Con Objetos sin numMesa
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
            #* Type Mesa = NumeroMesa,MozoAsignado,"Pedidos",Disponible?(Boolean),MontoAPagar
            numMesa = int(input("Ingrese el numero de mesa: ")) 
            numMozo = int(input("Ingrese el numero de mozo: "))
            pedidosMesa = [] = input("Ingrese los pedidos: ")

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