#!/usr/bin/env python

class Clock():
    def _init_(self, time):
        
        self.time = time
        
    def long_hand(self):
        a, b =  self.time.split(':')
        return (float(b) / 60) * 360
    def short_hand(self):
        a, b =  self.time.split(':')
        return (int(a)  / 12.00 ) * 360 + int(b) / 60.00 * 30.00
        
