fd = open("sesion 9\mbox.txt", "r")
email = set()
for linea in fd:
    if linea.startswith("From:"):
        correo = linea.split()[1]
        if correo not in email:
            print(correo,
                "--> Vota por mi  mascota :::> [CORREO ENVIADO]")
            email.add(correo)

