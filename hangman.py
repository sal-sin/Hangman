import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    for c in secretWord:
        if c not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    s=''
    for i in secretWord:
        if i not in lettersGuessed:
            s=s+'_'
        else:
            s=s+i
    return s

def getAvailableLetters(lettersGuessed):
    s='abcdefghijklmnopqrstuvwxyz'
    res=''
    for char in s:
        if char not in lettersGuessed:
            res+=char
    return res

def hangman(secretWord):
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord))+ ' letters long.'
    print '------------'
    guesses=8
    char='a'
    lettersGuessed=[]
    while guesses>0:
        print 'You have ' + str(guesses) + ' guesses left.'
        print 'Available letters: ' + str(getAvailableLetters(lettersGuessed))
        char=str(raw_input ('Please guess a letter: '))
        char=char.lower()
        if char in lettersGuessed:
            print "Oops! You've already guessed that letter:",
        elif char in secretWord:
            lettersGuessed+=[char]
            print 'Good guess:',
        else:
            lettersGuessed+=[char]
            print 'Oops! That letter is not in my word:',
            guesses-=1
        print str(getGuessedWord(secretWord, lettersGuessed))
        print '------------'
        if isWordGuessed(secretWord, lettersGuessed)==True:
            print 'Congratulations, you won!'
            break

    if guesses==0:
        print 'Sorry, you ran out of guesses. The word was ' + str(secretWord) + '.'

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
