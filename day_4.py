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

# Nested lists
fruits = ["strawberries", "nectarines", "apples"]
vegetables = ["spinach", "tomatoes", "celery", "carrots"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

print(dirty_dozen[0]) // fruits
print(dirty_dozen[1]) // vegetables

print(dirty_dozen[1][2]) // celery
print(dirty_dozen[1][3]) // carrots

# Challenge: 
# write a program that allows you to mark a square on the map using a two-digit system. 
# The first digit in the input will specify the column (the position on the horizontal axis).
# The second digit in the input will specify the row number (the position on the vertical axis). 

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️","⬜️️*️"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1] // to get the column no
selected_row[horizontal - 1] = 'X' // to get the row x-ed
#  or
map[vertical - 1][horizontal - 1] = 'X'

print(f"{row1}\n{row2}\n{row3}")
