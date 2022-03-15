import random

def play():
  user = input('Choose rock(r), paper(p) or scissors(s): ')
  computer = random.choice(['r', 'p', 's'])

  if user == computer:
    print('It\'s a tie!')

  print('It\'s not a tie!')

play()