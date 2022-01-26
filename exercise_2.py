# Student Name: Paul Thottappilly
# Group Members: Hassan Chughtai, Ivory Steed, Tony Le, Shekar Balasubramaniam 

# Link used below for exercise 
# https://stackabuse.com/python-check-if-string-contains-substring/ 

# User inputs in two strings and stores it into variables
subword = str(input("Enter a string: "))
fullword = str(input("Enter another string: "))

# Checks to see if the substring is in the string and prints if it is or isn't
if subword in fullword:
    print("True")
else:
    print("False")