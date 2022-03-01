from sortari.merge_sort import merge_sort

def problema7(lista_initiala, k):
    """
    problema determina al k lea cel mai mare element al listei initiale
    transformam lista initiala in multime pentru a elimina duplicatele
    apoi o readucem la forma de lista pentru a o putea parcurge
    sortam lista cu elemente unice si returam elementul cautat
    :param lista_initiala: lista de intreg
    :param k: intreg care reprezinta al catelea element cel mai mare il cautam
    :return: al k lea element cel mai mare
    """
    multime = set(lista_initiala)
    lista = list(multime)
    merge_sort(lista)
    return lista[len(lista)-k]

assert(problema7([2, 8, 7, 2, 2, 5, 2, 3, 1, 2, 2], 3)==5)
assert(problema7([7, 4, 6, 3, 9, 1], 3)==6)