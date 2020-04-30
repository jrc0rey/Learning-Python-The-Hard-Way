#Parameters, Unpacking, Variables

from sys import argv

script, first, second, third, fourth = argv

print "The Script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
q = raw_input("what's your " + fourth + "? ")
print(q)
