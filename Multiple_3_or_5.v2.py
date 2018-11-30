#!/usr/bin/env python
n = 2
a = []
while n < 1000:
    if n % 3 == 0 or n % 5 == 0:
        a.append(n)
    n += 1

print a

print sum(a)
         

