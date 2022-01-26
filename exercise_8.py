# Student Name: Paul Thottappilly
# Group Members: Hassan Chughtai, Ivory Steed, Tony Le, Shekar Balasubramaniam 

# Links below indicate help found online
# https://stackoverflow.com/questions/12887042/python-using-set-to-create-list-of-elements-that-only-appear-once

# Imports the function for Counter
from collections import Counter

x = []
y = []

# Takes in 10 numbers and adds them to a list
for i in range(0, 10):
    nnums = int(input("Enter a number: "))
    x.append(nnums)

# Creates a new list with only elements that appear once
for numonce, num in Counter(x).most_common():
    if num == 1:
        y.append(numonce)
# Prints the list with the unique elements
print(y)
