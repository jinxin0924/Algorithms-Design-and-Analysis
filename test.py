__author__ = 'Xing'

def find_xiao(x):
    if x=='a':
        return ['a','aa']
    elif x=='b':
        return ['b','bb']
    return [x]


def replace(x,s=None,d=0):
    global n
    if d==0:
        s=[]
    if d==n:
        yield s
    for i in find_xiao(x[d]):
        s.append(i)
        d+=1
        replace(x[d-1],s,d)


x=['a','b','c']
n=len(x)

print(list(replace(x)))