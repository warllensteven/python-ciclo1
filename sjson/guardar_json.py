import json

lista = ["Daniel", "Maria", "Ada", "Gabriel", ["Daniel", "Ricardo"]]

# campers = {
#     1: {
#         "nombre": "Daniel",
#         "edad": 20,
#         "sexo": "f",
#         "telefonos": [123, 456]
#     },

#     2: {
#         "nombre": "Maria",
#         "edad": 21,
#         "sexo": "m",
#         "telefonos": [789]
#     }
# }

with open("json/datos.json", "w") as fd:
    json.dump(lista, fd)

if not fd.closed(): #True si el archivo esta cerrado
    fd.close()