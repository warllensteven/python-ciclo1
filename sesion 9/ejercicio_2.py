#Escriba un programa que envie un mensaje "Vota por mi mascota" a todos los correos que aparecen en el From:
#Su programa debe mostrar un mensaje como el siguiente por cada correo:
#cwen@iupi.edu --> "Vota por mi  mascota" :::> [CORREO ENVIADO]



for linea in fd:
    if linea.startswith("From:"):
        i = linea.split(",")
        print(f"{i[5:-1]} --> 'Vota por mi  mascota' :::> [CORREO ENVIADO]")



