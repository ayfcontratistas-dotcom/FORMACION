def calcula_precio(lprec,ldesc,liva):
    ldesc_eu=lprec*(ldesc/100)   #descuento precio*descuento en porcentaje que es dividido 100
    linc_iva=lprec*(liva/100)   #iva precio*iva en porcentaje que es dividido 100
    lprec_final=lprec-ldesc_eu+linc_iva  #precio - descuento + iva
    return lprec_final,ldesc_eu,linc_iva        #precio final

precio_inic=80
descuent=20
iva=21
prec_final, desc, iva=calcula_precio(precio_inic,descuent,iva)
print (f"precio inicial {precio_inic} descuento {desc:.2f} iva{iva:.2f} precio final{prec_final:.2f}")
print (f"precio inicial {precio_inic} descuento {desc:>10} iva{iva:>10} precio final{prec_final:>10}")
print (f"{precio_inic:10.2f} {desc:10.2f} {iva:10.2f} {prec_final:10.2f}")
print (f"{"precio ini":>16s} {"desc":>16s} {"iva":>16s} {"prec_final":>16s}")
print (f"{precio_inic:16.2f} {desc:16.2f} {iva:16.2f} {prec_final:16.2f}")
