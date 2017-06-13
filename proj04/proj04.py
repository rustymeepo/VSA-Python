# Name:
# Date:

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""

str1 = []
print 'type in a word or phrase, and i will see if it is a palindrome.'
count = 0
print
wordA = raw_input()
for letter in wordA:
    if letter != ' ':
        str1.append(letter)
    else:
        pass
word = ''.join(str1)
while word:
    word = word.lower()
    if word[0] == word[-1]:
        word = word[1: -1]
    else:
        print 'Sorry, that word or phrase is not a palindrome.'
        break
if len(word) == 0 or len(word) == 1:
    print 'That word or phrase is a palindrome!'
