#!/usr/bin/env python
a = set([i * 3 for i in range(1, int(10/3) +1)])
b = set([i * 5 for i in range(1, int(10/5) +1)])

for x in b:
    a.add(x)
print a

print sum(a)
         

