##importing##

import random

#Contents:
#Lines 1-70 Variables                               #
#Lines 70-315 system functions (e.g. combat)        #
#lines 315-365 item drop functions                  #
#lines 365 - 1000 forest encounters (functions)     #
#lines 1000 - 1265 forest exploration (functions)   #
#lines 1265 - 1556 town functions                   #
#lines 1556 - 1580 setup questions                  #
#lines 1580- 1630 game loop                         #

### Variables ###

gameOver = False #to run the game loop
playerWin = True #will be determined in all encounters, losing returns player to town

usrName = "Placeholder" #placeholder user name, will be used in dialogue later
attackDmg = 0 #damage variable, used in combat
enemyDmg = 0 #enemy damage variable, also used in combat
enemyHealth = 0 #enemy health variable

#flags relating to each area, Clear means the boss has died, while "boss" is whether the player has located the boss
forestClear = 0
forestBoss = 0 #when you find the encampment
ogreGuard = 0 #when you kill the guard



##player stats
pHealth = 120
pHealthMax = 120
pMana = 20
pManaMax = 20
pLevel = 1
pExperience = 0
##inventory

gold = 100
healthPotions = 1
manaPotions = 1
weaponList = ["Plywood Staff", "Bronze Sword", "Bronze Daggers"]
#list will be called for descriptions
weaponDict = {"Staff": 1, "Sword": 1, "Dagger": 1}
#dictionary stores "quality" of material and is used when calculating damage
weaponChoice = 0
#which weapon you're currently using
armourList = ["No Helm", "Leather Armour", "Cloth Boots"]
armourDict = {"Helm": 0, "Armour": 10, "Boots": 10}
#armour dict stores +hp values of the 3 parts of armour, but only helmets are currently purchaseable

##skills
strength = 10
agility = 10
intel = 10
dodge = 1

##town shops:
#weapons
staffDict = {"Pine Staff": 50, "Oak Staff": 100, "Willow Staff": 200}
swordDict = {"Iron Sword": 50, "Steel Sword": 100, "Mithril Sword": 200}
daggerDict = {"Iron Daggers": 50, "Steel Daggers": 100, "Mithril Daggers": 200}

#armour
helmDict = {"Leather Helm": 20, "Bronze Helm": 40, "Iron Helm": 100}
bodyDict = {"Chainmail": 100, "Iron Plate": 200, "Mithril Plate": 500}
bootDict =  {"Leather Boots": 50, "Iron Boots": 100}
##functions below
def pWeapon(): #function to show weaponlist
    global weaponChoice
    print("You are currently carrying the following weapons:")
    for i in range(0, 3):
        print(i + 1, "-", weaponList[i])
        #prints the weapons list
    inputCheck = True
    while inputCheck == True:
        pinput = input("Which weapon would you like to use? (1), (2), or (3)?\n").lower()
        if pinput in ["1", "staff"]:
            weaponChoice = 0
            print("You have chosen to use your", weaponList[0]) #description of your current staff
            inputCheck = False
        elif pinput in ["2", "sword"]:
            weaponChoice = 1
            print("You have chosen to use your", weaponList[1]) #chosen to use your sword
            inputCheck = False
        elif pinput in ["3", "dagger"]:
            weaponChoice = 2
            print("You have chosen to use your", weaponList[2]) #chosen to use your daggers
            inputCheck = False
        else:
            print("Invalid input")


def pStatus():  ##function to show current status, will be used after every encounter

    print("\nYou are currently level", str(pLevel), "and need", 100-pExperience,"experience to reach the next level")
    print("\nYou have",pHealth, "out of", pHealthMax, "health remaining and", pMana,"out of", pManaMax, "mana remaining")
    print("\nYour current stats are as follows:\nStrength: %d\nAgility: %d\nIntelligence: %d\n" % (strength, agility, intel))


def pCombatStatus(): #short version of above to be used in combat
    print("\nYou have",pHealth, "out of", pHealthMax, "health remaining and", pMana,"out of", pManaMax, "mana remaining")

def pEconomy():#economystatus
    print("You have ", gold, "gold\n")


def combatFormula(): #decides damage you will do:
    global attackDmg
    global pMana

    #multipliers based on quality of weapon
    staffMultiplier = int(weaponDict["Staff"])
    swordMultiplier = int(weaponDict["Sword"])
    daggerMultiplier = int(weaponDict["Dagger"])

    # when you have mana and you have chosen your staff
    if weaponChoice == 0 and pMana > 0:
        print("You point your staff in the direction of your opponent and recite an incantation")
        # damage formula used elsewhere, at 10 intelligence you deal 11 damage with a spell
        attackDmg = int((5 + (intel * 3) / 5) * staffMultiplier)
        pMana -= 1
        if intel < 20:
            print("You hurl a small fireball from your staff!")
        elif intel < 50:
            print("You hurl a large fireball from your staff!")
            attackDmg += 5
        elif intel > 50:
            print("You hurl a blue fireball from your staff, setting your opponent on fire!")
            attackDmg += 40
    # when you choose your staff but are out of mana (<= incase I mess up with mana)
    elif weaponChoice == 0 and pMana <= 0:
        print("You're out of mana, so you attempt to strike the goblin with your staff!")
        attackDmg = int((5 + strength / 10 + agility / 10)* staffMultiplier)
    #when you choose your sword, different text and formula based on strength
    elif weaponChoice == 1:
        if strength < 20:
            print("You cautiously lift your sword and strike at the enemy!")
            attackDmg = int((10 + (strength * 2) / 5) * swordMultiplier)
        elif strength < 40:
            print("You competently strike at the enemy with your sword!")
            attackDmg = int((15 + (strength * 2) / 5) * swordMultiplier)
        elif strength >50:
            print("You expertly swing your sword through the air and strike your opponent!")
            attackDmg = int((20 + (strength *2) / 5) * swordMultiplier)
        #critical strike when you have both high strength and agility
        elif strength >40 and agility > 25:
            print("You dash past your opponent and expertly strike him at a weak point, dealing a critical hit!")
            attackDmg = int((30 + (strength*4) / 5) * swordMultiplier)
    #when wielding daggers
    elif weaponChoice == 2:
        attackDmg = int(agility * daggerMultiplier)
        if agility <20:
            print("You cautiously dash at your opponent, slashing twice with your daggers")
        elif agility <50:
            print("You rapidly dash at your opponent, slashing twice with your daggers")
            attackDmg +=5
        elif agility > 50:
            print("You expertly dash at your opponent, slashing twice upwards then twice again in your downswing")
            attackDmg += 50
    print("You do ", attackDmg, "damage to your opponent\n")


def enemyCombat(): ##rolls enemy damage and takes into account dodge bonuses
    global enemyDmg

    enemyRoll = random.randint(1, 10)
    
    if enemyRoll <= int(dodge/2):
        print("You skillfully dodge as your opponent strikes, completely avoiding his attack!")
        enemyDmg = 0
    elif enemyRoll <= dodge:
        print("You manage to avoid most of your opponent's strike, taking only a glancing blow!")
        enemyDmg = (enemyDmg+enemyRoll)/2
    else:
        print("You couldn't dodge the attack in time!")
        enemyDmg += enemyRoll

def playerLost(): #if you lose a battle
    global pHealth
    global pMana
    global gold

    print("\nYou've lost this battle and attempt to flee!")
    print("You manage to make it to the edge of the forest before collapsing and passing out.")
    print("You wake up back in town at an inn with a concerned doctor looking over you\n")
    print("\"You're lucky", usrName, "that an adventurer found you by the Ming forest and brought you here.")
    print("Unfortunately, my medical services are not free, nor is this inn."
          "\nBut I'm not cruel enough to leave you in debt, so I'll only take what you can afford\"\n")
    pHealth = pHealthMax #restores health and mana to full
    pMana = pManaMax
    print("Your health and mana have been restored to full!\n")
    if gold < 100:
        gold = 0
    else:
        gold -= 100

    pEconomy() #gold update





def pLevelUp(): ##levelling function, happens whenever you level up
    #initialising all global variables that may be edited
    global pLevel
    global pHealth
    global pHealthMax
    global pMana
    global pManaMax
    global strength
    global agility
    global intel
    global dodge

    pLevel = pLevel + 1
    pHealthMax += 10
    pHealth += 10
    pManaMax += 5
    pMana += 5

    print("Congratulations!!! You've now reached level ",str(pLevel),"!\nYour maximum health and mana have increased\nYou can upgrade one of your attributes by 5!")

    inputloop = True
    # avoiding input errors
    while inputloop == True:
        print("\nYour current stats are as follows:\nStrength: %d\nAgility: %d\nIntelligence: %d\n" % (
        strength, agility, intel))
        pinput = input("Please pick one of (Strength), (Agility) and (Intelligence) to upgrade\n").lower()
        if pinput in ["strength", "str", "s"]:
            #when the player chooses to upgrade strength
            confirminput = input("You wish to upgrade your strength, is that correct? (Y)/(N)\n").lower()
            if confirminput in ["yes", "y"]:
                strength += 5
                print("You feel stronger from your combat experience! You are now more comfortable with the sword.")

                pHealth += 30
                pHealthMax += 30
                print("You feel sturdier. You have more health now!\n")
                inputloop = False
            else:
                print()
                #when either an invalid input is put in or they type no, return to attribute upgrade selection
                #repeats for each attribute choice
        elif pinput in ["agility", "agi", "a"]:
            #when the player chooses to upgrade agility
            confirminput = input("You wish to upgrade your agility, is that correct? (Y)/(N)\n").lower()
            if confirminput in ["yes", "y"]:
                agility += 5
                print("You feel more surefooted! You are now more comfortable with the dagger.")

                dodge += 1
                print("Your combat experience has increased your awareness in combat, you may dodge more attacks!\n")
                inputloop = False
            else:
                print()
        elif pinput in ["intelligence", "intel", "int", "i"]:
            #when the player chooses to upgrade intelligence
            confirminput = input("You wish to upgrade your intelligence, is that correct? (Y)/(N)\n").lower()
            if confirminput in ["yes", "y"]:
                intel += 5
                print("Your knowledge of the arcane has increased! You are now more comfortable with the staff.")

                pMana += 10
                pManaMax += 10
                print("Your experience in combat has increased your endurance! You cast more spells\n")
                inputloop = False
            else:
                print()

def potionDrink():  #function for drinking a potion
    global healthPotions
    global manaPotions
    global pHealth
    global pMana

    healthDifference = (pHealthMax - pHealth)     #shows how much health missing
    manaDifference = (pManaMax - pMana)           #shows how much mana missing

    inputCheck = True                             #loop to catch input errors
    while inputCheck == True:
        print("You have %d health potions and %d mana potions" % (healthPotions, manaPotions))
        print("Each health potion restores 100 health, and every mana potion restores 10 mana.")
        pCombatStatus()                           #shows hp/mana remaining
        pinput = input("What would you like to do:\n(1). Drink a health potion\n(2). Drink a mana potion\n(3). Return to the fight\n").lower()

        if pinput in ["1", "health", "hp"]:
            #when selecting the health potion:
            if pHealth == pHealthMax:
            #when you are already at full health
                print("You have full health already.\n")
            #if a health potion will heal you to max hp
            elif healthDifference <= 100:
                healthPotions -= 1
                pHealth = pHealthMax

            else:
            #when a health potion doesn't heal you to maximum health
                pHealth += 100
                healthPotions -= 1
        elif pinput in ["2", "mana", "mp"]:       #always returns to potions in case you want to drink multiple
            if pMana == pManaMax:
                print("You have full mana already.\n")
            elif manaDifference <= 10:
                manaPotions -= 1
                pMana = pManaMax

            else:
                pMana += 10
                manaPotions -= 1
        elif pinput in ["3", "return", "fight"]:
            inputCheck = False #ends the function and returns to the fighting loop
        else:
            print("Invalid input") #returns to the start of function in the case of an incorrect input

#itemdrop events:
def coinDrop(): #when you find a coinpurse
    global gold
    purseValue = random.randint(10,20)
    print("While wandering through the forest you find a dropped coinpurse")
    print("You open it and find %d coins inside!" % (purseValue))
    gold += purseValue  #adds value of coinpurse to goldpile
    pEconomy()          #shows gold in inventory
def healthDrop(): #when you find a health potion
    global healthPotions

    print("You come across a health potion, carefully pack it in your bag")
    healthPotions += 1
    print("You have %d health potions and %d mana potions" % (healthPotions, manaPotions))

def manaDrop():
    global manaPotions

    print("You come across a mana potion, carefully pack it in your bag")
    manaPotions += 1
    print("You have %d health potions and %d mana potions" % (healthPotions, manaPotions))

def chest():
    global gold
    global manaPotions
    global healthPotions

    chestValue = random.randint(80, 250)        #Randomising chest contents
    manaPotValue = random.randint(1,3)
    healthPotValue = random.randint(1,3)

    print("You come across an unopened chest")
    inputCheck = True
    while inputCheck == True:
        pinput = input("Do you:\n(1). Open it\n(2). Leave it be\n").lower()
        if pinput in ["1", "open"]:
            print("You find %d gold inside the chest, as well as %d mana and %d health potions" % (chestValue, manaPotValue, healthPotValue))
            #adding chest contents to inventory
            gold += chestValue
            manaPotions += manaPotValue
            healthPotions += healthPotValue

            pEconomy()                          #update player on gold
            inputCheck = False
        elif pinput in ["2", "leave"]:          #"player choice"
            inputCheck = False
        else:
            print("Invalid input")              #error handling

#Encounters (and exploration)

#Forest zone encounters.

def encGoblin():
    ##this encounter will have more notation, but the basic encounter is reused for multiple enemies, values are changed
    #Goblin encounter.

    #global variables for things that can change after combat
    global pExperience
    global gold
    global pHealth
    global playerWin
    global enemyDmg
    global enemyHealth
    # goldEarned = 0 #will be replaced with a random number
    # expEarned = 0 #will be replaced by a formula
    enemyHealth = 20 #default hp for a goblin
    enemyDmg = 10 #default damage of a goblin
    escape = False

    print("You are faced with a small goblin")
    inputCheck = True
    while inputCheck == True:
        pinput = input("Do you wish to fight?\n(1). Yes\n(2). No\n").lower()
        if pinput in ("1", "yes"):
            fight = True
            inputCheck = False
        elif pinput in ("2", "no"):
            fight = False
            inputCheck = False
        else:
            print("Invalid input")

    while fight == True: ##fight loop, ends when either part wins, or you run away
        print("You are currently wielding your", weaponList[weaponChoice])
        inputCheck = True
        while inputCheck == True:
            pinput = input("Do you wish to change your weapon?\n(1). Yes\n(2). No\n").lower()
            if pinput in ("1", "yes"):
                pWeapon()
                inputCheck = False
            elif pinput in ("2", "no"):
                inputCheck = False
            else:
                print("Invalid input")

        pCombatStatus() #short status showing health and mana
        print("The goblin is currently at", enemyHealth,"Health")

        inputCheck = True
        while inputCheck == True:
            pinput = input("What do you want to do?\n(1). Attack \n(2). Drink a potion\n(3). Attempt to Escape\n").lower()
            if pinput in ("1", "attack"):
                inputCheck = False
            elif pinput in ("2", "potion", "drink"):
                potionDrink()
            elif pinput in ("3", "run", "escape"):
                inputCheck = False
                fight = False
                escape = True
            else:
                print("Invalid input")
        if escape != True:
            combatFormula() #runs the combat code

            if attackDmg >= enemyHealth:
                print("You defeated the goblin!")

                playerWin = True
                # gold reward
                goldEarned = random.randint(10, 20)
                gold += goldEarned
                print("You found ", goldEarned, "gold!")

                #exp reward
                expEarned = (40-pLevel*2) #player exp is less the higher level they are
                print("You earned ", expEarned, "experience!")
                if pExperience + expEarned >= 100: #if the player gets over 100 exp, they level up
                    pLevelUp()
                    pExperience = (pExperience + expEarned - 100) #extra experience is carried over to the next level
                else:
                    pExperience += expEarned
                pStatus()
                fight = False #ends the combat
            else:
                enemyHealth -= attackDmg #subtracts health from goblin and continues to goblin attack turn
                print("The goblin lunges at you with his short sword!")
                if enemyDmg >= pHealth:
                    fight = False
                    playerWin = False
                    playerLost()
                else:
                    pHealth -= enemyDmg
                    print("You lost", enemyDmg, "health!\n")


def encBear(): ##random bear encounter
    global pExperience
    global gold
    global pHealth
    global playerWin
    global enemyDmg
    global enemyHealth
    enemyHealth = 40 #default hp for a bear
    enemyDmg = 15 #default damage of a bear
    escape = False
    
    print("You are faced with a black bear")
    inputCheck = True
    while inputCheck == True:
        pinput = input("Do you wish to fight?\n(1). Yes\n(2). No\n").lower()
        if pinput in ("1", "yes"):
            fight = True
            inputCheck = False
        elif pinput in ("2", "no"):
            fight = False
            inputCheck = False
        else:
            print("Invalid input")

    while fight == True: ##fight loop, ends when either part wins, or you run away
        print("You are currently wielding your", weaponList[weaponChoice])
        inputCheck = True
        while inputCheck == True:
            pinput = input("Do you wish to change your weapon?\n(1). Yes\n(2). No\n").lower()
            if pinput in ("1", "yes"):
                pWeapon()
                inputCheck = False
            elif pinput in ("2", "no"):
                inputCheck = False
            else:
                print("Invalid input")

        pCombatStatus() #short status showing health and mana
        print("The bear is currently at", enemyHealth,"Health")

        inputCheck = True
        while inputCheck == True:
            pinput = input("What do you want to do?\n(1). Attack \n(2). Drink a potion\n(3). Attempt to Escape\n").lower()
            if pinput in ("1", "attack"):
                inputCheck = False
            elif pinput in ("2", "potion", "drink"):
                potionDrink()
            elif pinput in ("3", "run", "escape"):
                inputCheck = False
                fight = False
                escape = True
            else:
                print("Invalid input")
        if escape != True:
            combatFormula() #runs the combat code

            if attackDmg >= enemyHealth:
                print("You defeated the bear!")

                playerWin = True
                # gold reward
                goldEarned = random.randint(20, 30)
                gold += goldEarned
                print("You found ", goldEarned, "gold!")

                #exp reward
                expEarned = (55-pLevel*2) #player exp is less the higher level they are
                print("You earned ", expEarned, "experience!")
                if pExperience + expEarned >= 100: #if the player gets over 100 exp, they level up
                    pLevelUp()
                    pExperience = (pExperience + expEarned - 100) #extra experience is carried over to the next level
                else:
                    pExperience += expEarned
                pStatus()
                fight = False #ends the combat
            else:
                enemyHealth -= attackDmg #subtracts health from enemy and continues to enemy attack turn
                print("The bear charges at you!")
                if enemyDmg >= pHealth:
                    fight = False
                    playerWin = False
                    playerLost()
                else:
                    pHealth -= enemyDmg
                    print("You lost", enemyDmg, "health!\n")



def encTroll(): ##Random troll encounter
    global pExperience
    global gold
    global pHealth
    global playerWin
    global enemyDmg
    global enemyHealth
    enemyHealth = 80 #default hp for a troll
    enemyDmg = 25 #default damage of a troll
    escape = False
    
    print("You are faced with a large troll, he stands at around 8 foot tall.")
    inputCheck = True
    while inputCheck == True:
        pinput = input("Do you wish to fight?\n(1). Yes\n(2). No\n").lower()
        if pinput in ("1", "yes"):
            fight = True
            inputCheck = False
        elif pinput in ("2", "no"):
            fight = False
            inputCheck = False
        else:
            print("Invalid input")

    while fight == True: ##fight loop, ends when either part wins, or you run away
        print("You are currently wielding your", weaponList[weaponChoice])
        inputCheck = True
        while inputCheck == True:
            pinput = input("Do you wish to change your weapon?\n(1). Yes\n(2). No\n").lower()
            if pinput in ("1", "yes"):
                pWeapon()
                inputCheck = False
            elif pinput in ("2", "no"):
                inputCheck = False
            else:
                print("Invalid input")

        pCombatStatus() #short status showing health and mana
        print("The Troll is currently at", enemyHealth,"Health")

        inputCheck = True
        while inputCheck == True:
            pinput = input("What do you want to do?\n(1). Attack \n(2). Drink a potion\n(3). Attempt to Escape\n").lower()
            if pinput in ("1", "attack"):
                inputCheck = False
            elif pinput in ("2", "potion", "drink"):
                potionDrink()
            elif pinput in ("3", "run", "escape"):
                inputCheck = False
                fight = False
                escape = True
            else:
                print("Invalid input")
        if escape != True:
            combatFormula() #runs the combat code

            if attackDmg >= enemyHealth:
                print("You defeated the troll!")

                playerWin = True
                # gold reward
                goldEarned = random.randint(50, 80)
                gold += goldEarned
                print("You found ", goldEarned, "gold!")

                #exp reward
                expEarned = (80-pLevel*2) #player exp is less the higher level they are
                print("You earned ", expEarned, "experience!")
                if pExperience + expEarned >= 100: #if the player gets over 100 exp, they level up
                    pLevelUp()
                    pExperience = (pExperience + expEarned - 100) #extra experience is carried over to the next level
                else:
                    pExperience += expEarned
                pStatus()
                fight = False #ends the combat
            else:
                enemyHealth -= attackDmg #subtracts health from enemy and continues to enemy attack turn
                print("The Troll swings a giant club at you!")
                if enemyDmg >= pHealth:
                    fight = False
                    playerWin = False
                    playerLost()
                else:
                    pHealth -= enemyDmg
                    print("You lost", enemyDmg, "health!\n")


