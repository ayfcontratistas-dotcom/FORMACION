def cantidad_horas(cantidad_minutos):
    HORA=60
    qt_horas =cantidad_minutos//HORA
    qt_minutos = cantidad_minutos%HORA
    return qt_horas, qt_minutos

gcantidad_minutos=135
ghoras, gminutos =cantidad_horas(gcantidad_minutos)
print("horas:",ghoras,"  ","minutos:" ,gminutos)

