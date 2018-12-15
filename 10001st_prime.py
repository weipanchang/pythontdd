#!/usr/bin/env python
import math
    
def primary_check(n):
    if n == 1 or n == 2 or n == 3:
        return True
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def find_primary_below(n):    
    i = m = 3
    while i <= n:
        m += 2
        if primary_check(m):
            i += 1
    print m
    
find_primary_below(5)
find_primary_below(6)
find_primary_below(7)
find_primary_below(12)
find_primary_below(10001)