#!/usr/bin/env python

import unittest
import largest_primary_factor

class test_Largest_prmary_factor(unittest.TestCase):
    def setUp(self):
        self.number = largest_primary_factor.Number()
        self.number.num = 0
    
    def test_check_primary(self):
        self.assertTrue(largest_primary_factor.primary_check(2))
        self.assertTrue(largest_primary_factor.primary_check(17))
        self.assertTrue(largest_primary_factor.primary_check(41))
        self.assertFalse(largest_primary_factor.primary_check(15))
                        
    def test_find_factor_1(self):
        self.number.num = 12
        self.assertEqual(self.number.find_factor(), 6)
        
    def test_find_factor_2(self):
        self.number.num = 17
        self.assertEqual(self.number.find_factor(), None)
    
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()