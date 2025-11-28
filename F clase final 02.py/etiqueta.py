def clasifica_edad(ledad):
    if (ledad<=18):
        letiqueta = "menor de edad"
    elif (ledad<=45):
        letiqueta = "joven"
    elif (ledad<=60):
        letiqueta = "adulto maduro"
    else:
        letiqueta = "adulto mayor"
    return letiqueta

print(clasifica_edad(12))
