# Dada la base y la altura de un triangulo,calcular y mostrar su area, a traves de la formula area = (base*altura)/2
# Entrada
# b:base : float
# h:altura : float

b = float(input("Introduzca la base del triangulo: "))
h = float(input("Introduzca la altura del triangulo: "))

a = b * h / 2

print("El area del triangulo es: {:.1f}".format(a))

#formateando la salida con cadenas f-string
print(f"El area del triangulo es: {a:.1f}")
# Proceso
# a = b * h / 2
# Salida
# a:area : float