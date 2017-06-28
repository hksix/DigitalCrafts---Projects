#lunchTracker #2



def list_of_resturants():
    list_of_resturants = ['1: Chipotle', '2: FarmBurger', '3: RuSans']
    list_of_resturants.append ('0: exit')
    return list_of_resturants   


def prompt_user():
    # list_of_r = list_of_resturants()
    # list_of_r.append ('4: exit')
    prompt_user =  int(raw_input("Please select from the list:"))
    return prompt_user

def resturant_choice_input(user_input):
    list_of_r = list_of_resturants()
    # print list_of_r
    if user_input == 1:
        ruser_input = list_of_r[0]
        return ruser_input
    elif user_input == 2:
        return list_of_r[1]
    elif user_input == 3:
        return list_of_r[2]
    elif user_input == 0:
        return list_of_r[3]

def counter(user_input):
    print "youve been to this place %s times" %(user_input)

def user_interaction():
    print list_of_resturants()
    u_input = prompt_user()
    return u_input
    counter(u_input)

def printer(u_input):
    name_of_rest = resturant_choice_input(u_input)
    printer =  "you have selected %s" % name_of_rest  
    return printer
    # print " you have been to %s %s many times" % (name_of_rest, counter(u_input))

def lunch_tracker_main():
    counter = 0
    position0 = 0
    position1 = 0
    position2 = 0
    move_forward = True
    while move_forward:
        choice = user_interaction()
        print printer(choice)
        # counter += 1
        if choice == 1:
            position0 += 1
            print "you have been here: ", position0
        elif choice == 2:
            position1 += 1
            print "you have been here: ", position1
        elif choice == 3:
            position2 +=1
            print "you have been here: ", position2
        elif choice ==0:
            print "Goodbye"
            move_forward = False
        counter += 1
        if position0 >=3 or position1 >=3 or position2 >=3:
            print "you have had enough! %s more than 3 times" % printer(choice)    
        if counter >=5:
            print "You have had enough food!"
            move_forward = False
    
        




def main_menu():
    print '\033[1m' + """Welcome to the main menu: 
    > Press 1: The Lunch Tracker Application
    > Press 2: Settings menu """ + '\033[0m'
    user_input = int(raw_input("enter selection "))
    if user_input == 1:
        lunch_tracker_main()
    if user_input == 2:
        settings_menu()
    if user_input == 3:
        print ('\x1b[1;31m'+'fuck off its late'+'\x1b[0m')




def settings_menu():
    print '\033[1m'+ """ Settings Menu:
    > Press 1: Update list of resturants
    > Press 2: Back to main menu""" + '\033[0m'
    user_input = int(raw_input("enter selection "))
    if user_input == 1:
        print "You selected: Update Resturants list"
        update_resturants()
    if user_input == 2:
        print "You selected: Go back to main menu"
        main_menu()

def update_resturants():
    print '\033[1m'+ """ Update resturants:
    > Press 1: Add three resturants 
    > Press 2: Back to main menu""" + '\033[0m'
    updated_list_of_resturants()

def updated_list_of_resturants():
    list_of_resturants_user =  []
    list_of_resturants_user.append(raw_input("add First resturant: "))
    list_of_resturants_user.append(raw_input("add Second resturant: "))
    list_of_resturants_user.append(raw_input("add Thrid resturant: "))
    return list_of_resturants_user

main_menu()



