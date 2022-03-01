from sortari.merge_sort import merge_sort
from sortari.quick_sort import quick_sort


def problema5(lista):
    """
    pentru a gasi elementul duplicat din lista
    sortam crescator lista iar apoi comparam elementele consecutive 2 cate 2
    pana cand gasim o potrivire
    :param lista: lista initiala
    :return: elementul duplicat
    """
    merge_sort(lista)
    #quick_sort(0, len(lista)-1, lista)

    for i in range (len(lista)-1):
        if lista[i] == lista[i+1]:
            return lista[i]

assert(problema5([1, 2, 3, 4, 2])==2)
assert(problema5([1, 2, 3, 4, 5, 1, 6, 8, 7])==1)