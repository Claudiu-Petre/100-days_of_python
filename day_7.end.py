import random
word_list = ["aardvark", "baboon", "camel"]

no_words = len(word_list)
random_word = random.randint(0, no_words - 1)
chosen_word = word_list[random_word]


print(f'Pssst, the solution is {chosen_word}.')


display = []
word_length = len(chosen_word)
for _ in range(word_length):
  display += '_'

print(display)

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