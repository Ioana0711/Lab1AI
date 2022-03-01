import numpy


def problema9(lista, matrice):
    """
    functie care calculeaza suma elementelor submatricei
    determinata de coordonatele a doua puncte ale matricei
    :param lista: lista cu coordonatele punctelor pentru care dorim
    sa aflam suma submatricei determinata de acestea
    :param matrice: matricea in care cautam submatricele a caror suma dorim sa o aflam
    :return: o lista cu sumele submatricelor dorite
    """
    sume = []
    matricea_mea = numpy.array(matrice)
    while lista:
        lista1 = lista[0]
        lista = lista[1:]
        p = lista1[0]
        q = lista1[1]
        r = lista1[2]
        s = lista1[3]

        suma = 0
        for i in range(p, r + 1):
            for j in range(q, s + 1):
                suma += matricea_mea[i][j]

        sume.append(suma)

    return sume


assert (problema9([[1, 1, 3, 3], [2, 2, 4, 4], [1, 2, 3, 3]],
                  [[0, 2, 5, 4, 1], [4, 8, 2, 3, 7], [6, 3, 4, 6, 2], [7, 3, 1, 8, 3], [1, 5, 7, 9, 4]]) == [38, 44,
                                                                                                             24])
assert (problema9([[1, 1, 3, 3], [2, 2, 4, 4]],
                  [[0, 2, 5, 4, 1], [4, 8, 2, 3, 7], [6, 3, 4, 6, 2], [7, 3, 1, 8, 3], [1, 5, 7, 9, 4]]) == [38, 44])
