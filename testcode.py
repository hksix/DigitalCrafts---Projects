# testlist = []
# testlist.append(raw_input("add "))
# print testlist
# testlist.append(raw_input("add "))
# print testlist
# testlist.append(raw_input("add "))
# print testlist
# testlist.append(raw_input("add "))
# print testlist


#notes 
# objects are "." things (.index .items .readlines .update)

# class Person(object):
#     def __init__(self):
#         self.name = "darth Carl"

#     def greet(self):
#         print "hello, my name is %s" % self.name

# darth_carl = Person()

# darth_carl.greet()

# class Counter(object):
#     def __init__(self):
#         self.count = 0
#     def increment(self):
#         self.count = self.count + 1
#         print self.count

# counter1 = Counter()
# counter1.increment()
# counter1.increment()
# counter1.increment()
# counter2 = Counter()
# counter2.increment()

class Contact(object):
    def __init__(self, first_name, last_name, email, phone):
        self.first = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    def show(self):
        print "%s, %s - %s, (%s)" %(self.last_name, self.first, self.email, self.phone)

me = Contact('chris', 'khan', 'emial@mail', '898989')
me.show()