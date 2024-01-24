import random

NUM_DIGITS = 3
MAX_GUESSES = 10



def main():
    print('___________________________________________________________________')
    print('__|_____|____|____|____|___|___|___|___|___|___|____|___|___|___|__')
    print('|____|____|____|____|____|___|___|___|___|___|____|___|___|___|___|')
    print('Bagels, a deductive logic game.')
    print('By Victor Villegas AKA: V')
    print('I am thinking of a 3-digits number. try to guess what it is.')
    print('Here are some clues:')
    print()
    print('When I say:      That means:')
    print(' Pico                One digit is correct but in the wrong position.')
    print(' Fermi               One digit is correct and in the right position.')
    print(' Bagels              No digit is correct.')
    print('For example, if the secret number was 248 and your guess was 843, the')
    print('clues would be Fermi Pico.'.format(NUM_DIGITS))
    print()


    while True:
        print('Do you want to play? (Yes or no)')
        if not input('>').lower().startswith('y'):
            break

        secretNum = getSecretNum()
        print()
        print('I have thought up a number.')
        print(' You have {} guesses to get it right.'.format(MAX_GUESSES))
        print()

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')
                
                
            clues = getClues(guess, secretNum)
            print(clues)
            print()
            numGuesses = numGuesses + 1


            if guess == secretNum:
                break

            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))
        print()    
        print('Do you want to play again? (Yes or no)')
        print()
        if not input('>').lower().startswith('y'):
            break
    print('Thanks for playing!')
    print()

        

def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    SecretNum = ''
    for i in range(NUM_DIGITS):
        SecretNum += str(numbers[i])
    return SecretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ''.join(clues)
        






if __name__ == '__main__':
    main()