#!/usr/bin/env python

import math
   
def find_factor(n):
    a = []
    for i in range(2, int(math.sqrt(n) + 1) ):
        if n % i == 0:
            a.append(i)
            a.append( n / i)
    return a
    
def primary_check(n):
    is_primary = True
    if n == 1 or n == 2 or n == 3:
        return True
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            is_primary = False
            break
    return is_primary

#a_list = sorted(find_factor(13195),reverse=True)
a_list = sorted(find_factor(600851475143),reverse=True)
print a_list
for i in a_list:
    if primary_check(i):
        print i
        break



    
 
