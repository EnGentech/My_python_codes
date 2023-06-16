a = int(input("Enter shape size\t\t"))
space = 0
decrementor = a
for x in range(0, a, 2):
    print(" "*space + " *"*decrementor)
    space += 2
    decrementor -= 2

space = int((a-3))
incrementor = 3
for x in range(a-1, 0, -2):
    print(" "*space + " *"*incrementor)
    space -= 2
    incrementor += 2


