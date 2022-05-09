# Guess the Number Game using python

import os
import random
import time

def run_it():
    correct_answer = random.randint(1, 30)
    print('''
        -----Welcome to Guess Game-----
        There is a hidden number between 1 to 30, You have 5 chances to guess.
        Now guess the number:\n ''')
    for times in range(1, 6):
        your_guess = int(input(f'Chance-{times} : '))
        if your_guess == correct_answer:
            print(f'''You Won !!
            Correct answer is {correct_answer}''')
            break
    else:
        print(f'''You Lost !!
        Correct answer is {correct_answer}''')
    print('''\nDo you want to play again? (Y/n) or Exit(x):''')
    choose = input('>> ').lower()
    if choose == 'y':
        run_it()
    elif choose == 'n':
        print('Thanks for playing.')
        for x in range(50):
            time.sleep(0.1)
            print('|', end='', flush=True)
        else:
            print('\n')
    elif choose == 'x':
        os.system('cls||clear')


run_it()