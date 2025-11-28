letra="a"
cadena="normas basicas del aula"

for i in cadena:
    print(i)


contar=0
for i in cadena:
    if i == letra:
     contar=contar+1

print("cantidad de letra es:",contar) #ejemplo con la letra a

cadena=cadena.upper()
print("en mayuscula:",cadena)

letra=letra.upper()
print("letra es:",letra)

n=cadena.count(letra)
print("cantidad de letra es:",n)
