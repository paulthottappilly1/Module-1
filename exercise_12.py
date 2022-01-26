from audioop import reverse

uinput = input("Enter a string: ")

lowerc = []
upperc = []

lowerc = [l for l in uinput if l.islower()]
upperc = [l for l in uinput if l.isupper()]

reverse = (lowerc + upperc)
for i in reverse:
    print(*i, sep = '', end ='')