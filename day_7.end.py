
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

word_list = ["aardvark", "baboon", "camel"]

no_words = len(word_list)
random_word = random.randint(0, no_words - 1)
chosen_word = word_list[random_word]

lives = 6

print(f'Pssst, the solution is {chosen_word}.')


display = []
word_length = len(chosen_word)
for _ in range(word_length):
  display += '_'


end_game = False

while not end_game:
  guess = input('Choose a letter: ').lower()

  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

  if guess not in chosen_word:
    lives -= 1
    if lives == 0:
      print('You lose!')
    
    if '_' not in display:
      end_game = True
      print('You win!')

  print(stages[lives])
