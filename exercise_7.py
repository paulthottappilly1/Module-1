# Student Name: Paul Thottappilly
# Group Members: Hassan Chughtai, Ivory Steed, Tony Le, Shekar Balasubramaniam 

# Link used below for exercise 
#https://www.quora.com/How-do-you-write-a-Python-program-that-takes-inputs-from-the-user-until-q-is-entered-Do-you-have-to-make-a-list-from-user-inputs

list=[]
evennumlist = []

# Inputs numbers into a list until the user types QUIT
while True:
    entry = input("Enter a number or QUIT: ")
    if entry == "QUIT":
        break
    
    list.append(int(entry))
# Takes the list and creates a new list with the even numbers in the original list
for x in list:
    if x % 2 == 0:
        evennumlist.append(x)

# Prints the list without brackets
print(evennumlist)