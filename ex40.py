#Modules, Classes, and Objects

#Classes are Uppercase
class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy Birthday to you",
"I don't want to get sued", "So I'll stop right there"
])

bulls_on_parade = Song(["They rally round the family", "With a pocket full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

trash = ["This is my song", "And it is garbage"]

more_lyrics = Song(trash)

more_lyrics.sing_me_a_song()
