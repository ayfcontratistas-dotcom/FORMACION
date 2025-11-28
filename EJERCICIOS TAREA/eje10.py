def precio_final(p_org_pro,porcentaje_descuento):
    valor_descuento=(p_org_pro*porcentaje_descuento)/100
    valor_neto=p_org_pro-valor_descuento
    return valor_descuento,valor_neto

gp_org_pro=250
gporcentaje_descuento=10
valor_descuento,valor_neto=precio_final(gp_org_pro,gporcentaje_descuento)
print("p_org_pro,porcentaje:",gp_org_pro,"  ","descuento:",valor_descuento,"  ","pago:",valor_neto)