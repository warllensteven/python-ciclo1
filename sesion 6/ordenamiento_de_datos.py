lista = ["Carlos", "Daniel", "Maria", "Laia", "Angel", "Oscar"]


nombre = "Maria"

if nombre in lista:
    pos = lista.index(nombre)
    print("Pasa al ciclo 3")
    print("posicion en la lsita es: ", pos)
else:
    print("Gracias por participar en python")   