#for i in range(0,10,3):
#    print(i , end=", ")

#mostrar los divisores de un numero ingresado por el usuario

n = int(input("Ingrese un numero entero positivo mayor que 1: "))

if n > 1:
    for d in range(1,n):
     if n % d == 0:
        print(d, end=", ")



else:
    print("Error . El numero debe ser mayor que 1.")