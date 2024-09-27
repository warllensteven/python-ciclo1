#products = {
#idProduct (string): {
#“name” : (string),
#“price” : float (2 decimals),
#“quantity” : int (greater equal to 0),
#“discountList” : [ float (2 decimals), float (2

#decimals), ..., float (2 decimals) ]
#}
#}
import json
import pprint

def guardar(products):
    with open("sesion 8/productos.json", "w") as fd:
        json.dump(products, fd)

    if not fd.closed:
        fd.close()


def leerId():
    while True:
        try:
            cod = input("Id del producto? ")
            if len(cod.strip()) == 0:
                print(">>> Error. Id invalido")
                continue
            return cod
        except Exception as e:
            print("Error al ingresar el Id\n" + e)

def leerName():
    while True:
        try:
            name = input("Nombre del producto? ")
            if len(name.strip()) == 0:
                print(">>> Error. Nombre invalido")
                continue
            return name
        except ValueError:
            print("Error al ingresar el codigo\n")

def leerPrecio():
    while True:
        try:
            precio = float(input("Precio del producto? "))
            if precio <= 0:
                print("Precio incorrecto,por favor ingresar un precio valido")
                continue
            return precio
        except Exception as e:
            print(">>> Error al ingresar el precio" + e)

def leerQuantity():
    while True:
        try:
            cant = int(input("Ingresar la cantidad del producto en inventario: "))
            if cant <= 0:
                print("Cantidad incorrecto,por favor ingresar un cantidad valida")
                continue
            return cant
        except Exception as e:
            print(">>> Error al ingresar la cantidad" + e)

def leerDiscont():
    discontList = []
    while True:
        try:
            descuento = float(input("Ingrese un descuento del producto(-1 para terminar)"))
            if descuento == -1:
                break
            else:
                discontList.append(descuento)
            return discontList
        except ValueError:
            print(">>> Error al ingresar el descuento")

def opc1(dic):
    print("***Bienvenido a al apartadp de creacion de productos***".center(50))
    idProduct = leerId()
    dDatos = {}
    dDatos["name"] = leerName()
    dDatos["price"] = leerPrecio()
    dDatos["quantity"] = leerQuantity()
    dDatos["discountList"] = leerDiscont()
    while True:
        descuento = float(input("Ingrese un descuento del producto(-1 para terminar)"))
        if descuento == -1:
            break
        dDatos["discountList"].append(descuento)
        
    dic[idProduct] = dDatos
    return print(f"Producto agregado correctamente {dic}")

def opc2(dic):
    s = True
    print("Bienvenido al apartado de búsqueda de productos")
    idProduct = input("Ingresa el ID del producto que deseas buscar: ")
    while s:
        
        if idProduct in dic:
            print(f"Producto encontrado: {idProduct}")
            print(f"Nombre del producto: {dic[idProduct]['name']}")  
            print(f"Precio del producto: {dic[idProduct]['price']}") 
            print(f"Cantidad de producto en el inventario: {dic[idProduct]['quantity']}")     
            print(f"Descuentos del producto: {dic[idProduct]['discountList']}")
        else:
            print("Producto no encontrado") 
                
        x = int(input("Si desea salir oprima(1),si desea seguir buscando oprima(0)"))
        if x == 0:
            s = True
            idProduct = input("Ingresa el ID del producto que deseas buscar: ")
        else:
            s = False        
    


def opc4(dic):
    comparacion = []
    for d in dic:
        cant = d["quantity"]
        comparacion.append(cant)
    
    return comparacion.min()       


def menu():
    op = -1
    products = {}
    while op != 8:
        print("***PRODUCTOS ACME***".center(50))
        print("Menu".center(50))
        print(" 1. Agregar producto")
        print(" 2. Buscar producto")
        print(" 3. Listar producto")
        print(" 4. Listar producto con menos inventario")
        print(" 5. Listar producto con mayor porcentaje de descuento")
        print(" 6. Listar producto con menor precion con descuento")
        print(" 7. Listar producto con mayor precio en inventario")
        print(" 8. Salir")
        op = int(input("Escoja una opcion(1-8)?"))
        match op:
            case 1:
                opc1(products)
                products = guardar(products)
            case 2:
                opc2(products)
                
            case 3:
                opc1()
            case 4:
                opc4(products)
            case 5:
                opc1()  
            case 6:
                opc1() 
            case 7:
                opc1()          
            case _:
                pass
        

menu()

def opc4(dic):
    # Verificar si el diccionario está vacío
    if not dic:
        print("No hay productos en el inventario.")
        return

    # Inicializar variables para almacenar el producto con menor cantidad
    menor_producto = None
    menor_cantidad = float('inf')

    # Iterar por los productos en el diccionario
    for idProduct, info in dic.items():
        cant = info["quantity"]
        if cant < menor_cantidad:
            menor_cantidad = cant
            menor_producto = idProduct

    # Mostrar los detalles del producto con menor cantidad
    print(f"Producto con menor cantidad: {dic[menor_producto]['name']}, "
          f"ID: {menor_producto}, Cantidad: {menor_cantidad}")
