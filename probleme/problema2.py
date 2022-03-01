from cmath import sqrt
from numpy import square


def problema2(lista1, lista2):
    """
    functie prin care dam ca input 2 perechi  de numere pentru care calculam distanta euclidiana
    intre cele 2 locatii identificate prin cele doua perechi
    """

    dist = square(lista1[0] - lista2[0]) + square(lista1[1] - lista2[1])
    return sqrt(dist).real

assert(problema2([1, 5], [4, 1])==5.0)
assert(problema2([1, 0], [4, 0])==3)