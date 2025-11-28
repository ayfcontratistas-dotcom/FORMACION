

def codifica_cualitativo(nota):
    if (nota<5):
        estado="mal"
    elif (nota==5):
        estado="regular"
    elif (nota<9):
        estado="bien"
    else:
        estado="exelente"
    return estado
    
mi_nota=3
mi_estado=codifica_cualitativo(mi_nota)
print(mi_estado)