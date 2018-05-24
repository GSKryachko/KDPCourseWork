import math

import numpy
import scipy.special

# from kdp_iterator import *

format_string = '{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}'


# for x in iterate_over_all_balanced_matrices(12, 9, 7):
#     print(x)
#     print('-' * 4)

def choose_max_from_k(k):
    return int(scipy.special.binom(k, k // 2))


def get_min_keys_for_member(k, n, l):
    for i in range(math.ceil(l) + 1):
        if scipy.special.binom(k, i) > (n * (n - 1) // 2):
            return i


def show_l_constraints(n):
    format_string = '{:<10} {:<10} {:<10} {:<10} {:<10} {:<10}'
    print(format_string.format('members', 'keys', 'm',
                               'choose(b,m)', 'pairs', 'choose(k,m)'))
    for i in range(3, n):
        keys = i - 1
        max_kpm = keys - 1
        max_partners = choose_max_from_k(max_kpm)
        max_different_subsets = choose_max_from_k(keys)
        members = i * (i - 1) // 2
        print(format_string.format(i, keys, max_kpm, max_partners,
                                   members, max_different_subsets))


# show_l_constraints(13)

keys = 9
max_kpm = keys - 1
max_partners = choose_max_from_k(max_kpm)
max_different_subsets = choose_max_from_k(keys)
members = 12 * (12 - 1) // 2
print(format_string.format('members', 'keys', 'm',
                           'choose(b,m)', 'pairs', 'choose(k,m)'))
print(format_string.format(members, keys, max_kpm, max_partners,
                           members, max_different_subsets))


def generate_kdp():
    k_i_lower = 6
    k_i_higher = 8
    for i in range(k_i_lower, k_i_higher + 1):
        for combination in combinations(range(9), i):
            yield tuple(1 if x in combination else 0 for x in range(9))


def get_intersection(a, b):
    return tuple([x * y for x, y in zip(a, b)])


def filter(kdps):
    ans = []
    intersections = set()
    for kdp in kdps:
        banned = False
        for kdp_2 in ans:
            intersection = get_intersection(kdp, kdp_2)
            # if sum(intersection) > 4:
            if not 2 <= sum(intersection) <= 5 or intersection in intersections:
                banned = True
        if not banned:
            ans.append(kdp)
            for kdp_2 in ans:
                intersection = get_intersection(kdp, kdp_2)
                intersections.add(intersection)
    return ans


