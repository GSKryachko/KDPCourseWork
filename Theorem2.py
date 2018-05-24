from kdp import *
from oabuilder import *


def build_scheme_using_oa(scheme: Kdp, oa):
    new_kdp = []
    for row in oa:
        new_kdp.append([])
        for number in row:
            new_kdp[-1].extend(scheme[number])
    return Kdp(new_kdp)


"""
Returns new Kdp(n*2,...) by Kdp(n,k). n should be a power of a prime.

"""


def build_scheme_by_theorem_2(scheme: Kdp):
    oa = build_oa(scheme.points, scheme.points + 1, 2, 1)
    return build_scheme_using_oa(scheme, oa)
