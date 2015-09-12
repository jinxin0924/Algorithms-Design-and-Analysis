__author__ = 'Xin'

import random



def rSelection(L,index ,low, high):
    i = low
    j = high
    if i >= j:
        return L[i]
    key = L[random.randint(i,j-1)]
    while i < j:
        while i < j and L[j] >= key:
            j = j-1
        L[i] = L[j]
        while i < j and L[i] <= key:
            i = i+1
        L[j] = L[i]
    L[i] = key
    if i==index:
        return L[i]
    elif i>index:
        RSelection(L, index,low, i-1)
    else:
        RSelection(L, j+1, high)


import random
import cProfile
import timeit
def rselection(num,index): #python list的使用
    global selection
#    global depth
    if len(num)<1:
        return selection
    greater=[]
    less=[]
#    p=num.pop(int(len(num)/2))
    p=num.pop(random.randint(0,len(num)-1))
    for item in num:
         if item < p:
             less.append(item)
         else:
             greater.append(item)
    p_index=len(less)
    if p_index+1==index:
        selection=p
    elif p_index+1>index:
        rselection(less,index)
    else:
        rselection(greater,index-p_index-1)
    return selection

#测试
def main():
    for i in range(1,9):
        l=[2, 3, 4, 6, 9, 1, 5,8, 7, 10]
        selection=0
        depth=0
        print(rselection(l,i))

cProfile.run('main()')
timeit.timeit('main()')


