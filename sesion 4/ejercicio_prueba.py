

sw = True




while sw:
 t1 = int(input("Ingresa la temperatura 1:"))
 t2 = int(input("Ingresa la temperatura 2:"))
 if t1 == 0:
  sw = False
 promedio = (t1 + t2) / 2
 if t1 >= 5 and t1 <= 15 and t2 >= 5 and t2 <= 15:
  print(f"el promedio de las temperaturas ingresadas es {promedio}")
  t1 = int(input("Ingresa la temperatura 1:"))
  t2 = int(input("Ingresa la temperatura 2:"))
  if t1 == 0:
   sw = False
