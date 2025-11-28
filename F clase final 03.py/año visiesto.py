año=1900
if ((año%400==0) or (año%4==0) and (año %100 !=0)):
    print ("bisiesto")
else:
    print ("no bisiesto")



def bisiesto (año):
    result= ((año%400==0) or (año%4==0) and (año %100 !=0))
    return result

result=bisiesto(año)
print (result)




def bisiesto (laño):
    lresult= ((año%400==0) or (año%4==0) and (año %100 !=0))
    return lresult

result=bisiesto(año)
print (result)


bisiesto =lambda año:((año%400==0) or (año%4==0) and (año %100 !=0))
print (bisiesto(año))

