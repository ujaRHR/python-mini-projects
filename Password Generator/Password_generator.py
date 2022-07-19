# Password Generator Using Python
from os import system, name
import random, string

# I use only 10 most used punctuation
char = string.ascii_uppercase + '!@#$%&-+=/?_/()' + string.digits + string.ascii_lowercase

# Clear terminal
try:
    system('cls') # Windows
except:
    system('clear') # MAC and linuX

how_long = int(input('Password Length -- '))
how_much = int(input('Quantity? -- '))

print('\n-----Here are your Passwords-----\n')
for x in range(how_much):
    for y in range(how_long):
        print(random.choice(char), end='')
    print('')
