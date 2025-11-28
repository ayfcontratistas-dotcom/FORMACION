#en clase
data=[10,25,21,33,14]

n=len(data)                  #forma larga 
for i in range(0,n):
    for j in range (i,n):
        if data[j]>data[i]:
            data[j],data[i]=data[i],data[j]

print("Ordenados")
for i in range(n):
    print (data[i])

# de la ia
ordenados = sorted(data)    #forma corta
print("data ordenada:",ordenados)     


