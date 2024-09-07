print("Ingrese tres numeros enteros")
n1 = int(input("Ingrese primer numero: "))
n2 = int(input("Ingrese segundo numero: "))
n3 = int(input("Ingrese tercer numero: "))

if n1 > n2 and n1 > n3:
    if n2 > n3:
        print("El orden de los numeros de mayor a menor es: ",n1 , " " ,n2, " ",n3)

if n1 > n2 and n1 > n3:
    if n3 > n2:
        print("El orden de los numeros de mayor a menor es: ",n1 , " " ,n3, " ",n2)

if n2 > n1 and n2 > n3:
    if n1 > n3:
        print("El orden de los numeros de mayor a menor es: ",n2 , " " ,n1, " ",n3) 

if n2 > n1 and n2 > n3:
    if n3 > n1:
        print("El orden de los numeros de mayor a menor es: ",n2 , " " ,n3, " ",n1)           

if n3 > n1 and n3 > n2:
    if n1 > n2:
        print("El orden de los numeros de mayor a menor es: ",n3 , " " ,n1, " ",n2)              

if n3 > n1 and n3 > n2:
    if n2> n1:
        print("El orden de los numeros de mayor a menor es: ",n3 , " " ,n2, " ",n1)        
