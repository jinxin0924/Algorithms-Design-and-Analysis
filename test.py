
@profile
def knapsack1(items,maxweight):
    @profile
    def bestvalue(i,j):
        if i==0:return 0
        value,weight=items[i-1]
        if weight>j:
            return bestvalue(i-1,j)
        else:
            return max(bestvalue(i-1,j),
                       bestvalue(i-1,j-weight)+value)
    j=maxweight
    result=[]
    for i in range(len(items),0,-1):
        if bestvalue(i,j)!=bestvalue(i-1,j):
            result.append(items[i-1])
            j-=items[i-1][1]
    result.reverse()
    return result,bestvalue(len(items),maxweight)
items = [(4, 12), (2, 1), (6, 4), (1, 1), (2, 2)]

for i in range(100):
    knapsack1(items,11)

import itertools

@profile
def test1(items,maxweight):
    best=0
    for i in range(1,len(items)):
        for j in itertools.combinations(items,i):
            value=sum([q[1] for q in j ])
            weight=sum([q[0] for q in j])
            if weight<=maxweight:
                best=max(best,weight)
    return best
for i in range(100):
    test1(items,11)


def rec_knapsack(w, v, c):  #Weights, values and capacity
    @profile
    def m(k, r):
        if k == 0 or r == 0: return 0
        i = k-1
        drop = m(k-1, r)
        if w[i] > r: return drop
        return max(drop, v[i] + m(k-1, r-w[i]))
    return m(len(w), c)
for i in range(100):
    rec_knapsack([i[0] for i in items],[i[1] for i in items],11)