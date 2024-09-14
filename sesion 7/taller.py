def aprob(definitiva):
   
   if definitiva >= 60:
      return True
   else:
      return False

n = int(input("Cantidad de estudiantes? "))

estudiantes = {}

for i in range(n):
    print(f"\n Estudiante {i+1}")
    codigo = input("Codigo? ")
    dNotas = {}
    dNotas["nombre"] = (input("Nombre? "))
    dNotas["nota 1"] = int(input("Ingrese la nota 1: "))
    dNotas["nota 2"] = int(input("Ingrese la nota 2: "))
    dNotas["nota 3"] = int(input("Ingrese la nota 3: "))
    dNotas["definitiva"] = (dNotas["nota 1"] * 0.30) + (dNotas["nota 2"] * 0.30) + (dNotas["nota 3"] * 0.40)

estudiantes[codigo] = dNotas
print(estudiantes)

if aprob(dNotas["definitiva"]):
   print("APROBADO")
else:
   print("REPROBADO")  # Este print no se ejecuta porque se encuentra fuera