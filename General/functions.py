def limpiarConsola():
    print("\033[H\033[J", end="")

def clear_except_last(n=3):
    print(f"\033[{n}A", end="")
    print("\033[1J", end="")
