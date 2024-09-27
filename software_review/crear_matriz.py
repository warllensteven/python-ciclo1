# #matriz en forma vertical
# print("matriz en forma vertical")
# for i in range(0,6):
#     print(0)

# print()
# #matriz en forma horizontal

# print("matriz en forma horizontal")
# for i in range(0,6):
#     print(0, end=" ")
# print()

#matriz bidimensional

print("matriz bidimensional")
matriz = []
for fila in range(1,7):
    col1 = []
    for col in range(1,7):
        if fila == col:
            col1.append(1)
        else:
            col1.append(0)
    matriz.append(col1)        


print("matriz bidimensional")
matriz = []
for fila in range(1,7):
    col1 = []
    for col in range(1,7):
        if fila == col:
            col1.append(1)
        else:
            col1.append(0)
    matriz.append(col1) 


for lista in matriz:
    print(lista)

# matriz = [[1], [0], [0], [0], [0], [0],
#           [0], [1], [0], [0], [0], [0],
#           [0], [0], [1], [0], [0], [0],
#           [0], [0], [0], [1], [0], [0],
#           [0], [0], [0], [0], [1], [0],
#           [0], [0], [0], [0], [0], [1]]

