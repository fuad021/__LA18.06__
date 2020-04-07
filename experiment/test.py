'''
# test_iv

================================
OBJS
================================


================================
VARS
================================


================================
REPORT
================================

'''

import pickle
import sys
from itertools import combinations 
from p1 import dot_product

it = int(sys.argv[1])
it_list = list(range(it))

read_file = str(it) + 'v.2.pkl'   # read  @ list_pv

with open(read_file, 'rb') as f:
    list_iv = pickle.load(f)

print('Total vectors of size ' + str(it) + ': ' + str(len(list_iv)))
combination = list(combinations(it_list, 2))

for i in range(len(list_iv)):
    a = list_iv[i]
    for c in combination:
        if dot_product(a[c[0]], a[c[1]]) > 0:
            print("ERROR: at line", i, ":", a[c[0]], a[c[1]], dot_product(a[c[0]], a[c[1]]))
