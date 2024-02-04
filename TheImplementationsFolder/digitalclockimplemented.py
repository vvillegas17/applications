import sys, time
import sevseg # Imports our seveg.py program.

am = print("""  /
               /__
              /    
""")

print(am)
try:
    while True: # Main program loop.
        # Clear the screen by printing several newlines:
        print('\n' * 60)
        
        # Get the current time from the computer's clock:
        currentTime = time.localtime()
        # % 12 so we use a 12-hour clock not 24:
        hours = str(currentTime.tm_hour % 12)
        if hours == '0':
            hours = '12' # 12-hour clocks show 12:, not 00:
            
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)

        # Get this digit strings from the sevseg module:
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow, = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigit = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigit.splitlines()

        # Display the digits:

        print('                                              Clock Made by Victor villegas AKA: V')
        print('                                              ' + hTopRow    +'     ' + mTopRow    +'     ' + sTopRow    ) #+ '     ' + pTopRow)
        print('                                              ' + hMiddleRow +'     ' + mMiddleRow +'     ' + sMiddleRow )# '     ' + pMiddleRow)
        print('                                              ' + hBottomRow +'     ' + mBottomRow +'     ' + sBottomRow )#+ '     ' + pLowerRow)
        print()
        print('                                               Press Ctrl-C to quit.')
        print()
        print()
        print()
        print()
        print('                                                       I Love Programming!')
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()

        # Keep looping until the second changes:
        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break
except KeyboardInterrupt:
    print('Digital Clock, by V')
    sys.exit() 


