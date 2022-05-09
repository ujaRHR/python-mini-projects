# a terminal-based dice rolling 'under or over 7' casino/betting/guess game using python
# Author: Reajul Hasan Raju


from os import system
import time
import random
import string

balance = [50]
bet_history = []
withdrawn_balance = [0]

# Function-- for main/home menu
def main_menu():
    print(f'''\n----- Welcome to My Casino -----
    You have ${"%.2f" %balance[0]} on your wallet. Place bet and earn.\n
            Play - p        Balance - b      Reset - r
         Deposit - d       Withdraw - w      Exit - x
       Know more - k        History - h      Fees - f
    ''')
    choose = input('>>>>> ').lower()
    if choose == 'k':
        see_details()
    elif choose == 'p':
        play_game()
    elif choose == 'x':
        system('cls||clear')
    elif choose == 'b':
        check_balance()
    elif choose == 'h':
        check_history()
    elif choose == 'w':
        withdraw_balance()
    elif choose == 'd':
        deposit()
    elif choose == 'r':
        reset_all()
    elif choose == 'f':
        fee_calculator()
    else:
        mistake()


# Function-- for main gameplay
def play_game():
    try:
        print(f'Balance: ${"%.2f" %balance[0]}   ~ Now place a bet and predict ~')
        stake = (input('Stake: $'))
        stake = float(stake)
        if stake > 0 and stake > balance[0]:
            not_enough_balance()
        elif stake == 0:
            print('''   You can\'t place a $0.00 bet''')
            play_game()
        elif stake > 0 and stake <= balance[0]:
            print('    u- Under 7   o- Over 7   e- Exactly 7')         
            prediction = input('Prediction: ').lower()
            hidden_answer1 = (random.randint(1,6))
            hidden_answer2 = (random.randint(1,6))
            hidden_answer = hidden_answer1 + hidden_answer2

            if prediction == 'u' and hidden_answer < 7 :
                balance[0] += stake*2.3
                print(f''' ((((((((({hidden_answer1}, {hidden_answer2})))))))))
                W I N (!)   You Won ${"%.2f" %(stake*2.3)}
                Total Balance: ${"%.2f" %balance[0]}''')
                bet_history.append(1)
                wanna_play_again()
            elif prediction == 'u' and hidden_answer >= 7:
                balance[0] -= stake
                print(f''' ((((((((({hidden_answer1}, {hidden_answer2})))))))))
                L O S T (!)   You Lost ${"%.2f" %(stake)}
                    Total Balance: ${"%.2f" %balance[0]}''')
                bet_history.append(0)
                wanna_play_again()
            elif prediction == 'e' and hidden_answer == 7:
                balance[0] += stake*5.5
                print(f''' ((((((((({hidden_answer1}, {hidden_answer2})))))))))
                B I G    W I N (!)   You Won ${"%.2f" %(stake*5.5)}
                Total Balance: ${"%.2f" %balance[0]}''')
                bet_history.append(1)
                wanna_play_again()
            elif prediction == 'e' and (hidden_answer > 7 or hidden_answer < 7):
                balance[0] -= stake
                print(f''' ((((((((({hidden_answer1}, {hidden_answer2})))))))))
                L O S T (!)   You Lost ${"%.2f" %(stake)}
                Total Balance: ${"%.2f" %balance[0]}''')
                bet_history.append(0)
                wanna_play_again()
            elif prediction == 'o' and hidden_answer > 7:
                balance[0] += stake*2.3
                print(f''' ((((((((({hidden_answer1}, {hidden_answer2})))))))))
                W I N (!)   You Won ${"%.2f" %(stake*2.3)}
                Total Balance: ${"%.2f" %balance[0]}''')
                bet_history.append(1)
                wanna_play_again()
            elif prediction == 'o' and hidden_answer <= 7:
                balance[0] -= stake
                print(f''' ((((((((({hidden_answer1}, {hidden_answer2})))))))))
                L O S T (!)   You Lost ${"%.2f" %(stake)}
                Total Balance: ${"%.2f" %balance[0]}''')
                bet_history.append(0)
                wanna_play_again()
            else:
                re_predict()
    except:
        re_predict()
            


