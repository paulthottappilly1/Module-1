# Student Name: Paul Thottappilly
# Group Members: Hassan Chughtai, Ivory Steed, Tony Le, Shekar Balasubramaniam 

# Links used below for exercise 
# https://www.kite.com/python/answers/how-to-find-common-elements-between-two-lists-in-python
# https://stackoverflow.com/questions/47454788/common-elements-between-two-lists-with-no-duplicates

lista = []
listb = []
listfinal = []

def intersection():
    listset = set(lista)
    intersection = listset.intersection(listb)

for i in range(0,5): # stores first 5 ints in a list
    inputlist = int(input("Enter a number for the first list: "))
    lista.append(inputlist) 

for i in range(0,5): # stores second 5 ints in a list
    inputlist = int(input("Enter a number for the second list: "))
    listb.append(inputlist)

for i in lista: # third list to have common ints between the first two arrays
    if i in listb and i not in listfinal:
        listfinal.append(i)
print(listfinal)