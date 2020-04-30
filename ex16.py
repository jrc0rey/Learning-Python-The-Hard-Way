#Reading & Writing Files

from sys import argv

script, filename = argv

print " We are gonna erase %s." % filename
print "If you don't want that hit CTRL-C."
print "If you do want that, hit RETURN."

raw_input("?")

answer = raw_input("Are you sure you want to erase %s?: " % filename)
if answer == "yes":
    target = open(filename, 'w')
    target.truncate()
    print "Erased"
else:
    print "Close Call"
    exit()

print " Now I'm gonna ask you for 3 lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to %s." % filename

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And now we shall close %s" % filename
target.close()
