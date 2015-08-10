__author__ = 'Xin'

#统计逆序数
def mergeinversion(lists):
    if len(lists) <=1:
        return lists,0
    num = int(len(lists)/2)
    left,a = mergeinversion(lists[:num])
    right,b = mergeinversion(lists[num:])
    sortedlist,c= countinversion(left,right)
    return(sortedlist,a+b+c)

def countinversion(left,right):
    i=0
    j=0
    r=[]
    n=len(left)
    cnt=0
    while i<len(left) and j <len(right):
        if left[i]<=right[j]:
            r.append(left[i])
            i+=1
        else:
            r.append(right[j])
            j+=1
            cnt+=n-i
    r+=left[i:]
    r+=right[j:]
    return(r,cnt)

import codecs
path1='/Users/Xing/Downloads/'
list1=[]
f1=codecs.open(path1+'IntegerArray.txt','r','utf-8')
for line in f1:
    list1.append(int(line[:-2]))
f1.close()
