import math

n = int(input("Ingrese un numero entero positivo mayor que 1 para saber si es narcisista: "))

if n > 0:
   lnum = int(math.log10(n)) + 1
   #print(lnum)
   
   suma = 0
   temp = n
   for i in range(1,lnum + 1):
       d = n % 10
       suma += d ** lnum
       n = n // 10

   if suma == temp:
       print("El numero es narciso")
   else:
       print("No es narciso")
else:
    print("Ingrese un numero entero positivo")