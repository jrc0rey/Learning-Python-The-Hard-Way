#More Files

from sys import argv
from os.path import exists

script, from_file, to_file = argv

in_file = open(from_file); indata = in_file.read()

print "The input file is %d bytes long" % len(indata)
print " Does the output file exist? %s" % exists(to_file)
print "Ready? Hit enter to continue..."; raw_input()

out_file = open(to_file, 'w'); out_file.write(indata); print "All done!!!!"

out_file.close(); in_file.close()
