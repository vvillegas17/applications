"""Cho-Han, by Victor Villegas AKA: V"""




import random, sys

Japenese_Numbers = {1: ' ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com
 
 In this traditional Japanese dice game, two dice are rolled in a bamboo
 cup by the dealer sitting on the floor. The player must guess if the
 dice total to an even (cho) or odd (han) number.
 ''')

purse = 5000
while True: # Main game loop
    # Place your bet:
    pot = input('> ')
    if pot.upper() == 'QUIT':
        print('Thanks for playing!')
        sys.exit()
    elif not pot.isdecimal():
        print('Please enter a number.')
    elif int(pot) > purse:
        print('You. do not have enough to make that bet')
    else:
        # This is a valid bet.
        pot = int(pot) # Convert pot to an integer/
        break # Exit the loop once a valid bet is placed.

# Roll the dice.
dice1 = random.randint(1, 6)
dice2 = random .randint(1, 6)

print('The dealer swirls the cup and you hear the rattle of dice.')
print('The dealer slams the cup on the floor, still covering the')
print('dice and asks for your bet.')
print()
print('    CHO (even) or HAN (odd)?')

# Let the player bet cho or han:
while True:
    bet = input('> ').upper()
    if bet != 'CHO' and bet != 'HAN':
        print('PLease enter either "CHO" or "HAN".')
        continue
    else:
        break

# Reveal the dice results:
print('The dealer lift the cup to reveal:')
print('  ', Japenese_Numbers[dice1], '-', Japenese_Numbers[dice2])
print('     ', dice1, '-', dice2)

# Determine if the player won:
rollIsEven = (dice1 + dice2) % 2 == 0
if rollIsEven:
    correctBet = 'CHO'
else:
    correctBet = 'HAN'

playerWon = bet == correctBet

# Display the bet results:
if playerWon:
    print('You won! you take, pot', 'mon.')
    purse = purse + pot # Add the pot form player's purse.
    print('The house collects a', pot // 10, 'mon fee.')
    purse = purse - (pot // 10) # the house fee is 10%
else:
    purse = purse - pot # Substract the pot from player's purse.
    print('YOu lost!')

# Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
        


