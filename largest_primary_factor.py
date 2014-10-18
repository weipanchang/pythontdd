#!/usr/bin/env python
import math

class Number():
    def _init_(self, num):
        self.num = num
    
    def find_factor(self):
        for i in range(2, int(math.sqrt(self.num) + 1)):
            if self.num % i == 0:
                if primary_check(self.num / i ) == True:
                    return self.num / i
        return None
    
def primary_check(n):
    is_primary = True
    if n == 1 or n == 2 or n == 3:
        return True
    for i in range(3, int(math.sqrt(n) + 1)):
        if n % i == 0:
            is_primary = False
            break
    return is_primary
        
