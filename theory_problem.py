__author__ = 'Xin'


#第一题：找到第二大的那个,整个包装成一个函数，全局变量变为局部变量
def findsecond(list1):
    def merge2nd(list1):
        n=len(list1)
        if n<=1:
            return list1[0]
        mid=int(n/2)
        left=merge2nd(list1[:mid])
        right=merge2nd(list1[mid:])
        if left not in dict1:   #将比较各个比较对象存入dict1，为的是记录与最大值进行比较过的数
            dict1[left]=[]
        if right not in dict1:
            dict1[right]=[]
        dict1[right].append(left)
        dict1[left].append(right)
        return comparision_2nd_merge(left,right)

    def comparision_2nd_merge(left,right):
        if left>right:
            return left
        else:
            return right

    dict1={} #局部变量
    maximum=merge2nd(list1)  #找到最大比较了n-1次
    second=dict1[maximum][0]
    for i in range(1,len(dict1[maximum])):   #在跟最大值比较过的数中，比较logn-1次，找到其中最大值，即为第二大的数
        if second<dict1[maximum][i]:
            second=dict1[maximum][i]
    return(second)
#----------------------------------------------------------------------------


#第二题：找到拐点
def merge_no2(list1):
    n=len(list1)
    if n<3:
        return('error')
    mid=int(len(list1)/2)
    if list1[mid-1]<list1[mid]<list1[mid+1]:
        merge_no2(list1[mid+1:])
    elif list1[mid-1]>list1[mid]>list1[mid+1]:
        merge_no2(list1[:mid-1])
    else:
        return(list1[mid])


#第三题：ai]=[i]
def merge_no3(list1,midindex):
    n=len(list1)
    if n<=1:
        if list1[0]==midindex:
            return(list1[0],midindex)
        else:
            return(list1[0],0)
    mid=int(len(list1)/2)
    if list1[mid]>midindex:
        merge_no3(list1[:mid],midindex-1-int(len(list1[:mid])/2))
    elif list1[mid]<midindex:
        merge_no3(list1[mid:],midindex+int(len(list1[:mid])/2))
    else:
        return(list1[mid],midindex)