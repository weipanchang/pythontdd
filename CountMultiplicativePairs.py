#!/usr/bin/env python

def solution(A,B):
    l = []
    count=0
    for i in range(len(A)):
        num = A[i] + (float(B[i]) /1000000)
        l.append(num)
    print l
    for i in range(len(l) -1 ):
        for j in l[i+1::]:
            if l[i] * j >= l[i] + j:
                count = count + 1
                print l[i], j
    return count
            



        

A=[0,1,2,2,3,5]
B=[500000,500000,0,0,0,20000]
print solution(A,B)

