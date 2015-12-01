__author__ = 'Xin'

from collections import defaultdict
import random
def counting_sort(A, key=lambda x: x):
    B, C = [], defaultdict(list)
    for x in A:
        C[key(x)].append(x) #
    for k in range(min(C), max(C)+1): #直接从最小的数开始，到最大的数的结束，如果碰到不存在的数，defaultdict也保证了得到的结果是空的list
        B.extend(C[k]) #将C[k]这个list拆散，元素加入B中
    return B

seq=[random.randint(1,100) for i in range(20)]

#时间复杂度为O(n+k),需要都是整数