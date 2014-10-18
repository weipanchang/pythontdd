#!/usr/bin/env python
import math

class Number:
    def _init_(self, value):
        self.value = value
    
    def dec_bin(self):
        n = self.value
        l = base_list(n)

        def recursive(n, i):
        
            if i ==  len(l) -1:
                
                return str(n)
            else:
                if n >= l[i]:
                    x = str(n // l[i])
                    n =  n % l[i]
                else: x = '0'
                return x + (recursive(n, i + 1))
        return recursive(n, 0)
#        return x
        
    
    def bin_dec(self):
        s = self.value
        def recursive(i):
            if i == len(s) - 1:
                return int(s[i]) * int(math.pow(2, len(s)- i -1))
            else:
                result = int(s[i]) * int(math.pow(2, len(s)- i - 1))
                return result + recursive(  i + 1)
        return recursive(0)
        return x
    
    def value_print(self):
        return "The value is %s" % (str(self.value))
    

def base_list(n):
    l = [int(math.pow(2, i)) for i in range(int(math.log(n, 2)), -1, -1)]
    return l