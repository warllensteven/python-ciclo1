# Métodos de strings más utilizados en Python con ejemplos

# 1. upper() - Convierte todas las letras en mayúsculas
cadena = "hola mundo"
print("1. upper():", cadena.upper())  # "HOLA MUNDO"

# 2. lower() - Convierte todas las letras en minúsculas
cadena = "HOLA MUNDO"
print("2. lower():", cadena.lower())  # "hola mundo"

# 3. capitalize() - Convierte la primera letra a mayúscula
cadena = "python es genial"
print("3. capitalize():", cadena.capitalize())  # "Python es genial"

# 4. title() - Convierte la primera letra de cada palabra en mayúscula
cadena = "python es genial"
print("4. title():", cadena.title())  # "Python Es Genial"

# 5. strip() - Elimina los espacios en blanco iniciales y finales
cadena = "   espacio extra   "
print("5. strip():", cadena.strip())  # "espacio extra"

# 6. lstrip() - Elimina los espacios en blanco solo al inicio
cadena = "   espacio extra   "
print("6. lstrip():", cadena.lstrip())  # "espacio extra   "

# 7. rstrip() - Elimina los espacios en blanco solo al final
cadena = "   espacio extra   "
print("7. rstrip():", cadena.rstrip())  # "   espacio extra"

# 8. find() - Encuentra la primera aparición de una subcadena, devuelve el índice
cadena = "aprendiendo python"
print("8. find():", cadena.find("python"))  # 12

# 9. replace() - Reemplaza una subcadena por otra
cadena = "me gusta python"
print("9. replace():", cadena.replace("python", "programar"))  # "me gusta programar"

# 10. split() - Divide una cadena en una lista utilizando un delimitador (por defecto es espacio)
cadena = "me gusta python"
print("10. split():", cadena.split())  # ['me', 'gusta', 'python']

# 11. join() - Une una lista de cadenas con un delimitador
lista = ["me", "gusta", "python"]
print("11. join():", " ".join(lista))  # "me gusta python"

# 12. startswith() - Verifica si una cadena empieza con una subcadena
cadena = "aprendiendo python"
print("12. startswith():", cadena.startswith("aprendiendo"))  # True

# 13. endswith() - Verifica si una cadena termina con una subcadena
cadena = "aprendiendo python"
print("13. endswith():", cadena.endswith("python"))  # True

# 14. isdigit() - Verifica si la cadena contiene solo dígitos
cadena = "12345"
print("14. isdigit():", cadena.isdigit())  # True

# 15. isalpha() - Verifica si la cadena contiene solo letras
cadena = "hola"
print("15. isalpha():", cadena.isalpha())  # True

# 16. isnumeric() - Verifica si la cadena contiene solo caracteres numéricos
cadena = "12345"
print("16. isnumeric():", cadena.isnumeric())  # True

# 17. count() - Cuenta el número de veces que aparece una subcadena en la cadena
cadena = "me gusta python porque python es fácil"
print("17. count():", cadena.count("python"))  # 2

# 18. format() - Formatea la cadena utilizando marcadores de posición
nombre = "Ana"
edad = 25
print("18. format():", "Mi nombre es {} y tengo {} años.".format(nombre, edad))  # "Mi nombre es Ana y tengo 25 años."

# 19. zfill() - Rellena la cadena con ceros al inicio hasta alcanzar la longitud indicada
cadena = "5"
print("19. zfill():", cadena.zfill(3))  # "005"

# 20. swapcase() - Cambia las letras mayúsculas por minúsculas y viceversa
cadena = "Hola Mundo"
print("20. swapcase():", cadena.swapcase())  # "hOLA mUNDO"
