from sys import argv

script = argv

name = raw_input("What's the file you would like to create?")

target = open(name, 'a')

input = raw_input("What would you like to say? ")

target.write(input)
