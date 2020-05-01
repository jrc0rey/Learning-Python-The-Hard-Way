from os.path import exists


header = "Jason Corey \n317 6th Ave. Apt. B \nVenice, CA 90291"

def pdf_generator(filename):
    target = open(filename, 'w')
    target.write(header)
    target.close()

create_question = raw_input("Would you like to create a new file? ")

if create_question == "yes":
    filename = raw_input("What's the name of the your file: ") + ".txt"
    while exists(filename):
        filename = raw_input("Please choose a new filename: ") + ".txt"
    pdf_generator(filename)
    print "It worked bitch!!!!!!" 
else:
    print "goodbye"
    exit()
