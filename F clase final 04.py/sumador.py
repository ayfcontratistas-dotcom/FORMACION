
n=30

for i in range(n):    #contar de 1 en 1
    print(f"{i}")



suma=0
for i in range(n):    #resultado de la suma (0+ 0=) + un numero consecutivo 0,1,2,3,...
    suma=suma+i
    print(f"la suma es:{suma}")



str_s=""
for i in range (n):
    temp= f"{i:3d}"
    str_s = str_s + temp
    print (str_s)
    