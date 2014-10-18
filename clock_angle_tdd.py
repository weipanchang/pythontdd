#!/usr/bin/env python
import unittest
import clock_angle

class test_Clock_angle(unittest.TestCase):
    def setUp(self):
        self.clock =  clock_angle.Clock()
        
    def testlonghandangle(self):
        self.clock.time='3:20'
        self.assertEqual(self.clock.long_hand(), 120)
        
    def testshorthandangle(self):
        self.clock.time='3:00'
        self.assertEqual(self.clock.short_hand(), 90)
        
    def testshorthandangle2(self):
        self.clock.time='6:30'
        self.assertEqual(self.clock.short_hand(), 195)
    
    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()