n = int(input("Cuantas palabras va a ingresar"))
p = input("Ingrese un prefijo para comparar")

sw = 1
cpre = 0
for i in range(n):
    w = input("Ingrese la palabra:")

    if w.startswith(p):
        cpre += 1

print(cpre)

