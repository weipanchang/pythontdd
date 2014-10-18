#!/usr/bin/env python

import os

def init_buy(c, n):
    return int(n/c)

def wraper(m, k):
    n= 0
    while m <= k:
        n += int(k/m)
        k -= n * m
        k += n
    return n

total = init_buy(2, 6)
print total
total = total + wraper(2, total)
print total