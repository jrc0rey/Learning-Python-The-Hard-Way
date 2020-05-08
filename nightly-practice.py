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


class Friend:
    def __init__(self, first_name, birthday):
        self.name = first_name
        self.birthday = birthday #mmddyyyy

friend = Friend("Chris", "01/10/1984")

print(friend.name, friend.birthday)
