__author__ = 'Xin'

# import sys
# sys.setrecursionlimit(10000) #例如这里设置为一百万
# import codecs
# import os
# path1= os.environ.get('DATA_PATH')
# sentence=[]
# word=set()
# f=codecs.open(path1+'output.txt','r','utf-8')
# for line in f:
#     a=line[:-1]
#     a1=a.split(',')
#     sentence.append(a1)
#     for j in a1:
#         word.add(j)
# f.close()


sentence=['AB','BCE','ABCD','ABEFG','E','BFE','G']
sentence=[['A', 'B'],['B', 'C', 'E'],['A', 'B', 'C', 'D'],['A', 'B', 'E', 'F', 'G'],['E','A'],['B', 'F', 'E'],['G']]
word=set()
for i in sentence:
    for j in i:
        word.add(j)
num=len(word)

def min_sentence(sentence,word):
    # @memoized
    def bestvalue(i, j):
        if i==0:return 100*len(word)
        set_i=set()
        for p in sentence[i-1]:
            set_i.add(p)
        q=len(set_i & j)
        return min(bestvalue(i - 1, j),
                   bestvalue(i - 1, j-set_i)-100*q + len(sentence[i-1]))

    j = word.copy()
    result = []
    for i in range(len(sentence), 0, -1):
        if bestvalue(i, j) != bestvalue(i - 1, j):
            result.append(i-1)
            set_i=set()
            for p in sentence[i-1]:
                set_i.add(p)
            j -= set_i
    result.reverse()
    return bestvalue(len(sentence),word),result

print(min_sentence(sentence,word))
# from functools import wraps
# def memo(func):
#     cache = {}
#     @wraps(func)
#     def wrap(*args):
#         if args not in cache:
#             cache[args] = func(*args)
#         return cache[args]
#     return wrap
#
# def rec_knapsack(w, v, c):
#     @memo
#     global all
#     def m(k, r):
#         global all
#         if k == 0 or r == 0: return 0
#         i = k-1
#         drop = m(k-1, r)
#         if w[i] > r: return drop
#         return max(drop, v[i] + m(k-1, r-w[i]))
#     return m(len(w), c)
# sentence=[['A', 'B'],['B', 'C', 'E'],['A', 'B', 'C', 'D'],['A', 'B', 'E', 'F', 'G'],['E','A'],['B', 'F', 'E'],['G']]
# word=[]
# all=set()
# for i in sentence:
#     for j in i:
#         all.add(j)
# for i in sentence:
#     word.append(set(i))
