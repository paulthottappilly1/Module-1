# Student Name: Paul Thottappilly
# Group Members: Hassan Chughtai, Ivory Steed, Tony Le, Shekar Balasubramaniam 

# Link used below for exercise 
# https://kodify.net/python/math/square/ 

# Imports the function for square root
from math import sqrt

k = 0

squarenum = int(input("Enter a number greater than 1: "))

# Prints out the squares of each integer from 0 to the inputted integer
for x in range(0,squarenum + 1):
    if k >= 0:
        print("The square of", k, "is", k ** 2)
        k = k + 1
    else:
        print("Invalid input")
        break