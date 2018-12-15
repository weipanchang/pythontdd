#!/usr/bin/env python
def find_diff(i,l):
    m = len(l)
    if i < m -1:
        if l[i] != l[i + 1]:
            return i
        else:
            return find_diff(i + 1, l)
    return i
    
def main(l):
    i = 0
    while i <= len(l)-1:
        print l[i], find_diff(i,l) - i + 1
        if i < find_diff(i,l):
            i = find_diff(i,l)
            
        i = i + 1
        
    
    
    
l = [2,2,1,3,3,4,3,3,3,5,5,4]
main(l)