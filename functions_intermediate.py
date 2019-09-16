# As part of this assignment, please create a function randInt() where

# 1.randInt() returns a random integer between 0 to 100
# 2.randInt(max=50) returns a random integer between 0 to 50
# 3.randInt(min=50) returns a random integer between 50 to 100
# 4.randInt(min=50, max=500) returns a random integer between 50 and 500


import random 
import math

def randIntFun():
    return math.floor(random.random()*100)

print(randIntFun())

def zero_to_fifty():
    return math.floor(random.randint(0,50))
print(zero_to_fifty())

def fifty_to_hundred():
    return math.floor(random.randint(50, 100))
print(fifty_to_hundred())

def fifty_to_fivehun():
    return math.floor(random.randint(50, 500))
print(fifty_to_fivehun())