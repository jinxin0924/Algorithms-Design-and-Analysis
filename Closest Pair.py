__author__ = 'Xing'
import math

def closet_pairs(L):
    def dist(x,y): #distance
        d=(x[0]-y[0])*(x[0]-y[0])+(x[1]-y[1])*(x[1]-y[1])
        return math.sqrt(d)

    def exchange(best,x,y): #exchange the best
        if dist(x,y)<best:
            best=dist(x,y)
            a,b=x,y

    def partition(L):
        n=len(L)
        if n<2: return L
        m=n//2
        left=partition(L[:m])
        right=partition(L[m:])
        return merge(left,right)

    def merge(left,right):
        m=(left[-1][0]+right[0][0])//2 #找到中间值
        mid=[]
        l=left+right
        for i in l: #考虑x轴范围内距离中间值<best的点
            if abs(i[0]-m)<=best:
                mid.append(i)
        mid.sort(key=lambda d:d[1])#根据y值排序
        for i in range(len(mid)):  #考虑后面7个点
            for j in range(i+1,i+8):
                if j < len(mid):
                    exchange(best,mid[i],mid[j])
        return l

    L.sort()
    a,b=L[0],L[1]
    best=dist(a,b)
    partition(L)
    return best,a,b

list1=[(0,0),(7,6),(2,20),(12,5),(16,16),(5,8),(19,7),(14,22),(8,19),(7,29),(10,11),(1,13)]
print(closet_pairs(list1))