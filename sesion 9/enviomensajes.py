with open("sesion 9\mbox.txt", "r") as fd:
    listaEmail = []
    for linea in fd:
        if linea.startswith("From:"):
            correo = linea.split()[1] + "enviado [ok]\n"
            if correo not in listaEmail:
                listaEmail.append(correo)

listaEmail.reverse()  #[::-1]

with open("sesion 9\correos.txt", "w") as fd:
    fd.writelines(listaEmail)