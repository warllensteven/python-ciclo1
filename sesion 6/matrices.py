#matrices
def ingresarDatosM(mat):
   for f in range(len(mat)):
      print(f"Ingrese datos de la fila{f+1}")
      for c in range(len(mat[f])):
         mat[f][c]= int(input(f"mat[{f+1}][{c+1}]? *"))


def imprimirMatriz(m):
   for f in range(len(m)):
      for c in range(len(m[f])):
         print(m[f][c], end="\t")
      print("")


def crearMatriz(fil,col):
    m = []
    for f in range(fil):
      m.append([None] * col)
  
    return m      


m = [[1, 2, 3], [4, 5, 6]] #2x3

print(m[1][1])

mat = []

mat = crearMatriz(5, 7)
ingresarDatosM(mat)
imprimirMatriz(mat)