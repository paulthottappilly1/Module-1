# Student Name: Paul Thottappilly
# Group Members: Hassan Chughtai, Ivory Steed, Tony Le, Shekar Balasubramaniam 

# Links used below for exercise 
# https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/
# https://www.geeksforgeeks.org/find-average-list-python/

# Imports the function for mean
from statistics import mean

# The function for average 
def Average(list):
    return mean(list)

list = []
k = 1
 
n = int(input("Enter a number: "))

# The loop takes in n floats from the user and stores them in a list
for i in range(0, n):
    nnums = float(input("Enter number " + str(k) + ": "))
    list.append(nnums)
    k = k + 1

average = Average(list)
# Prints the list and the mean
print("List:", list)
print("Average:", average)
