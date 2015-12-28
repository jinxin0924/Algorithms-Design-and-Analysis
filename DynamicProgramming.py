__author__ = 'Xing'
from itertools import combinations


from functools import wraps
def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap


def fib(i):
    if i < 2: return 1
    return fib(i-1) + fib(i-2)
fib = memo(fib)
# print(fib(100))

@memo
def fib(i):
    if i < 2: return 1
    return fib(i-1) + fib(i-2)
# print(fib(100))

# Shortest Paths in Directed Acyclic Graphs
#  Let’s say the distance from a node v to our end node is d(v). Let the edge weight of edge (u,v) be w(u,v).
# Then, if we’re in node u, we already (by inductive hypothesis) know d(v) for each neighbor v,
# so we just have to follow the edge to the neighbor v that minimizes the expression w(u,v) + d(v)
def rec_dag_sp(W, s, t): # Shortest path from s to t
    @memo
    def d(u):
        if u == t: return 0
        return min(W[u][v]+d(v) for v in W[u])  # Best of every first step
    return d(s)                                 # Apply f to actual start node


def topsort(G,S=None):
    if S is None:
        S=set(range(len(G)))
    seq=[]
    while S:
        p=set()
        for i in S:
            p=p|set(G[i])
        Q=S-p
        x=Q.pop()
        seq.append(x)
        S.remove(x)
    return(seq)


def dag_sp(W, s, t):  # Shortest path from s to t
    d = {u:float('inf') for u in W} # Distance estimates
    d[s] = 0 # Start node: Zero distance
    for u in topsort(W): # In top-sorted order...
        if u == t: break # Have we arrived?
        for v in W[u]: # For each out-edge ...
            d[v] = min(d[v], d[u] + W[u][v]) # Relax the edge
    return d[t]  # Distance to t (from s)

# Longest Increasing Subsequence Problem
def naive_lis(seq): # n, n-1, ... , 1
    for length in range(len(seq), 0, -1):# n, n-1, ... , 1
        for sub in combinations(seq, length):# Subsequences of given length
            if list(sub) == sorted(sub):# An increasing subsequence?
                return sub
# print(naive_lis([3,1,0,2,4]))

def rec_lis(seq):# Longest increasing subseq.
    @memo
    def L(cur):# Longest ending at seq[cur]
        res = 1 # Length is at least 1
        for pre in range(cur): # Potential predecessors
            if seq[pre] <= seq[cur]: # A valid (smaller) predec.
                res = max(res, 1 + L(pre)) # Can we improve the solution?
        return res
    return max(L(i) for i in range(len(seq)))
print(rec_lis([3,1,0,2,4,5]))


def iter_lis_jx(seq):
    d={i:1 for i in range(len(seq))}
    for index in range(1,len(seq)):
        for pre in range(index):
            if seq[pre]<=seq[index]:
                d[index]=max(d[index],1+d[pre])
    m=1
    for index in range(len(seq)):
        if m<d[index]:m=d[index]
    return m
print(iter_lis_jx([3,1,0,2,4,5]))