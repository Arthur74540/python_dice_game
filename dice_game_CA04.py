import random
import sys

def search_count(text, nb):
    count = counter.count(nb)
    if count > 0:
        print(str(count)+' '+text)
        return True
    else:
        return False

counter = []
for i in range(7):
    counter.append(0)

dices = []
nb = 4
if len(sys.argv) > 1:
    nb = int(sys.argv[1])

for i in range(nb):
    dices.append(random.randint(1,6))

print(dices)
print(sorted(dices))

for dice in dices:
    counter[dice] += 1
print(counter)

def search_run():
    totalcounter = 0
    for i in range(nb):
        if counter[i] == counter[i+1] and counter[i] != 0:
            totalcounter += 1
    if search_count("Four the same", 4):
        print("")
    elif search_count("Three the same", 3):
        print("")
    elif totalcounter == 3:
        print("Run of four")
    elif totalcounter == 2 and search_count("Pair", 2):
        print("Run of three with a pair")
    elif search_count("Pair", 2):
        print("")
    elif totalcounter == 2:
        print("Run of three")
    elif totalcounter == 0 and search_count("Pair", 2):
        print("Two pairs")
    else:
        print("All different")



search_run()


    



