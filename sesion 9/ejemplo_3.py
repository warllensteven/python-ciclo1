import io

fd = open("sesion 9\data.txt", "r")

cad = fd.readlines()
print(cad)


fd.close()