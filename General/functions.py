import os

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

#* Esta funcion se encarga de ordenar una lista de forma ascendente o descendente (segun el segundo parametro)
def ordenarBubble(lista, mode="asc"):
    longitud = len(lista)
    for pasada in range(longitud):
        for indice in range(0, longitud - pasada - 1):
            fuera_de_orden = (
                lista[indice] < lista[indice + 1] if mode == "asc"
                else lista[indice] > lista[indice + 1]
            )
            if fuera_de_orden:
                lista[indice], lista[indice + 1] = lista[indice + 1], lista[indice]

def ordenarBubbleParalela(Lista, ListaParalela, mode="asc"):
    longitud = len(Lista)
    for pasada in range(longitud):
        for indice in range(0, longitud - pasada - 1):
            fuera_de_orden = (
                Lista[indice] < Lista[indice + 1] if mode == "asc"
                else Lista[indice] > Lista[indice + 1]
            )
            if fuera_de_orden:
                Lista[indice], Lista[indice + 1] = Lista[indice + 1], Lista[indice]
                ListaParalela[indice], ListaParalela[indice + 1] = ListaParalela[indice + 1], ListaParalela[indice]

def checkAndConvertToInt(value):
    if value.strip().isdigit():
        newValue = int(value)
        return True,newValue
    else:
        return False,value
    
def checkAndConvertToFloat(value):
    if value.strip().replace('.', '', 1).isdigit():
        newValue = float(value)
        return True,newValue
    else:
        return False,value
    
def pct(parte, total):
    return round(parte * 100 / (total or 1))
