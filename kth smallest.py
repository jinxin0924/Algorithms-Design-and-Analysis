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


#随机快排
def qsort(seq):
    n=len(seq)
    if n==0:
        return seq
    pivot=random.randint(0,n-1)
    pi=seq[pivot]
    less=[x for x in seq if x<pi]
    larger=[x for x in seq if x>pi]
    left=qsort(less)
    right=qsort(larger)
    return left+[pi]+right

def pivot_median(seq): #返回中位数
    if len(seq)==0:
        return
    Sseq=qsort(seq)
    n=len(seq)//2
    return Sseq[n]

def bfprt(seq,k):
    if len(seq)>=5: #如果list的长度大于5，采用中位数的中位数
        pivot_list=[]
        for i in range(0,len(seq),5):
            slice=seq[i:i+5]
            if len(slice)==5: #舍弃长度小于5的
                median=pivot_median(slice) #slice的中位数
                pivot_list.append(median)
        pivot=pivot_median(pivot_list)#中位数的中位数
    else:
        pivot=seq[0]
    seq.remove(pivot)#可以处理有重复数字的情况
    left=[i for i in seq if i<=pivot]
    right=[i for i in seq if i>pivot]
    m=len(left)
    if m==k:
        print(pivot)
        return pivot
    elif m>k:
        return bfprt(left,k) #注意要有return，这样才能有结果输出
    else:
        return bfprt(right,k-m-1)


seq=[random.randint(1,100) for i in range(30)]
# seq=[61, 32, 35, 65, 84, 17, 97, 56, 1, 81, 89, 9, 53, 88, 64, 100, 92, 27, 13, 59, 100, 18, 17, 13, 46, 29, 74, 16, 43, 9]
print(select(seq,5))
print(seq)
print(bfprt(seq,5))