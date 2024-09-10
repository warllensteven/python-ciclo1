#crear una funcion si una contraseeña  es aceptable
#es aceptable cuando:
# tenga de 3 a 20 caracteres

def validContrasena(contra):
    longContra = len(contra)
    if longContra >= 3 and longContra <= 20:
        return True
    else:
        return False
    
#programa que valide una contraseña
passw = input("Contraseña: ")
while not validContrasena(passw):
    passw = input("Contraseña ")

print("Ingrese")    