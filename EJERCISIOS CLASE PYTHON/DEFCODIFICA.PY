def dec_tiempo(segi):
    h= segi//3600
    resto=segi%3600
    min= resto//60
    seg= resto%60
    return h, resto, min, seg

lsegi=6030
lh, lresto, lmin, lseg= dec_tiempo(lsegi)
print ("hora:",lh, " ",  "minutos:",lmin, " ", "segundos:",lseg)




def codifica(hora,min,seg):
    seg_sal=(hora*3600+min*60+seg)
    return seg_sal

lhora=1
lmin=40
lseg=30
lseg_sal=codifica(lhora,lmin,lseg)
print ("total_seg:",lseg_sal)

             
   

    
