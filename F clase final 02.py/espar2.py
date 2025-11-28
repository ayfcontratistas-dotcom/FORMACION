#true: si el numero es par
#false: si el numero es igual


def espar(lnum):
    if((lnum%2)==0):
        lespar=True
    else:
        lespar=False
    return lespar

print(espar(42))
print(espar(43))
