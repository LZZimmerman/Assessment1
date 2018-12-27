### Variables ###

##inventory
g = 0
inventory = ()
gameOver = False


##player setup questions
print("This game is an adventure game where you will explore, gain experience and collect weapons.\nPlease answer a few questions about your character:")
usrName = input("What would you like to call yourself?")
usrHand = input("Are you right or left handed?")
### Game loop ###

while not gameOver:
