'''
# p2

================================
OBJS
================================
create vector triplets with ndp
out of 1000 vector pairs created
by Exp 1.1

================================
VARS
================================
try         : 1000
input_file  : 2v.pkl | 2v.2.pkl
output_file : 3v.pkl | 3v.2.pkl
'''

import pickle
from p1 import get_vector, dot_product

tries = 1000
list_3v = []

with open('2v.2.pkl', 'rb') as f:
    list_2v = pickle.load(f)
    
print('read length', len(list_2v))
    
for i in range(len(list_2v)):
    a = list_2v[i][0]
    b = list_2v[i][1]
    for j in range(tries):
        c = get_vector()
        if dot_product(a, c) < 0 and dot_product(b, c) < 0:
            l = []
            l.append(a)
            l.append(b)
            l.append(c)
            list_3v.append(l)
            break
        
print('write length', len(list_3v))

with open('3v.2.pkl', 'wb') as f:
    pickle.dump(list_3v, f)
