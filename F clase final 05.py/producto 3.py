
import matplotlib.pyplot as plt

gasto = [3, 4, 5, 2, 1, 6, 10, 7, 11, 4, 3, 13]
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    

for mes, valor in zip(meses, gasto):
    print(f"Mes {mes}: {valor}")

max_gasto = max(gasto)
mes_max = gasto.index(max_gasto) + 1  

print(f"El mes de mayor gasto fue el mes {mes_max} con un gasto de {max_gasto}")

plt.title("Gasto Mensual")
plt.bar(meses, gasto)
plt.show()