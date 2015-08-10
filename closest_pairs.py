__author__ = 'Xin'


# closest paris,o(nlogn)
import scipy
def dist(tup): #计算距离
    distance=scipy.sqrt(scipy.square(tup[0][0]-tup[1][0])+scipy.square(tup[0][1]-tup[1][1]))
    return(distance)

def testpair(minleft): #测试是否为最佳，是的话就替换
    global best
    if minleft[1]<best[1]:
        best=minleft

def closest_paris(list1):#divide
    global best
    n=len(list1)
    if n<2:
        return(list1)
    mid=int(n/2)
    left=closest_paris(list1[:mid])
    right=closest_paris(list1[mid:])
    sortedlist=split_paris(left,right) #合并
    return(sortedlist)

def split_paris(left,right): #合并
    global best
    i,j=0,0
    r=[]
    while i<len(left) and j < len(right): #对按照y值排序，time为O(n)
        if left[i][1]<=right[j][1]:
            r.append(left[i])
            i+=1
        else:
            r.append(right[j])
            j+=1
    r+=left[i:]
    r+=right[j:]
    split=[p for p in r if abs(p[0]-right[0][0])<best[1]] #筛选出距离中间点x值（-d，d)的点
    for i in range(len(split)):
        for j in range(1,8): #画出长为2d，宽为d的矩形，分隔成8个边长为d/2的正方形，因此最多7个
            if i+j<len(split):
                points=(split[i],split[i+j])
                test1=(points,dist(points))
                testpair(test1)
    return(r)


list1=[(0,0),(7,6),(2,20),(12,5),(16,16),(5,8),(19,7),(14,22),(8,19),(7,29),(10,11),(1,13)]
best=((list1[0],list1[1]),dist((list1[0],list1[1])))
list1.sort()
closest_paris(list1)  #瑕疵：返回的不是最近距离的点，要看全局变量best

# 改进型，整个包装成一个函数，全局变量变为局部变量
from scipy import sqrt,square
def closestpairs(L):
    def dist(p,q):
        return sqrt(square(p[0]-q[0])+square(p[1]-q[1]))
    # check whether pair (p,q) forms a closer pair than one seen already
    L.sort()
    best = [dist(L[0],L[1]), (L[0],L[1])] #初始化best值

    def test(p,q):
        if dist(p,q)<best[0]:
            best[0]=dist(p,q)
            best[1]=p,q

    def merge(left,right): #sort and merge by y value
        i,j=0,0
        r=[]
        while i<len(left) and j<len(right):
            if left[i][1]<=right[j][1]:
                r.append(left[i])
                i+=1
            else:
                r.append(right[j])
                j+=1
        r+=left[i:]
        r+=right[j:]
        return(r)

    def devidepairs(L):
        n=len(L)
        if n<2:
            return(L)
        mid=int(n/2)
        left=devidepairs(L[:mid])
        right=devidepairs(L[mid:])
        sortedlist=merge(left,right)
        split=[p for p in sortedlist if abs(p[0]-right[0][0])< best[0]] # Find possible closest pair across split line
        for i in range(len(split)):
            for j in range(1,8):
                if i+j<len(split):
                    test(split[i],split[i+j])
        return(sortedlist)

    devidepairs(L)
    return(best)

