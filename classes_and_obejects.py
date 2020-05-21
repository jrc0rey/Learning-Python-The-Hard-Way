#Work & practice with classes and objects

class Robot(object):
    def __init__(self, name, color, height):
        self.name = name
        self.color = color
        self.height = height
    def introduction(self):
        print("Hello, my name is %s and I'm a %s robot. I'm %s ft. tall!!!" % (self.name, self.color.lower(), self.height))

r1 = Robot('Jason', 'Red', '10')
r2 = Robot('Chad', 'Purple', '15')

r1.introduction()
r2.introduction()

class Person:
    def __init__(self, name, personality, isSitting):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting
    def sit_down(self):
        self.isSitting = True
    def stand_up(self):
        self.isSitting = False

p1 = Person('Alice', 'Aggresive', False)
p2 = Person('Becky', 'Talkative', True)

p1.robotOwned = r1
p2.robotOwned = r2

p2.stand_up()
