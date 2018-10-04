def firstDuplicate(a):
    for i in range(0,len(a)):
        if a[ abs(a[i]) -1 ] < 0:
            return abs( a[i] )
        a[ abs(a[i]) -1 ] = - a[ abs( a[i ]) - 1]
    return -1
a: [2, 1, 3, 5, 3, 2] = 3
a: [2, 4, 3, 5, 1] = -1
a: [1] = -1
a: [2, 2] = 2
a: [2, 1] = -1