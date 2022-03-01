def problema3(lista1, lista2):
    """
    functie prin care calculam produsul scalar a doi vectori rari
    verificam daca numerele de pe aceeasi pozitie din cei 2 vectori
    sunt nenule
    """

    suma = 0
    for i in range (len(lista1)):
        for j in range (len(lista2)):
            if i==j and lista1[i] != 0 and lista2[j] != 0:
                suma += lista1[i] * lista2[j]

    return suma

assert(problema3([1, 2, 0], [0, 5, 4]) == 10)
assert(problema3([1, 2, 0, 3, 0], [1, 0, 2, 1, 3]) == 4)