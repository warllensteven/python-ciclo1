cod = str(input("Ingrese su codigo: "))
nom = str(input("Ingrese su nombre: "))
estado = str(input("Ingrese su estado,V si es vigente o S si es suspendido: "))
estrato = int(input("Ingrese su estrato: "))
consumo = int(input("Ingrese el consumo de agua en cm3: "))


if estado == "v" or estado == "V":
   for i in range(0,6):
    if i == 1:
     est1 = 10000
     valor = (consumo * 200)
     valorFinal = est1 + (consumo * 200)
     print(f"{nom},{est1},{valor},{valorFinal}")
    if i == 2:
     est2 = 20000
     valor = (consumo * 200)
     valorFinal = est1 * (consumo * 200)
     print(f"{nom},{est1},{valor},{valorFinal}")
    if i == 3:
     est3 = 30000
     valor = (consumo * 200)
     valorFinal = est1 * (consumo * 200)
     print(f"{nom},{est1},{valor},{valorFinal}")
    if i == 4:
     est4 = 45000
     valor = (consumo * 200)
     valorFinal = est1 * (consumo * 200)
     print(f"{nom},{est1},{valor},{valorFinal}")
    if estrato == 5:
     est5 = 60000
     valor = (consumo * 200)
     valorFinal = est1 * (consumo * 200)
     print(f"{nom},{est1},{valor},{valorFinal}")
    if estrato == 6:
     est6 = 70000
     valor = (consumo * 200)
     valorFinal = est1 * (consumo * 200)
     print(f"{nom},{est1},{valor},{valorFinal}")
else:
  print("Su estado es suspendido")