import random
from words import words
import string

def get_valid_word(words):
  word = random.choice(words)

  while '-' in word or ' ' in word:
    word = random.choice(words)

  return word


def hangman():
  word = get_valid_word(words)
  word_letters = set(word)
  alphabet = set(string.ascii_uppercase)
# a collection of letters from user guesses
  used_letters = set()

  # get user input and save it into a variable
  user_letter = input('Guess a letter: ').upper()

  # if user_letter in alphabet and user_letter not in used_letters:
  if user_letter in alphabet - used_letters:
    used_letters.add(user_letter)
    

hangman()