n = int(input("Ingrese un numero entero positivo mayor que 1 para saber si es perfecto: "))

if n > 1:
    suma = 0
    for d in range(1,n):
     if n % d == 0:
        suma += d
        
    if suma == n:
           print("Es perfecto")
    else:
           print("No es perfecto")



else:
    print("Error . El numero debe ser mayor que 1.")