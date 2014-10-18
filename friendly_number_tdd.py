#!/usr/bin/env python

import os
import unittest
import friendly_number as f

class test_frendly_number(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_case_1(self):
        
        self.assertEqual(f.find_divisor(16), [1, 2, 4, 8, 16 ])

    def test_case_2(self):
        
        self.assertEqual(f.unfriend_number([2,5,7,4,3,8,3,18], [1, 2, 4, 8, 16 ]), 1)
        
    def test_case_3(self):
        
        self.assertEqual(f.unfriend_number([2,5,7,4,3,8,3,18], f.find_divisor(16)), 1)
        
    def test_case_4(self):
        
        self.assertEqual(f.unfriend_number([2,5,7,4,3], f.find_divisor(16)), 2)
    
    def tearDown(self):
        pass
    
  
    
    
if __name__ == "__main__":
    unittest.main()
    