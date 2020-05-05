# Making Decisions

print ("You enter a dark room with 2 doors. Do you want to go through door 1 or 2?")

door = input("> ")

if door == "1":
    print ("There's a giant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear!")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good Job!")
    elif bear == "2":
        print("The bear eats your legs off. Good Job!")
    else:
        print ("Well, doing %s is probably better. Bear runs away" % bear)

elif door == "2":
    print("You stare into the abyss of a new universe.")
    print("1. Walk into the unkown...")
    print("2. Go through door one.")
    print("3. Say 'Fuck it' and jump with your eyes closed.")

    abyss = input("> ")

    if abyss == "1" or abyss == 3"3":
        print("You've been sucked into a black hole for which there is no escape :( ")
    elif abyss == "2":
        print("The bear has finished his cake and decides to munch on you. You gone!")
    else:
        print("No Choice is automatic death!!!. Goodbye")

else:
    print("You don't understand choice. Automatic evaportation. You're dead fucker!")
