import os

#phoneBook part 2

import pickle
# # open the file in write mode (w)
# myfile = open('phoneBook.pickle', 'w')
# # dump the contents of the phonebook_dict into myfile - the open file
# pickle.dump(main_dict, myfile)
# # close myfile
# myfile.close()

dictionary = {
    'Adrian': '123', 
    'Hamza':'1234'
    }


def main_dictionaryf():
    dictionary.update() 
    return dictionary

# ===================================
def lookup_entry_dictionary(person):
    if person in main_dictionaryf():
        lookup = dictionary[person]
        return lookup
    else:
        print "name not found"    
def main_menu():
    print """    =====================
    Electronic Phone Book
    =====================
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Save entries
    6. Load Saved Entries
    7. Quit
    Please select an item: (1-6)""" 
    answer = user_response_main_menu()
    if answer == 1:
        lookup()
    if answer == 2:
        set_up_entry()
    if answer == 3:
        del_entry()
    if answer == 4:
        os.system('clear')
        print main_dictionaryf()
        # for key, value in sorted(maindict.items()):
        #     print key, value
    if answer == 5:
        save_entries()
    if answer ==6:
        Load_saved_entries() 
    if answer == 7:
        os.system('clear')
        print "Thanks for using Hamza's phonebook"
        return answer
    if answer == 8:
        pass


def save_entries():
    main_dictionary = main_dictionaryf()
    # open the file in write mode (w)
    myfile = open('phonebook.pickle', 'w')
    # dump the contents of the phonebook_dict into myfile - the open file
    pickle.dump(main_dictionary, myfile)
    # close myfile
    print main_dictionaryf()
    myfile.close()

def Load_saved_entries():
    # open the file in read mode (r)
    myfile = open('phonebook.pickle', 'r')
    # load the contents from the file and store it in the phonebook_dict variable
    main_dictionary = pickle.load(myfile)
    print main_dictionary
    dictionary.update(main_dictionary)
    myfile.close()

def user_response_main_menu():
    response = int(raw_input(" "))
    return response

def lookup():
    os.system('clear')
    entry = raw_input('What is the name? ')
    print "The contact information :" ,lookup_entry_dictionary(entry)


def set_up_entry():
    os.system('clear')
    name_of_entry = raw_input("Type in name: ")
    num_of_entry = raw_input("Type number: ")
    dictionary[name_of_entry] = num_of_entry
    dictionary.update()
    print dictionary
    # return main_dictionaryf(all)

def del_entry():
    os.system('clear')
    name_del_entry = raw_input("Type in name: ")
    if name_del_entry in dictionary:
        del dictionary[name_del_entry]
        dictionary.update()
    else:
        print "   **** Name not found **** \n    Returning to main menu"
    


# ===================================
def main():
  

    main_run = True
    while main_run is True:
        answer = main_menu()
        if answer == 7:
            main_run = False




main()
