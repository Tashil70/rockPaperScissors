import random

def play():
    user = input("What's your choice? \n'r' for Rock, 'p' for Paper and 's' for Scissors\n").lower()
    computer = random.choice(['r','p', 's'])
    print(f"Computer chooses {computer}!")
    if user == computer:
        return 'It\'s a draw!'
    
    if is_win(user, computer):
        return 'You win!'
    
    return 'You Lost!'
    
def is_win(player, opp):
    if (player =='r' and opp =='s') or (player =='s' and opp=='p') or (player == 'p' and opp == 'r'):
        return True
    
print(play())