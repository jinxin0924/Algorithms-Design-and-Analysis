__author__ = 'Xin'
import collections
import functools
items = [(4, 12), (2, 1), (6, 4), (1, 1), (2, 2)]
from functools import wraps
def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


def rec_knapsack(w, v, c):  #Weights, values and capacity
    @memo
    def m(k, r):
        if k == 0 or r == 0: return 0
        i = k-1
        drop = m(k-1, r)
        if w[i] > r: return drop
        return max(drop, v[i] + m(k-1, r-w[i]))
    return m(len(w), c)
print(rec_knapsack([i[0] for i in items],[i[1] for i in items],11))

def knapsack(w, v, c):
    n = len(w)  # Number of available items
    m = [[0]*(c+1) for i in range(n+1)]   # Empty max-value matrix
    P = [[False]*(c+1) for i in range(n+1)]  # Empty keep/drop matrix
    for k in range(1,n+1):    # We can use k first objects
        i= k-1                # Object under consideration
        for r in range(1,c+1):   # Every positive capacity
            m[k][r] = drop = m[k-1][r]    # By default: drop the object
            if w[i] > r: continue         # Too heavy? Ignore it
            keep = v[i] + m[k-1][r-w[i]]  # Value of keeping it
            m[k][r] = max(drop, keep)     # Best of dropping and keeping
            P[k][r] = keep > drop         # Did we keep it?
    return m, P

items = [(4, 12), (2, 1), (6, 4), (1, 1), (2, 2)]
w=[i[0] for i in items]
v=[i[1] for i in items]
c=11
m, P = knapsack(w, v, c)
k, r, items = len(w), c, set()
while k > 0 and r > 0:
    i = k-1
    if P[k][r]:
        items.add(i)
        r -= w[i]
    k -= 1
print (items)