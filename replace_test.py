__author__ = 'Xin'
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

def replace(s):
    s=list(s)
    pattern={}
    length=0
    pattern[0]=['']
    while s:
        word=s.pop()
        length=length+1
        pattern[length]=[]
        for syn_word in xiaoci(word):
            for string in pattern[length-1]:
                newword=syn_word+string
                pattern[length].append(newword)
    return list(pattern[length])

print(replace('abc'))
