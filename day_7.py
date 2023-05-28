# Hangman game

import random
word_list = ["aardvark", "baboon", "camel"]

#TODO - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
no_words = len(word_list)
random_word = random.randint(0, no_words - 1)
chosen_word = word_list[random_word]
print(chosen_word)

# chosen_word = random.choice(word_list)
# print(chosen_word)

#TODO - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# guess = input('Choose a letter: ').lower()

#TODO - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
  if letter == guess:
    print('Right')
  else:
    print('Wrong')

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

display = []
word_length = len(chosen_word)
for _ in range(word_length):
  display += '_'

print(display)
  
# for letter in chosen_word:
#   letter = '-'
#   display += letter


#TODO: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
#TODO: - Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all the letters in the chosen_word 
# and 'display' has no more blanks ("_"). 
# Then you can tell the user they've won.
end_game = False

while not end_game:
  guess = input('Choose a letter: ').lower()

  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  print(display)

  if '_' not in display:
    end_game = True
    print('You win!')


