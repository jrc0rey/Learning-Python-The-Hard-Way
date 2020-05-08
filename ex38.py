#Doing things to lists

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print ("Wait there's not ten things in that list, let's fix that.")

stuff = ten_things.split(' ')
more_things = ["Day", "Night", "Song", "frisbee", "CORN", "Banana", "Girl", "Boy" ]

better_thing = [ ]
for i in more_things:
    better_thing.append(i.title())
while len(stuff) != 10:
    next_one = better_thing.pop()
    print("Adding", next_one)
    stuff.append(next_one)
    print("There's %d items now!" % len(stuff))

print("There we go:", stuff)

print("Let's do some things with stuff")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
