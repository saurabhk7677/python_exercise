mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])
print()

#######################################################################

# this goes in mystuff.py
def apple():
    print("I AM APPLES!")
print()

#######################################################################

def apple():
    print("I AM APPLES!")

# this is just a variable
tangerine = "Living reflection of a dream"
print()

####################################################################

mystuff['apple'] # get apple from dict
mystuff.apple() # get apple from module
mystuff.tangerine # same thing, it's just a variable
print()

######################################################################

class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")
print()

#######################################################################

# dict style
mystuff['apples']

# module style
mystuff.apples()
print(mystuff.tangerine)

# class style
thing = MyStuff()
thing.apples()
print(thing.tangerine)
print()

############################################################################

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha fa,ily",
                        "with pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

#############################################################################

