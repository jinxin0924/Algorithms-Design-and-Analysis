__author__ = 'Xing'

#Python Algorithms- Mastering Basic Algorithms in the Python Language, Page 82
# looking for one node with incoming edges from all other nodes, but with no outgoing edges.
def naive_celeb(G):
    n = len(G)
    for u in range(n):  # For every candidate...
        for v in range(n):  # For everyone else...
            if u == v: continue  # Same person? Skip.
            if G[u][v]: break  # Candidate knows other
            if not G[v][u]: break  # Other doesn't know candidate
        else:
            return u
    return None

def celeb(G):
    n = len(G)
    u, v = 0, 1
    for c in range(2,n+1):
        if G[u][v]:
            u = c
        else:
            v=c
    if u == n:
        c = v
    else:
        c=u
    for v in range(n):
        if c == v: continue
        if G[c][v]: break
        if not G[v][c]: break
    else:
        return c
    return None


def celeb_jx(G):
    n=len(G)
    a=set([i for i in range(n)])
    not_celeb=set()
    i,j=0,1
    while i<=n-1 and j<=n-1:
        if i==j:
            j+=1
        if not G[i][j]:
            not_celeb.add(j) #如果G[i][j]=0，说明j不被i认识，j抛弃，看下个
            j+=1
        else:
            not_celeb.add(i)
            i=j #i直接跳到j
    return(a-not_celeb)


from random import randrange

def test1(): #重新构建新的函数是因为timeit直接调用有参数函数会出错，提示没有该变量
    n = 1000
    G = [[randrange(2) for i in range(n)] for i in range(n)]
    c = randrange(n)
    for i in range(n):
        G[i][c] = 1 #i认识c
        G[c][i] = 0 #c不认识i
    naive_celeb(G)

def test2():
    n = 1000
    G = [[randrange(2) for i in range(n)] for i in range(n)]
    c = randrange(n)
    for i in range(n):
        G[i][c] = 1 #i认识c
        G[c][i] = 0 #c不认识i
    naive_celeb(G)
    celeb(G)
def test3():
    n = 1000
    G = [[randrange(2) for i in range(n)] for i in range(n)]
    c = randrange(n)
    for i in range(n):
        G[i][c] = 1 #i认识c
        G[c][i] = 0 #c不认识i
    naive_celeb(G)
    celeb_jx(G)

print(test1())
print(str(test2())+'\t'+'celeb')
print(str(test3())+'\t'+'celeb_jx')

import timeit
t1= timeit.Timer("test1", "from __main__ import test1")
print(t1.repeat(3,100))
t2= timeit.Timer("test2", "from __main__ import test2")
print(t2.repeat(3,100))
t3= timeit.Timer("test3", "from __main__ import test3")
print(t3.repeat(3,100))

#后两个明显比第一个快，O(n^2)与O(n)的区别
# import timeit
# t4=timeit.Timer(lambda :naive_celeb(G))
# print(t4.timeit(1000))
# t5=timeit.Timer(lambda :celeb(G))
# print(t5.timeit(1000))
# t6=timeit.Timer(lambda :celeb_jx(G))
# print(t6.timeit(1000))

# import cProfile
# cProfile.run('test1()')
# cProfile.run('test2()')
# cProfile.run('test3()')