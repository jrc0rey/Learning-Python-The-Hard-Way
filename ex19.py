#Functions & Variables

print "\n"

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %s cheeses!" % cheese_count
    print "You have %s boxes of crackers!" % boxes_of_crackers
    print "Man, that's enough for a party!!"
    print "Get a blanket. \n"

print "We can just give the function numbers directly: "

cheese_and_crackers(20,300)

print "Or we can just use variables from our script:"
cheese = 200
crackers = 300

cheese_and_crackers(cheese, crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 6, 15*5)

print "And we can combine the two, variables & math:"
cheese_and_crackers(cheese + 500, crackers +900)

print "Let's use some user input to get our arguments:"
user_cheese = int(raw_input("How many cheeses do you have? "))
user_crackers = int(raw_input("How many boxes of crackers do you have? "))
print "\n"
cheese_and_crackers(user_cheese, user_crackers)
