# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 22:04:10 2019

@author: Admin
"""
class Cat:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    def meow(self):
        print("meow, my name is"+" "+self.name)
        print("meow, my color is"+" "+self.color)
        if self.weight > 12:
            print("meow, I'm fat")
        else:
            print("meow, I'm skinny")
