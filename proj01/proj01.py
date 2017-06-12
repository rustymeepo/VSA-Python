# Name:
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!

# this will work, no problems here.
user_input = raw_input("Enter in your name. " )
print 'Hello there, ' + str(user_input)
user_input = raw_input('could you tell me your age please? ')
yearX = 2017 + 100
yearY = int(yearX) - int(user_input)
bday = raw_input("Have you had a birthday yet? ")
if bday == 'yes' or 'yeah' or 'yep':
    print 'OK! ' + 'well then, happy belated birthday! You will be 100 in the year ' + str(yearY)
elif bday == 'no' or 'nada' or 'nope':
        newYY = yearY - 1
        print 'you will be 100 in the year ' + str(newYY)

