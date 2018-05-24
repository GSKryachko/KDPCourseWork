from Theorem2 import *


def build_scheme_by_theorem_3(first: Kdp, second: Kdp, oa):
    third = build_scheme_using_oa(first, oa)
    fourth = expand_scheme(second, first.blocks)
    return Kdp.unite(third, fourth)


def expand_scheme(scheme: Kdp, k):
    new_scheme = []
    for row in scheme:
        new_scheme.append([])
        for value in row:
            new_scheme[-1].extend([value] * k)
    return Kdp(new_scheme)
