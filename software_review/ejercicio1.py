num = input("Ingrese el numero de telefono: ")
numFinal = len(num)
print(numFinal)

final = " "

for c in num:
    print(c)
    for c in range(3,numFinal-3):
        final = final + c