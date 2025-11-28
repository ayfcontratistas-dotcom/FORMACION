# en un rago de numeros divisibles
div3=lambda x : x % 3== 0
mensaje= ["False" , "True"]

print(f"{mensaje[True]}")
print(f"{mensaje[False]}")

for n in range (1,13):   #rango
    print(f"el numero {n} es es divisible 3? {mensaje[div3(n)]}")



#un solo numero divisible
div3=lambda x : x % 3== 0
mensaje= ["False" , "True"]

print(f"{mensaje[True]}")
print(f"{mensaje[False]}")

n= 21   #un numero
print(f"el numero{n} es divisuble por 3? {div3(n)}")
print(f"el numero {n} es es divisible 3? {mensaje[div3(n)]}")


espar= lambda x: x%2 == 0
x=espar(32)
print ("el numero es par:",x)



def es_par(x):
    return x % 2 == 0
print("el número es par:", es_par(32))




def es_par(x):
    return x % 2 == 0
x = 32
if es_par(x):
    print(x, "es un número par")
else:
    print(x, "es un número impar")

