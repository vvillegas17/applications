"""Deep Cave, by Victor Villegas AKA: V"""





import random, sys, time

# Set up the constants:
WIDTH = 70 # (!) tHE changing this 10 or 30.
PAUSE_AMOUNT = 0.05 # (!) Try changing this tto 0 or 1.0.

print('Deep Cave. by V')
print('Press Ctrl-C to stop.')
time.sleep(2)

leftWidth = 20
gapWidth = 5 

while True:
    # Display the tunnel segment:
    rightWidth = WIDTH - gapWidth - leftWidth
    print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))
    
    # Check for Ctrl-C press during the brief pause:
    try:
        time.sleep
    except KeyboardInterrupt:
        sys.exit() # When Ctrl-C is pressed, end the program.

    # Adjust the left side width:
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth = leftWidth -1 # Decrease left side width.
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        leftWidth = leftWidth + 1 # Increase left side width.
    else:
        pass # Do nothing; no change in the left width.
    
    # Adjust the gap width:
    # (!) Try uncomenting out all of the following code:
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and gapWidth > 1:
       gapWidth = gapWidth - 1 # Decrease gap width.
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
       gapWidth = gapWidth + 1 # Increase gap width.
    else:
       pass  # Do nothing: no change in gap width.

    exit