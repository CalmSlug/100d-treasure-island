print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You start your adventure standing at the crossroads.")
print("Do you go RIGHT or LEFT?")
crossroads = input().lower()

if crossroads == "left":
    print("After some thinking you decide to go left.")
    print("The road leads you to a lake and a small island in it.")
    print("Do you SWIM to the island or WAIT for a boat?")
    lake = input().lower()
    
    if lake == "wait":
        print("You decide to wait.")
        print("An empty boat docks nearby. Is this your ride?")
        print("Cautiosly you board the boat and swim to the island.")
        print("Once you arrive to the island you see a weird hut.")
        print("The hut has 3 doors of different colors.")
        print("Which door do you open: RED, BLUE or YELLOW?")
        hut = input().lower()
        
        if hut == "yellow":
            print("You pick the yellow door.")
            print("It effortlessly opens and you find a treasure chest.")
            print("The chest is filled with coins and baubles.")
            print("Congratulations! You Win")
        
        elif hut == "red":
            print("You pick the red door.")
            print("It blows up in your face and tears you into shreds.")
            print("Game Over")
        
        elif hut == "blue":
            print("You pick the blue door.")
            print("It is so cold to the touch that it turns you into ice.")
            print("Game Over")
        
        else:
            print("Unable to decide you try to step away from the hut.")
            print("The sky darkens and you are struck by a lightning bolt.")
            print("Game Over")
    
    else:
        print("You decide to swim.")
        print("That was silly of you because you don't know how to do that.")
        print("Within minutes you drown in the cold depths of the lake.")
        print("Game Over")

else:
    print("After some thinking you decide to go right.")
    print("Oops! That road goes way too close to some ancient ruins.")
    print("A pack of gargoyles swoops in and kills you.")
    print("Game Over")
