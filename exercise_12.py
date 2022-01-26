# Student Name: Paul Thottappilly
# Group Members: Hassan Chughtai, Ivory Steed, Tony Le, Shekar Balasubramaniam 

# Links used below for exercise 
# https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/#:~:text=In%20Python%2C%20lower()%20is,it%20returns%20the%20original%20string.
from audioop import reverse

# User inputs string
uinput = input("Enter a string: ")

# Creates two lists to print the upper and lower case letters
lowerc = []
upperc = []

# Turns all the lowercase letters into uppercase and all the uppercase letter into lowercase
lowerc = [l for l in uinput if l.islower()]
upperc = [l for l in uinput if l.isupper()]

# Orders the lowercase letters first and the uppercase letters second
reverse = (lowerc + upperc)
for i in reverse:
    print(*i, sep = '', end ='')