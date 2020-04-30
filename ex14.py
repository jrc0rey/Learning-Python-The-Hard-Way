#Prompting & Passing
from sys import argv

script, user_name = argv
prompt = "> "

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % (user_name)
likes = raw_input(prompt)

print "Where do you live %s?" % (user_name)
location = raw_input(prompt)

print "What kind of comp do you have?"
computer = raw_input(prompt)

print "Now %s, are you gay or straight?" % (user_name)
sexuality = raw_input(prompt)

print  """Alright, so you said %s about liking me.
You live in %s. Not sure where that is.
And you have a %s computer. Nice! And you are super %s""" % (likes.title(), location.upper(), computer.title(), sexuality.upper())
