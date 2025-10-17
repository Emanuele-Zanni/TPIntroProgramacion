from utils.isMesaValid import isMesaValid
from utils.isMozoValid import isMozoValid

def levantarMesa(listaMesas,listaMozos):
            pedidosMesa = []
            mesaValida=False
            mozoValido=False
            pedidoValido=False
            #* Type Mesa = NumeroMesa,MozoAsignado,"Pedidos",Disponible?(Boolean),MontoAPagar

            #* Validar Mesa con/sin funcion
            while mesaValida==False:
                numMesa = int(input("Ingrese el numero de mesa: "))

                mesaValida = isMesaValid(listaMesas,numMesa)

            #* Validar Mozo
            while mozoValido==False:
                numMozo = int(input("Ingrese el numero de mozo: "))

                mozoValido = isMozoValid(listaMozos,numMozo)

            item = "placeholder"
            while item != "":
                item = input("Ingrese un item o ingrese enter vacio para finalizar la carga: ")
                if item!= "":
                    pedidosMesa.append(item)
                else:
                    print("Mesa Levantada exitosamente!")
                
            #* Esto reemplazar por funcion LevantarMesa()
            listaMesas[numMesa-1] = [numMozo,pedidosMesa,False,0] #* usar listaMozos[numMozo-1] para guardar el nombre del mozo en vez del num
        