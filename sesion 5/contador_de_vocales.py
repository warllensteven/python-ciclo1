def imprimeList(lst):
  for e in lst:
    print(e, end=" | ")

n = int(input("Cuantas letras va a ingresar: "))

vocales = [0] * 5

for i in range(n):
    letra = input(f"Ingrese la letra {i+1}: ")
    letra = letra.strip()
    if len(letra) > 0:
        letra = letra[0]
      #  if letra.lower() == "a":
       #     vocales[0] += 1
        #elif letra.lower() == "e":
        #    vocales[1] += 1    
        #elif letra.lower() == "i":
        #    vocales[2] += 1 
        #elif letra.lower() == "o":
         #   vocales[3] += 1 
        #elif letra.lower() == "u":
         #   vocales[4] += 1           
    match letra:
        case "a":
            vocales[0] += 1
        case "e":
            vocales[1] += 1
        case "i":
            vocales[2] += 1
        case "o":
            vocales[3] += 1
        case "u":
            vocales[4] += 1   
        case _:
            pass             


imprimeList(vocales)