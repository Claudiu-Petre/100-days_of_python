#  Randomization with Random Module
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



# and Lists

