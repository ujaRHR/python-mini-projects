# Rock Paper Scissors Game

from os import system
import random

def start_playing():
    system('clear')
    human = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if human == computer:
        return 'It\'s Tie'

    # r > s, s > p, p > r
    if is_win(human, computer):
        return "You Win"
    
    return 'You Lost'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

print(start_playing())