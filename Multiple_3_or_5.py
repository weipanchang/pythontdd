#!/usr/bin/env python
a = set([i * 3 for i in range(int(21/3))])
b = set([i * 5 for i in range(int(21/5))])

for x in b:
    a.add(x)
print a

print sum(a)
         

