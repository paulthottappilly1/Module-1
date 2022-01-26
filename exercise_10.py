# Student Name: Paul Thottappilly
# Group Members: Hassan Chughtai, Ivory Steed, Tony Le, Shekar Balasubramaniam 

# Links used below for exercise 
# https://www.geeksforgeeks.org/break-list-chunks-size-n-python/

# Takes in a string from the user
ustring = input("Enter a string: ")
ustring = str(ustring)

# Splits the string into an array of single characters
def split(ustring):
    return list(ustring)
ustring = (split(ustring))

# Prints the string in lists of 3 elements
n = 3
slist = [ustring[i * n:(i +1) * n] for i in range ((len(ustring) + n - 1) // n)]
print(slist)