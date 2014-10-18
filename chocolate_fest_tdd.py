#!/usr/bin/env python
import os
import chocolate_fest
import unittest

class test_chocolate_fest(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_init_buy_1(self):
        self.assertEqual(chocolate_fest.init_buy(2, 5), 2)
        self.assertEqual(chocolate_fest.init_buy(6, 4), 0)
        
    def test_wraper(self):
        self.assertEqual(chocolate_fest.wraper(2, 4), 2)
        self.assertEqual(chocolate_fest.wraper(5, 4), 0)
        self.assertEqual(chocolate_fest.wraper(2, 13), 9)
        
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()