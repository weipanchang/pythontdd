#!/usr/bin/env python
import sys
import unittest
import decimal_binary_convert

class TestConvertTests(unittest.TestCase):
    def setUp(self):
        self.n = decimal_binary_convert.Number()
        
    def test_print(self):
        self.n.value = 2
        self.assertEqual(self.n.value_print(), 'The value is 2')
        
        self.n.value= '10'
        self.assertEqual(self.n.value, '10')
        
    def test_base_list(self):

        self.assertEqual(decimal_binary_convert.base_list(2), [2,1])
        self.assertEqual(decimal_binary_convert.base_list(15), [8,4,2,1])
    
    def test_dec_to_bin(self):
        
        self.n.value = 2
        self.n.value = self.n.dec_bin()
        self.assertEqual(self.n.value, '10')
        
        self.n.value = 15
        self.n.value = self.n.dec_bin()
        self.assertEqual(self.n.value, '1111')
        
        self.n.value = 33
        self.n.value = self.n.dec_bin()
        self.assertEqual(self.n.value, '100001')
        
        
    def test_bin_to_dec(self):

        self.n.value = '10'
        self.n.value = self.n.bin_dec()
        self.assertEqual(self.n.value, 2)
        
        self.n.value = '10101'
        self.n.value = self.n.bin_dec()
        self.assertEqual(self.n.value, 21)
        
    def tearDown(self):
        pass
        
if __name__ == "__main__":
    unittest.main()
