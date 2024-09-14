#Diccionarios

dCampers = {1:"Ada", 2:"Juan", 3:"Diego", 4:"Oscar", 5:"Anderson"}
print(dCampers)

#crear diccionario vacio
#dcampers = {}
#dcampers = dict()
#print(dcampers)

print(dCampers.setdefault(4))#existe

#print(dCampers.setdefault(6))##no existe

print(dCampers.setdefault(6, "Maria"))
print(dCampers)

dCategoria = {1:25_000, 2:30_000, 3: 40_000, 4:45_000, 5:
              60_000}

print(dCategoria.items())

for k, v in dCategoria.items():
    print(k, v)

dCategoria.pop(4)
print(dCategoria)

for v in dCategoria.values():
    print(v)