#Names, Variables, Code, Functions

def print_two(*args):
    arg1,arg2 = args
    print "arg1: %s, arg2: %s" % (arg1, arg2)

def print_two_again(arg1,arg2):
    print "arg1: %s, arg2: %s" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %s" % (arg1)

def print_none():
    print "I got nothing!!!!"

print_two("Zedd", "Bobby")
print_two_again("Mike", "Tommy")
print_one("Jason")
print_none()