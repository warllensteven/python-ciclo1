#Eliminación de espacios en blanco (Whitespace)
s = ' A sentence with whitespace. \n'
print('{}'.format(s.lstrip()))  # "A sentence with whitespace. \n" (sin espacios al inicio)
print('{}'.format(s.rstrip()))  # " A sentence with whitespace." (sin espacios al final)
print('{}'.format(s.strip()))   # "A sentence with whitespace." (sin espacios al inicio y al final)

print('{}'.format(s.rstrip('A')))  # Elimina la 'A' al final si existe.

#División de cadenas (Splitting Strings)
s = 'KDnuggets is a fantastic resource'
print(s.split())  # ['KDnuggets', 'is', 'a', 'fantastic', 'resource']

s = 'these,words,are,separated,by,comma'
print(s.split(','))  # ['these', 'words', 'are', 'separated', 'by', 'comma']

#Unir elementos de una lista en una cadena (Joining List Elements)
s = ['KDnuggets', 'is', 'a', 'fantastic', 'resource']
print(' '.join(s))  # "KDnuggets is a fantastic resource"

s = ['Eleven', 'Mike', 'Dustin', 'Lucas', 'Will']
print(' and '.join(s))  # "Eleven and Mike and Dustin and Lucas and Will"

#Invertir una cadena (Reversing a String)
s = 'KDnuggets'
print('The reverse of KDnuggets is {}'.format(s[::-1]))  # "steggunDK"

# Convertir mayúsculas y minúsculas (Converting Uppercase and Lowercase)
#upper() convierte la cadena a mayúsculas.
#lower() convierte la cadena a minúsculas.
#swapcase() intercambia mayúsculas y minúsculas.
s = 'KDnuggets'
print(s.upper())  # "KDNUGGETS"
print(s.lower())  # "kdnuggets"
print(s.swapcase())  # "kdNUGGETS"

#6. Verificación de membresía en cadenas (Checking for String Membership)
#Usa el operador in para verificar si una subcadena está presente en otra cadena.
s1 = 'perpendicular'
s2 = 'pen'
s3 = 'pep'
print('\'pen\' in \'perpendicular\': {}'.format(s2 in s1))  # True
print('\'pep\' in \'perpendicular\': {}'.format(s3 in s1))  # False

#7. Encontrar la ubicación de una subcadena (Find the location of a substring)
#find() devuelve el índice de la primera aparición de una subcadena. Si no la encuentra, devuelve -1.
s = 'Does this string contain a substring?'
print('\'string\' location -> {}'.format(s.find('string')))  # 10
print('\'spring\' location -> {}'.format(s.find('spring')))  # -1

#8. Reemplazar subcadenas (Replacing Substrings)
#replace() reemplaza todas las ocurrencias de una subcadena por otra
s1 = 'The theory of data science is of the utmost importance.'
s2 = 'practice'
print(s1.replace('theory', s2))  # "The practice of data science is of the utmost importance."

#9. Combinar el contenido de múltiples listas (Combining Multiple Lists)
#zip() combina elementos de múltiples listas elemento por elemento.
countries = ['USA', 'Canada', 'UK', 'Australia']
cities = ['Washington', 'Ottawa', 'London', 'Canberra']
for x, y in zip(countries, cities):
    print('The capital of {} is {}.'.format(x, y))
#salida
#The capital of USA is Washington.
#The capital of Canada is Ottawa.
#The capital of UK is London.
#The capital of Australia is Canberra.

#10. Verificar anagramas (Checking for Anagrams)
#Los anagramas tienen las mismas letras en diferentes órdenes. 
#Puedes usar Counter de la librería collections para comparar las frecuencias de las letras.
from collections import Counter
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

print('listen is an anagram of silent -> {}'.format(is_anagram('listen', 'silent')))  # True

#11. Verificar palíndromos (Checking for Palindromes)
#Un palíndromo es una palabra que se lee igual hacia adelante y hacia atrás. 
#Para verificarlo, invierte la cadena y compárala con la original.
def is_palindrome(s):
    reverse = s[::-1]
    return s == reverse

print('racecar is a palindrome -> {}'.format(is_palindrome('racecar')))  # True
