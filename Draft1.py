### Variables ###

##inventory
g = 0
inventory = ()
gameOver = False
usrHandness = 0 ##1 = right handed 2 = left handed

##player setup questions

print("This game is an adventure game where you will explore, gain experience and collect weapons.\nPlease answer a few questions about your character:")
nameCheck = True
while nameCheck == True:
    usrName = input("What would you like to call yourself?")
    if usrName.isdigit():
        print("Please enter a name, not a number")
    elif len(usrName) > 20:
        print("Please enter a shorter name")
    else:
        print("Your name is " + usrName)
        nameCheck2 = True
        while nameCheck2 == True:
            nameConfirm = input("Confirm [Y/N}").lower()
            if nameConfirm in ["y", "yes"]:
                nameCheck = False
                nameCheck2 = False
            elif nameConfirm in ["n", "no"]:
                nameCheck2 = False
            else:
                print("Please enter a valid input")
handCheck = True
while handCheck == True:
    usrHand = input("Are you right or left handed?").lower()
    if usrHand in ["right, r"]:
        usrHandness = 1
        print("You are right-handed.")
        handCheck = False
    elif usrHand in ["left", "l"]:
        usrHandness = 2
        print("You are left-handed")
        handCheck = False
    else:
        print("Please enter a valid input")
        
### Game loop ###

#while not gameOver:

