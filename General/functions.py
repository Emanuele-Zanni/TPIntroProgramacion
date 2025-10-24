def limpiarConsola():
    print("\033[H\033[J", end="")

def clear_except_last(n=3):
    print(f"\033[{n}A", end="")
    print("\033[1J", end="")

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


