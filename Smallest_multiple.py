#!/usr/bin/env python
import math
def LCM(m, n):
    a = [m, n]
    a = [m,n] if m >= n else [n,m]
    while a[1]:
        a[0], a[1] = a[1], a[0] % a[1]
    return ((m * n) / a[0])
        
def is_primary(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def generate_primary_list(m):
    l = [2,3]
    for i in range(4, m + 1):
        if is_primary(i):
            l.append(i)
    return l

def Smallest_multiple(m):
    l = generate_primary_list(m)
#    print l
    prod= reduce(lambda a, b : a * b, l)
    for i in range(2, m + 1):
        if i not in l:
            prod = LCM(prod, i)
    return prod

print "The Smallest Multiple for ", "1 to 10 is ", Smallest_multiple(10)
print "The Smallest Multiple for ", "1 to 20 is ", Smallest_multiple(20)
print "The Smallest Multiple for ", "1 to 30 is ", Smallest_multiple(30)
    
    
    