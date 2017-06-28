#dictionaries

# choice = raw_input("which re")
# for n in range(len(resturant_name))

# resturants = {
#     'farm Burger': 3,
#     'Ru San\'s': 1,
#     'Chipotle': 2
# }

# # keys must be hashable
# #no lists, no dictionaries

# resturants['farm Burger']
# #prints 3

# resturants['farm Burger'] = resturants['farm Burger'] + 1
# # assigns 4

# resturants.get('mcDs', 0)

# empty_dictionary = {}
# empty_dictionary['chris'] = 1234532
# #prints ['chris' : 1234532]

# resturants.keys()
# resturants.values()

# for key in resturants.keys():
#    ...:     print resturants[key]

# resturants.items()

# resturants.items()[0][1]
# #outputs 4 since farm burger is assigned to 4 

# #del command ex del dicname[name of segment to be deleted]
# # soreted command
# # pass keybord - pass replace for indentation 

phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

#Print Elizabeth's phone number.
print phonebook_dict['Elizabeth']
# Add a entry to the dictionary: Kareem's number is 938-489-1234.
phonebook_dict['Kareem'] = '938-489-1234'
# Delete Alice's phone entry.
phonebook_dict["Alice"] = ""
# Change Bob's phone number to '968-345-2345'.
phonebook_dict['Bob'] = '968-345-2345'

# Print all the phone entries.
print phonebook_dict.keys()
#       this prints out all the names which are the keys
print phonebook_dict.values()
#       this prints out all the phone numbers which are the values assigned to keys