def encTrollAmbush(): ##slightly different encounter for the troll who ambushes you
    global pExperience
    global gold
    global pHealth
    global playerWin
    global enemyDmg
    global enemyHealth
    global forestBoss #new variable as defeating the troll unlocks the boss encampment
    enemyHealth = 100 #this troll is slightly stronger
    enemyDmg = 30 #same as above
    escape = False
    
    print("You turn as a troll rushes out of the undergrowth")
    inputCheck = True
    while inputCheck == True:
        pinput = input("Do you wish to fight?\n(1). Yes\n(2). No\n").lower()
        if pinput in ("1", "yes"):
            fight = True
            inputCheck = False
        elif pinput in ("2", "no"):
            fight = False
            inputCheck = False
        else:
            print("Invalid input")

    while fight == True: ##fight loop, ends when either part wins, or you run away
        print("You are currently wielding your", weaponList[weaponChoice])
        inputCheck = True
        while inputCheck == True:
            pinput = input("Do you wish to change your weapon?\n(1). Yes\n(2). No\n").lower()
            if pinput in ("1", "yes"):
                pWeapon()
                inputCheck = False
            elif pinput in ("2", "no"):
                inputCheck = False
            else:
                print("Invalid input")

        pCombatStatus() #short status showing health and mana
        print("The Troll is currently at", enemyHealth,"Health")

        inputCheck = True
        while inputCheck == True:
            pinput = input("What do you want to do?\n(1). Attack \n(2). Drink a potion\n(3). Attempt to Escape\n").lower()
            if pinput in ("1", "attack"):
                inputCheck = False
            elif pinput in ("2", "potion", "drink"):
                potionDrink()
            elif pinput in ("3", "run", "escape"):
                inputCheck = False
                fight = False
                escape = True
            else:
                print("Invalid input")
        if escape != True:
            combatFormula() #runs the combat code

            if attackDmg >= enemyHealth:
                print("You defeated the troll!")

                playerWin = True
                # gold reward
                goldEarned = random.randint(50, 80)
                gold += goldEarned
                print("You found ", goldEarned, "gold!")

                #exp reward
                expEarned = (100-pLevel*2) #player exp is less the higher level they are
                print("You earned ", expEarned, "experience!")
                if pExperience + expEarned >= 100: #if the player gets over 100 exp, they level up
                    pLevelUp()
                    pExperience = (pExperience + expEarned - 100) #extra experience is carried over to the next level
                else:
                    pExperience += expEarned
                pStatus()
                forestBoss = 1 #unlocks the forest boss encampment
                fight = False #ends the combat
            else:
                enemyHealth -= attackDmg #subtracts health from enemy and continues to enemy attack turn
                print("The Troll swings a giant club at you!")
                if enemyDmg >= pHealth:
                    fight = False
                    playerWin = False
                    playerLost()
                else:
                    pHealth -= enemyDmg
                    print("You lost", enemyDmg, "health!\n")

def encOgreGuard(): ##Ogre guard encounter, when not too weak
    global pExperience
    global gold
    global pHealth
    global playerWin
    global enemyDmg
    global enemyHealth
    global ogreGuard #determines if you defeat an ogre guard
    escape = False
    
    enemyHealth = 180 #this ogre is a bit stronger
    enemyDmg = 40

    print("You approach the ogre guard")
    print("\n\"Who dares challenge me?\" the ogre guard booms")
    inputCheck = True
    while inputCheck == True:
        pinput = input("Do you wish to fight?\n(1). Yes\n(2). No\n").lower()
        if pinput in ("1", "yes"):
            fight = True
            print("\n\"I do, I am ", usrName, "and I will have your head, as well the king you serve!\"")
            print("\"You insolent whelp, I'll crush you like a bag of bones!\" The ogre retorts.")
            inputCheck = False
        elif pinput in ("2", "no"):
            fight = False
            inputCheck = False
        else:
            print("Invalid input")

    while fight == True: ##fight loop, ends when either part wins, or you run away
        print("You are currently wielding your", weaponList[weaponChoice])
        inputCheck = True
        while inputCheck == True:
            pinput = input("Do you wish to change your weapon?\n(1). Yes\n(2). No\n").lower()
            if pinput in ("1", "yes"):
                pWeapon()
                inputCheck = False
            elif pinput in ("2", "no"):
                inputCheck = False
            else:
                print("Invalid input")

        pCombatStatus() #short status showing health and mana
        print("The Ogre guard is currently at", enemyHealth,"Health")

        inputCheck = True
        while inputCheck == True:
            pinput = input("What do you want to do?\n(1). Attack \n(2). Drink a potion\n(3). Attempt to Escape\n").lower()
            if pinput in ("1", "attack"):
                inputCheck = False
            elif pinput in ("2", "potion", "drink"):
                potionDrink()
            elif pinput in ("3", "run", "escape"):
                inputCheck = False
                fight = False
                escape = True
            else:
                print("Invalid input")
        if escape != True:
            combatFormula() #runs the combat code

            if attackDmg >= enemyHealth:
                print("You defeated the Ogre!")

                playerWin = True
                # gold reward
                goldEarned = random.randint(300, 400)
                gold += goldEarned
                print("You found ", goldEarned, "gold!")

                #exp reward
                expEarned = (120-pLevel*2) #player exp is less the higher level they are
                print("You earned ", expEarned, "experience!")
                if pExperience + expEarned >= 100: #if the player gets over 100 exp, they level up
                    pLevelUp()
                    pExperience = (pExperience + expEarned - 100) #extra experience is carried over to the next level
                else:
                    pExperience += expEarned
                pStatus()
                ogreGuard = 1 #unlocks the forest boss fight
                fight = False #ends the combat
            else:
                enemyHealth -= attackDmg #subtracts health from enemy and continues to enemy attack turn
                print("The ogre swings a giant great-sword at you!")
                if enemyDmg >= pHealth:
                    fight = False
                    playerWin = False
                    playerLost()
                else:
                    pHealth -= enemyDmg
                    print("You lost", enemyDmg, "health!\n")



