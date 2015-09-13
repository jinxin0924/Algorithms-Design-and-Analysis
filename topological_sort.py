__author__ = 'Xing'
def naive_topsort(G, S=None):
    if S is None:
        S = set(range(len(G)))
    if len(S) == 1:
        return list(S)
    v = S.pop()
    seq = naive_topsort(G, S)
    min_i = 0
    for i, u in enumerate(seq):
        if v in G[u]:
            min_i = i+1
    seq.insert(min_i, v)
    return seq

G=[[1,5],[2,3,5],[3],[4,5],[5],[]] #举例说明，G[0]=[1,5],标识第0个点后面跟着1，5这两个点
print(naive_topsort(G))

def topsort_jx(G,S=None):
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
print(topsort_jx(G))

def topsort_jx2(G):
    S=range(len(G))
    count=[0 for i in S] #记录每个点作为儿子出现次数，次数为0，即可出现
    for i in G:
        for j in i:
            count[j]+=1
    Q=[i for i in S if count[i]==0]
    seq=[]
    while Q:
        x=Q.pop()
        seq.append(x)
        for i in G[x]:
            count[i]-=1
            if count[i]==0:
                Q.append(i)
    return seq

print(topsort_jx2(G))
#o(n)

import timeit
t1=timeit.Timer(lambda :naive_topsort(G))
t2=timeit.Timer(lambda :topsort_jx(G))
t3=timeit.Timer(lambda :topsort_jx2(G))

print(t1.timeit(2000))
print(t2.timeit(2000))
print(t3.timeit(2000))
