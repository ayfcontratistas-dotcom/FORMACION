data={"enero":33}
salarios={"honorarios":[12,13,34,35]}

c= data.get("enero")
d= salarios.get("honorarios")

print (c)
print(d)

#mas corta
persona = {"nombre": "Freddy", "ciudad": "Jaén", "departamento": "andalucia", "pueblo": "mancha real"}
print(persona.get("nombre"))  
print(persona.get("pueblo"))  