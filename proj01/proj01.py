# Name:
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!

# this will work, no problems here.
user_input = raw_input("Enter in your name. " )
print 'Hello there,'
print user_input
print 'Could you tell me your age'
user_input = raw_input('please? ')
print user_input
yearX = 2017 + 100
yearY = int(yearX) - int(user_input)
bday = raw_input("Have you had a birthday yet? ")
if bday == 'yes':
    print 'OK! ' + 'You will be 100 in the year ' + str(yearY)
    else:
        newYY = yearY - 1
        print 'well then, happy belated birthday! you will be 100 in the year' + str(newYY)
