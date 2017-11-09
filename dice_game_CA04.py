import random
import sys

def search(text, nb):
    count = counter.count(nb)
    if count > 0:
        print(str(count)+' '+text)

counter = []
for i in range(7):
    counter.append(0)

dices = []
nb = 4
if len(sys.argv) > 1:
    nb = int(sys.argv[1])

for i in range(nb):
    dices.append(random.randint(1,6))

def counter():
    totalcounter = 0
    for i in range(3):
        if sorted(dices)[i] == sorted(dices[i+1]):
            totalcounter = totalcounter + 1           

print(dices)
print(sorted(dices))

for dice in dices:
    counter[dice] += 1


search("Four the same", 4)
search("Three the same", 3)
search("Pair", 2)

counter()
if totalcounter == 3:
    print("Run of four")
elif totalcounter == 2 and search("Pair", 2):
    print("Run of three with a pair")
elif totalcounter == 2:
    print("Run of three")
elif totalcounter == 0 and search("Pair", 2):
    print("Two pairs")
else:
    print("All different")


    



