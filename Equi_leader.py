#!/usr/bin/env python

def solution(A):
    def max_occ(A):
        n = 0
        ch=''
        for i in A:
            if A.count(i) > n:
                n = A.count(i)
                ch = i
        #print (n, ch)
        return (n, ch)
    x= 0
    for i in range(len(A)):
        print A[:i+1:], A[i+1::]
        if max_occ(A[:i+1:]) == max_occ(A[i+1::]) and max_occ(A[:i+1:])[0] > x:
            x =  max_occ(A[:i+1:])[0]

    return x
   
            
A= [4,4, 3,4,4,4,2]
print solution(A)