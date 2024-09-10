print("Programa para calcular calificaciones")

nom = str(input("Ingrsa tu nombre: "))

n1 = float(input("Ingrese la nota 1 del parcial: "))

n2 = float(input("Ingrese la nota 2 del parcial: "))

n3 = float(input("Ingrese la nota 3 del parcial: "))

n4 = float(input("Ingrese la nota de ingles: "))

nota1 = n1 * 0.20
nota2 = n2 * 0.25
nota3 = n3 * 0.35
nota4 = n4 * 0.20
definitiva = nota1 + nota2 + nota3 + nota4

print(f"{nom}, tu nota definitiva es: {definitiva:.1f}")