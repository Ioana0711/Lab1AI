import numpy


def problema10(matrice):
    """
    functie care cauta linia unei matrici
    care contine cele mai multe valori de 1
    comparand sumele liniilor intre ele
    :param matrice: matricea initiala ce contine 0 si 1
    :return: indexul liniei din matrice cu cele mai multe valori de 1
    """
    matrice_noua = numpy.array(matrice)
    sume = []
    while matrice:
        suma = 0
        lista1 = matrice[0]
        matrice = matrice[1:]
        for i in range(len(lista1)):
            suma += lista1[i]
        sume.append(suma)

    poz = 0
    maxim = sume[0]
    for i in range(1, len(sume)):
        if maxim < sume[i]:
            maxim = sume[i]
            poz = i
    return poz


assert (problema10([[0, 0, 0, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1]]) == 1)
assert (problema10([[0, 0, 0, 1, 1], [0, 1, 1, 1, 1], [0, 0, 1, 1, 1], [1, 1, 1, 1, 1]]) == 3)
