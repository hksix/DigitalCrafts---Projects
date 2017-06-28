# You've learned to work with strings, which can be
# created with quotes. (What kinds of quotes?)

# When working with numbers, here are 2 kinds

5 # a whole number, otherwise known as an integer
5.0 # a number with a decimal place, a.k.a. a "float" or floating-point number

# math with numbers:

15 + 50 # addition
27 - 3 # subtraction
8 * 9 # multiplication
4 / 2 # division

# with division, python will automatically round for you:

8 / 3 # this prints the number 2

# to get the precise anser, at least one of the numbers should be floats

8.0 / 3 # prints 2.6666666666666665

# you get the same result from:
8 / 3.0
8.0 / 3.0

# You can substitue a number into a string, too.
# But, instead of %s, you use the placeholders
# %d for an integer
# or %f for a float
howmany = 12
print "It's the ship that made the Kessel Run in less than %d parsecs" % howmany

number_of_gigawatts = 1.21
print " Marty, I'm sorry, but the only power source capable of generating %f gigawatts of electricity is a bolt of lightning." % number_of_gigawatts

# To control how many decimal places, you would do something like this:
number_of_gigawatts = 1.2128234723424329243
print "I said %.2f gigawatts" % number_of_gigawatts

# And, of course, if you need to supply more than one placeholder value,
# you need parentheses and commas

problems = 99
not_problems = 1
print "I got %d problems but ipython ain't %s" % (problems, not_problems)

# converting a string to a number
int("5") # this gives you back the number 5

# why do you want to do this?
# question: what does this do?
cats = raw_input("How many cats do you have?")
# user enters the number 2

# then you try to add 1...
# In [2]: cats + 1
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-5-d11af168c6c4> in <module>()
# ----> 1 cats + 1

# TypeError: cannot concatenate 'str' and 'int' objects

# Instead, you could do this:

cats = int(raw_input("How many cats do you have?"))
cats + 1 # prints 3

# how does this work?
# On the RHS (Right Hand Side of the assignment),
# python looks at the innermost parentheses and sees a string.
# It gives the string to raw_input, which presents it to the user.
# Let's say the user types the number 3 (and presses the Enter key).
# Then, raw_input gives the string "3" to int.
# Now, int does the conversion and what's left on the RHS?
# The number 3 (not the string).

# That's a lot of stuff going on.
# You might want to break that up into separate steps.
# How could you do that?
# Any time you have nested parentheses, you can always take
# the inner part and make it its own step.
# For example:
cats_string = raw_input("How many cats do you have?")
cats = int(cats_string)
cats + 1

# some other math operations:

abs(-20) # absolute value of negative 20
pow(2, 5) # 2 to the 5th power
round(5.6) # rounds up to 6

# If you want more math functionality, you'll need
# to ask python for help.
# To do that, you can ask for python's extra math code.
# (This is also known as a "module")
import math
math.floor(5.6) # 5.0
math.ceil(5.4) # 6.0
math.sqrt(20736) # 144.0
print math.pi # prints 3.14159265359

# doing "math" with strings
print "yeah " * 3 # prints yeah yeah yeah


# You can also compare numbers

# is 5 less than 10?
5 < 10 # True

# is 5 greater than 10?
5 < 10 # False

# is 4 less than or equal to 4?
4 <= 4 # True
# is 4 less than or equal to 3?
4 <= 3 # False

# is 5 greater than or equal to 4?
5 >= 4 # True
# is 5 greater than or equal to 9?
5 >= 9 # False

# You don't have to compare number literals, you
# can use identifers, too

how_many_cats = 8
too_many_cats = 21
how_many_cats < too_many_cats # True

# And now, you can use this in an if condition:

if how_many_cats < too_many_cats:
    print "Totally fine. Maybe you need another cat?"
else:
    print "Whoa. Slow down with the cats, already."


# What if you only want to know if two things
# are equal?

your_cats = 3
my_cats = 3
their_cats = 2

your_cats == my_cats # True
your_cats == their_cats # False

# These can also be used in a conditional

if your_cats == their_cats:
    print "You have the same number of cats as they do!"
elif your_cats == my_cats:
    print "You have the same number of cats as me, but not the same number as they do..."

# Those comparisions are *expressions*
# meaning that they reduce down to a single value.
# These values are called Booleans.
# The two boolean literals are: True and False
# (note the spelling, and also - there are no quotes.)

# So, what is the value of the identifier needs_more_cats?
too_many_cats = 10
my_cats = 5
needs_more_cats = my_cats < too_many_cats

# And what is the value of needs_more_cats now?
my_cats = 50
print needs_more_cats # what prints?

# Why is that?
# Remember, the RHS gets reduced down to a single
# value *before* the assignment is actually made.

# to reevaluate the comparision, you have to
# reassign the value of needs_more_cats
needs_more_cats = my_cats < too_many_cats


# But, there are other values that are
# considered False (other than just False):
False # boolean literal
0 # the integer zero
0.0 # the float zero
"" # empty string
None # The "None" value in python
[] # empty list
{} # empty dictionary
() # empty tuple

# Everything else is "truthy"

# You can also chain booleans together.
# To do this, use the following operators:
# or
# and

# They don't quite work the way you might expect.
# or will start with the value to the left
# and see if it's "truthy"
# If so, it's done. The result is that truthy value.
# otherwise, it moves on to the next value.
# If that value is truthy, that becomes the result.
# If that value is falsey, that's the result.

5 or 6 or False # 5
0 or 6 or False # 6
0 or "" or False # False

# or returns the first truthy value in the chain (moving from left to right)
# if it doesn't find one, it returns the last falsey value

# and works the opposite way:
0 and "" and True # 0
5 and "" and True # ""
5 and 6 and True  # True

# It returns the first falsey value, starting with the left-most value.
# If it doesn't find one, it returns the last truthy value.