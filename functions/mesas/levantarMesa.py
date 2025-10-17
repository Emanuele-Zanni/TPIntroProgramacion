from utils.isMesaValid import isMesaValid
from utils.isMozoValid import isMozoValid
from functions.stock.funciones import *

def levantarMesa(listaMesas,listaMozos,listaProductos):
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

            item = 1
            total = 0
            producto = ""
            codigo = 0
            while codigo != -1:
                codigo = int(input("Ingrese el codigo del item a cargar (-1 para finalizar): "))
                producto = getProduct(listaProductos,codigo)
                if producto!= "":
                    pedidosMesa.append(producto[0])
                    total += producto[2]
                elif codigo == -1:
                    print("Mesa Levantada exitosamente!")
                
            
            listaMesas[numMesa-1] = [numMozo,pedidosMesa,False,total] #* usar listaMozos[numMozo-1] para guardar el nombre del mozo en vez del num
        