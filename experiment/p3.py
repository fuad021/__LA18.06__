'''
# p3

================================
OBJS
================================
create iterative process to find
out the number of vector possible
with ndps.

================================
VARS
================================
tries       : 1000
iteration   : [4 - .?. ]
input_file  : <i-1>v.pkl    | <i-1>v.2.pkl
output_file : <i>v.pkl      | <i>v.2.pkl

================================
REPORT
================================
-> 700+ v4 for tries 1000
-> 749 v4 for fries 10000
-> 60000+ v4 for tries 100  v.2
-> 86000+ v4 for fries 1000 v.2

-> 0 v5 for tries 1000
-> 0 v5 for fries 10000
-> 0 v4 for tries 100  v.2  [-500 to 500]
-> 0 v4 for fries 1000 v.2
'''

import sys
import pickle
from itertools import combinations 
from p1 import get_vector, dot_product

def dot_product_i(a, c):
    flag = 0 # 0 means negative
    for i in range(len(a)):
        if dot_product(a[i], c) >= 0:
            flag = 1
            break
    return flag

it = int(sys.argv[1])
tries = int(sys.argv[2])

list_iv = []

read_file = str(it - 1) + 'v.2.pkl'   # read  @ list_pv
write_file = str(it) + 'v.2.pkl'      # store @ list_iv

with open(read_file, 'rb') as f:
    list_pv = pickle.load(f)
print('read length', len(list_pv))

        
for i in range(len(list_pv)):
    a = list_pv[i]

    for j in range(tries):
        c = get_vector()
        if dot_product_i(a, c) == 0:
            a.append(c)
            list_iv.append(a)
            break
        
print('write length', len(list_iv))

with open(write_file, 'wb') as f:
    pickle.dump(list_iv, f)
