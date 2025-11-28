def decodificar_cod(codigo):
    id=codigo//10000
    peso=codigo%10000
    return id, peso

lcodigo=3823495
lid, lpeso=decodificar_cod(lcodigo)
print ("id_producto:",lid, " ", "peso_gramos:" ,lpeso)

    