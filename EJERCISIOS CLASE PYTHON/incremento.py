def incre_relativo(lvi, lvf):
    lincre=(lvf-lvi)/lvi*100
    return lincre

vi=700
vf=720
incre=incre_relativo(vi,vf)
print ("incremento:",incre)