# Function-- for Play Again
def wanna_play_again():
    play_again = input('Want to play again? (Y/n) or Exit(x) or Home(h): ').lower()
    if play_again == 'y':
        play_game()
    elif play_again == 'n':
        main_menu()
    elif play_again == 'x':
        system('cls||clear')
    elif play_again == 'h':
        main_menu()
    else:
        mistake()


# Fuction-- for see details
def see_details():
    print('''  Throw a dice, guess and win generous bonuses.
        1) Choose your side:
                a.  Under 7
                b.  Over 7
                c.  Exactly 7
        2) If you guess Over or Under correctly, your stake is multiplied by 2.3
           If you correctly predict 7, your stake is multiplied by 5.5
        ''')
    main_menu()


# Function-- for check total balance and ID
def check_balance():
    wallet_address = ''
    char = string.ascii_lowercase + string.digits + string.ascii_uppercase
    for x in range(15):
        generate_wallet = (random.choice(char))
        wallet_address += generate_wallet
    print(f'''
    Wallet Address : {wallet_address}
      Main Balance : ${"%.2f" %balance[0]}
     Saved Balance : ${"%.2f" %withdrawn_balance[0]}
    ''')
    for x in range(50):
        time.sleep(0.1)
        print('|', end='', flush=True)
    main_menu()


# Function-- for check Bet history
def check_history():
    win = 0
    lost = 0
    for x in range(len(bet_history)):
        if bet_history[x] == 0:
            lost += 1
        elif bet_history[x] == 1:
            win +=1
    print(f'''You have played total {len(bet_history)} game(s).
        {win} Win and {lost} Lost.''')
    print('''
    menu - m   |   exit - x''')
    bet_history_choose = input('>>> ').lower()
    if bet_history_choose == 'm':
        main_menu()
    elif bet_history_choose == 'x':
        system('cls||clear')


# Function-- if prediction mis-typed.
def re_predict():
    print('Type Mistake! Try again...')
    play_game()

# Function-- If any mistake happen
def mistake():
    print('''    Type Mistake (!)  redirecting to Main Menu...''')
    for x in range(50):
        time.sleep(0.1)
        print('|', end='', flush=True)
    else:
        print('\n')
        main_menu()


# Function - For 'Not Enough Balance' bar show
def not_enough_balance():
    print('     Not enough balance')
    for x in range(50):
        time.sleep(0.1)
        print('|', end='', flush=True)
    else:
        print('\n')
        main_menu()


# Function-- For withdraw money
def withdraw_balance():                             # withdraw_balance()   - Function Name
    print('You have to keep minimum $1 to your main wallet. Transaction fee 1.9% ')
    if balance[0] > 1:
        how_much_withdraw = float(input('Amount : $'))
        with_transaction_fee = how_much_withdraw + (how_much_withdraw * 0.019)
        trx_ID = ''
        char = string.ascii_lowercase + string.digits + string.ascii_uppercase
        for x in range(30):
            generate_trx_ID = random.choice(char)
            trx_ID += generate_trx_ID
        print(f'''
        Withdraw   : ${"%.2f" %how_much_withdraw}
        Total Cost : ${"%.2f" %with_transaction_fee}
        Refference : {trx_ID}
        ''')
        withdraw_confirmation = input('Do you want to proceed?(Y/n): ').lower()
        if withdraw_confirmation == 'y':
            if balance[0] >= with_transaction_fee:
                balance[0] -= with_transaction_fee
                withdrawn_balance[0] += how_much_withdraw
                print('Transfering......')
                for x in range(50):
                    time.sleep(0.1)
                    print('|', end='', flush=True)
                else:
                    print(f'''\nWithdraw completed successfully
                    Main Balance: ${"%.2f" %balance[0]}
                   Saved Balance: ${"%.2f" %withdrawn_balance[0]}
                Main Menu - m      Exit Game - x
                ''')
                after_withdrawal_choose = input('>>> ').lower()
                if after_withdrawal_choose == 'm':
                    main_menu()
                elif after_withdrawal_choose == 'x':
                    system('cls||clear')
                else:
                    mistake()
            elif balance[0] < with_transaction_fee:
                not_enough_balance()
        elif withdraw_confirmation == 'n':
            main_menu()
        else:
            mistake()
    elif balance[0] < 1:
        not_enough_balance()


