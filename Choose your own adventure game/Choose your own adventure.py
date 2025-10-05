print("Welcome Too The Adventure!")

print("""This is an choose you own adventure game. 
That means that this is a 100% text based game, where you choose your paths you wish to take.
That can be anything from walking left or right, to choosing to kill a beast or not. 
This game have multiple endings, and it's up too you to discover them all!""")


#Add too or change this?

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

while True:
    left_or_right = input("You walk down a dark, cold and musty hallway in an abandoned castle.\nThese ancient hallways, is made of old stone brick, and haven't seen any sight of life in many years.\nYou walk down this cold hall for a while, before you see the corridor split.\nThe hall splits into to two, a hallway to the left and one to the right.\nDo you go Left, or Right?: ").lower()  # this lets people type in lowercase

    if left_or_right == "Left":
        print("You turn left, and continue down the left corridor")
    # elif left_or_right == "Left":
    else:
        print(
            "You turn right, and continue down the dark hallway.\nWhile you are walking down the corridor, your torch goes out.\nYou don't have any other torches on you, so you decide too feel along the wall for another one.\nAs you move along the wall, you forget to be careful in your desperate search for light, you suddenly loose your footing, and fall into a hole.\nYou Die.\nGAME OVER")

    swim_or_wait = input("""You walk down the left hallway.
    After a few minutes of walking, arrive at what seems to be a giant lake inside the castle. You don't know how this is possible, but as you are looking out over the water, you see a boat.
    It seems like the boat is slowly drifting towards you.
    Do you Wait, for the boat to arrive, or do you Swim to it and then row on?: """).lower()  # this lets people type in lowercase

    if swim_or_wait == "Wait":
        print("""You wait for the boat. After about 10min, the boat reaches your side of the lake. You get on and row across the lake. It takes you about 20min, but you get across safely.
        You see a new path way and walk on.""")
    else:
        print("""You choose to swim to the boat. With your heavy equipment on, the swim is difficult, but you know you will make it.
        You are halfway to the boat, before you suddenly see fish swimming around you. Out of no where, 15 angry trouts attack you.
        Hitting your body allover, swimming into the pockets of your cloths and equipment, dragging you down below.
        You fight the fish away, doing your best to keep your head above water, but soon you grow to tierd. The fighting, the swimming the armor, and other equipment is to much.
        Your body is to weak, you try so hard to keep your head above water, but it is to late, you are sinking.
        You give it your all, but its not good enough, you drown.
        GAME OVER""")

    which_door = input("""You come tot he end of the corridor, and in front of you are three doors. One Red, one Blue and one Yellow.
    What door do you go through?: """).lower()  # this lets people type in lowercase
    if which_door == "Red":
        print("""You go through the red door. 
        You walk into the hallway, everything looks fine until you suddenly feel your foot sink into the floor.
        You look down to see that you stepped on a pressure plate. 
        Before you can react, you get entirely engulfed in flames, turning you to ash.
         GAME OVER""")
    elif which_door == "Blue":
        print("""You walk through the blue door.
        You walk into the hallway, everything looks fine until you suddenly see a three sets of glowing eyes in the distance.
        Before you have time to react, three hungry dire wolfs attacks you, tearing you completely apart.
        GAME OVER""")
    elif which_door == "Yellow":
        print("""You open the yellow door.
        When you look in the door, you see a chest on a pedestal, filled to the brim with gems and gold.
        You did it! You found the treasure!
        YOU WIN
    
    
        Now, how do you get all of this home?""")
    else:
        print("""You look around, not wanting to open any of the doors. You look high and low for any other passageway, any secret door.
        Only to realize that there is nothing else at the end of this hallway. As you are standing there, looking at the doors, you suddenly hear noises behind you.
        You turn around, only too see eye to eye with a beholder. Before you have time to react, one of it's eye stocks shoots you with a black beam, turning you to dust.
        GAME OVER""")
        break

#Make a backstory, something that can give the adventure a reason for being her.
#Make a date so an inventory, make a fighting system? Melee and magic? 