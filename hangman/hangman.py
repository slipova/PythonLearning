import random
from words import words
import string

def get_valid_word(words):
  word = random.choice(words)

  while '-' in word or ' ' in word:
    word = random.choice(words)

  return word.upper()


def hangman():
  word = get_valid_word(words)
  word_letters = set(word)
  alphabet = set(string.ascii_uppercase)
# a collection of letters from user guesses
  used_letters = set()

  while len(word_letters) > 0:
    print('You have used these letters: ', ' '.join(used_letters))

    # if a letter is in the used_letters, then it should show, otherwise it's a dash
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print('Current word: ', ' '.join(word_list))

    # get user input and save it into a variable
    user_letter = input('Guess a letter: ').upper()

    # if user_letter in alphabet and user_letter not in used_letters:
    if user_letter in alphabet - used_letters:
      used_letters.add(user_letter)
      # check if the letter is in the word
      if user_letter in word_letters:
        word_letters.remove(user_letter)
        print('')
    
    elif user_letter in used_letters:
      print('You have already used this character. Please try again')

    else:
      print('Please enter a valid character!')
hangman()