def encOgreRandom(): ##Random Ogre encounter
    global pExperience
    global gold
    global pHealth
    global playerWin
    global enemyDmg
    global enemyHealth

    enemyHealth = 160 #regular ogre's hp/damage
    enemyDmg = 35
    escape = False

    print("You come across an ogre in the forest")
    inputCheck = True
    while inputCheck == True:
        pinput = input("Do you wish to fight?\n(1). Yes\n(2). No\n").lower()
        if pinput in ("1", "yes"):
            fight = True
            inputCheck = False
        elif pinput in ("2", "no"):
            fight = False
            inputCheck = False
        else:
            print("Invalid input")

    while fight == True: ##fight loop, ends when either part wins, or you run away
        print("You are currently wielding your", weaponList[weaponChoice])
        inputCheck = True
        while inputCheck == True:
            pinput = input("Do you wish to change your weapon?\n(1). Yes\n(2). No\n").lower()
            if pinput in ("1", "yes"):
                pWeapon()
                inputCheck = False
            elif pinput in ("2", "no"):
                inputCheck = False
            else:
                print("Invalid input")

        pCombatStatus() #short status showing health and mana
        print("The Ogre is currently at", enemyHealth,"Health")

        inputCheck = True
        while inputCheck == True:
            pinput = input("What do you want to do?\n(1). Attack \n(2). Drink a potion\n(3). Attempt to Escape\n").lower()
            if pinput in ("1", "attack"):
                inputCheck = False
            elif pinput in ("2", "potion", "drink"):
                potionDrink()
            elif pinput in ("3", "run", "escape"):
                inputCheck = False
                fight = False
                escape = True
            else:
                print("Invalid input")
        if escape != True:
            combatFormula() #runs the combat code

            if attackDmg >= enemyHealth:
                print("You defeated the Ogre!")

                playerWin = True
                # gold reward
                goldEarned = random.randint(200, 250)
                gold += goldEarned
                print("You found ", goldEarned, "gold!")

                #exp reward
                expEarned = (100-pLevel*2) #player exp is less the higher level they are
                print("You earned ", expEarned, "experience!")
                if pExperience + expEarned >= 100: #if the player gets over 100 exp, they level up
                    pLevelUp()
                    pExperience = (pExperience + expEarned - 100) #extra experience is carried over to the next level
                else:
                    pExperience += expEarned
                pStatus()
                fight = False #ends the combat
            else:
                enemyHealth -= attackDmg #subtracts health from enemy and continues to enemy attack turn
                print("The ogre swings a giant great-sword at you!")
                if enemyDmg >= pHealth:
                    fight = False
                    playerWin = False
                    playerLost()
                else:
                    pHealth -= enemyDmg
                    print("You lost", enemyDmg, "health!\n")

def encOgreGuardweak(): ##specific encounter when underleveled
    global pHealth
    print("You recklessly charge at the ogre guard, confident in your abilities.")
    print("The ogre guard looks at you then brings his foot backwards.")
    print("You are unable to dodge the kick and sends you flying, perhaps he is a bit too strong for you right now.")
    if pHealth <= 40: #you take 40 damage from the encounter, return when above level 5 where you can confidently take the ogre on
        playerLost()
    else:
        print("You slowly gain consciousness and find yourself mostly intact.\nYou make your way out of the forest and return to town.")
        pHealth -= 40
        pCombatStatus()

def modarakEnc(): ##Ogre king encounter
    global pExperience
    global gold
    global pHealth
    global playerWin
    global enemyDmg
    global enemyHealth
    global forestClear #killing the boss clears the forest
    
    enemyHealth = 300 #as the final boss, he has the highest stats
    enemyDmg = 50
    escape = False
    
    
    print("You approach the ogre king, Modarak")
    print("\n\"I am Modarak, king of all in this forest, what puny thing comes before me?\" Modarak bellows.")
    inputCheck = True
    while inputCheck == True:
        pinput = input("Do you wish to fight?\n(1). Yes\n(2). No\n").lower()
        if pinput in ("1", "yes"):
            fight = True
            print("\n\"I am ", usrName, "and I have come to liberate the Ming forest from your tyranny!\"")
            print("\"Foolish words, I will crush you little one\" Modarak retorts.")
            inputCheck = False
        elif pinput in ("2", "no"):
            fight = False
            inputCheck = False
        else:
            print("Invalid input")

    while fight == True: ##fight loop, ends when either part wins, or you run away
        print("You are currently wielding your", weaponList[weaponChoice])
        inputCheck = True
        while inputCheck == True:
            pinput = input("Do you wish to change your weapon?\n(1). Yes\n(2). No\n").lower()
            if pinput in ("1", "yes"):
                pWeapon()
                inputCheck = False
            elif pinput in ("2", "no"):
                inputCheck = False
            else:
                print("Invalid input")

        pCombatStatus() #short status showing health and mana
        print("The Ogre guard is currently at", enemyHealth,"Health")

        inputCheck = True
        while inputCheck == True:
            pinput = input("What do you want to do?\n(1). Attack \n(2). Drink a potion\n(3). Attempt to Escape\n").lower()
            if pinput in ("1", "attack"):
                inputCheck = False
            elif pinput in ("2", "potion", "drink"):
                potionDrink()
            elif pinput in ("3", "run", "escape"):
                inputCheck = False
                fight = False
                escape = True
            else:
                print("Invalid input")
        if escape != True:
            combatFormula() #runs the combat code

            if attackDmg >= enemyHealth:
                print("You defeated the ogre king Modarak!")
                print("Congratulations, you have successfully saved the forest of Ming!")

                playerWin = True
                # gold reward
                goldEarned = 900
                gold += goldEarned
                print("You found ", goldEarned, "gold!")

                #exp reward
                ##defeating the ogre king levels you up 3 times
                pLevelUp()
                pLevelUp()
                pLevelUp()

                pStatus()
                forestClear = 1 #you successfully cleared the forest!
                fight = False #ends the combat
            else:
                enemyHealth -= attackDmg #subtracts health from enemy and continues to enemy attack turn
                print("Modarak draws upon his arcane power and hurls a fel-flame bolt at you!")
                if enemyDmg >= pHealth:
                    fight = False
                    playerWin = False
                    playerLost()
                else:
                    pHealth -= enemyDmg
                    print("You lost", enemyDmg, "health!\n")


