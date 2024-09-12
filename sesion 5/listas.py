def posElemMayorList(lst):
  mayor = lst[0]
  pos = 0
  for i in range(len(lst)):
   if lst[i] > mayor:
      mayor = lst[i]
      pos = i
  return [pos, mayor]

#funcion mayor
def posMayorList(lst):
  mayor = lst[0]
  pos = 0
  for i in range(len(lst)):
   if lst[i] > mayor:
      mayor = lst[i]
      pos = i
  return pos

      

  return mayor 

#funcion mayor
def mayorLista(lst):
  mayor = 0
  for e in lst:
    if e > mayor:
      mayor = e

  return mayor 

#funcion menor
def menorLista(lst):
  menor = lst[0]
  for e in lst:
    if e < menor:
      menor = e

  return menor 


#funcion sumaLista
def sumaLista(lst):
  suma = 0
  for e in lst:
    suma += e

  return suma  


def imprimeList(lst):
  for e in lst:
    print(e, end=", ")
    print("")

listaNumeros = [10, 15, 20, 30, 40]
print(type(listaNumeros))
print(listaNumeros)
print(listaNumeros[3])
print(listaNumeros[-5])

#recorrer lista
#1.por sus posiciones
for i in range (len(listaNumeros)):
    print(listaNumeros[i], end=", ")
print("") 

for i in range(-1, -len(listaNumeros)-1, -1):
 print(listaNumeros[i], end="* ")
print("") 

for i in range(len(listaNumeros)-1, -1, -1):
 print(listaNumeros[i], end=", ")
print("")

#2. por sus elementos
for e in listaNumeros:
  print(e, end=" | ")
print("")

#llamado con funcion
imprimeList(listaNumeros)


#funcion que devuelve la suma de los numeros
print("la suma de los elementos de la lista es: ",sumaLista(listaNumeros))

#imprimir el elemento mayor de la lista
print("el mayor elemento de la lista es : ", mayorLista(listaNumeros))
#imprimir el elemento menor de la lista
print("el menor elemento de la lista es : ", menorLista(listaNumeros))
#imprimir la posicion del elemneto mayor de la lista
print("El elemento mayor se encuentra en la posicion: ", posMayorList(listaNumeros) + 1)
#imprimir la posicion del elemneto mayor y posicion de la lista
lstResult = posElemMayorList(listaNumeros)
print(f"El elemento mayor es {lstResult[1]} y su posicion es: {lstResult[0] + 1}")
#como modificar una lista
listaNumeros[-1] = 35

#operadores de las listas
#concatenacion
listaNumeros2 = [1, 2]
listaNumeros3 = listaNumeros + listaNumeros2
print(listaNumeros3)

#operador (*) repeticion
listaNumeros3 = listaNumeros2 * 3
print(listaNumeros3)