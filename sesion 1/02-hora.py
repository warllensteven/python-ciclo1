print("Conversor de segundos a minutos y horas")
s = float(input("Introduzca segundos: "))
minutos = s / 60
horas = minutos / 60
minutosFinal = minutos % 60
segundosFinal = s % 60
print(f"las horas minutos son: {horas:.0f} horas, {minutosFinal:.0f} minutos, {segundosFinal:.0f} segundos")