# Date:

def intersection(lst1, lst2):
    return list(set(lst1).intersection(lst2))


# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def HangMan():
    # end of helper code
    # -----------------------------------

    # actually load the dictionary of words and point to it with
    # the wordlist variable so that it can be accessed from anywhere
    # in the program
    wordlist = load_words()
    derp = choose_word(wordlist)
    word = list(derp)
    ans_lst = []

    #print derp
    # your code begins here!
    print "Welcome to the game, Hangman!"
    for x in range(0, len(word)):
        ans_lst.append('_')
    guess_lst = []
    print ' '.join(ans_lst),' '
    print "I am thinking of a word that is " + str(len(word)) + " letters long."
    guess = raw_input()
    guesses = len(word) + 2
    while guesses > 1:
        guess = guess[:1]
        guess = guess.lower()
        guess_lst.append(guess)
        for number in range(len(word)):
            if word[number] == guess:
                ans_lst[number] = guess
        print 'Guessed Letters:  ' + ' '.join(guess_lst),' '
        print ' '.join(ans_lst), ' ',
        guess = guess + ' '
        comm_lst = intersection(guess, word)
        if ans_lst == list(word):
            print 'Congratulations! You win!'
            break
        if len(comm_lst) > 0:
            print 'Correct!'

        else:
            guesses -= 1
            print "Wrong! you have " + str(guesses) + ' guesses left!'
        print 'Guess again!'
        guess = raw_input()
    print "My word was " + str(derp) + '!'

print 'Press ENTER to start a game of hangman!'
raw_input()
HangMan()