# Function-- For deposit feature inside withdraw feature
def deposit():
    print('Minimum deposit $1. Transaction fee 1.9%')
    if withdrawn_balance[0] >= 1:
        how_much_deposit = float(input('Amount: $'))
        if how_much_deposit <= withdrawn_balance[0]:
            deposit_with_transaction_fee = how_much_deposit + (how_much_deposit * 0.019)
            trx_ID = ''
            char = string.ascii_lowercase + string.digits + string.ascii_uppercase
            for x in range(30):
                generate_trx_ID = random.choice(char)
                trx_ID += generate_trx_ID
        print(f'''
           Deposit : ${"%.2f" %how_much_deposit}
        Total Cost : ${"%.2f" %deposit_with_transaction_fee}
        Refference : {trx_ID}
        ''')
        deposit_confirmation = input('Do you want to proceed?(Y/n): ').lower()
        if deposit_confirmation == 'y':
            if withdrawn_balance[0] >= deposit_with_transaction_fee:
                withdrawn_balance[0] -= deposit_with_transaction_fee
                balance[0] += how_much_deposit
                print('Transfering......')
                for x in range(50):
                    time.sleep(0.1)
                    print('|', end='', flush=True)
                else:
                    print(f'''\nDeposit completed successfully
                    Main Balance : ${"%.2f" %balance[0]}
                   Saved Balance : ${"%.2f" %withdrawn_balance[0]}
                Main Menu - m      Exit Game - x
                ''')
                after_withdrawal_choose = input('>>> ').lower()
                if after_withdrawal_choose == 'm':
                    main_menu()
                elif after_withdrawal_choose == 'x':
                    system('cls||clear')
                else:
                    mistake()
            elif withdrawn_balance[0] < deposit_with_transaction_fee:
                not_enough_balance()
        elif deposit_confirmation == 'n':
            main_menu()
        else:
            mistake()
    elif withdrawn_balance[0] < 1:
        not_enough_balance()


# Function-- For reset all values
def reset_all():
    print('++++++++++++++ R  E  S  E  T ++++++++++++++')
    reset_choose = input('Do you want to proceed?(Y/n): ').lower()
    if reset_choose == 'y':
        print('Reseting.......')
        bet_history.clear()
        balance[0] = 50
        withdrawn_balance[0] = 0
        for x in range(50):
            time.sleep(0.1)
            print('|', end='', flush=True)
        else:
            print('\n')
            main_menu()
    elif reset_choose == 'n':
        main_menu()
    else:
        mistake()

# Function-- For fee calculator
def fee_calculator():
    print('++++++++++ Fee Calculator ++++++++++')
    print('Withdraw Fee - w      Deposit Fee - d')
    fee_choose = input('>>> ').lower()
    if fee_choose == 'w':
        print('''1 - Amount to Total Cost\n2 - Total Cost to Amount''')
        direction = input('>>> ')
        if direction == '1':
            your_amount = float(input('Your Amount: $'))
            total_cost = your_amount + (your_amount * 0.029)
            print(f'''
            Your Amount: ${"%.2f" %your_amount}
             Total Cost: ${"%.2f" %total_cost}\n''')
        elif direction == '2':
            total_cost = float(input('Total Cost: $'))
            your_amount = (total_cost / 1.029)
            print(f'''
              Total Cost: ${"%.2f" %total_cost}
             Your Amount: ${"%.2f" %your_amount}\nmain menu - m    exit - x\n''')
            choose = input('>>> ').lower()
            if choose == 'm':
                main_menu()
            elif choose == 'x':
                system('cls||clear')
            else:
                mistake() 
        else:
            mistake()
    elif fee_choose == 'd':
        print('''1 - Amount to Total Cost\n2 - Total Cost to Amount''')
        direction = input('>>> ')
        if direction == '1':
            your_amount = float(input('Your Amount: $'))
            total_cost = your_amount + (your_amount * 0.019)
            print(f'''
            Your Amount: ${"%.2f" %your_amount}
             Total Cost: ${"%.2f" %total_cost}\n''')
        elif direction == '2':
            total_cost = float(input('Total Cost: $'))
            your_amount = (total_cost / 1.019)
            print(f'''
              Total Cost: ${"%.2f" %total_cost}
             Your Amount: ${"%.2f" %your_amount}\nmain menu - m    exit - x\n''')
            choose = input('>>> ').lower()
            if choose == 'm':
                main_menu()
            elif choose == 'x':
                system('cls||clear')
            else:
                mistake() 
        else:
            mistake()


# Call main Function
main_menu()
