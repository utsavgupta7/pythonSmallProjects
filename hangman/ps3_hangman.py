# Hangman game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    flag=True
    for i in range(0,len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            flag=False
    return flag
        



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word=''
    for i in range(0,len(secretWord)):
        if secretWord[i] in lettersGuessed:
            word=word+secretWord[i]
        else:
            word=word+' _ '
    return word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    case=string.ascii_lowercase
    avail_letters=''
    for char in case:
        if char not in lettersGuessed:
            avail_letters=avail_letters+char
            
    return avail_letters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed=[]
    mistakesMade=0
    availableLetters=string.ascii_lowercase
    
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is ",len(secretWord)," letters long."
    print "-----------"
    while mistakesMade<8:
        print "You have ",8-mistakesMade," guesses left."
        print "Available Letters:",getAvailableLetters(lettersGuessed)
        
        letter=raw_input("Please guess a letter: ")
        letter=letter.lower()
        if letter not in lettersGuessed:
            lettersGuessed.append(letter)
            if letter in secretWord:
                print "Good guess: ",getGuessedWord(secretWord,lettersGuessed)
            else:
                print "Oops! That letter is not in my word:",getGuessedWord(secretWord,lettersGuessed)
                mistakesMade=mistakesMade+1
        else:
            print "Oops! You've already guessed that letter: ",getGuessedWord(secretWord,lettersGuessed)
        print "-----------"
        if isWordGuessed(secretWord, lettersGuessed):
            print "Congratulations, you won!"
            break
    if not isWordGuessed(secretWord, lettersGuessed):
        print "Sorry, you ran out of guesses. The word was ",secretWord,"."






secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

