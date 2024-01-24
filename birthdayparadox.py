import datetime, random

def getBirthdays(numberOfBirthdays):
    birthdays =[]
    for i in range(numberOfBirthdays):

        startOfYear = datetime.date(2024, 1, 1)

        ramdomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + ramdomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None
    
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA
            
print('Birthday Paradox, by Victor villegas AKA: V ')
# if this comment still here i need to continue the messages avobe

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Nov', 'Dec')

while True:
    print('How many birthday shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break
    
print()

print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end = '')
    monthName = MONTHS[birthday.month - 2]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end = '')

print()
print()

match = getMatch(birthdays)

print('in this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have birthday on', dateText)
else:
    print('there are no matching birthday.')
print()

print('Generating', numBDays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('let\'s run another 100,000 simulations.')
simMatch = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, 'simulations run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1

print('100,00 simulations run.')

probalility = round(simMatch / 100_000 * 100, 2)
print('Out of 100,000 simulations of', numBDays, ' pleople, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probalility, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more then you would think!')



