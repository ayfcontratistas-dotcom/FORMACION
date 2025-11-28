def id_categoria(numero):
    id=numero//100
    cat=numero%100
    return id, cat

lnumero=10234
lid, lcat=id_categoria(lnumero)
print ("identificacion:", lid, " ", "categoria:", lcat)

def id_categoria(numero):
    id=numero//100
    cat=numero%100
    return id, cat

lnumero=26512
lid, lcat=id_categoria(lnumero)
print ("identificacion:", lid, " ", "categoria:", lcat)