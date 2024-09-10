#funcion que reciba un numero y me devualva true si es primo o false si no lo es

def esPrimo(num):
    if num > 1:
     esPrimo = True
     for i in range(2,num):
      if num % i == 0:
       esPrimo = False
       break
     
      if esPrimo:
       return True
      else:
       return False  

    else:
        return False  
    

#Programa que reciba una serie de numeros hasta que se ingrese un primo
n = int(input("Numero? "))
while not esPrimo(n):
  n = int(input("Numero? "))

  