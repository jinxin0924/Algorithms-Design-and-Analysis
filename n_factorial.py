__author__ = 'Xin'
import math
#计算n的阶乘末尾有多少个0
def f(n):
    if n==1:
        return 1
    return n*f(n-1)

def count(n):
    k=int(math.log(n,5))
    s=0
    for i in range(1,k+1):
        s+= n//(int(math.pow(5,i)))
    return s

print(count(10))
