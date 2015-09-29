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
    m=0
    result=[]
    def exchange(A):
        s=sum(A)
        if s>m:
            m,result=s,A

    def partition(A):
        n=len(A)
        if n<1:
            return A
        if n==1:
            exchange(A)
        m=n//2
        left=partition(A[:m])
        right=partition(A[m+1:])
        return merge(left,right)

    def merge(left,right):
        l=left[-1]+right[0]
        a=len(left)
        b=len(right)
        for i in range(a):



n=30
A=[random.randint(-100,100) for i in range(n)]
print(A)
print(greatest1(A))
print(greatest2(A))