#!/usr/bin/env python

friend_number = 16
unfriend_list= [2,5,7,4,3,8,3,18]

def find_divisor(n):
    l = []
    for i in range(1, n + 1):
        if n % i ==0:
            l.append(i)
    return l

def unfriend_number(a, b):
    n = 0
    for j in b:
        isDivided = False
        for i in a:
            if i % j ==0:
                isDivided = True
                break
        if not isDivided:
            n += 1
       
    return n