#!/usr/bin/env python

class fibonacci():
    def _init_(self, value):
        self.value = value
    
    def fibonacci_number(self):
        m = self.value

        def recursive(n):
            
            if n == 1:            
                return 1
            elif n == 2:
                return 2
            else:
                return recursive(n-1) + recursive(n-2)

        return recursive(m)

    def fibonacci_list(self, top):
        self.value = 0
        l = []
        while 1:
            self.value += 1
            x = self.fibonacci_number()
            if x > top: break
            l.append(x)
        return l
    
    def even_fibonacci_list(self, top):
        l = self.fibonacci_list(top)
        return [x for x in l if x % 2 == 0 ]
            
            
            
            