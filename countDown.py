"""Countdown, by Victor Villegas AKA: V"""







import sys, time
import sevseg # imports sevseg.py program.

# (!) Change this to any number of seconds:
print()
secondsLeft = input('How long do you want the timer for in minutes:')
print()
print()
secondsLeft =  int(secondsLeft)
secondsLeft = secondsLeft * 60


try:
    while True: # Main program Loop.
        # Clear the screen by printing several newlines:
        print('\n' * 60)

        # Get the hours/minutes\seconds from secondsLeft:
        # For example: 7265 is 2 hours, 1 minute, 5 seconds.
        # So 7265 // 3600 is 2 hours:
        hours = str(secondsLeft // 3600)
        # And 7265 % 3600 is 65, and 65 // 60 is 1 minute:
        minutes = str((secondsLeft % 3600) // 60)
        # And 7265 % 60 is 5 seconds:
        seconds =  str (secondsLeft % 60)

        # Get the digit strings from the sevseg module:
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # Diplay the Digits:
        print('                    ',  hTopRow     +  '         ' + mTopRow    + '         ' + sTopRow)
        print('                    ', hMiddleRow  +  '    *    ' + mMiddleRow + '    *    ' + sMiddleRow)
        print('                    ', hBottomRow  +  '    *    ' + mBottomRow + '    *    ' + sBottomRow)
        print()
        print()

        if secondsLeft == 0:
            print()
            print('                               * * * * BOOM * * * *')
            break

        print()
        print()
        print('                                  Press Ctrl-C to quit.')
        print('                                        CountDown, V')
        print('                                   I love Programming')

        time.sleep(1) # Insert a one-second pause.
        secondsLeft -= 1    
except KeyboardInterrupt:

    sys.exit() # When Ctrl-C is pressed, end the program.