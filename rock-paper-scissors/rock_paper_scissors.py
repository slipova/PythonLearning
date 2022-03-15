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
  return False


play()