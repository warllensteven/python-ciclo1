import io

fd = open("sesion 9\data.txt", "r")

#RECORRIDO DE ARCHIVOS
for linea in fd:
    print(linea.strip().title())

fd.seek(0)

for car in fd.read():
    print(car.strip(), end=",")

fd.close()