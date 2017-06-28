# class Song(object):

#     def __init__(self, lyrics):
#         self.lyrics = lyrics
    
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print line

# happy_bday = Song(["Happy birthday to you",
#                    "I don't want to get sued",
#                    "So I'll stop right there"])

# bulls_on_parade = Song(["They rally around tha family",
#                         'With pockets full of shells'])

# happy_bday.sing_me_a_song()

# bulls_on_parade.sing_me_a_song()

# import random
# from urllib import urlopen
# import sys

# WORD_URL = "http://learncodethehardway.org/words.txt"
# WORDS = []

# PHRASES = {
#     "class %%%(%%%):":
#       "Make a class named %%% that is-a %%%.",
#     "class %%%(object):\n\tdef __init__(self, ***)" :
#       "class %%% has-a __init__ that takes self and *** parameters.",
#     "class %%%(object):\n\tdef ***(self, @@@)":
#       "class %%% has-a function named *** that takes self and @@@ parameters.",
#     "*** = %%%()":
#       "Set *** to an instance of class %%%.",
#     "***.***(@@@)":
#       "From *** get the *** function, and call it with parameters self, @@@.",
#     "***.*** = '***'":
#       "From *** get the *** attribute and set it to '***'."
# }

# # do they want to drill phrases first
# if len(sys.argv) == 2 and sys.argv[1] == "english":
#     PHRASE_FIRST = True
# else:
#     PHRASE_FIRST = False

# # load up the words from the website
# for word in urlopen(WORD_URL).readlines():
#     WORDS.append(word.strip())


# def convert(snippet, phrase):
#     class_names = [w.capitalize() for w in
#                    random.sample(WORDS, snippet.count("%%%"))]
#     other_names = random.sample(WORDS, snippet.count("***"))
#     results = []
#     param_names = []

#     for i in range(0, snippet.count("@@@")):
#         param_count = random.randint(1,3)
#         param_names.append(', '.join(random.sample(WORDS, param_count)))

#     for sentence in snippet, phrase:
#         result = sentence[:]

#         # fake class names
#         for word in class_names:
#             result = result.replace("%%%", word, 1)

#         # fake other names
#         for word in other_names:
#             result = result.replace("***", word, 1)

#         # fake parameter lists
#         for word in param_names:
#             result = result.replace("@@@", word, 1)

#         results.append(result)

#     return results


# # keep going until they hit CTRL-D
# try:
#     while True:
#         snippets = PHRASES.keys()
#         random.shuffle(snippets)

#         for snippet in snippets:
#             phrase = PHRASES[snippet]
#             question, answer = convert(snippet, phrase)
#             if PHRASE_FIRST:
#                 question, answer = answer, question

#             print question

#             raw_input("> ")
#             print "ANSWER:  %s\n\n" % answer
# except EOFError:
#     print "\nBye"

# class Person(object):
#     def __init__(self, name):
#         self.name = name
#     def greet(self, whom):
#         print "hello %s, i am %s " %(whom, self.name)

# jethro = Person('Jethro')
# jethro.greet('oakley')


class Person(object):
    def __init__(self, name, email, phone): #friend, greeting_count,people_greeted):
        self.name = name
        self.email = email
        self.phone = phone
        self.friend = []
        self.greeting_count = 0
        self.people_greeted = []

    
    def __repr__(self):
        return 'name: %s \n emial: %s \n phone: %s' % (self.name, self.email, self.phone)

    def greet(self, other_person):
        print "Hello %s, I am %s!" % (other_person.name, self.name)
        self.greeting_count = self.greeting_count + 1
        self.people_greeted.append(other_person.name)
        print "You have greeted %s %s times" % (other_person.name, self.greeting_count)
    
    def contact_info(self):
        print "%s\'s contact info: \n email: %s \n phone: %s" % (self.name, self.email, self.phone)

    def add_friend(self, other_person):
        self.friend.append(other_person.name)
    
    def num_friends(self):
        print "%s has %s friend(s)" % (self.name, len(self.friend))
    
    def num_unique_people_greeted(self):
        print "Unique number of people greeted" ,len(set(self.people_greeted))

        

        
        
        

sonny = Person('Sonny', 'sonny@hotmail.com','483-485-4948') #[],0)
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456') #, [],0)
sonny.greet(jordan)
jordan.greet(sonny)
sonny.contact_info()
jordan.contact_info()
# sonny.friends.append(jordan)
# jordan.friends.append(sonny)
sonny.add_friend(jordan)
sonny.num_friends()
jordan.num_friends()
jordan.add_friend(sonny)
jordan.num_friends()
sonny.greeting_count
print sonny
sonny.num_unique_people_greeted()
sonny.greet(jordan)
sonny.num_unique_people_greeted()
print sonny.name



# class Vehical(object):
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def print_info(self):
#         print " %s %s %s" %(self.year, self.make, self.model)
    
# my_car = Vehical("Mercedes-Benz", 'C63 AMG S', '2017')
# print "My car is made by %s" % my_car.make
# print "The model is called %s" % my_car.model
# print "It is a %s model" % my_car.year
# my_car.print_info()