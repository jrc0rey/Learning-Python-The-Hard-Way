#While Loops(use sparingly)

# i = 0
# numbers = []
#
# while i < 6:
#     print ("At the top i is %d" % i)
#     i += 1
#     numbers.append(i)
#     print("Numbers now:", numbers)
#     print("At the bottom i is %d" % i)
#
# print("The Numbers:")
# for i in numbers:
#     print(i)


widgets = 0

def widget_counter(number):
    while number < 50:
        number += 1
        print("Adding number %d" % number)
    widgets = number
    print(widgets)

widget_counter(widgets)
