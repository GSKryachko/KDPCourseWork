from kdp import *
from Theorem2 import *
from construction1_5 import *
from theorem3 import *
from oabuilder import *

kdp4_6 = Kdp.get_trivial_kdp(4)
# This function will try to generate substantial oa
kdp16_30 = build_scheme_by_theorem_2(kdp4_6)
print(kdp16_30)

# Or you can generate oa beforehand...
oa = build_oa(4, 5, 2, 1)
# ... and then pass it to this function together with the kdp
kdp16_30 = build_scheme_using_oa(kdp4_6, oa)
print(kdp16_30)

# Writing kdp to a file
with open('kdp16_30.txt', 'w') as f:
    f.write(str(kdp16_30))