##function for exploring the forest. lists all encounters
def forestExp():
    ##this is the function for all forest events, in hindsight I may have been better served having different functions
    ##based on the global variables of boss being found/area being cleared.
    global forestBoss
    if forestClear >= 1:
        ##forest info once the boss has been defeated
        print("\nYou wander through the Ming forest.\nThere are signs of wildlife returning to live in the forest")
        print("You hear the sounds of birds chirping through the forest and can hear small animals rustling through the bushes")
        print("Most of the evil creatures have fled after you defeated King Modarak")
        forestloop = True
        while forestloop == True:
            #loop of choices within the forest, forestloop = False will return the player to town
            print("You are in the Ming forest")
            pinput = input("Do you wish to:\n(1). Search for any remaining stragglers\n(2). Return to town \n").lower()
            if pinput in ["1", "search"]:
                if random.randint (1,2) == 1:  ##50% chance of no enemy
                    print("You searched far and wide, but couldn't find any evil creatures in the forest")
                else:
                    encounterRoll = random.randint (0+pLevel,10+pLevel)
                    if encounterRoll <= 3:
                        encGoblin()
                        ## the below if statement is used whenever there is combat (repeated after every combEnemy function)
                        ##Winning allows the player to continue the forest loop
                        ##Losing will return them to town, losing money as they are treated by a doctor.
                        if playerWin != True:
                            forestloop = False
                        ##end of combat if statment
                    elif encounterRoll <= 6:
                        encBear()
                        if playerWin != True:
                            forestloop = False
                    else:
                        encTroll()
                        if playerWin != True:
                            forestloop = False
            elif pinput in ["2", "return"]:
                print("You've decided to leave the forest and return to town.\n")
                forestloop = False
    else:
        ##when you haven't cleared the forest, there are more enemies and you start on the outskirts
        print("\nYou've are at the edge of the Ming forest.\nThe Ogre King Modarak reigns over the forest lands")
        print("Little wildlife roams the forest now, and it's inhabited by evil beings such as goblins and trolls")
        print("Sticking to the outskirts will be safer, the more dangerous creatures dwell deep within\n")
        forestloop = True
        while forestloop == True:
            print("You are at the edge of the Ming forest")
            if forestBoss == 1:

                ##if the player has discovered the encampment of the ogre king, the forest options include directly approaching his encampment.

                pinput = input("Do you wish to:\n(1). Search the outskirts of the forest\n(2). Search the deep forest areas \n(3). Approach the Ogre Encampment\n(4). Return to town\n").lower()
                if pinput in ["1", "outskirts"]:
                    if random.randint(1, 3) == 1:
                        ##33% chance of no enemy or items
                        print("You searched the outskirts of the forest for an hour, but encountered no enemies.")
                    elif random.randint(1, 3) == 2:
                        itemRoll = random.randint (1,10)
                        ##chance for different drops
                        if itemRoll <= 5:
                            print("coins")
                        elif itemRoll <= 8:
                            print("healthpot")
                        elif itemRoll == 9:
                            print("twig")
                        else:
                            print("Chest")
                    else:
                        encounterRoll = random.randint(0 + pLevel, 10 + pLevel)
                        ##scaling enemy spawns, less chance of a hard encounter on the outskirts
                        if encounterRoll <= 6:
                            encGoblin()
                            if playerWin != True:
                                forestloop = False
                        else:
                            encBear()
                            if playerWin != True:
                                forestloop = False
                elif pinput in ["2", "deep"]:
                    if random.randint(1, 3) == 1:
                        #always an encounter in the deep forest, 33% for item, 66%enemy
                        itemRoll = random.randint (1,10)
                        ##chance for different drops, common coin drops and rare chest encounters
                        if itemRoll <= 5:
                            coinDrop()
                        elif itemRoll <= 7:
                            healthDrop()
                        elif itemRoll <= 9:
                            manaDrop()
                        else:
                            chest()
                    else:
                        encounterRoll = random.randint(0 + pLevel, 10 + pLevel)
                        ##scaling enemy spawns, minimum level 5 to encounter a troll
                        if encounterRoll <= 3:
                            encGoblin()
                            if playerWin != True:
                                forestloop = False
                        elif encounterRoll <=6:
                            encBear()
                            if playerWin != True:
                                forestloop = False
                        elif encounterRoll <=15:
                            encTroll()
                            if playerWin != True:
                                forestloop = False
                        else:
                            encOgreRandom()
                            if playerWin != True:
                                forestloop = False
                elif pinput in ["3", "approach"]:
                    print("As you approach the encampment, you see a massive ogre standing guard")
                    if pLevel <= 5:
                        #if you are too low level to fight an ogre, you automatically fail
                        inputCheck = True
                        #loop for invalid inputs, I do this more often
                        while inputCheck == True:
                            pinput = input("The ogre seems to be a formidable opponent do you:\n(1). Press on\n(2). Escape to the edge of the forest\n")
                            if pinput in ["1", "press", "fight"]:
                                encOgreGuardweak()
                                inputCheck = False
                                forestloop = False
                                #as you are too low level to fight an ogre, you lose by default.
                                #after the ogre beats you handedly, you are returned to town.
                            elif pinput in ["2", "escape", "run"]:
                                print("You managed to escape to the edge of the forest")
                                inputCheck = False
                            else:
                                print("invalid input, please choose 1 or 2.")
                    else:
                        #when you are above level 5, you have a chance.
                        inputCheck = True
                        while inputCheck == True:
                            pinput = input("What do you want to do?\n(1). Press on and fight the ogre\n(2). Escape to the edge of the forest\n")
                            if pinput in ["1", "press", "fight"]:
                                encOgreGuard()
                                inputCheck = False
                                if playerWin == True and ogreGuard == 1:
                                    ##after defeating the ogre, the player can fight the boss
                                    print("You've defeated the ogre guard, this is your chance to attack King Modarak!")
                                    print("If you choose not to fight him now, there will likely be a new guard when you return.")
                                    inputCheck2 = True
                                    while inputCheck2 == True:
                                        pinput2 = input("Do you: (1). Press on and fight King Modarak\n(2). Escape to the edge of the forest\n")
                                        if pinput2 in ["1", "press", "fight"]:
                                            #starts the bossfight
                                            modarakEnc()
                                        elif pinput2 in ["2", "escape", "run"]:
                                            print("You managed to escape to the edge of the forest")
                                            inputCheck2 = False
                                            ogreGuard = 0
                                        else:
                                            print("Invalid input, please choose 1 or 2.")
                                else:
                                    forestloop = False
                            elif pinput in ["2", "escape", "run"]:
                                print("You managed to escape to the edge of the forest")
                                inputCheck = False
                            else:
                                print("Invalid input, please choose 1 or 2.")
                elif pinput in ["4", "return"]:
                    print("You've decided to leave the forest and return to town.\n")
                    forestloop = False
                else:
                    print("Invalid input")
            ## if the player hasn't discovered the castle
            ## some of the code is copied from above, I probably should have used a function for it
            else:

                pinput = input(
                    "Do you wish to:\n(1). Search the outskirts of the forest\n(2). Search the deep forest areas \n(3). Return to town\n").lower()
                if pinput in ["1", "outskirts"]:
                    if random.randint(1, 3) == 1:
                        ##33% chance of no enemy or items
                        print("You searched the outskirts of the forest for an hour, but encountered no enemies.")
                    elif random.randint(1, 3) == 2:
                        itemRoll = random.randint(1, 10)
                        ##chance for different drops
                        if itemRoll <= 5:
                            coinDrop()
                        elif itemRoll <= 7:
                            healthDrop()
                        elif itemRoll <= 9:
                            manaDrop()
                        else:
                            chest()
                    else:
                        encounterRoll = random.randint(0 + pLevel, 10 + pLevel)
                        ##scaling enemy spawns, less chance of a hard encounter on the outskirts
                        if encounterRoll <= 6:
                            encGoblin()
                            if playerWin != True:
                                forestloop = False
                        else:
                            encBear()
                            if playerWin != True:
                                forestloop = False
                elif pinput in ["2", "deep"]:
                    if random.randint(1, 3) == 1:
                        #always an encounter in the deep forest, 33% for item, 33% you trigger the event to find the boss and 33% random enemy
                        itemRoll = random.randint(1, 10)
                        ##chance for different drops
                        if itemRoll <= 5:
                            coinDrop()
                        elif itemRoll <= 7:
                            healthDrop()
                        elif itemRoll <= 9:
                            manaDrop()
                        else:
                            chest()
                    elif random.randint(1, 3) == 2:
                        #chance to trigger event to find the castle
                        print("You find a path with some heavy footprints, they seem fresh")
                        inputCheck = True
                        while inputCheck == True:
                            pinput2 = input("Do you:\n(1). Follow the path\n(2). Escape to the edge of the forest\n").lower()
                            if pinput2 in ["1", "follow"]:
                                print("As you follow the path, you are ambushed by a troll!")
                                encTrollAmbush()
                                if forestBoss == 1:
                                    print("You follow the path until it reaches a clearing. You've found the Ogre King's encampment!")
                                    print("You carefully make your way to the edge of the forest, marking the path so you can return.")
                                    inputCheck = False
                                else:
                                    inputCheck = False
                                    forestloop = False
                            elif pinput2 in ["2", "escape"]:
                                print("You managed to escape to the edge of the forest")
                                inputCheck = False

                    else:
                        encounterRoll = random.randint(0 + pLevel, 10 + pLevel)
                        ##scaling enemy spawns, weaker enemies less likely to be encountered when higher level
                        if encounterRoll <= 3:
                            encGoblin()
                            if playerWin != True:
                                forestloop = False
                        elif encounterRoll <= 6:
                            encBear()
                            if playerWin != True:
                                forestloop = False
                        elif encounterRoll <= 15:
                            encTroll()
                            if playerWin != True:
                                forestloop = False
                        else:
                            encOgreRandom()
                            if playerWin != True:
                                forestloop = False
                elif pinput in ["3", "return"]:
                    print("You've decided to leave the forest and return to town.\n")
                    forestloop = False
                else:
                    print("Invalid input")


