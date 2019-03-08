# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 22:05:27 2019

@author: Admin
"""
from cat import Cat

start = input("Do you have a cat?(Y/N)")
while True:
    if start.upper() == "Y":
        name = input("Cat Name?")
        color = input("cat color?")
        weight = int(input("weight(lbs)?"))
        cat = Cat(name, color, weight)
        cat.meow()
        start = input("Another cat?(Y/N)")
    elif start.upper() == "N":
        break
    else:
        start = input("Sorry, try again? (Y/N)")
print("Goodbye")