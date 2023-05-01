# Conditional Statements; Logical Operators; Code block and Scope

# IF / ELSE
    # Modulo: odd or even
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print ('This is an even number')
else:
    print('This is an odd number')

# Nested if/elif/else
height = int(input('What is your height in cm? '))
if height >= 120:
    print('You can ride')
    age = int(input('What is your age? '))
    if age < 12:
        print('Child tickets are $5')
    elif (age <= 18):
        print('Youth tickets are 7$')
    else:
        print('Adult tickets are $12')
else:
    print('Sorry, grow up!')

# Challenge: BMI with interpretation
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print(f'Your bmi is {bmi}, you are underweight')
elif bmi < 25:
    print(f'Your bmi is {bmi}, you have a normal weight')
elif bmi < 30:
    print(f'Your bmi is {bmi}, you are slightly overweight')
elif bmi < 35:
    print(f'Your bmi is {bmi}, you are obese')
else:
    print(f'Your bmi is {bmi}, you arr clinically obese')

# Challenge: This is how you work out whether if a particular year is a leap year.
# on every year that is evenly divisible by 4 
# **except** every year that is evenly divisible by 100 
# **unless** the year is also evenly divisible by 400
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    print('Leap year.')
elif year % 100 == 1:
    print('Leap year')
elif year % 400 == 0:
    print('Leap year')
else:
    print('Not leap year.')


# Multiple IFs in succession
height = int(input('What is your height in cm? '))
bill = 0 
if height >= 120:
    print('You can ride')

    age = int(input('What is your age? '))
    if age < 12:
        bill = 5
        print('Child tickets are $5')
    elif (age <= 18):
        bill = 7
        print('Youth tickets are 7$')

    elif age >= 45 and age<= 55:
        print('Have a free ride on us') // AND operator

    else:
        bill = 12
        print('Adult tickets are $12')

    wants_photo = input('Do you want a photo? Y or N')
    if wants_photo == 'Y':
        bill += 3
    print(f'Your final bill is ${bill}')

else:
    print('Sorry, grow up!')

# #  Challenge: Pizza Delivery
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == 'S':
  bill += 15
elif size == 'M':
  bill += 20
else:
  bill += 25

if add_pepperoni == 'Y':
  if size == 'S':
    bill +=2
  else:
    bill += 3

if extra_cheese == 'Y':
  bill += 1

print(f'Your final bill is: ${bill}')

# OR
bill = 0

if size == 'S':
    bill += 15
    if add_pepperoni == 'Y':
        bill += 2
    if extra_cheese == 'Y':
        bill += 1

if size == 'M':
    bill += 20
    if add_pepperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1

if size == 'L':
    bill += 25
    if add_pepperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1

print(f'Your final bill is: ${bill}')

# Challenge: Love calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1 + name2
# print(combined_name)
combined_name_lower = combined_name.lower()
# print(combined_name_lower)

total_t = combined_name_lower.count("t")
total_r = combined_name_lower.count("r")
total_u = combined_name_lower.count("u")
total_e = combined_name_lower.count("e")
total_true = total_t + total_r + total_u + total_e
# print(total_true)

total_l = combined_name_lower.count("l")
total_o = combined_name_lower.count("o")
total_v = combined_name_lower.count("v")
total_e = combined_name_lower.count("e")
total_love = total_l + total_o + total_v + total_e
# print(total_love)

score = str(total_true) + str(total_love)
# print(score)
score_int = int(score)
if score_int < 10 or score_int > 90:
    print(f'Your score is {score_int}, you go together like coke and mentos.')
elif score_int >= 40 and score_int <= 50:
    print(f'Your score is {score_int}, you are alright together.')
else:
    print(f'Your score is {score_int}.')

# Challenge: Tresure Island
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

direction = input('Which way do you wanna go? "left" of "right"?: \n').lower()
if direction == 'left':
  action = input('You got to choose between "wait" and "swim"! \n').lower()
  if action == 'wait':
    color = input('Which door? "red", "blue" or "yellow"?: \n').lower()
    if color == 'red':
      print('Fired!')
    elif color == 'blue':
      print ('Monsters')
    elif color == 'yellow':
      print('You win!')
    else: 
      print('Fail!')
  else:
    print('You drawned!')
else:
  print('Game over!')