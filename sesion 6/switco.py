def prodMAyIngSem(mat, lst):
    lsting = []
    for c in range(len(mat[c])):
        suma = 0
        for f in range(len(mat)):
            suma += mat[c][f] * lst[f]
        lsting.append(suma)

    mayor = max(lsting)       
    prod = lsting.index(mayor) + 1

    return [prod, mayor]

lstPrecios = [1500, 5000, 6500, 2500,22500]

ventas = [[100, 88, 92, 94, 85, 110, 100],
          [30, 42, 31, 32, 38, 40, 37],
          [23, 35, 39, 45, 55, 60, 61],
          [45, 50, 56, 65, 47, 57, 68],
          [18, 25, 33, 21, 22, 28, 32]]

prod, ingrprod = prodMAyIngSem(ventas,lstPrecios)
print("El proceso que genera mas ingresos en la semana es:"
    , prod, f" - Vendio: ${ingrprod:,}") 