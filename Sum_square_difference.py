#!/usr/bin/env python
def sum_square_difference(m):
    l = [i for i in range(m+1)]
    return sum(l) ** 2 - reduce((lambda a, b : a + (b ** 2)), l)

print "sum_square_difference for 10 is ",  sum_square_difference(10)
print "sum_square_difference for 100 is ",  sum_square_difference(100)
print "sum_square_difference for 10000 is ",  sum_square_difference(1000)



    
