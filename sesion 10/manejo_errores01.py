from datetime import datetime

def leerFecha(msg):
    while True:
        try:
            #%d%m%Y es dd/mm/yyyy
            fecha = datetime.strptime(input(msg), "%d/%m/%Y")
            ano, mes, dia = str(fecha).split()[0].split("-")
            return f"{dia}/{mes}/{ano}"
        except ValueError:
            print("Error. formato de fecha invalido")

def leerFlotante(msg):
    while True:
        try:
            num = float(input(msg))
            return num
        except ValueError:
            print("Error. Ingrese un numero entero valido.n")

def leerEnteroPositivo(msg):
    while True:
        try:
            num = int(input(msg))
            if num < 0:
                print("Error. Ingrese un numero positivo\n")
                continue
            return num
        except ValueError:
            print("Error. Ingrese un numero entero valido.n")

def leerEntero(msg):
    while True:
        try:
            num = int(input(msg))
            break
        except ValueError:
            print("Error. Ingrese un numero entero valido.n")

    return num

#edad = leerEnteroPositivo("Ingrese la edad: " )

#print(edad, type(edad))

# temperatura = leerFlotante("Ingrese la edad: " )
# print(temperatura, type(temperatura))

fecnac = leerFecha("Ingrese la fecha de nacimiento: ")
print(fecnac)