##town related functions:
def townHelm(): #Helmetshop interactions
    #framework for other forms of armour, but tedious to code at the moment
    global gold
    global armourDict
    global armourList
    global helmDict
    global pHealth
    global pHealthMax

    print("\"Welcome to my helmet shop,", usrName, "\"")
    print("\"This is our current offer of helmets, prices are in gold of course\"")
    for k in (helmDict.keys()): #prints a list of prices/inventory
        print(k,helmDict[k])
    pEconomy()
    inputcheck2 = True
    while inputcheck2 == True:
        pinput2 = input("What will you pick?\n(1). Leather\n(2). Bronze\n(3). Iron\n(4). Leave the shop\n").lower()
        if pinput2 in ["1", "leather"]:
            if gold < 20:
                print("You can't afford that at the moment")
            else:
                print("You've successfully purchased a leather helm for 20 gold.")
                gold -= 20
                pEconomy()
                
                #changes health value gained from armour
                healthAdded = 20 - armourDict["Helm"]
                pHealthMax += healthAdded
                pHealth += healthAdded
                print("You've increased your maximum health")
                #replacing all parts in respective lists and dictionaries
                armourList[0] = "Leather Helm"
                armourDict["Helm"] = 20
                del helmDict["Leather Helm"]
                inputcheck2 = False
        elif pinput2 in ["2", "bronze"]:
            if gold < 40:
                print("You can't afford that at the moment")
            else:
                print("You've successfully purchased a bronze helm for 40 gold.")
                gold -= 40
                pEconomy()
                
                # changes health value gained from armour
                healthAdded = 30 - armourDict["Helm"]
                pHealthMax += healthAdded
                pHealth += healthAdded
                print("You've increased your maximum health")
                # replacing all parts in respective lists and dictionaries
                armourList[0] = "Bronze Helm"
                armourDict["Helm"] = 30
                del helmDict["Bronze Helm"]
                inputcheck2 = False  # returns to town
        elif pinput2 in ["3", "iron"]:
            #when purchasing an iron helm
            if gold < 100:
                #gold check
                print("You can't afford that at the moment")
            else:
                print("You've successfully purchased an iron helm for 100 gold.")
                gold -= 100
                pEconomy()
                
                # changes health value gained from armour
                healthAdded = 60 - armourDict["Helm"]
                pHealthMax += healthAdded
                pHealth += healthAdded
                print("You've increased your maximum health")

                # replacing all parts in respective lists and dictionaries
                armourList[0] = "Iron Helm"
                armourDict["Helm"] = 60
                del helmDict["Iron Helm"]
                inputcheck2 = False  # returns to town
        elif pinput2 in ["4", "leave"]:
            inputcheck2 = False
        else:
            print("Invalid input")




def townSword(): #Swordshop interactions
    global gold
    global weaponDict
    global weaponList
    global swordDict


    print("\"Welcome to my sword shop", usrName, "\"")
    print("\"This is our current offer of swords, prices are in gold of course\"")
    for k in (swordDict.keys()): #prints a list of prices/inventory
        print(k,swordDict[k])
    pEconomy()
    inputcheck2 = True
    while inputcheck2 == True:
        pinput2 = input("What will you pick?\n(1). Iron\n(2). Steel\n(3). Mithril\n(4). Leave the shop\n").lower()
        if pinput2 in ["1", "iron"]:
            if gold < 50:
                print("You can't afford that at the moment")
            else:
                print("You've successfully purchased an Iron sword for 50 gold.")
                gold -= 50
                pEconomy()
                #replacing all parts in respective lists and dictionaries
                weaponList[1] = "Iron Sword"
                weaponDict["Sword"] = 2
                del swordDict["Iron Sword"]
                inputcheck2 = False
        elif pinput2 in ["2", "steel"]:
            if gold < 100:
                print("You can't afford that at the moment")
            else:
                print("You've successfully purchased a Steel sword for 100 gold.")
                gold -= 100
                pEconomy()
                # replacing all parts in respective lists and dictionaries
                weaponList[1] = "Steel Sword"
                weaponDict["Sword"] = 3
                del swordDict["Steel Sword"]
                inputcheck2 = False  # returns to town
        elif pinput2 in ["3", "mithril"]:
            #when purchasing an Mithril sword
            if gold < 200:
                #gold check
                print("You can't afford that at the moment")
            else:
                print("You've successfully purchased a Mithril sword for 200 gold.")
                gold -= 200
                pEconomy()
                # replacing all parts in respective lists and dictionaries
                weaponList[1] = "Mithril Sword"
                weaponDict["Sword"] = 4
                del swordDict["Mithril Sword"]
                inputcheck2 = False  # returns to town
        elif pinput2 in ["4", "leave"]:
            inputcheck2 = False
        else:
            print("Invalid input")


