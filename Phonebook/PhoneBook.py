# Project for creating a phonebook using python.
import os
# every saved contacts name will save here.
saved_name = []
# every saved contact's number will store here.
saved_number = []

# function to choose option from a common platform.
def main_menu():
    print('-----PhoneBook-----')
    print('''
        Create new contact - n
        Exit - x
        My Phonebook - p
        ''')
    choose = input(('Choose a option to continue >> ')).lower()
    if choose == 'x':
        os.system('cls||clear')
    elif choose == 'n':
        wanna_try()
    elif choose == 'p':
        phonebook()


# function for storing/saving contact.
def wanna_try():
    ask = input('Want to save a contact? (Y/n): ').lower()
    if ask == 'y':
        ask_name = input('Name: ')
        saved_name.append(ask_name)
        ask_number = input('Number: ')
        saved_number.append(ask_number)
        main_menu()
    elif ask == 'n':
        print('''--> All-right.
                    redirecting you to main menu.........''')
        main_menu()
    elif ask == 'x':
        exit()
    else:
        print('''--> Type Mistake!
                    redirecting you to main menu.........''')
        main_menu()

# function to see saved contacts.
def phonebook():
    print(f'''-----My PhoneBook-----
    You have total {len(saved_name)} contact(s) saved.''')
    total = len(saved_name)
    for item in range(total):
        print(f'{saved_name[item]} - {saved_number[item]}')
    print('''
    Main Menu - m
    Exit - x''')
    choose = input('--> ').lower()
    if choose == 'm':
        main_menu()
    elif choose == 'x':
        exit()
    else:
        print('''--> Type Mistake!
                    redirecting you to main menu.........''')
        main_menu()



# code will run from here.
main_menu()

# Every saved contacts will be removed after you close the program 