def codifica_cualitativo (porcentaje):
    if(porcentaje>80):
        incremento="malo"
    elif(porcentaje>50):
        incremento="regular"
    elif(porcentaje>30):
        incremento="bueno"
    else:
        incremento="exelente"
    return incremento


mi_porcentaje=52
mi_incremento=codifica_cualitativo(mi_porcentaje)
print("mi_incremento:",mi_incremento)
