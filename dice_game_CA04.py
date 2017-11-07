import random
import sys

counter = []
for i in range(7):
    counter.append(0)

dicesValues = []
nbofdices = int(input("With how much dices do you want to play?"))
if len(sys.argv) > 1:
    nbofdices = int(sys.argv[1])

for i in range(nbofdices):
    dicesValues.append(random.randint(1,6))

print(dicesValues)
print(sorted(dicesValues))

for dice in dicesValues:
    counter[dice] += 1

print(counter)

for i in range(7):
    if counter[i] == nbofdices:
        print(nbofdices,"the same")
        
checking = False
while checking == False:
    if counter[i] == 1:
        checking = True
        print("run of",nbofdices)


    



