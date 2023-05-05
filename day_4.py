#  Randomization with Random Module     &     LISTS
import random

# generates random WHOLE numbers

random_integer = random.randint(1, 10)
print(random_integer)

# generates random FLOATS numbers

random_float = random.random() 
# does NOT take the last number. generates a float between 0 and 1
print(random_float)

# expand beyond 0.9999999
random_float = random.random() * 5
# 0.111111 - 4.99999

# e.g: for dice, flipping coins, etc
love_score = random.randint(1, 100)
print(f'Your love score is {love_score}')

# Coin: heads and tails

random_side = random.randint(0, 1)
if random_side == 1:
  print("Heads")
else:
  print("Tails")



                            # LISTS

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland"]

# pull items:
  # positive: from the beginning of the list
print(states_of_america[3])

  # negative: from the back of the list
print(states_of_america[-2])

#  change items in the list:
states_of_america[1] = "Pencilvania"

# ADD at he END of the list
states_of_america.append("ClauBAu")
states_of_america.extend(['ClauBAu', 'MerePere'])

# Challenge: write a program that will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.
name_string = input("Give me everybody's name, separated by a comma. ")
names = name_string.split(', ')

# get the no of items in the list
no_items = len(names)
# create the random choice from the list based on indexes
random_choice = random.randint(0, no_items - 1)
# apply the random choice to the list
payer = names[random_choice]
print(f'{payer} is going to buy the meal today')

# OR using CHOICE()
payer = random.choice(names)
print(f'{payer} is going to buy the meal today')
