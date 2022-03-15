import random

def play():
  user = input('Choose rock(r), paper(p) or scissors(s): ')
  computer = random.choice(['r', 'p', 's'])

  if user == computer:
    print('It\'s a tie!')
    return

  if is_win(user, computer):
    print('You won!')
    return

  print('You lost!')


def is_win(player, opponent):
  if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
    return True



play()