__author__ = 'Xing'

import random
def insert_sort(seq,i):
    if i==0:
        return
    insert_sort(seq,i-1)
    j=i
    while j>0 and seq[j-1]>seq[j]:
        seq[j-1],seq[j]=seq[j],seq[j-1]
        j-=1


seq=[random.randint(1,100) for i in range(20)]


def inser_sort(seq):
    for i in range(len(seq)):
        j=i
        while j>0 and seq[j-1]>seq[j]:
            seq[j-1],seq[j]=seq[j],seq[j-1]
            j-=1

def sel_sort(seq,i):
    if i==0:
        return
    for j in range(0,i-1):
        if seq[j]>seq[i]:
            seq[i],seq[j]=seq[j],seq[i]
    sel_sort(seq,i-1)

