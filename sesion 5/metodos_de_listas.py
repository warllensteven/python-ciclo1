lista = [10, "Juan", 30, "Sergio"]
#append
lista.append(40) #añade un elemeto al final de la lista
print(lista)
#extend
lista2 = ["Maria", 20]
lista.extend(lista2)
print(lista)
#inser
lista.insert(2, 50)
print(lista)
#pop
lista.pop(2)
print(lista)
#remove
lista.remove("Sergio")
print(lista)