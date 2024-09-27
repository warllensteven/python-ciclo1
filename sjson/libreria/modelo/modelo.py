import pprint

from persistencia.persistencia import guardar

def leerPrecio():
    while True:
        try:
            precio = int(input("Precio del libro? "))
            if precio < 500:
                print(">>> Error. Precio incorrecto")
                continue
            return precio      
        except ValueError:
            print("Error al ingresar el precio del libro\n")

def leerAutor():
    while True:
        try:
            aut = input("Autor del libro? ")
            if len(aut.strip()) == 0:
                print(">>> Error. Autor invalido")
                continue
            return aut
        except Exception as e:
            print("Error al ingresar el autor\n" + e)

def leerTitulo():
    while True:
        try:
            tit = input("Titulo del libro? ")
            if len(tit.strip()) == 0:
                print(">>> Error. Codigo invalido")
                continue
            return tit
        except Exception as e:
            print("Error al ingresar el titulo\n" + e)

def leerCodigo():
    while True:
        try:
            cod = input("Codigo del libro? ")
            if len(cod.strip()) == 0:
                print(">>> Error. Codigo invalido")
                continue
            return cod
        except Exception as e:
            print("Error al ingresar el codigo\n" + e)


def insertar(libreria, arch):
    print("\n\n**1. Insertar ***")

    cod = leerCodigo()
    if cod not in libreria:
        titulo = leerTitulo()
        autor = leerAutor()
        precio = leerPrecio()

        datlib = {
            "titulo": titulo,
            "autor": autor,
            "precio": precio
        }

        libreria[cod] = datlib
        # pprint.pprint(libreria)
        libreria = dict(sorted(libreria.items()))
        #pprint.pprint(libreria)
        
        guardar(libreria, arch)

    else:
        print("El codigo ya existe en la libreria")

    return libreria

    input("Presione cualquier tecla para volver al menu")

def consultar(lib):
    print("\n\n**2. Consultar ***")
    
    cod = input("\n Codigo del libro? ")

    if cod in lib:
        print("--> Codigo", cod)
        print(f"-> Titulo: {lib[cod]['titulo']}")
        print(f"-> Autor: {lib[cod]['autor']}")
        print(f"-> Precio: ${lib[cod]['precio']:,.0f}")
    else:
        print(">>> Error el codigo del libro no existe en la libreria")


    input("Presione cualquier tecla para volver al menu")
