


choiceList = ["Chipotle", "Farm Burger" ,"RuSan's", "Exit"]


# def counterTrack(count):
#     if count >= 5:
#         print "Limit reached fatty"


def userChoice():
    user_choice = int(raw_input("Pick a resturant - 1: Chipotle 2: Farm Burger 3: RuSan's 0: Exit " ))
    return user_choice

def List_of_resturant(user_number):
    if user_number == 1:
        rchoice = "Chipotle"
        return rchoice
    elif user_number == 2:
        rchoice = "Farm Burger"
        return rchoice
    elif user_number == 3:
        rchoice = "RuSan's"
        return rchoice
    elif user_number == 0:
         rchoice = "exit"
         return rchoice
    else:
        rchoice = "INVALID SELECTION"
        return rchoice 

def printOutput(user_number):
    choice = List_of_resturant(user_number)
    return choice
    # print "you selected %s" % choice
    # listNumber = user_number - 1
    # print choiceList[listNumber]
        
# def quit_tracker():
#     user_choice_exit = userChoice()
#     if user_choice_exit == 0:
#         exit_test = False
#         return exit_test
#     else:
#         exit_test = True
#         return exit_test
             

def lunch_tracker():
    choice_num = userChoice()
    count = 0
    while count <= 5:
        print "you selected %s" % printOutput(choice_num)
        count += 1
        print "you've had enough fatty!"
        exit_no = False
        

        

lunch_tracker()


