import random

##testing code in the game

# a = 5
# b = 6
# for i in range(0,20):
#     i = random.randint (1+a,3+a)
#     print(i)
#
# inputcheck = True
# while inputcheck == True:
#     print("before loop break")
#     inputcheck = False
#     print("after loop break")
testDict = {"Sword": 1, "Staff": 1}
testList = ("Wooden Sword", "Wooden Staff", "Wooden Dagger")
liststring = "\n".join(testList)
print(liststring)
print(testDict["Sword"])

for i in range(0,3):
    print(i+1,"-",testList[i])
testChoice = 1
print("You have chosen to use your", testList[0])
print("You have chosen to use your", testList[testChoice])

attackdmg = 0
intel = 19
print("hey", attackdmg, "hey")
attackdmg = int(5+(intel)/10)
print(attackdmg)