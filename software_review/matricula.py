matricula = 10000  # Matrícula inicial
años = 0           # Número de años
tasa = 0.07        # Tasa de aumento anual

while matricula < 20000:  # Bucle hasta que la matrícula se duplique
    matricula += matricula * tasa
    años += 1

print(f"Tomará {años} años para que la matrícula se duplique.")

