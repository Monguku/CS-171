'''
7.
a) A[stop]
b)
temp = A[i]
A[i] = A[stop]
A[stop] = temp

'''

#8
#a
def merge(a, b):
    c = []

    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.pop(0)
        else:
            c.append(b[0])
            b.pop(0)
    while len(a) > 0:
        c.append(a.pop(0))
    while len(b) > 0:
        c.append(b.pop(0))
    return c

#b
def msort(x):
    if len(x) > 1:
        middle = len(x)//2
        a = msort(x[:middle])
        b = msort(x[middle:])
        c = merge(a, b)
        return c
    else:
        return x

#c
def partition(a, start, stop):
    pivot = a[stop]
    i = start
    for j in range(start, stop):
        if a[j] <= pivot:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
            i += 1
    temp2 = a[i]
    a[i] = a[stop]
    a[stop] = temp2

    return i

#d
def qsort(a, start, stop):
    if start < stop:
        p = partition(a, start, stop)
        qsort(a, start, p-1)
        qsort(a, p+1, stop)

#tests
import random
for x in range(0, 10):
    L = [random.randint(0,100)  for k in range(0, 10)]
    print('Merge input:', L)
    L = msort(L)
    print('Result after msort:', L)
for x in range(0, 10):
    L = [random.randint(0,100) for k in range(0, 10)]
    print('Quick sort input:', L)
    qsort(L, 0, len(L) - 1)
    print('qsort result:', L)
