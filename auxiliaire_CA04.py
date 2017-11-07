import random
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
dice3 = random.randint(1,6)
dice4 = random.randint(1,6)

diceValues = [dice1, dice2, dice3, dice4]
print(diceValues)
print(sorted(diceValues))
sortdiceValues = [sorted(diceValues)]

counter = [6]
count1 = diceValues.count(1)
count2 = diceValues.count(2)
count3 = diceValues.count(3)
count4 = diceValues.count(4)

if count1 == 4 or count2 == 4 or count3 == 4 or count4 == 4:
    print("four the same")
elif count1 == 3 or count2 == 3 or count3 == 3 or count4 == 3:
    print("three the same")
elif count1 == 1 and count2 == 1 and count3 == 1 and count4 == 1:
    print("run of four")
elif count1 == 2 and count2 == 2 or count1 == 2 and count3 == 2 or count1 == 2 and  count4 == 2 or count2 == 2 and count3 == 2 or count2 == 2 and count4 == 2 or count3 == 2 and count4 == 2:
    print("Two pairs")
elif count1 == 1 and count2 == 1 or count1 == 1 and count3 == 1 or count1 == 1 and count4 == 1 or count2 == 1 and count3 == 1 or count2 == 1 and count4 == 1 or count3 == 1 and count4 == 1:
    print("pair")
elif count1 == 1 and count2 == 1 and count3 == 1 or count2 == 1 and count3 == 1 and count4 == 1 and count1 == 1 and count2 == 1 or count1 == 1 and count3 == 1 or count1 == 1 and count4 == 1 or count2 == 1 and count3 == 1 or count2 == 1 and count4 == 1 or count3 == 1 and count4 == 1:
    print("run of three with a pair")
elif count1 == 1 and count2 == 1 and count3 == 1 or count2 == 1 and count3 == 1 and count4 == 1:
    print("run of three")
    
