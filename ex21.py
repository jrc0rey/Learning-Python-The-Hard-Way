#Functions can return something

def add(a,b):
    print ("Adding %s + %s" % (a,b))
    return a + b

def subtract(a,b):
    print ("Subtracting %s - %s" % (a,b))
    return a - b

def multiply(a,b):
    print ("Multiplying %s * %s" % (a,b))
    return a * b

def divide(a,b):
    print ("Dividing %s / %s" % (a,b))
    return a / b

print ("Let's do some math with functions!")

age = add(30,5)
height = subtract(78,4)
weight = multiply(12,13)
iq = divide(200,2)

print ("My age is %s, and my height is %s. I weigh %s lbs, and have an IQ of %s!!!" % (age,height,weight,iq))
