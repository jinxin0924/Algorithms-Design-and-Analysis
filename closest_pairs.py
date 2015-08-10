__author__ = 'Xin'


# closest paris,o(nlogn)
import scipy
def dist(tup): #计算距离
    distance=scipy.sqrt(scipy.square(tup[0][0]-tup[1][0])+scipy.square(tup[0][1]-tup[1][1]))
    return(distance)

def testpair(minleft):
    global best
    if minleft[1]<best[1]:
        best=minleft

def closest_paris(list1):
    global best
    n=len(list1)
    if n<2:
        return(list1)
    mid=int(n/2)
    left=closest_paris(list1[:mid])
    right=closest_paris(list1[mid:])
    sortedlist=split_paris(left,right)
    return(sortedlist)

def split_paris(left,right):
    global best
    i,j=0,0
    r=[]
    while i<len(left) and j < len(right):
        if left[i][1]<=right[j][1]:
            r.append(left[i])
            i+=1
        else:
            r.append(right[j])
            j+=1
    r+=left[i:]
    r+=right[j:]
    split=[p for p in r if abs(p[0]-right[0][0])<best[1]]
    for i in range(len(split)):
        for j in range(1,8):
            if i+j<len(split):
                points=(split[i],split[i+j])
                test1=(points,dist(points))
                testpair(test1)
    return(r)




list1=[(0,0),(7,6),(2,20),(12,5),(16,16),(5,8),(19,7),(14,22),(8,19),(7,29),(10,11),(1,13)]
best=((list1[0],list1[1]),dist((list1[0],list1[1])))
list1.sort()
closest_paris(list1)