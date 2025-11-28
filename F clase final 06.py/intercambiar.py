#cambiar el ultimo por el primero
datos=[11,3,4,15]
n =len (datos)
ultimo=n-1
datos[0],datos[ultimo] = datos[ultimo], datos[0]
print (datos)



#cambiar de valor una variable
a=3
b=5
temp=a   # temp ahora vale 3
a=b      # a ahora vale 5
b=temp    # b ahora vale 3
print (a)
