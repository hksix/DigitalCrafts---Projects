import os

main_dictionary = {
    'Adrian': '123', 
    'Hamza':'1234'
    }
    
# ===================================
def lookup_entry_dictionary(person):
    lookup = main_dictionary
    person = lookup[person]
    return person

def main_menu():
    print """    =====================
    Electronic Phone Book
    =====================
    1. Look up an entry
    2. Set an entry
    3. Delete an entry
    4. List all entries
    5. Quit
    Please select an item: (1-5)""" 
    answer = user_response_main_menu()
    if answer == 1:
        lookup()
    if answer == 2:
        set_up_entry()
    if answer == 3:
        del_entry()
    if answer == 4:
        os.system('clear')
        for key, value in sorted(main_dictionary.items()):
            print key, value
    if answer == 5:
        os.system('clear')
        print "Thanks for using Hamza's phonebook"
        return answer
    

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
    main_dictionary[name_of_entry] = num_of_entry

def del_entry():
    os.system('clear')
    name_del_entry = raw_input("Type in name: ")
    if name_del_entry in main_dictionary:
        del main_dictionary[name_del_entry]
    else:
        print "   **** Name not found **** \n    Returning to main menu"
    


# ===================================
def main():
    main_run = True
    while main_run is True:
        answer = main_menu()
        if answer == 5:
            main_run = False




main()
