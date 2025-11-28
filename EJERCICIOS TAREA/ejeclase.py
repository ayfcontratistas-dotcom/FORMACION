def suma_media(nota1,nota2,nota3):
    sum=nota1+nota2+nota3
    med=sum//3
    return sum, med


lnota1=8
lnota2=5
lnota3=9
lsum, lmed = suma_media(lnota1,lnota2,lnota3)
print ("suma:",lsum, " " ,"media:",lmed)