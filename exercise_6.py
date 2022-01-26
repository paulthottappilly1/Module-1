# Student Name: Paul Thottappilly
# Group Members: Hassan Chughtai, Ivory Steed, Tony Le, Shekar Balasubramaniam 

# Link used below for exercise 
# https://www.kite.com/python/answers/how-to-print-a-list-without-brackets-in-python#:~:text=Use%20*%20to%20print%20a%20list,set%20sep%20to%20%22%2C%20%22%20.

# Inputs a row number from 1 to 5 and a column number from 1 to 5
rownumber = int(input("Enter a row num from 1 to 5: "))
columnnumber = int(input("Enter a col num from 1 to 5: "))

# Creates the grid of 0s and puts a 1 in the row and column numbers inputted 
g = [([0] * 5) for i in range(5)]
g[rownumber - 1][columnnumber - 1] = 1

# Prints the list without brackets
for i in g:
    print(*i, sep = ' ')