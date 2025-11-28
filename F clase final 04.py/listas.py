#importar la libreria

import matplotlib.pyplot as pl

pesos=[4,6,8,10]
nombres=["a","b","c","d"]

suma=0
tamaño=len(pesos)

for i in pesos:  #cuenta elementos
    print (i)

for i in pesos:
    suma+=i             #sumatoria
    print ("la suma de cada uno:",suma)

for i in pesos:
    promedio=suma/len(pesos)
    print("el promedio es:",promedio)

pl.bar(nombres,pesos)
pl.show()

