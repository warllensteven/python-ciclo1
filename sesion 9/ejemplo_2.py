import io

fd = open("sesion 9\data.txt", "r")

cad = fd.readline().strip()
print(cad)

cad = fd.readline().strip()
print(cad)

fd.close()