# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 14:50:16 2015

@author: Xin
"""

def subsets(s):
    if not s:
        yield ()
    else:
        head, rest = s[:1], s[1:]
        for se in subsets(rest):
            yield se
            yield head + se

def test5(arr):
    list1=[]
    for ss in subsets(arr):
        if len(ss)>0:
            list1.append(list(ss))
    return list1
    
def xiaoci(s):
    if s=='a':
        return(['a','aa'])
    if s=='b':
        return(['b','bb'])    
    if s=='c':
        return(['c','cc'])
    else:
        return([s])
        
def replace(s,depth):    
    global string    
    if depth==0:
        string=''
    if len(s)<1:
        list1.append(string)
        string=string[:-1]
    else:
        depth+=1
        for i in xiaoci(s[0]):
            string+=i        
            replace(s[1:],depth)
    return list1

list1=[]
string='' 
replace('ab',0)  
#---------------------------------------------------------------------------- 
#merge sort
def MergeSort(lists):
    if len(lists) <=1:
        return lists
    num = int(len(lists)/2)
    left = MergeSort(lists[:num])
    right = MergeSort(lists[num:])
    return merge(left,right)

def merge(left,right):
    i=0
    j=0
    r=[]
    while i<len(left) and j <len(right):
        if left[i]<=right[j]:
            r.append(left[i])
            i+=1
        else:
            r.append(right[j])
            j+=1
    r+=left[i:]
    r+=right[j:]
    return(r)

