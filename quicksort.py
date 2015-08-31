__author__ = 'Xin'

 def getrandata(num):
    a=[]
    i=0
    while i<num:
        a.append(random.randint(0,10000000))
        i+=1
    return a



def quickSort(L, low, high):
    i = low
    j = high
    if i >= j:
        return L
    key = L[j]
    while i < j:
        while i < j and L[i] <= key:
            i = i+1
        L[j] = L[i]
        while i < j and L[j] >= key:
            j = j-1
        L[i] = L[j]

    L[i] = key
    quickSort(L, low, i-1)
    quickSort(L, j+1, high)
    return L

#随机选取pivot
def quickSort(L, low, high):
    i = low
    j = high
    if i >= j:
        return L
    key = L[random.randint(i,j-1)]
    while i < j:
        while i < j and L[j] >= key:
            j = j-1
        L[i] = L[j]
        while i < j and L[i] <= key:
            i = i+1
        L[j] = L[i]
    L[i] = key
    quickSort(L, low, i-1)
    quickSort(L, j+1, high)
    return L


def quickSort(L, low, high): #统计比较次数
    i = low
    j = high
    if i >= j:
        return 1
    key = L[i]
    cnt=0
    while i < j:

        while i < j and L[j] >= key:
            j = j-1
            cnt+=1
        L[i] = L[j]
        while i < j and L[i] <= key:
            i = i+1
            cnt+=1
        L[j] = L[i]
    L[i] = key
    a=quickSort(L, low, i-1)
    b=quickSort(L, j+1, high)
    return a+b

def quickSort(L, low, high):
    i = low
    j = high
    if i >= j:
        return 1
    key = L[j]
    cnt=0
    while i < j:
        while i < j and L[i] <= key:
            i = i+1
            cnt+=1
        L[j] = L[i]
       while i < j and L[j] >= key:
            j = j-1
            cnt+=1
        L[i] = L[j]
    L[i] = key
    a=quickSort(L, low, i-1)
    b=quickSort(L, j+1, high)
    return a+b

def QuickSort(num): #python list的使用
    if len(num)<=1:
        return(num)
    greater=[]
    less=[]
    p=num.pop(random.randint(0,len(num)-1))
    for item in num:
         if item < p:
             less.append(item)
         else:
             greater.append(item)
    return (QuickSort(less)+[p]+QuickSort(greater))