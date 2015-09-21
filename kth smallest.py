__author__ = 'Xing'
# 1. 选择最开始的k的元素，然后遍历n，每个元素用类似insert sort的方式与k个元素比较，维护这些k，O(n*k)
# 2. 选择最开始的k个元素，用heap来维护这k个元素，o(n*lg(k))
#以上这些问题，都存在给k排序的问题，实际上对这些k无需排序，所以存在更有方案
# 3. 利用类似快速排苏的pivot，来partition，randomized select（partition1)
# 4. bfprt，中位数中的中位数，线性时间 selection


import random
#kth smallest
def partition(seq):
    pi, seq = seq[0], seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo, pi, hi
def select(seq, k):
    lo, pi, hi = partition(seq)
    m = len(lo)
    if m == k: return pi
    elif m < k:
        return select(hi, k-m-1)
    else:
        return select(lo, k)
#跟快排原理一样

#练习随机快排

def partition1(seq):
    n=len(seq)
    if n==0:
        return seq
    pivot=random.randint(0,n-1)
    pi=seq[pivot]
    less=[x for x in seq if x<pi]
    larger=[x for x in seq if x>pi]
    left=partition1(less)
    right=partition1(larger)
    return left+[pi]+right


def bfprt():





seq=[random.randint(1,100) for i in range(30)]
print(select(seq,29))
print(partition1(seq))