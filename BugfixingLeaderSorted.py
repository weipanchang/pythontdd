#!/usr/bin/env python

def solution(A):
    n = len(A)
    L = [-1] + A
    print A
    count = 0
    pos = (n ) // 2
    candidate = L[1]
    for i in xrange(1, n + 1):
        if (L[i] == candidate):
            count = count + 1
            if (count > pos):
                 return candidate
    return -1
    
    
    
    
A=[2,2,1]
print solution(A)