from itertools import *
from kdp_checker import *
import numpy as np

from kdp import Kdp


def iterate_over_all(n, k):
    arrays = [np.reshape(np.array(i), (k, n)) for i in product([0, 1], repeat=k * n)]
    for array in arrays:
        good = True
        for row in array:
            if 1 not in row or 0 not in row:
                good = False
                break
        for row in zip(*array):
            if 1 not in row or 0 not in row:
                good = False
                break
        if good:
            yield Kdp(array)
            # for i in range(k):
            #     for j in range(n):
            #         pass


def iterate_over_all_vectors(k):
    for i in range(2 ** k):
        vector = get_bin_vector(i)
        if 1 < sum(vector) < k:
            yield [0] * (k - len(vector)) + vector


def iterate_over_all_vectors_with_sum(k, s):
    for i in range(2 ** k):
        vector = get_bin_vector(i)
        if sum(vector) == s:
            yield [0] * (k - len(vector)) + vector


def iterate_over_all_balanced_matrices(n, k, s):
    vectors = list(iterate_over_all_vectors_with_sum(k, s))
    for combination in combinations(vectors, n):
        good = True
        for row in zip(*combination):
            if sum(row) != s:
                good = False
                break
        if good:
            yield Kdp(combination)


def iterate_over_all_matrices(n, k):
    vectors = list(iterate_over_all_vectors(k))
    for combination in combinations(vectors, n):
        good = True
        for row in zip(*combination):
            if not 1 < sum(row) < n:
                good = False
                break
        if good:
            yield Kdp(combination)


def get_bin_vector(n):
    binary = []
    while n != 0:
        bit = n % 2
        binary.append(bit)
        n //= 2
    binary.reverse()
    return binary


def add_row(kdp):
    returned = set()
    for row in iterate_over_all_vectors_with_sum(9, 8):
        new_kdp = Kdp.unite(kdp, Kdp([row]))
        if check_kdp(new_kdp):
            sorted_kdp = tuple(tuple(x for x in new_kdp.sorted()))
            if sorted_kdp not in returned:
                returned.add(sorted_kdp)
            yield sorted_kdp


for x2 in add_row(Kdp([[0, 1, 1, 1, 1, 1, 1, 1, 1]])):
    for x3 in add_row(x2):
        for x4 in add_row(x3):
            for x5 in add_row(x4):
                for x6 in add_row(x5):
                    print(repr(x6))
