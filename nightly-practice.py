# class User:
#     pass
#
# user1 = User()
# user1.firt_name = "Brad"
# user1.last_name = "Pitt"
#
# user2 = User()
# user2.firt_name = "Bob"
# user2.last_name = "Clarke"


class Robot(object):
    def __init__(self, name, color, personality):
        self.name = name
        self.color = color
        self.personality = personality
    def greeting(self):
        print('Hello, my name is ' + self.name + ' and I\'m ' + self.color + ' with an ' + self.personality + ' personality!')


r1 = Robot('Jason', 'Black', 'Aggresive')
r2 = Robot('Fred', 'Red', 'Easy-Going')

r1.greeting()
r2.greeting()
