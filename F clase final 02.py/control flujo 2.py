edad=22

if (edad<18):
    print ("acceso denegado")

if (edad>50):
    print ("vayase a dormir viejito")

else:
    print ("accseo aprobado")




def acceso (edad): #utilizando funcion
    lapro=edad>=18
    ldene=edad<18
    return lapro


apro=acceso(edad)
print (apro)






