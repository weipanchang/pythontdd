#!/usr/bin/env python

def find_special_pythagorean_triple(N):
    triplet = [(a,b,c) for a in range(1,N//3+1) for b in range(a,N//2+1) for c in range(b,N-1) if (a**2 + b**2 == c**2) and (a+b+c == N)]
    print triplet, reduce(lambda x,y: x * y , triplet[0])
    return

find_special_pythagorean_triple(12)
find_special_pythagorean_triple(1000)


