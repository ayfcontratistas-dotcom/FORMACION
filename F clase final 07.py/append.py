numeros = [1, 2, 3]
numeros.append(4)
print(numeros)



data= { "sueldos de enero":{1125, 2532, 1425, 956, 750, 650 }, "sueldos de febrero":{850, 1145, 2350,}}
print (data)
alist=[]
alist.append(data.get("sueldos de enero"))
alist.append(data.get("sueldos de febrero"))
print (alist)

todos = list(data["sueldos de enero"]) + list(data["sueldos de febrero"])
print(todos)
print("suledo mayor de Enero:", max(data["sueldos de enero"]))
print("suledo mayor de Febrero:", max(data["sueldos de febrero"]))

