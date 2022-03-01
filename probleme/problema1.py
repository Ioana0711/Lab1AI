from sortari.merge_sort import merge_sort


def problema1(sir):
    """
    functia returneaza ultimul cuvant dpdv alfabetic dintr-o fraza
    :param sir: fraza initiala
    :return: ultimul cuvant dpdv alfabetic
    """
    cuvinte = sir.split(" ")
    merge_sort(cuvinte)
    return cuvinte[len(cuvinte)-1]

assert(problema1("Ana are mere rosii si galbene")=='si')
assert(problema1("Ana are mere rosii si galbene zi")=='zi')