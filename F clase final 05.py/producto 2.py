import matplotlib.pyplot as plt

gasto=[3,4,5,2,1,6,10,7,11,4,3,13]

def calcular_mayor_gasto(lgasto):
    pos_mayor=0
    for i,valor in enumerate(lgasto):
        if lgasto[pos_mayor]<lgasto[i]:
            pos_mayor=i
            mes_mayor_consumo=pos_mayor
    return mes_mayor_consumo
    

def salida_datos(lgasto, lpos_mayor):
    meses=["ene","feb","mar","abr","may","jun","jul","ago","sep","oct","nov","dic"]
   
    print (f"el mayor gasto fue:{lgasto[lpos_mayor]} en el mes {lpos_mayor+1}")

    plt.bar(meses,lgasto)
    plt.show()


gmayor_gasto=calcular_mayor_gasto(gasto)
salida_datos(gasto ,gmayor_gasto)