def espar_01(lnumero):
    if((lnumero%2)==0):
        lespar=True
    else:
        lespar=False
    return lespar

def espar_02(lnumero):
    lespar=(lnumero%2)==0
    return lespar

def espar_03(lnumero):
    return(lnumero%2)==0

espar_04 = lambda lnumero: (lnumero%2)==0

print(espar_01(35))
print(espar_02(48))
print(espar_03(62))
print(espar_04(32))

