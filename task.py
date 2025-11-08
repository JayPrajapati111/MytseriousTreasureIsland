print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
choice_1 = input('You are at a crossroad in forest,Where do you want to go? Type "left"  or "right"').lower()
if choice_1 == "left":
    choice_2 =input('You\'ve came to a lake,'
                    'There is an  Mysterious island in the middle of the lake.'
                    'Type "Wait" to wait for a Boat or Type "Swim" to swim across.').lower()
    if choice_2 == "wait":
        choice_3 = input("You arrived at the island unharmed.This place feels mysterious. "
                         "there is a house in the island with 3 Doors, 1 red, 1 Yellow , 1 Blue "
                         "Which door do you want to choose?:").lower()
        if choice_3 == "red":
            print("You got locked inside this door,"
                  "There is no way out,"
                  "You dont know you're body starts giving up,headaches,hunger."
                  "Few Days have passed you're body is dehydrated,You Died.Game Over!")
        elif choice_3 == "yellow":
            print(" Congrats You've Found the TREASURE.Hurray!,You WIN!!!")
        elif choice_3 == "blue":
            print("The door got locked.There is an mysterious gas coming inside the room,You can't breathe,"
                  "The gas is poisonous to inhale,You Died,Game Over")
        else:
            print("You choose the door that don't exist,Game Over!")
    else:
        print("You got attacked by pack of piranhas.Game Over!.")
else:
    print("You got killed by the packs of wolf.Game Over!")
