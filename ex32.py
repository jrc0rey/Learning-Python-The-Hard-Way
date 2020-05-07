#Loops & Lists

from bcrypt import *

the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this kind of for loop goes through a List

for i in the_count:
    print('This is count %d' % i)

for i in fruits:
    print('This type of fruit: %s' % i)

for i in change:
    print('I got %r' % i)

#We can also build Lists

empty_list = []

for i in range(1,6):
    print('Adding %d to the list' % i)
    empty_list.append(i)

for i in empty_list:
    print('This is number %d in my list' % i)

#The list() function that creates lists in a simplified manor

new_list = list(range(16))
print(new_list)
