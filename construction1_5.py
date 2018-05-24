from kdp import Kdp

"""
Takes two kdps and returns third with n_1 + n_2 members and k_1 * k_2 keys.
New scheme is not guaranteed to save collusion-resistance
"""


def construct_kdp(first: Kdp, second: Kdp):
    incidence_matrix = []
    for i in range(first.points + second.points):
        incidence_matrix.append([])
        for x in range(first.blocks):
            for y in range(second.blocks):
                if i < first.points and first[i][x]:
                    incidence_matrix[i].append(1)
                elif i >= first.points and \
                        second[i - first.points][y]:
                    incidence_matrix[i].append(1)
                else:
                    incidence_matrix[i].append(0)
    return Kdp(incidence_matrix)
