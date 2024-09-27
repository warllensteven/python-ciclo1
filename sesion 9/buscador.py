fd = open("sesion 9\mbox.txt", "r")

cont = 0
for linea in fd:
    if linea.startswith("From:"):
        cont += 1

print(cont)