def townDagger(): #Daggershop interactions
    global gold
    global weaponDict
    global weaponList
    global daggerDict

    print("\"Welcome to my dagger shop", usrName, "\"")
    print("\"This is our current offer of daggers, prices are in gold of course\"")
    for k in (daggerDict.keys()): #prints a list of prices/inventory
        print(k,daggerDict[k])
    pEconomy()
    inputcheck2 = True
    while inputcheck2 == True:
        pinput2 = input("What will you pick?\n(1). Iron\n(2). Steel\n(3). Mithril\n(4). Leave the shop\n").lower()
        if pinput2 in ["1", "iron"]:
            if gold < 50:
                print("You can't afford that at the moment")
            else:
                print("You've successfully purchased an Iron dagger for 50 gold.")
                gold -= 50
                pEconomy()  #shows updated gold
                
                #replacing all parts in respective lists and dictionaries
                weaponList[2] = "Iron Daggers"
                weaponDict["Dagger"] = 2
                del daggerDict["Iron Daggers"]
                inputcheck2 = False
        elif pinput2 in ["2", "steel"]:
            if gold < 100:
                print("You can't afford that at the moment")
            else:
                print("You've successfully purchased a Steel dagger for 100 gold.")
                gold -= 100
                pEconomy()  #shows updated gold
                
                # replacing all parts in respective lists and dictionaries
                weaponList[2] = "Steel Daggers"
                weaponDict["Dagger"] = 3
                del daggerDict["Steel Daggers"]
                inputcheck2 = False  # returns to town
        elif pinput2 in ["3", "mithril"]:
            #when purchasing an Mithril dagger
            if gold < 200:
                #gold check
                print("You can't afford that at the moment")
            else:
                print("You've successfully purchased a Mithril dagger for 200 gold.")
                gold -= 200
                pEconomy()  #shows updated gold
                
                # replacing all parts in respective lists and dictionaries
                weaponList[2] = "Mithril Daggers"
                weaponDict["Dagger"] = 4
                del daggerDict["Mithril Daggers"]
                inputcheck2 = False  # returns to town
        elif pinput2 in ["4", "leave"]:
            inputcheck2 = False
        else:
            print("Invalid input")


def townStaff():  # Daggershop interactions
    global gold
    global weaponDict
    global weaponList
    global staffDict

    print("\"Welcome to my staff shop", usrName, "\"")
    print("\"This is our current offer of staffs, prices are in gold of course\"")
    for k in (staffDict.keys()):  # prints a list of prices/inventory
        print(k, staffDict[k])
    pEconomy()
    inputcheck2 = True
    while inputcheck2 == True:
        pinput2 = input("What will you pick?\n(1). Pine\n(2). Oak\n(3). Willow\n(4). Leave the shop\n").lower()
        if pinput2 in ["1", "pine"]:
            if gold < 50:
                print("You can't afford that at the moment")
            else:
                print("You've successfully purchased an Pine staff for 50 gold.")
                gold -= 50
                pEconomy()  # shows updated gold

                # replacing all parts in respective lists and dictionaries
                weaponList[2] = "Pine Staff"
                weaponDict["Staff"] = 2
                del staffDict["Pine Staff"]
                inputcheck2 = False
        elif pinput2 in ["2", "oak"]:
            if gold < 100:
                print("You can't afford that at the moment")
            else:
                print("You've successfully purchased a Oak staff for 100 gold.")
                gold -= 100
                pEconomy()  # shows updated gold

                # replacing all parts in respective lists and dictionaries
                weaponList[2] = "Oak Staff"
                weaponDict["Staff"] = 3
                del staffDict["Oak Staff"]
                inputcheck2 = False  # returns to town
        elif pinput2 in ["3", "willow"]:
            # when purchasing an Willow staff
            if gold < 200:
                # gold check
                print("You can't afford that at the moment")
            else:
                print("You've successfully purchased a Willow staff for 200 gold.")
                gold -= 200
                pEconomy()  # shows updated gold

                # replacing all parts in respective lists and dictionaries
                weaponList[2] = "Willow Staff"
                weaponDict["Staff"] = 4
                del staffDict["Willow Staff"]
                inputcheck2 = False  # returns to town
        elif pinput2 in ["4", "leave"]:
            inputcheck2 = False
        else:
            print("Invalid input")

def townInn():
    global gold
    global pHealth
    global pMana

    print("Welcome to the Inn,", usrName, "would you like to stay the night? It will cost you 10 gold.\nI promise you will feel refreshed!")
    pEconomy() #shows current gold

    inputcheck = True
    while inputcheck == True:
        pinput = input("Would you like to stay the night?\n(1). Yes\n(2). No\n").lower()
        if pinput in ["1", "yes"]:
            if gold < 10:
                print("Not enough money, you'll have to sleep in the stables")
                inputcheck = False
            else:
                print("You rest at the Inn overnight. When you wake up your mana and health have refilled")
                gold -= 10                              #10 gold cost for staying the night
                pHealth = pHealthMax                    #refresh all health and mana values
                pMana = pManaMax
                inputcheck = False
        elif pinput in ["2", "no", "leave"]:
            inputcheck = False
        else:
            print("Invalid input")


##player setup questions

print("\nThis game is an adventure game where you will explore, fight monsters and gain experience.\nPlease answer a few questions about your character:")
nameCheck = True
while nameCheck == True:
    usrName = input("What would you like to call yourself?\n")
    if usrName.isdigit():                               #checking for invalid input in form of integer before testing len(usrName)
        print("Please enter a name, not a number")
    elif len(usrName) > 20:
        print("Please enter a shorter name")
    elif len(usrName) <3:
        print("Please enter a longer name")
    else:                                               #confirmation
        print("Your name is: " + usrName)
        nameCheck2 = True
        while nameCheck2 == True:
            nameConfirm = input("Confirm [Y/N}\n").lower()
            if nameConfirm in ["y", "yes"]:
                nameCheck = False
                nameCheck2 = False
            elif nameConfirm in ["n", "no"]:
                nameCheck2 = False
            else:
                print("Please enter a valid input")     #error handling


### Game loop ###
print("You are in the town of Grant, which borders the wild forests of Ming")
print("Recently, an ogre king has settled in the forest and attract various evil monsters")
print("Gather experience and gold to help prepare yourself before you liberate the town from the threat they face")
while gameOver == False:
    if forestClear == 1:
        gameOverCheck = True
        while gameOverCheck == True: #Active after killing the boss
            pinput = input("You've cleared the forest of evils, would you like to end the game? (Y)/(N)")
            if pinput in ["y", "yes", "end"]:
                quit()
            elif pinput in ["n", "no", "play"]:
                gameOverCheck = False
            else:
                print("Invalid input")
    #player status update
    print("You're in the town centre of \'Grant\', a busy place that has small dedicated shops")
    pStatus()
    pEconomy()

    #Actions while in town center
    townInputCheck = True
    while townInputCheck == True:
        playerInput = input("What would you like to do?\n\n(1). Venture to the forest\n(2). Go to the Inn\n(3). Visit the helmet shop\n(4). Visit the sword shop\n(5). Visit the dagger shop\n(6). Visit the staff shop\n").lower()
        if playerInput in ["1", "forest"]:
            forestExp() #runs the massive forest function (lines 1013 to 1266)
            townInputCheck = False
        elif playerInput in ["2", "inn"]:
            townInn() #inn function (line 1532)
            townInputCheck = False
        elif playerInput in ["3", "helm", "helmet"]:
            townHelm() #helmshop (line 1270)
            townInputCheck = False
        elif playerInput in ["4", "sword"]:
            townSword() #Sword shop (line 1352)
            townInputCheck = False
        elif playerInput in ["5", "dagger"]:
            townDagger() #Dagger shop (line 1411)
            townInputCheck = False
        elif playerInput in ["6", "staff"]:
            townStaff() #Staff shop (line 1472)
            townInputCheck = False
        else:
            print("invalid input") #errorhandling
