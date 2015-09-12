__author__ = 'Xin'
#Python Algorithms- Mastering Basic Algorithms in the Python Language, Page 78
# Eight persons with very particular tastes have bought tickets to the movies.
# Some of them are happy with their seats, but most of them are not,
# and after standing in line in Chapter 3, they’re getting a bit grumpy.
# Let’s say each of them has a favorite seat,
# and you want to find a way to let them switch seats to make as many people as possible happy
# with the result (ignoring other audience members, who may eventually get a bit tired by the antics of our moviegoers).
# However, because they are all rather grumpy, all of them refuse to move to another seat if they can’t get their favorite.

M = [2, 2, 0, 5, 3, 5, 7, 4] #记录座位上的人所喜欢的位子
def naive_max_perm(M, A=None):
    if A is None:
        A = set(range(len(M)))
    if len(A) == 1:
        return A
    B = set(M[i] for i in A)
    C=A- B
    if C:
        A.remove(C.pop())
        naive_max_perm(M, A)
    return A
#O(n^2)

def max_perm(M):
    n=len(M)
    a=set(range(n)) #记录座位号
    count=[0]*n
    for i in M:
        count[i]+=1 #记录每个座位被喜欢的个数，如果为0，则废弃
    q=[i for i in range(n) if count[i]==0] # 记录废弃的座位
    while q:
        i=q.pop() #处理废弃的i
        a.remove(i) #第i个座位和坐在i上的人绑定
        j=M[i] #第i个座位上的人喜欢的座位号
        count[j]-=1
        if count[j]==0:
            q.append(j)
    return a




