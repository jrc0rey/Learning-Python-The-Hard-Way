#Branches and Functions

from sys import exit

def gold_room():
    print ("This room  is full of gold! How much should you take?")

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man learn to type a number!")

    if how_much < 50:
        print("Nice, you're not greedy. You win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("""There is a bear in here.
    The Bear has a bunch of money.
    The Fat Bear is in front of another door.
    How are you going to move the bear?
    """)

    bear_moved = False

    while True:
        next = input("> ")

        if next == "take honey":
            dead("The Bear looks at you then slaps yor face off!")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed and chews your legs off!")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I have no idea what that means!!!!")

def cthulu_room():
    print("""Here you see the great and evil Cthulu
    He, It, whatever stares at you and you go insane.
    Do you flee for your life or eat your head??
    """)

    next = input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulu_room()

def dead(why):
    print(why, "Good Job!")
    exit(0)

def start():
    print ("""You are in a dark room.
    There is a door to your right and left.
    Which door do you take?""")

    next = input("> ")

    if "right" in next:
        cthulu_room()
    elif "left" in next:
        bear_room()
    else:
        dead("You stumble around the room until you starve.")

start()
