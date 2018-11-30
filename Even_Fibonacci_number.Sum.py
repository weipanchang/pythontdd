#!/usr/bin/env python

a=[1,2]
while (a[-1]+ a[-2]) <4000000:
    a.append(a[-1] + a[-2])
    

b = [x for x in a if x % 2 == 0]
print sum(b)
