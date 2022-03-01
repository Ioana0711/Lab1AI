def problema6(lista):
    """
    numaram de cate ori apare fiecare element din lista
    daca apare de mai mult de n/2 ori, il returnam
    :param lista: lista initiala de numere
    :return: elementul care apare de mai mult de n/2 ori, daca exista
    """
    for i in range(len(lista)):
        count = 0
        for j in range(len(lista)):
            if lista[i] == lista[j]:
                count += 1

        if count > len(lista)/2:
            return lista[i]


assert(problema6([2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2])==2)
assert(problema6([1, 1, 3, 1, 5, 3, 1, 1, 2, 1])==1)