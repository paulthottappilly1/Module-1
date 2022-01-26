# Student Name: Paul Thottappilly
# Group Members: Hassan Chughtai, Ivory Steed, Tony Le, Shekar Balasubramaniam 

# Links used below for exercise 
# https://www.w3schools.com/python/python_howto_reverse_string.asp

# The function will take the string and slices it backwards
def reversestring(s):
    return s[::-1]

# Calls the function
s = reversestring(input("Enter a string: "))
# Prints the input
print(s)