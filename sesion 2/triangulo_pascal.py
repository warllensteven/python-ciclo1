# Solicitar al usuario el número de filas del Triángulo de Pascal
n = int(input("Ingrese el número de filas para el Triángulo de Pascal: "))

# Generar y mostrar el Triángulo de Pascal
for i in range(n):
    valor = 1   
    for j in range(i + 1):
        print(valor, end=" ")
        valor = valor * (i - j) // (j + 1)
    print()