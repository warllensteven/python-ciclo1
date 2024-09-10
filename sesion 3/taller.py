nom = input("Ingrese un nombre: ")
estrato = int(input("Ingrese su estrato: "))
conf = True

while conf:
    taf_basic = 0
    if estrato == 1:
        taf_basic = 10_000
    elif estrato == 2:
        taf_basic = 20_000
    elif estrato == 3:
        taf_basic = 30_000
    elif estrato == 4:
        taf_basic = 45_000
    elif estrato == 5:
        taf_basic = 60_000            

    print("\n", "=" * 40)
    print("Nombre:",nom)
    print("Tarifa basica:",taf_basic)
    print("\n", "=" * 40)

    opcion = input("\n>>> Desea continuar (S/N)")
    
    if opcion == "N" or opcion == "n":
        continuar = False
    else:
        print("\n", "=" * 40)
        nom = input("Ingrese un nombre: ")
        estrato = int(input("Ingrese su estrato: "))    