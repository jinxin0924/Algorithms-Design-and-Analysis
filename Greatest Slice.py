__author__ = 'Xing'
import random
def greatest1(A):
    n=len(A)
    result=max((A[i:j] for i in range(n) for j in range(i+1,n+1)), key=sum)
    m=sum(result)
    return m,result

def greatest2(A):
    result=[]
    m=0
    for k in range(1,n+1):
        s=sum(A[:k])
        if s>m:
            m,result=s,A[:k]
        for i in range(1,n-k+1):
            s=s-A[i-1]+A[i+k-1]
            if s>m:
                m,result=s,A[i:i+k]
    return m,result

def greatest3(A):
    def exchange(A):
        s=sum(A)
        if s>dict1['max']:
            dict1['max']=s
            dict1['result']=A

    def partition(A):
        n=len(A)
        if n<1:
            return A
        if n==1:
            exchange(A)
            return A
        mid=n//2
        left=partition(A[:mid])
        right=partition(A[mid:])
        return merge(left,right)

    def merge(left,right):
        left_length=len(left)
        right_length=len(right)
        if left_length==0 or right_length==0:
            return(left+right)
        l=[left[-1],right[0]]
        lmax=sum(l)
        list1=l.copy()
        for i in range(1,left_length):
            l.insert(0,left[-i-1])
            if sum(l)>lmax:
                lmax,list1=sum(l),l.copy()
        if lmax<0:
            l=[left[-1],right[0]]
            lmax=sum(l)
        else:
            l=list1.copy()
        for i in range(1,right_length):
            l.append(right[i])
            if sum(l)>lmax:
                lmax,list1=sum(l),l.copy()
        # print(left,right)
        # print(left+right)
        # print((lmax,list1))

        exchange(list1)
        return(left+right)
    dict1={}
    dict1['max']=0
    dict1['result']=[]
    partition(A)
    return dict1['max'],dict1['result']





n=30
# A=[random.randint(-100,100) for i in range(n)]
A=[78, -34, 73, -45, -50, -99, -56, -68, 94, -40, -54, -5, 2, -65, -81, -21, -26, 57, -1, -36, 29, 94, -77, -68, 36, 12, -51, -26, 38, 84]
print(A)
# print(greatest1(A))
# print(greatest2(A))
# print(greatest3(A))

import timeit
t1=timeit.timeit(lambda: greatest1(A))
t2=timeit.timeit(lambda: greatest2(A))
t3=timeit.timeit(lambda: greatest3(A))

print(t1.repeat(3,10))
print(t2.repeat(3,10))
print(t3.repeat(3,10))