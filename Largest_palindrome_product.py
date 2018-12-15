#!/usr/bin/env python

def check_palindrome(n):
    s = str(n)
    for i in xrange(len(s) //2 + 1):
        if s[i] != s[len(s) - i -1]:
            return False
    return True

def find_factor(n):
    for i in xrange(999,100,-1):
        if n % i == 0 and len(str(n/i)) == 3:
            print "The palindrome is ", n, " The factors are ", i, n/i
            return True
    return None

for n in xrange(999999,100001, -1):
    if check_palindrome(n) == True:
        if find_factor(n) == True:
            break
#    print "Not found"
# print check_palindrome(1001)
# print check_palindrome(1012)
# print check_palindrome(990099)
# print find_factor(9009)
    