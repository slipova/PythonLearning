import random

def guess_number(x):
  random_number = random.randint(1, x)
  guess = 0

  while guess != random_number:
    guess = int(input(f"Pick a number between 1 and {x}: "))
    if guess > random_number:
      print("Your number is too high! Guess again: ")
    elif guess < random_number:
      print("Your number is too low! Guess again: ")

  print(f"Congratulations! You got the number {random_number} correctly!")


guess_number(10)