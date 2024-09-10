import random

puntos_totales = 1000000  # Número total de puntos a generar
puntos_en_circulo = 0     # Puntos dentro del círculo

for _ in range(puntos_totales):
    x = random.uniform(-1, 1)  # Coordenada x aleatoria
    y = random.uniform(-1, 1)  # Coordenada y aleatoria
    if x**2 + y**2 <= 1:       # Verificar si el punto está dentro del círculo
        puntos_en_circulo += 1

# Aproximación del valor de π
pi_aprox = 4 * puntos_en_circulo / puntos_totales
print(f"Valor aproximado de π: {pi_aprox}")
