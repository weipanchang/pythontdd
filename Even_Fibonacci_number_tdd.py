#!/usr/bin/env python
import sys
import unittest
import Even_Fibonacci_number

class test_Even_fibonacci(unittest.TestCase):
    def setUp(self):
        self.f =  Even_Fibonacci_number.fibonacci()
#        self.f.value = 0
    
    def test_max(self):
        self.f.value = 3
        self.assertEqual(self.f.value, 3)
    
    def test_fibonacci_number_1(self):
        self.f.value =1
        self.assertEqual(self.f.fibonacci_number(),1)
        
    def test_fibonacci_number_2(self):
        self.f.value =2
        self.assertEqual(self.f.fibonacci_number(),2)
        
    def test_fibonacci_list_1(self):

        self.assertEqual(self.f.fibonacci_list(2),[1,2])
        
    def test_fibonacci_list_3(self):

        self.assertEqual(self.f.fibonacci_list(3),[1,2,3])
        
    def test_fibonacci_list_4(self):

        self.assertEqual(self.f.fibonacci_list(35),[1,2,3,5,8,13,21,34])
    
    def test_even_fibonacci_list_1(self):
        
        self.assertEqual(self.f.even_fibonacci_list(35),[2,8,34])
    
    def tearDown(self):
        pass
    
    

if __name__ == "__main__":
    unittest.main()