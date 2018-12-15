#!/usr/bin/env python

def solution(N, A):
    
    counter = [0] * N
    max_value =  0
    for i in A:
        if i < N + 1:
            counter[i-1] = counter[i-1] + 1
            if counter[i-1] > max_value:
                max_value = counter[i-1]
        else:
            counter = [max_value] * N
    return counter
    
   
    
A=[3,4,4,6,1,4,4]
print solution(5,A)
    