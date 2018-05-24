from kdp import Kdp
from itertools import *


def check_kdp(kdp: Kdp):
    for combination in combinations([x for x in range(kdp.points)], 2):
        other_members = {x for x in range(kdp.points) if x not in combination}
        for j in range(kdp.blocks):
            if kdp[combination[0]][j] == kdp[combination[1]][j] == 1:
                for i in other_members.copy():
                    if kdp[i][j] == 0:
                        other_members.remove(i)
        if other_members:
            # print(combination, other_members)
            return False
    return True


kdp10_9 = [[0, 0, 1, 1, 1, 1, 1, 1, 1],
           [1, 0, 0, 1, 1, 1, 1, 1, 1],
           [1, 1, 0, 0, 1, 1, 1, 1, 1],
           [1, 1, 1, 0, 0, 1, 1, 1, 1],
           [1, 1, 1, 1, 0, 0, 1, 1, 1],
           [1, 1, 1, 1, 1, 0, 0, 1, 1],
           [1, 1, 1, 1, 1, 1, 0, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 0, 0],
           [0, 1, 1, 1, 1, 1, 1, 1, 0],
           [0, 1, 1, 0, 1, 1, 1, 1, 1]]
kdp9_9 = [[0, 0, 1, 1, 1, 1, 1, 1, 1],
          [1, 0, 0, 1, 1, 1, 1, 1, 1],
          [1, 1, 0, 0, 1, 1, 1, 1, 1],
          [1, 1, 1, 0, 0, 1, 1, 1, 1],
          [1, 1, 1, 1, 0, 0, 1, 1, 1],
          [1, 1, 1, 1, 1, 0, 0, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 0], ]
print(check_kdp(Kdp(kdp9_9)))
