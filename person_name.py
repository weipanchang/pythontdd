#!/usr/bin/env python
import sys

class person:
    def __init__(self, f, l):
        self.first = f
        self.last = l
        self.age = 12
    def prt(self):
        return self.first + " " + self.last + " " + str(self.age)


def main(l):
    input1 = l[0]
    input2 = l[1]
    #print input1, input2
    p = person(input1, input2)
    print p.prt()
    for i in range(1, 10):
        p.age = p.age + 1;
        print p.prt()    
        
    

if __name__ == "__main__":
    print("two.py is being run directly")
    main(sys.argv[1:])
else:
    print("two.py is being imported into another module")
    
