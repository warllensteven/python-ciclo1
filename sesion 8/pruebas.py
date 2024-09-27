def opc1(dic):
    print("***Bienvenido al apartado de creación de productos***".center(50))
    idProduct = input("Ingrese el id del producto: ")
    dDatos = {}
    dDatos["name"] = input("Nombre del producto? ")
    dDatos["price"] = float(input("Precio del producto? "))
    dDatos["quanty"] = int(input("Unidades del producto? "))
    
    while dDatos["quanty"] <= 0:
        dDatos["quanty"] = int(input("El número de unidades debe ser mayor a 0, ¿cuántas unidades son? "))
    
    dDatos["discountList"] = []
    while True:
        descuento = float(input("Ingrese un descuento del producto (-1 para terminar): "))
        if descuento == -1:
            break
        dDatos["discountList"].append(descuento)
    
    dic[idProduct] = dDatos
    print(f"Producto agregado correctamente: {dic}")

def opc2(dic):
    print("Bienvenido al apartado de búsqueda de productos")
    idProduct = input("Ingresa el ID del producto que deseas buscar: ")
    if idProduct in dic:
        print(f"Producto encontrado: {dic[idProduct]}")
    else:
        print("Producto no encontrado")

def menu():
    op = -1
    products = {}
    while op != 8:
        print("***PRODUCTOS ACME***".center(50))
        print("Menu".center(50))
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Listar productos")
        print("4. Listar producto con menos inventario")
        print("5. Listar producto con mayor porcentaje de descuento")
        print("6. Listar producto con menor precio con descuento")
        print("7. Listar producto con mayor precio en inventario")
        print("8. Salir")
        
        op = int(input("Escoja una opción (1-8): "))
        
        match op:
            case 1:
                opc1(products)
            case 2:
                opc2(products)
            case 3:
                print("Función no implementada")
            case 4:
                print("Función no implementada")
            case 5:
                print("Función no implementada")
            case 6:
                print("Función no implementada")
            case 7:
                print("Función no implementada")
            case 8:
                print("Saliendo del programa...")
            case _:
                print("Opción inválida, intenta de nuevo")

menu()
