def isCodeReal(listaStock, code):
    for item in listaStock:
        if item[0] == code:
            return True
    return False