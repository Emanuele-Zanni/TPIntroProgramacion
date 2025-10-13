from utils.isMesaValid import isMesaValid
from utils.isMozoValid import isMozoValid

def levantarMesa(listaMesas,listaMozos):
            pedidosMesa = []
            mesaValida=False
            mozoValido=False
            pedidoValido=False
            #* Type Mesa = NumeroMesa,MozoAsignado,"Pedidos",Disponible?(Boolean),MontoAPagar

            # from utils.isMesaValid import isMesaValid

            #* Validar Mesa con/sin funcion
            while mesaValida==False:
                numMesa = int(input("Ingrese el numero de mesa: "))

                mesaValida = isMesaValid(listaMesas,numMesa)

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
            while mozoValido==False:
                numMozo = int(input("Ingrese el numero de mozo: "))

                mozoValido = isMozoValid(listaMozos,numMozo)

                # for i in range(len(mozos)):
                #     if numMozo-1 != i:
                #         if i+1 == len(mozos):
                #             print("Mozo no encontrado")
                #     else:
                #         mozoValido=True
                #         print("Mozo encontrado exitosamente")
                #         print(f"Mozo numero {numMozo}: {mozos[numMozo-1]}")
                #         # break

            item = "placeholder"
            while item != "":
                item = input("Ingrese un item o ingrese enter vacio para finalizar la carga: ")
                if item!= "":
                    pedidosMesa.append(item)
                else:
                    print("Mesa Levantada exitosamente!")
                
            #* Esto reemplazar por funcion LevantarMesa()
            listaMesas[numMesa-1] = [numMozo,pedidosMesa,False,0] #* usar listaMozos[numMozo-1] para guardar el nombre del mozo en vez del num
        