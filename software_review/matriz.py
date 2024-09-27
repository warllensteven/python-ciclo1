import random

def crearMat(fil,col):
    matriz = []
    for f in range(fil):
        matriz.append([None] * col)
    return matriz

def printMat(mat):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            print(mat[f][c], end="\t")
        print("")

def InputMat(mat):
    for f in range(len(mat)):
        print("Fila", f+1)
        for c in range(len(mat[f])):
            mat[f][c] = int(input(f"mat[{f+1}][{c+1}]? "))

        print("-" * 10, "\n")

def randomtMat(mat, ini, fin):
    for f in range(len(mat)):
        for c in range(len(mat[f])):
            mat[f][c] = random.randrange(ini, fin)

        print("-" * 10, "\n")

def matrizIdentidad(mat):
    tamf = len(mat)
    tamc = len(mat[0])
    if tamf == tamc:
        for f in range(tamf):
            for c in range(tamc):
                if f != c:
                    mat[f][c] = 0
                else:
                    mat[f][c] = 1
        return mat
    else:
        return None
