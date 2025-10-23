def limpiarConsola():
    print("\033[H\033[J", end="")

def clear_except_last(n=3):
    print(f"\033[{n}A", end="")
    print("\033[1J", end="")

def ordenarBubble(Lista, ListaParalela, descendente=False):
    longitud = len(Lista)
    for pasada in range(longitud):
        for indice in range(0, longitud - pasada - 1):
            fuera_de_orden = (
                Lista[indice] < Lista[indice + 1] if descendente
                else Lista[indice] > Lista[indice + 1]
            )
            if fuera_de_orden:
                Lista[indice], Lista[indice + 1] = Lista[indice + 1], Lista[indice]
                ListaParalela[indice], ListaParalela[indice + 1] = ListaParalela[indice + 1], ListaParalela[indice]


