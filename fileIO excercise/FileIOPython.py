#FileIO excercise
import pickle
def prompt_user():
    user_response = raw_input("Type in a file name: ")
    return user_response

def open_user_file(file_name):
    file_open = open(file_name)
    return file_open

def read_user_file(opened):
    file_user = opened.read()
    return file_user

def close_user_file(fileName):
    fileName.close()
    return


# def open_file_writemode(fileName):
#     open_in_write = open(fileName, 'w')
#     return

def write_to_file(fileName):
    user_file = open(fileName, 'a')
    user_file.write(raw_input("type some shit in "))
    user_file.close()


def print_user_file():
    user_response = prompt_user()
    open_file = open_user_file(user_response)
    read_file = read_user_file(open_file)
    print read_file
    close_user_file(open_file)
    
def write_to_file_function():
    user_response = prompt_user()
    write_to_file(user_response)
    
def letter_hist_function():
    name_of_file = prompt_user()
    open_file = open_user_file(name_of_file)
    read_file = read_user_file(open_file)
    letter_summary(read_file)
    # open_file.close()
    words_summary(read_file)
    open_file.close()
def words_summary(content):
    Testwords = content
    words_array = []
    words_seperated = ""
    words_dict = {}

    for stuff in Testwords:
        if stuff != " ":
            words_seperated += stuff
        else:
             words_array.append(words_seperated)  
             words_seperated = "" 

    for xstuff in words_array:
        if xstuff in words_dict:
            words_dict[xstuff] +=1
        else:
            words_dict[xstuff] = 1
    
    print "Here is a word histogram of the content in your file \n", words_dict
    # print words_dict.values()
    
def letter_summary(content):
    word = content
    letter_count = {}
    for stuff in word:
        for letter in stuff:
            if letter in letter_count:
                letter_count[letter] +=1
            else:
                letter_count[letter] = 1
    print "here is the letter Histogram for the content in you file \n" , letter_count , "\n"



letter_hist_function()


