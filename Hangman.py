
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
from Hangman_word import word_list

chosen_word = random.choice(word_list)
lives = 6

from Hangman_logo import logo
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display+= "_"
print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter : ").lower()
    if guess in display:
        print(f"You'r have already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. you lose a life")
        lives -= 1
        if lives == 0:
            end_of_game=True
            print("You lose")

    print(display)

    if "_" not in display:
        end_of_game=True
        print("You Win")

    print(stages[lives])