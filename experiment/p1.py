'''
# p1

================================
OBJS
================================
create 1000 pairs of vectors
that have negative dot product

================================
VARS
================================
count       : 1000    | 100000  
range       : -5 to 5 | -500 to 500
output_file : 2v.2.pkl
'''

import random
import pickle

def get_rand():
    '''returns a random integer in range -5 to 5'''
    return random.randrange(-500, 500, 1)

def get_vector():
    '''returns a vector in xyz space as a list'''
    return list((get_rand(), get_rand(), get_rand()))

def dot_product(a, b):
    '''returns dot product of two vectors'''
    return ((a[0]*b[0]) + (a[1]*b[1]) + (a[2]*b[2]))

count = 0
list_2v = []
while(count < 100000):
    a = get_vector()
    b = get_vector()
    dp = dot_product(a, b)
    if dp < 0:
        l = []
        l.append(a)
        l.append(b)
        list_2v.append(l)
        count += 1

with open('2v.2.pkl', 'wb') as f:
    pickle.dump(list_2v, f)        
