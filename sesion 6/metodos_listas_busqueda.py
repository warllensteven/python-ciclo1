#algo busqueda lineal
def busquedaLineal(lst, elem):
    for i in range(len(lst)):
     if lst[i] == elem:
        return [True, i]
    return [False, None]     

list = ["Carlos", "Daniel", "Maria", "Laia", "Angel"]

existe, pos = busquedaLineal(list, "Gabo")

if existe:
   print("Pasa al ciclo 3")
   print("Posicion:", pos)
else:
   print("Muchas gracias por estar en campus") 