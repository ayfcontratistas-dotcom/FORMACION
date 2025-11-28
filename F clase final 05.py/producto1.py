import matplotlib.pyplot as plt

productos=[3,4,5,2,1,6,10,7,11,4,3,13]

def calcular_mayor_gasto(lproducto):
    pos_mayor=0
    for i,valor in enumerate(lproducto):
        if lproducto[pos_mayor]<lproducto[i]:
            pos_mayor=i
            mes_mayor_consumo=pos_mayor
    return mes_mayor_consumo
    

def salida_datos(lproducto, lpos_mayor):
    meses=["ene","feb","mar","abr","may","jun","jul","ago","sep","oct","nov","dic"]
   
    print (f"el mayor gasto fue:{lproducto[lpos_mayor]} en el mes {lpos_mayor+1}")

    plt.bar(meses,lproducto)
    plt.show()


gmayor_consumo=calcular_mayor_gasto(productos)
salida_datos(productos, gmayor_consumo)





    



