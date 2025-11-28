numeros = [1, 2, 3, 4, 5, 6]

#buscar los pares y elevarlos a la potencia 2
nueva_lista=[n**2 for n in numeros if n%2==0]
print ("pares elevados a potencia 2:",nueva_lista)


#divisibles pares residuo 0
numeros= range(30)
nueva_lista=[n**2 for n in numeros if n%2==0]
print ("pares elevados a potencia 2:",nueva_lista)

#a partir del 10
numeros= range(30)
nueva_lista=[n**2 for n in numeros if n>10]
print ("pares elevados a potencia 2:",nueva_lista)